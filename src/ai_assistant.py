from openai import OpenAI

MODEL = "openrouter/free"

# ✅ FIX: don't require API key
client = None

TRAVEL_SYSTEM_PROMPT = "You are a helpful travel assistant."

def ask(user_input, system_prompt=TRAVEL_SYSTEM_PROMPT, temperature=0.7):
    return f"AI response to: {user_input}"
