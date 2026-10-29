"""Built-in sample itinerary so the app can be demoed without an API key."""

from .models import Activity, DayPlan, Itinerary

SAMPLE_ITINERARY = Itinerary(
    trip_title="Sun, Sand & Spice: 3 Days in Goa",
    overview=(
        "A relaxed mix of North Goa's lively beaches, Old Goa's Portuguese heritage "
        "and laid-back South Goa sunsets — with plenty of seafood along the way."
    ),
    days=[
        DayPlan(
            day=1, date="Fri, 13 Nov 2026", theme="North Goa Beaches",
            activities=[
                Activity(time_of_day="Morning", title="Fort Aguada", place="Candolim",
                         description="17th-century Portuguese fort and lighthouse with sea views.",
                         estimated_cost="₹50"),
                Activity(time_of_day="Afternoon", title="Baga & Calangute Beach", place="Baga",
                         description="Swim, try water sports or relax in a beach shack.",
                         estimated_cost="₹1,500"),
                Activity(time_of_day="Evening", title="Sunset at Chapora Fort", place="Vagator",
                         description="Short climb for a famous sunset view over Vagator.",
                         estimated_cost="Free"),
            ],
            food_recommendation="Goan fish thali at Britto's, Baga",
            daily_cost="₹3,500 per person",
        ),
        DayPlan(
            day=2, date="Sat, 14 Nov 2026", theme="Heritage & Culture",
            activities=[
                Activity(time_of_day="Morning", title="Basilica of Bom Jesus", place="Old Goa",
                         description="UNESCO World Heritage church housing St. Francis Xavier's relics.",
                         estimated_cost="Free"),
                Activity(time_of_day="Afternoon", title="Fontainhas Latin Quarter", place="Panaji",
                         description="Walk colourful Portuguese-era lanes and art cafés.",
                         estimated_cost="₹300"),
                Activity(time_of_day="Evening", title="Mandovi River Cruise", place="Panaji Jetty",
                         description="Hour-long sunset cruise with Goan folk music and dance.",
                         estimated_cost="₹500"),
            ],
            food_recommendation="Pork vindaloo & bebinca at Viva Panjim",
            daily_cost="₹2,800 per person",
        ),
        DayPlan(
            day=3, date="Sun, 15 Nov 2026", theme="South Goa Serenity",
            activities=[
                Activity(time_of_day="Morning", title="Cabo de Rama Fort", place="Canacona",
                         description="Quiet clifftop fort ruins with sweeping coastal views.",
                         estimated_cost="Free"),
                Activity(time_of_day="Afternoon", title="Palolem Beach", place="Palolem",
                         description="Crescent beach — try kayaking or a boat ride to Butterfly Beach.",
                         estimated_cost="₹800"),
                Activity(time_of_day="Evening", title="Beach-shack dinner", place="Palolem",
                         description="Fresh catch of the day by candlelight on the sand.",
                         estimated_cost="₹1,200"),
            ],
            food_recommendation="Butter-garlic crab at Dropadi, Palolem",
            daily_cost="₹3,200 per person",
        ),
    ],
    estimated_total_budget="≈ ₹9,500 per person (excluding stay and flights)",
    packing_list=["Sunscreen (SPF 50)", "Swimwear", "Light cotton clothes", "Sunglasses & hat",
                  "Flip-flops", "Reusable water bottle", "Modest outfit for churches"],
    local_tips=[
        "Rent a scooter (~₹400/day) — it's the easiest way to get around.",
        "Use the GoaMiles app for fixed-price taxis.",
        "Carry cash; many beach shacks don't accept cards.",
        "Cover shoulders and knees when visiting churches.",
    ],
)
