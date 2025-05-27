# Hardcoded Agent
from sample_functions import get_weather

from openai_module import generate_text_basic
from prompts import react_system_prompt

# Available actions
available_actions = {
    "get_weather": get_weather,
    # Add more actions here
}
prompt = f"""Should I take an umbrella today in Toronto?"""

response = generate_text_basic(prompt, model="gpt-4", system_prompt=react_system_prompt)

print(f"Response: {response}")
# Need to instruct the model to call the action or the function

# Example of json response from the model
json_response = {
    "function_name": "get_weather",
    "function_params": {
        "city": "Toronto"
    }
}

# Execute the action from response
if json_response:
    function_name = json_response[0].get("function_name")
    function_params = json_response[0].get("function_params")

    if function_name in available_actions:
        # Call the function with parameters
        action_function = available_actions[function_name](**function_params)
        print(f"Action Response: {action_function}")
    else:
        print(f"Function {function_name} not found.")
