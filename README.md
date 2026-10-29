# ✈️ AI Itinerary Planner

A **Generative AI** web app that creates personalised, day-by-day travel itineraries.
Enter a destination, dates, budget, travel style and interests — Google **Gemini**
generates a structured plan with activities, food picks, costs, packing list and local tips.

---

## ✨ Features
- 🧠 **LLM-powered planning** using Google Gemini (`gemini-flash-latest` by default — always the newest Flash model)
- 🧩 **Structured output** — Gemini returns JSON validated by a Pydantic schema, rendered as cards
- 🗂️ Day-by-day **tabs** with Morning / Afternoon / Evening activity cards
- 💰 Cost estimates per activity, per day and for the whole trip
- 🎒 Interactive packing checklist + local tips
- ⬇️ Export as **Markdown** or **JSON**
- 🎛️ Model selector and creativity (temperature) slider
- 🧪 **Demo mode** — works without an API key (great for presentations)

## 🏗️ Architecture
```
 User ──► Streamlit UI (app.py)
              │  TripRequest
              ▼
        prompts.py  ──►  Prompt engineering (system instruction + user prompt)
              │
              ▼
          llm.py    ──►  Google Gemini API  (response_schema = Itinerary)
              │  JSON
              ▼
        models.py   ──►  Pydantic validation  ──►  Cards / tabs / downloads
```

## 📁 Project structure
```
itinerary-planner/
├── app.py                 # Streamlit UI
├── planner/
│   ├── models.py          # TripRequest + Itinerary schemas (Pydantic)
│   ├── prompts.py         # System instruction & prompt template
│   ├── llm.py             # Gemini API call with structured output
│   ├── export.py          # Markdown export
│   └── sample.py          # Demo itinerary (no API key needed)
├── assets/style.css       # Custom styling
├── .streamlit/config.toml # Theme
├── tests/test_planner.py  # Unit tests (no network)
├── requirements.txt
├── .env.example
├── run.sh / run.bat       # One-command launchers
└── README.md
```

## 🚀 Quick start

### 1. Get a free Gemini API key
👉 https://aistudio.google.com/apikey

### 2. Run it
**macOS / Linux**
```bash
./run.sh
```
**Windows**
```bat
run.bat
```
**Manual**
```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env               # then paste your key into .env
streamlit run app.py
```
The app opens at http://localhost:8501. You can also paste your key in the sidebar.

### 3. Run tests (optional)
```bash
pip install pytest && pytest -q
```

## 🛠️ Tech stack
| Layer | Tool |
|---|---|
| Frontend | Streamlit |
| LLM | Google Gemini via `google-genai` SDK |
| Validation | Pydantic v2 |
| Config | python-dotenv |

## 🔮 Future scope
- Maps view of each day's route
- Live weather & hotel/flight suggestions
- Chat-based editing ("make day 2 more relaxed")
- Save & share itineraries

---
⚠️ *AI-generated plans can be inaccurate — always verify opening hours and prices.*
