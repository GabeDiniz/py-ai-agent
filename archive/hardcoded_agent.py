from openai_module import generate_text_basic
from sample_functions import get_weather

# This is an example of a Hard coded agent

current_weather = get_weather("Toronto")
# Here, we are injecting the result from the function above, inside the prompt below
prompt = f"""
Should I take an umbrella to go out today in Toronto based on the following conditions: {current_weather}?
"""

response = generate_text_basic(prompt)

print(response)