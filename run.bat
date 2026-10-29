@echo off
REM One-command setup & launch (Windows)
cd /d "%~dp0"
if not exist .venv (
  echo Creating virtual environment...
  python -m venv .venv
)
call .venv\Scripts\activate
pip install -q -r requirements.txt
if not exist .env copy .env.example .env
REM Skip Streamlit's one-time "enter your email" prompt
if not exist "%USERPROFILE%\.streamlit" mkdir "%USERPROFILE%\.streamlit"
if not exist "%USERPROFILE%\.streamlit\credentials.toml" (
  echo [general]> "%USERPROFILE%\.streamlit\credentials.toml"
  echo email = "">> "%USERPROFILE%\.streamlit\credentials.toml"
)
echo Starting AI Itinerary Planner... (opens at http://localhost:8501)
streamlit run app.py
