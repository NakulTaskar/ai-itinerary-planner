"""Data models for trip requests and AI-generated itineraries.

The `Itinerary` model doubles as the JSON schema passed to Gemini, so the LLM
returns structured data we can render as cards instead of free-form text.
"""

from dataclasses import dataclass, field
from datetime import date

from pydantic import BaseModel


# ---------- User input ----------
@dataclass
class TripRequest:
    destination: str
    start_date: date
    days: int
    budget: str
    travelers: str
    pace: str
    interests: list[str] = field(default_factory=list)
    notes: str = ""


# ---------- LLM output (structured) ----------
class Activity(BaseModel):
    time_of_day: str          # Morning / Afternoon / Evening
    title: str
    description: str
    place: str
    estimated_cost: str


class DayPlan(BaseModel):
    day: int
    date: str
    theme: str
    activities: list[Activity]
    food_recommendation: str
    daily_cost: str


class Itinerary(BaseModel):
    trip_title: str
    overview: str
    days: list[DayPlan]
    estimated_total_budget: str
    packing_list: list[str]
    local_tips: list[str]
