from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

project_endpoint = "https://samplecontent-8655-resource.services.ai.azure.com/api/projects/samplecontent-8655"
model_deployment = "gpt-5-mini-1"  # your deployment name

# 1. Connect to the project
project_client = AIProjectClient(
    credential=DefaultAzureCredential(),
    endpoint=project_endpoint
)

# 2. Get an OpenAI-compatible chat client
openai_client = project_client.get_openai_client()

# 3. Send a prompt
# Track responses
last_response_id = None

# Loop until the user wants to quit
print("Assistant: Enter a prompt (or type 'quit' to exit)")
while True:
    input_text = input('\nYou: ')
    if input_text.lower() == "quit":
        print("Assistant: Goodbye!")
        break

    # Get a response
    request_args = {
        "model": model_deployment,
        "instructions": "You are a helpful AI assistant that explains technology concepts clearly.",
        "input": input_text,
    }
    if last_response_id:  # only send it after the first turn
        request_args["previous_response_id"] = last_response_id

    response = openai_client.responses.create(**request_args)

    assistant_text = response.output_text
    print("\nAssistant:", assistant_text)
    last_response_id = response.id