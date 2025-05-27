# Hardcoded Agent
from openai_module import generate_text_basic
from prompts import react_system_prompt

prompt = f"""Should I take an umbrella today in Toronto?"""

response = generate_text_basic(prompt, model="gpt-4", system_prompt=react_system_prompt)

print(response)
