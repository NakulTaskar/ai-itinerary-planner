"""✈️ AI Itinerary Planner — Streamlit front-end.

Run with:  streamlit run app.py
"""

import html
import os
from datetime import date, timedelta
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

from planner.export import to_markdown
from planner.llm import AVAILABLE_MODELS, generate_itinerary
from planner.models import Itinerary, TripRequest
from planner.sample import SAMPLE_ITINERARY

load_dotenv()

st.set_page_config(page_title="AI Itinerary Planner", page_icon="✈️", layout="wide")
CSS = (Path(__file__).parent / "assets" / "style.css").read_text()
st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)

INTERESTS = ["🏛️ History", "🍜 Food", "🏖️ Beaches", "🌿 Nature", "🛍️ Shopping",
             "🎉 Nightlife", "🧗 Adventure", "🎨 Art & Culture", "📸 Photography"]
TIME_ICONS = {"Morning": "🌅", "Afternoon": "☀️", "Evening": "🌙"}

# ---------------------------------------------------------------- Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    api_key = st.text_input(
        "Gemini API key",
        value=os.getenv("GEMINI_API_KEY", ""),
        type="password",
        help="Free key: https://aistudio.google.com/apikey",
    )
    model = st.selectbox("Model", AVAILABLE_MODELS)
    temperature = st.slider("Creativity", 0.0, 1.0, 0.7, 0.1)
    demo_mode = st.toggle("Demo mode (no API key needed)", value=not api_key)
    st.divider()
    st.caption("Built with Streamlit + Google Gemini · Generative AI project")

# ---------------------------------------------------------------- Header
st.markdown(
    """<div class="hero">
        <h1>✈️ AI Itinerary Planner</h1>
        <p>Tell us where you're going — Generative AI builds your perfect day-by-day plan.</p>
    </div>""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------- Form
with st.form("trip_form"):
    c1, c2, c3 = st.columns([2, 1, 1])
    destination = c1.text_input("📍 Destination", placeholder="e.g. Goa, Paris, Tokyo")
    start_date = c2.date_input("📅 Start date", value=date.today() + timedelta(days=14))
    days = c3.number_input("🗓️ Days", min_value=1, max_value=10, value=3)

    c4, c5, c6 = st.columns(3)
    budget = c4.select_slider("💰 Budget", ["Backpacker", "Moderate", "Comfort", "Luxury"],
                              value="Moderate")
    travelers = c5.selectbox("👥 Travelling as", ["Solo", "Couple", "Family with kids", "Friends"])
    pace = c6.radio("🚶 Pace", ["Relaxed", "Balanced", "Packed"], index=1, horizontal=True)

    interests = st.pills("❤️ Interests", INTERESTS, selection_mode="multi",
                         default=["🏛️ History", "🍜 Food"])
    notes = st.text_area("📝 Special requests (optional)",
                         placeholder="Vegetarian, wheelchair accessible, no early mornings…")

    submitted = st.form_submit_button("✨ Generate my itinerary", type="primary",
                                      use_container_width=True)

# ---------------------------------------------------------------- Generate
if submitted:
    if demo_mode:
        st.session_state.itinerary = SAMPLE_ITINERARY
        st.info("Demo mode is on — showing a sample itinerary. Add an API key and turn "
                "demo mode off to generate a real one.", icon="ℹ️")
    elif not api_key:
        st.error("Please add your Gemini API key in the sidebar.", icon="🔑")
    elif not destination.strip():
        st.error("Please enter a destination.", icon="📍")
    else:
        trip = TripRequest(
            destination=destination.strip(),
            start_date=start_date,
            days=int(days),
            budget=budget,
            travelers=travelers,
            pace=pace,
            interests=[i.split(" ", 1)[1] for i in (interests or [])],  # strip emoji
            notes=notes.strip(),
        )
        with st.spinner(f"Planning your {days}-day trip to {trip.destination}…"):
            try:
                st.session_state.itinerary = generate_itinerary(api_key, trip, model, temperature)
            except Exception as exc:  # surface API/validation errors nicely
                msg = str(exc)
                if "404" in msg or "NOT_FOUND" in msg:
                    st.error(f"The model **{model}** isn't available for your key. "
                             "Pick another model in the sidebar.", icon="⚠️")
                elif "429" in msg or "RESOURCE_EXHAUSTED" in msg:
                    st.error("Free-tier limit reached. Wait a minute and try again, or "
                             "choose **gemini-3.5-flash-lite** in the sidebar.", icon="⏳")
                elif "API_KEY_INVALID" in msg or "API key not valid" in msg:
                    st.error("Your API key isn't valid. Copy it again from "
                             "https://aistudio.google.com/apikey", icon="🔑")
                else:
                    st.error(f"Couldn't generate the itinerary: {exc}", icon="⚠️")


# ---------------------------------------------------------------- Render
def esc(text: str) -> str:
    return html.escape(str(text))


def render(it: Itinerary) -> None:
    st.markdown(f'<div class="trip-title">{esc(it.trip_title)}</div>'
                f'<div class="trip-overview">{esc(it.overview)}</div>', unsafe_allow_html=True)

    m1, m2, m3 = st.columns(3)
    m1.metric("Days", len(it.days))
    m2.metric("Activities", sum(len(d.activities) for d in it.days))
    m3.metric("Est. budget", it.estimated_total_budget.split("(")[0].strip())

    tabs = st.tabs([f"Day {d.day} · {d.theme}" for d in it.days] + ["🎒 Tips & Packing"])

    for tab, d in zip(tabs, it.days):
        with tab:
            st.caption(f"📅 {d.date}")
            for a in d.activities:
                icon = TIME_ICONS.get(a.time_of_day, "📌")
                st.markdown(
                    f"""<div class="card {esc(a.time_of_day)}">
                        <div class="when">{icon} {esc(a.time_of_day)}</div>
                        <div class="title">{esc(a.title)}</div>
                        <div class="desc">{esc(a.description)}</div>
                        <div class="meta">
                            <span class="pill">📍 {esc(a.place)}</span>
                            <span class="pill cost">💵 {esc(a.estimated_cost)}</span>
                        </div>
                    </div>""",
                    unsafe_allow_html=True,
                )
            st.markdown(
                f"""<div class="day-footer">
                    <span>🍽️ <b>Must eat:</b> {esc(d.food_recommendation)}</span>
                    <span>💰 <b>Day total:</b> {esc(d.daily_cost)}</span>
                </div>""",
                unsafe_allow_html=True,
            )

    with tabs[-1]:
        left, right = st.columns(2)
        with left:
            st.subheader("🎒 Packing list")
            for item in it.packing_list:
                st.checkbox(item, key=f"pack_{item}")
        with right:
            st.subheader("💡 Local tips")
            for tip in it.local_tips:
                st.markdown(f"- {tip}")
        st.success(f"**Estimated total budget:** {it.estimated_total_budget}", icon="💰")

    st.divider()
    slug = it.trip_title.lower().replace(" ", "_")[:40]
    d1, d2 = st.columns(2)
    d1.download_button("⬇️ Download as Markdown", to_markdown(it), f"{slug}.md",
                       use_container_width=True)
    d2.download_button("⬇️ Download as JSON", it.model_dump_json(indent=2), f"{slug}.json",
                       use_container_width=True)


if "itinerary" in st.session_state:
    render(st.session_state.itinerary)

st.markdown('<div class="footer-note">Always verify opening hours, bookings, and local prices before you travel.</div>', unsafe_allow_html=True)
