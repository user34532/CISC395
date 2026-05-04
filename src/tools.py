def budget_breakdown(destination, budget, days):
    daily = budget / days
    return f"""Trip to {destination} for {days} days:

Total budget: ${budget}
Daily budget: ${daily:.2f}

Suggested:
- Hotel: ${daily * 0.4:.2f}
- Food: ${daily * 0.3:.2f}
- Activities: ${daily * 0.2:.2f}
- Transport: ${daily * 0.1:.2f}
"""

def get_weather(city):
    return f"The weather in {city} is mild and pleasant."

def search_guides_tool(query):
    return f"Guide info about {query}"

def run_agent(user_input):
    response = ""

    if "budget" in user_input.lower() or "$" in user_input:
        response += budget_breakdown("Paris", 1500, 10)

    if "weather" in user_input.lower():
        response += "\n" + get_weather("Paris")

    return response if response else "I couldn't find relevant tools to use."
