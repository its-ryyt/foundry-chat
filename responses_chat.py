from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://ai.azure.com/.default"
)

openai_client = OpenAI(
    base_url="https://samplecontent-8655-resource.openai.azure.com/openai/v1/",
    api_key=token_provider,
)

previous_id = None

while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ("quit", "exit"):
        break

    response = openai_client.responses.create(
        model="gpt-5-mini-1",
        instructions="You are a helpful assistant.",
        input=user_input,
        previous_response_id=previous_id   # links to the earlier turn
    )

    print("AI:", response.output_text)
    previous_id = response.id