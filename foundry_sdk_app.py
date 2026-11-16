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
response = openai_client.chat.completions.create(
    model=model_deployment,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is Microsoft Foundry?"}
    ]
)

print(response.choices[0].message.content)