"""Prompt templates (prompt engineering) for the itinerary planner."""

from .models import TripRequest

SYSTEM_INSTRUCTION = (
    "You are an expert local travel planner. You create realistic, well-paced "
    "itineraries with real, specific places, sensible travel times between them, "
    "and honest cost estimates in the destination's local currency. "
    "Never invent places that do not exist."
)


def build_prompt(trip: TripRequest) -> str:
    interests = ", ".join(trip.interests) if trip.interests else "a bit of everything"
    return f"""Plan a trip with these details:

- Destination: {trip.destination}
- Start date: {trip.start_date:%d %B %Y}
- Duration: {trip.days} day(s)
- Travelling as: {trip.travelers}
- Budget level: {trip.budget}
- Pace: {trip.pace}
- Interests: {interests}
- Special requests: {trip.notes or "none"}

Requirements:
1. Give the trip a short catchy title and a 2-3 sentence overview.
2. For each day give a theme, the calendar date, and 3-4 activities
   (Morning, Afternoon, Evening) with a specific place, a one-line
   description and an estimated cost.
3. Recommend one local dish or restaurant per day and a daily cost estimate.
4. Group nearby places on the same day to minimise travel.
5. Finish with an estimated total budget, a packing list (5-8 items)
   and 3-5 practical local tips.
"""
