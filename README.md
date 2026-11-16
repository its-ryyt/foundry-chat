# Foundry Chat Training Project

This project contains multiple examples for calling Azure-hosted models using both:

- OpenAI SDK patterns
- Azure AI Foundry Project SDK patterns
- Responses API and Chat Completions API
- Sync and async request styles

## Project Files

- `openai_sdk_app.py`: OpenAI SDK + Azure AD token + Chat Completions (single prompt)
- `responses_app.py`: OpenAI SDK + Responses API (single prompt)
- `responses_chat.py`: OpenAI SDK + Responses API (multi-turn chat loop)
- `async_response_app.py`: Async OpenAI SDK + concurrent prompts with `asyncio.gather`
- `foundry_sdk_app.py`: Azure AI Projects SDK + OpenAI-compatible client + Chat Completions
- `foundry_directmodels_app.py`: Azure AI Projects SDK + Responses API + conversational state

## Prerequisites

1. Python 3.10+ installed
2. Azure subscription with access to:
   - Azure AI Foundry project
   - Azure OpenAI model deployment (example in this repo: `gpt-5-mini-1`)
3. Azure CLI installed
4. VS Code terminal (PowerShell)

## Step 1: Open Project Folder

In VS Code, open:

`C:\Project\Custom MCP Server Training\foundry-chat`

## Step 2: Create and Activate Virtual Environment

If `.venv` does not exist yet:

```powershell
python -m venv .venv
```

Activate in PowerShell:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

## Step 3: Install Dependencies

Install required libraries:

```powershell
python -m pip install --upgrade pip
pip install openai azure-identity azure-ai-projects
```

Optional (recommended): save dependencies

```powershell
pip freeze > requirements.txt
```

## Step 4: Authenticate to Azure

Login with Azure CLI:

```powershell
az login
```

If you use multiple tenants/subscriptions, set the correct subscription:

```powershell
az account set --subscription "<your-subscription-id-or-name>"
```

These scripts use Azure AD auth through `DefaultAzureCredential`, so your local login/session is used automatically.

## Step 5: Update Endpoint and Model Settings

Review these values in the scripts before running:

1. Azure OpenAI endpoint (`base_url`)
2. Foundry project endpoint (`project_endpoint`)
3. Model deployment name (`model`, `model_deployment`)

Current examples reference:

- Resource endpoint: `samplecontent-8655-resource.openai.azure.com`
- Project endpoint: `samplecontent-8655-resource.services.ai.azure.com`
- Model deployment: `gpt-5-mini-1`

Replace with your own values if different.

## Step 6: Run Each Example

### A) OpenAI SDK + Chat Completions

```powershell
python .\openai_sdk_app.py
```

### B) OpenAI SDK + Responses API (single request)

```powershell
python .\responses_app.py
```

### C) OpenAI SDK + Responses API (chat loop)

```powershell
python .\responses_chat.py
```

Type your messages. Enter `quit` or `exit` to stop.

### D) Async Responses with Concurrent Prompts

```powershell
python .\async_response_app.py
```

This runs 3 prompts concurrently and prints all answers.

### E) Foundry SDK + Chat Completions

```powershell
python .\foundry_sdk_app.py
```

### F) Foundry SDK + Responses API (stateful turns)

```powershell
python .\foundry_directmodels_app.py
```

Type prompts interactively. Enter `quit` to stop.

## Authentication Notes

These scripts use:

- `DefaultAzureCredential`
- `get_bearer_token_provider(..., "https://ai.azure.com/.default")`

Credential resolution order typically includes:

1. Environment variables
2. Managed identity (if running in Azure)
3. Azure CLI login
4. Developer tooling credentials

For local development, `az login` is usually enough.

## Security and Git Safety

A repository-level `.gitignore` is configured to prevent accidental commit of:

- Environment files (`.env`, `.env.*`)
- Certificates/keys/tokens (`*.pem`, `*.key`, `*secret*.json`, etc.)
- Virtual environments and local caches

Still important:

1. Never hardcode API keys or secrets in source code.
2. Prefer Azure AD token auth (already used here).
3. Rotate credentials immediately if you suspect exposure.
4. If a secret was already committed, remove it from git history.

## Common Troubleshooting

### 401/403 errors

- Ensure your account has access to the model deployment and project.
- Re-run `az login`.
- Confirm correct subscription/tenant with `az account show`.

### Model not found

- Verify deployment name (for example `gpt-5-mini-1`) exactly matches your Azure deployment.

### Endpoint errors

- Double-check `base_url` and `project_endpoint` values.
- Ensure region/resource names are correct.

### Import errors

- Confirm virtual environment is activated.
- Reinstall dependencies:

```powershell
pip install openai azure-identity azure-ai-projects
```

## Suggested Next Improvements

1. Move endpoint/model settings to environment variables.
2. Add a `requirements.txt` file to the repo.
3. Add a small config loader utility shared across all scripts.
4. Add structured logging and exception handling in each script.
5. Add `.env.example` with placeholder values (no real secrets).
