import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")


def get_story_prompt(theme, place, prompt):
    return f"""
    Create a fun and engaging children's story of theme : {theme} {"happening in " + place if place else ""} under 200 words with emojis, markdown for bold, underline, italic with the following details:

    {prompt}

    Include playful and imaginative elements suitable for children.
    Incorporate dialogues to make the story interactive.
    Ensure the story has a positive and educational message.

    Dont give any note!
    """


def call_llm(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"

    payload = {
        "messages": [{"role": "user", "content": prompt}],
        "model": "llama3-8b-8192",
    }

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        response_data = response.json()
        print("Mistral AI called")
        return response_data["choices"][0]["message"]["content"]
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)
        return ""


def generate_story(*args):
    story_prompt = get_story_prompt(*args)
    story = call_llm(story_prompt)
    return story_prompt, story
