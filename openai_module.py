from openai import OpenAI
import os
from dotenv import load_dotenv

# Load env vars
load_dotenv()

# Create openAI instance class
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_text_basic(prompt: str, model = "gpt-3.5-turbo", system_prompt: str = "You are help"):
    response = openai_client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content