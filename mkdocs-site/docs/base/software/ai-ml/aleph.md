---
title: "Aleph"
slug: "aleph"
lang: "base"

source_wiki_title: "Aleph"
source_hash: "81f22471529c779715e6c91e0dc2bada"
last_synced: "2026-09-13T00:40:43.713374+00:00"
last_processed: "2026-09-13T01:32:29.861216+00:00"

tags:
  - ai-and-machine-learning

keywords:
  - "empty or truncated answer"
  - "science models"
  - "~/.claude/settings.json"
  - "model list"
  - "HTTP 503 scaled to zero"
  - "HTTP 429"
  - "OpenAI Python SDK"
  - "model scaling to zero"
  - "Aleph inference gateway"
  - "Alliance username"
  - "OpenAI-compatible endpoints"
  - "reasoning_effort"
  - "Vulcan cluster"
  - "retry guidance"
  - "failed request"
  - "OpenAI and Anthropic SDK"
  - "Claude Code"
  - "reduce request rate and retry"
  - "automatic API key"
  - "HTTP 502/504 client timeout"
  - "Aleph platform"
  - "Aleph base URL"
  - "gpt-oss-120b"
  - "model aliases"
  - "max_tokens"

questions:
  - "How can an Alliance user obtain and activate their Aleph API key for accessing models on the Vulcan cluster?"
  - "What are the steps and required commands to make a successful inference request to Aleph using curl or the OpenAI Python SDK?"
  - "What limitations and performance considerations should users be aware of when using Aleph as a proof‑of‑concept service?"
  - "How do the OpenAI and Anthropic Python SDKs interact with Aleph, and what limitations do they have regarding commercial API keys and model access?"
  - "What is the behavior of models that are scaled to zero on Aleph, and how should clients handle responses indicating a model is not ready?"
  - "Where can users seek assistance or request new models for Aleph on Vulcan, and what information should they provide in their support request?"
  - "Which field in the API response holds the model’s answer?"
  - "How should the Aleph base URL be formatted when using the OpenAI Python SDK?"
  - "What is the role of the “reasoning_effort” parameter in the request?"
  - "What actions should be taken when an HTTP 429 response is received?"
  - "How should HTTP 503, 502, 504, or client timeout errors be handled according to the guidance?"
  - "What checks and steps are recommended if the answer returned is empty or truncated?"
  - "What details must be provided (and what must be omitted) when reporting a failed request to Aleph?"
  - "How should the `~/.claude/settings.json` file be configured to run Claude Code against the Aleph Anthropic‑compatible endpoint?"
  - "What do the client‑side aliases `opus`, `sonnet`, and `haiku` represent in Aleph, and how does their compatibility depend on the Claude Code version and model capabilities?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

**Aleph** is the AI inference gateway on the Vulcan cluster at the University of Alberta in Edmonton. It gives Alliance users API access to hosted models through OpenAI- and Anthropic-compatible endpoints, so most existing SDKs and tools work with nothing more than a change of base URL.

Inference runs entirely on Vulcan hardware under Alliance operation. Nothing leaves the cluster, and there is no commercial API in the path.

*   **Model list, documentation and examples:** https://inference.vulcan.alliancecan.ca/
*   **Web chat interface:** https://llm.vulcan.alliancecan.ca/ — a ChatGPT-style interface, open to any Alliance user with no key required. If that is all you need, you can stop here.

!!! warning "Proof of Concept Service"
    Aleph is a proof of concept with no service-level agreement (SLA). Capacity is shared and demand has been well beyond what we expected, so availability and performance vary.

## Get your API key

!!! note "Automatic Key Generation"
    **There is no key to request manually.** Aleph generates your personal key automatically the first time you log into Vulcan.

### 1. Request Vulcan access

