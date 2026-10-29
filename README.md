# ✈️ Itinerary Planner

A smart, automated travel planning app that crafts personalised, day-by-day travel itineraries. Enter a destination, dates, budget, travel style, and interests — the platform instantly generates a complete, structured plan with activities, dining picks, cost estimates, a packing checklist, and local tips.

---

## ✨ Features
- ⚡ **Intelligent Planning Engine** that curates comprehensive, tailored travel plans
- 🧩 **Structured Itinerary Layout** rendered as clean, intuitive activity cards
- 🗂️ Day-by-day **tabs** with Morning / Afternoon / Evening activity timelines
- 💰 Cost estimates per activity, per day, and for the entire trip
- 🎒 Interactive packing checklist + practical local travel tips
- ⬇️ One-click export as **Markdown** or **JSON**
- 🎛️ Customisable pace, budget, and travel interests
- 🧪 **Demo Mode** — explore pre-built sample trips instantly

## 🏗️ Architecture
```
 User ──► Web UI (app.py)
              │  TripRequest
              ▼
        prompts.py  ──►  Template & parameter formulation
              │
              ▼
          llm.py    ──►  Planning Engine API (response_schema = Itinerary)
              │  JSON
              ▼
        models.py   ──►  Data validation (Pydantic)  ──►  Cards / tabs / downloads
```

## 📁 Project Structure
```
itinerary-planner/
├── app.py                 # Main Web UI (Streamlit)
├── planner/
│   ├── models.py          # TripRequest & Itinerary data schemas
│   ├── prompts.py         # Travel prompt & instruction templates
│   ├── llm.py             # Planning engine client integration
│   ├── export.py          # Markdown & file export handlers
│   └── sample.py          # Pre-built sample trip data
├── assets/style.css       # Custom styling & card theme
├── .streamlit/config.toml # Theme configuration
├── tests/test_planner.py  # Automated unit test suite
├── requirements.txt       # Project dependencies
├── .env.example           # Environment configuration template
├── run.sh / run.bat       # Single-command launchers (macOS/Linux & Windows)
└── README.md              # Project documentation
```

## 🚀 Quick Start

### 1. Prerequisites & API Setup
Grab an API key at https://aistudio.google.com/apikey

### 2. Run the App
**macOS / Linux**
```bash
./run.sh
```
**Windows**
```bat
run.bat
```
**Manual Launch**
```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env               # Add your key to .env
streamlit run app.py
```
The application opens in your browser at `http://localhost:8501`.

### 3. Run Tests (Optional)
```bash
pip install pytest && pytest -q
```

## 🛠️ Tech Stack
| Layer | Tool |
|---|---|
| Frontend | Streamlit |
| Planning Engine | Google Gemini (`google-genai` SDK) |
| Data Validation | Pydantic v2 |
| Environment Config | python-dotenv |

## 🔮 Future Scope
- Interactive map view with route navigation
- Live weather forecasts & flight/hotel price integrations
- In-app interactive itinerary adjustments
- Social sharing and bookmarking itineraries
