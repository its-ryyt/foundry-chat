import asyncio
from openai import AsyncOpenAI
from azure.identity.aio import DefaultAzureCredential, get_bearer_token_provider  # async version

base_url="https://samplecontent-8655-resource.openai.azure.com/openai/v1/"
defaultCredential = "https://ai.azure.com/.default"
model_deployment = "gpt-5-mini-1"  # your deployment name


async def ask(client, prompt):
    response = await client.responses.create(
        model=model_deployment,
        input=prompt
    )
    return response.output_text


async def main():
    # Async credential: close it when finished
    async with DefaultAzureCredential() as credential:
        token_provider = get_bearer_token_provider(
            credential, defaultCredential
        )

        async with AsyncOpenAI(
            base_url=base_url,
            api_key=token_provider,
        ) as client:

            # Issue three requests concurrently instead of one after another
            prompts = [
                "Explain quantum computing briefly.",
                "Summarize the benefits of async I/O.",
                "Give a one-sentence definition of machine learning."
            ]
            results = await asyncio.gather(*(ask(client, p) for p in prompts))

            for prompt, output in zip(prompts, results):
                print(f"Q: {prompt}\nA: {output}\n")


asyncio.run(main())