# Hardcoded Agent
from sample_functions import get_weather

from openai_module import generate_text_with_conversation
from prompts import react_system_prompt

# Available actions
available_actions = {
    "get_weather": get_weather,
    # Add more actions here
}
prompt = f"""Should I take an umbrella today in Toronto?"""

messages = [
    {"role": "system", "content": react_system_prompt},
    {"role": "user", "content": prompt}
]

turn_count = 1
max_turns = 5

while turn_count < max_turns:
    print(f"Turn {turn_count}:")
    print("-" * 20)
    turn_count += 1

    response = generate_text_with_conversation(messages, model="gpt-4")

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
            result = available_actions[function_name](**function_params)
            result_message = f"Action Response: {result}"
            messages.append({"role": "user", "content": result_message})
            print(result_message)
        else:
            print(f"Function {function_name} not found.")
    else:
        print("End of conversation.")
        break
