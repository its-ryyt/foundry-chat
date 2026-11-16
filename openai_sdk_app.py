from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://ai.azure.com/.default"
)

openai_client = OpenAI(
    base_url="https://samplecontent-8655-resource.openai.azure.com/openai/v1/",
    api_key=token_provider,
)

response = openai_client.chat.completions.create(
    model="gpt-5-mini-1",
    messages=[{"role": "user", "content": "Explain the OpenAI SDK in one sentence."}]
)

print(response.choices[0].message.content)