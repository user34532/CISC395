import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    api_key=API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

MODEL = "openrouter/free"

TRAVEL_SYSTEM_PROMPT = "You are a helpful travel assistant who gives clear, practical, and friendly advice."


def ask(prompt, system_prompt=TRAVEL_SYSTEM_PROMPT, temperature=0.7):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        temperature=temperature,
        extra_body={"reasoning": {"enabled": True}}
    )

    try:
        content = response.choices[0].message.content

        # Handle OpenRouter case where content may be None
        if content is None:
            return "No response content returned."

        return content.strip()

    except Exception as e:
        return f"Error: {e}"


# ✅ Prompt Chaining Function
def generate_trip_briefing(city, country, notes=None):
    # Call 1: Overview
    overview_prompt = f"Give a short travel overview for {city}, {country}."

    if notes:
        overview_prompt += f" The traveler has these notes: {notes}"

    overview = ask(overview_prompt)

    # Call 2: Packing list (uses overview = chaining)
    packing_prompt = f"Based on this trip: {overview}, suggest a practical packing list."

    packing = ask(packing_prompt)

    return overview, packing


# ✅ TEST BLOCK (THIS WAS YOUR MISSING PIECE BEFORE)
if __name__ == "__main__":
    print("\n--- Trip Briefing Test ---")

    overview, packing = generate_trip_briefing("Tokyo", "Japan")

    print("\nOverview:")
    print(overview)

    print("\nPacking list:")
    print(packing)