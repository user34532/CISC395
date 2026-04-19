import os
from openai import OpenAI
from dotenv import load_dotenv
from src.rag import search_guides

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    api_key=API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

def ask(prompt):
    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def rag_ask(question):
    chunks = search_guides(question)

    if not chunks:
        return "No guide data found. Please add guides and rebuild the index."

    context = "\n\n".join(chunks)

    prompt = f"""
Answer ONLY using the information below.

{context}

Question: {question}
"""

    return ask(prompt)