You need an Alliance account with access to Vulcan. Go to [Access Systems in CCDB](https://ccdb.alliancecan.ca/me/access_systems) and select **Vulcan**.

### 2. Log into Vulcan

Once access is granted, SSH in with your Alliance username:

```bash
ssh YOUR_ALLIANCE_USERNAME@vulcan.alliancecan.ca
```

!!! note "Important"
    **That first login is what triggers key generation.** Requesting access in CCDB is not enough on its own.

### 3. Find your key

The key is written to a hidden file in your Vulcan home directory. It can take a few minutes to appear after your first login.

```bash
ls -la ~/.aleph_tyk.env
cat ~/.aleph_tyk.env
```

Note the leading dot: the file will not show up in a plain `ls` listing, which is why the example uses `ls -la`.

!!! note "Single API Key"
    **One key covers every model on Aleph.** There is no per-model key, and the same key works for both the OpenAI- and Anthropic-compatible endpoints.

!!! warning "Security Notice"
    Treat it as a password. Keep it out of shared notebooks, Git repositories, screenshots and support requests.

### 4. Load the key into your shell

```bash
set -a
source ~/.aleph_tyk.env
set +a
```

Your key is now in the environment as `TYK_KEY`, including for programs launched from that shell. Repeat this in each new shell.

Check that it works by listing the models:

```bash
curl --silent --show-error --fail-with-body \
  --max-time 120 \
  -H "Authorization: Bearer $TYK_KEY" \
  https://inference.vulcan.alliancecan.ca/v1/models
```

A successful request returns JSON listing the available chat models. Add `?all=true` to include science, embedding, vision and other non-chat models.

### If the key file does not appear

Automatic key generation is a recent addition. If the file has not turned up after a few minutes, email [support@tech.alliancecan.ca](mailto:support@tech.alliancecan.ca), mentioning **Aleph on Vulcan**, with your Alliance username and roughly when you first logged in. Reports genuinely help at this stage.

!!! warning "Do Not Send Your Key"
    **Do not send your key.**

## Make a request

These examples assume you have loaded `~/.aleph_tyk.env`. Calls run on Aleph's hosted compute — you do not need to start a model server, reserve a GPU or submit a Slurm job to use it.

!!! tip "Model Identifiers"
    Use the exact model identifier shown in the model list.

### curl

```bash
curl --silent --show-error --fail-with-body \
  --max-time 120 --retry 0 \
  https://inference.vulcan.alliancecan.ca/v1/chat/completions \
  -H "Authorization: Bearer $TYK_KEY" \
  -H "Content-Type: application/json" \
  --data-binary '{
    "model": "gpt-oss-120b",
    "messages": [{
      "role": "user",
      "content": "What is 17 times 19? Reply with only the integer."
    }],
    "reasoning_effort": "low",
    "max_tokens": 1024
  }'
```

The answer is in `choices[0].message.content`.

### OpenAI Python SDK

Use Aleph's base URL, including `/v1`, with your Aleph key in place of a commercial one:

```python
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://inference.vulcan.alliancecan.ca/v1",
    api_key=os.environ["TYK_KEY"],
    timeout=120.0,
    max_retries=0,
)

response = client.chat.completions.create(
    model="gpt-oss-120b",
    messages=[{
        "role": "user",
        "content": "What is 17 times 19? Reply with only the integer.",
    }],
    reasoning_effort="low",
    max_tokens=1024,
)

print(response.choices[0].message.content)
```

### Anthropic Python SDK

Same key, with the `/anthropic` base URL. The SDK appends `/v1/messages`.

```python
import os
from anthropic import Anthropic

client = Anthropic(
    base_url="https://inference.vulcan.alliancecan.ca/anthropic",
    api_key=os.environ["TYK_KEY"],
    timeout=120.0,
    max_retries=0,
)

response = client.messages.create(
    model="qwen38-27b",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": "What is 17 times 19? Reply with only the integer.",
    }],
)

for block in response.content:
    if block.type == "text":
        print(block.text)
```

!!! note "SDK Usage"
    The OpenAI and Anthropic SDKs are just client libraries. Using one with Aleph does not require a commercial API key and does not give you access to that company's models.

!!! tip "Model-Specific Parameters"
    Thinking controls vary between models — some take reasoning effort levels, others switch thinking on or off — so check the model's entry in the catalogue rather than assuming they behave alike.

## How models scale

Aleph is compute-constrained. Some models stay always-up; the rest scale to zero when idle and start on demand. The model list marks which is which.

!!! note "Scaled-to-Zero Models"
    If you call a model that is scaled to zero, the response tells you it is not ready and roughly when to come back, usually a few minutes, or that there is not enough free compute to start it right now. Hit the endpoint, read the response, come back when it says. Once a model is up it should stay up for you.

!!! warning "Retry Guidance"
    Send one request at a time while a model is starting, and follow the retry guidance in the response rather than retrying in a tight loop.

!!! warning "Incomplete Responses"
    A model's context window and its maximum output are separate limits, and on reasoning models the output budget covers the thinking as well as the answer — a request can spend the whole budget reasoning and return nothing. A response with `finish_reason: "length"` (OpenAI format) or `stop_reason: "max_tokens"` (Anthropic format) is incomplete, even though the HTTP status is `200`.

## Science models

!!! note "Beyond LLMs"
    Aleph is not only for LLMs, and we would like it to be more science than chat. It is built to run as an AI tools server alongside your Slurm jobs — protein folding, genomics, weather, materials, forecasting and similar — callable directly from your code.

!!! tip "Science Model Details"
    Science models often use different input formats and endpoint paths, so follow the examples on their individual model cards.

## Request a model

!!! note "Requesting New Models"
    **If your work depends on a model we are not hosting, tell us and we will look at hosting it.** Email [support@tech.alliancecan.ca](mailto:support@tech.alliancecan.ca), mentioning **Aleph on Vulcan**, with the model name or upstream link and a short description of what you want to do with it. Hosting depends on compatibility and available capacity.

The same goes for anything you need switched to always-up, or kept running for a planned evaluation.

## Support

Contact [support@tech.alliancecan.ca](mailto:support@tech.alliancecan.ca) and mention **Aleph on Vulcan**.

| Problem                            | First checks                                                                                                   |
| :--------------------------------- | :------------------------------------------------------------------------------------------------------------- |
| Key file is missing                | Confirm Vulcan access was granted and that you have completed an SSH login. Allow a few minutes.                 |
| HTTP `401` or `403`                | Re-run the `source` step and check your client is sending the key to the right endpoint.                       |
| HTTP `429`                         | Reduce your request rate and concurrency, and follow the retry guidance in the response.                       |
| HTTP `503`                         | Normal for a model that is scaled to zero. Read the response and retry when it says.                           |
| HTTP `502`, `504` or a client timeout | Note the time, model, elapsed duration and response. Check availability before assuming the key is bad.      |
| Empty or truncated answer          | Check the finish reason, output budget and thinking settings.                                                  |

For a failed request, include your Alliance username, the date and time (UTC preferred), the model identifier and endpoint, the HTTP status and error message, and a minimal example with anything sensitive removed.

!!! warning "Support Requests"
    **Do not send your API key or authorization headers.**

Aleph records operational usage information — account identity, model, token counts, request duration and status — for accounting and troubleshooting.

## Advanced: Claude Code

Claude Code can run against Aleph through the Anthropic-compatible endpoint. Put your key in `~/.claude/settings.json`, merging with anything already there:

```json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "PutURKeyHere",
    "ANTHROPIC_BASE_URL": "https://inference.vulcan.alliancecan.ca/anthropic",
    "API_TIMEOUT_MS": "300000",
    "CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS": "1",
    "CLAUDE_CODE_ATTRIBUTION_HEADER": "0",
    "CLAUDE_CODE_ALWAYS_ENABLE_EFFORT": "1",
    "CLAUDE_CODE_AUTO_COMPACT_WINDOW": "110000",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "qwen35-122b",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "qwen38-27b",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "gpt-oss-120b"
  },
  "model": "opus",
  "effortLevel": "high"
}
```

`opus`, `sonnet` and `haiku` here are client-side aliases mapped to Aleph models. They do not select Anthropic's Claude models. Compatibility depends on your Claude Code version and on the capabilities of the model you map to.