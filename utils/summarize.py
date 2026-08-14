import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_summary(topic):
    prompt = f"""
You are an AI Research Assistant.

Research the topic: {topic}

Return:
1. Overview
2. Key Points
3. Applications
4. Future Scope

Keep it simple and professional.
"""

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt,
    )

    return response.text