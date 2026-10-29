#!/usr/bin/env bash
# One-command setup & launch (macOS / Linux)
set -e
cd "$(dirname "$0")"
if [ ! -d .venv ]; then
  echo "📦 Creating virtual environment..."
  python3 -m venv .venv
fi
source .venv/bin/activate
pip install -q -r requirements.txt
[ -f .env ] || cp .env.example .env
# Skip Streamlit's one-time "enter your email" prompt
mkdir -p ~/.streamlit
[ -f ~/.streamlit/credentials.toml ] || printf '[general]\nemail = ""\n' > ~/.streamlit/credentials.toml
echo "🚀 Starting AI Itinerary Planner... (opens at http://localhost:8501)"
streamlit run app.py
