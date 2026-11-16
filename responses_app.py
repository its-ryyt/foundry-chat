from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://ai.azure.com/.default"
)

openai_client = OpenAI(
    base_url="https://samplecontent-8655-resource.openai.azure.com/openai/v1/",
    api_key=token_provider,
)

response = openai_client.responses.create(
    model="gpt-5-mini-1",
    instructions="You are a helpful assistant. Microsoft Foundry is Microsoft's Azure platform "
                 "for building AI apps and agents (formerly Azure AI Foundry). Answer briefly.",
    input="What is Microsoft Foundry?",
    # temperature=0.8,  # Higher temperature for more creativity
    # max_output_tokens=200  # Limit response length
)

print(response.output_text)
# print(f"Response: {response.output_text}")
# print(f"Response ID: {response.id}")
# print(f"Tokens used: {response.usage.total_tokens}")
# print(f"Status: {response.status}")