"""Gemini LLM integration."""

from google import genai
from google.genai import types

from .models import Itinerary, TripRequest
from .prompts import SYSTEM_INSTRUCTION, build_prompt

# "gemini-flash-latest" always points to Google's newest Flash model, so the app
# keeps working when older model versions are retired.
DEFAULT_MODEL = "gemini-flash-latest"
AVAILABLE_MODELS = [
    "gemini-flash-latest",    # recommended, auto-updates
    "gemini-3.8-flash",
    "gemini-3.6-flash",
    "gemini-3.5-flash-lite",  # fastest / highest free quota
]


def generate_itinerary(
    api_key: str,
    trip: TripRequest,
    model: str = DEFAULT_MODEL,
    temperature: float = 0.7,
) -> Itinerary:
    """Send the trip request to Gemini and return a validated Itinerary."""
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model=model,
        contents=build_prompt(trip),
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            temperature=temperature,
            response_mime_type="application/json",
            response_schema=Itinerary,
        ),
    )
    if isinstance(response.parsed, Itinerary):
        return response.parsed
    return Itinerary.model_validate_json(response.text)
