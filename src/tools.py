import json

# -------------------------------
# TOOL 1: Budget Breakdown
# -------------------------------
def budget_breakdown(total_budget, days):
    daily = total_budget / days

    breakdown = {
        "accommodation": round(daily * 0.4, 2),
        "food": round(daily * 0.25, 2),
        "transport": round(daily * 0.15, 2),
        "activities": round(daily * 0.2, 2),
    }

    return json.dumps({
        "daily_budget": round(daily, 2),
        "breakdown": breakdown
    })


# -------------------------------
# TOOL 2: Weather
# -------------------------------
def get_weather(city):
    return json.dumps({
        "city": city,
        "temperature_C": "20",
        "description": "Sunny"
    })


# -------------------------------
# TOOL 3: Guides Search
# -------------------------------
def search_guides_tool(query):
    return json.dumps({
        "results": [
            f"Top places for {query}",
            "Visit landmarks",
            "Try local food"
        ]
    })


# -------------------------------
# REACT AGENT (no API)
# -------------------------------
def run_agent(user_input):
    text = user_input.lower()

    print("\n[Agent Thinking...]\n")

    final_answer = "Your travel info is ready."

    if "budget" in text:
        print("[Tool call] budget_breakdown")
        result = budget_breakdown(1200, 8)
        print("[Tool result]", result)

    if "weather" in text:
        print("[Tool call] get_weather")
        result = get_weather("Paris")
        print("[Tool result]", result)

    if "tokyo" in text:
        print("[Tool call] search_guides_tool")
        result = search_guides_tool("Tokyo")
        print("[Tool result]", result)

    print("\nFinal Answer:\n" + final_answer + "\n")

    return final_answer


# -------------------------------
# TEST
# -------------------------------
if __name__ == "__main__":
    print(budget_breakdown(1200, 8))
    print(get_weather("Paris"))
    print(search_guides_tool("Tokyo"))
