import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai.errors import ServerError

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_summary(topic, search_results):

    context = ""

    for result in search_results:
        context += f"""
Title: {result['title']}
URL: {result['url']}
Content: {result['content']}

"""

    prompt = f"""
You are an AI Research Assistant.

Research Topic:
{topic}

Use ONLY the information below.

{context}

Generate a report with:

# Overview

# Key Findings

# Important Insights

# Applications

# Future Scope

Finally add a section:

# References

List every URL used.
"""

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-flash-latest",
                contents=prompt
            )
            return response.text

        except ServerError:
            if attempt < 2:
                time.sleep(3)
            else:
                return "⚠️ Gemini is currently experiencing high traffic. Please try again in a few moments."