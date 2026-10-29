"""Offline unit tests — no API calls."""

import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from planner.export import to_markdown
from planner.models import Itinerary, TripRequest
from planner.prompts import build_prompt
from planner.sample import SAMPLE_ITINERARY


def test_prompt_contains_trip_details():
    trip = TripRequest("Paris", date(2026, 12, 1), 4, "Comfort", "Couple", "Relaxed",
                       ["Food", "Art & Culture"], "vegetarian")
    prompt = build_prompt(trip)
    for text in ["Paris", "4 day", "Comfort", "Couple", "Relaxed", "Food", "vegetarian",
                 "01 December 2026"]:
        assert text in prompt


def test_sample_round_trips_through_json():
    again = Itinerary.model_validate_json(SAMPLE_ITINERARY.model_dump_json())
    assert again == SAMPLE_ITINERARY


def test_markdown_export():
    md = to_markdown(SAMPLE_ITINERARY)
    assert md.startswith("# ")
    assert md.count("## Day ") == len(SAMPLE_ITINERARY.days)
    assert "Packing list" in md
