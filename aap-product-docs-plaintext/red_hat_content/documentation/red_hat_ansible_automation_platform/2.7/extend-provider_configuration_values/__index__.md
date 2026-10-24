# Provider configuration values

Valid provider values for the automation intelligent assistant and when to use each one.

The `lightspeed_chatbot_default_provider` inventory variable accepts three values. Choose the value that matches your LLM service deployment type, not the API compatibility layer it exposes.

*Table 1. Provider values and usage*

| Provider value | LLM service type            | When to use                                                                                                                                      | Example URL pattern                                  |
| -------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------- |
| `rhoai`        | Red Hat Enterprise Linux AI | Your LLM is deployed on Red Hat Enterprise Linux AI with vLLM Server as the inference engine                                                     | `https://<your-rhelai-host>/v1`                      |
| `rhoai`        | Red Hat OpenShift AI        | Your LLM is deployed on Red Hat OpenShift AI single-model serving platform using vLLM runtime, or your model URL contains`rhoai` in the hostname | `https://litellm-*.apps.*.rhoai.*.com/v1`            |
| `openai`       | OpenAI                      | You are using the OpenAI API platform directly (not a self-hosted model with OpenAI-compatible API)                                              | `https://api.openai.com/v1`                          |
| `azure`        | Microsoft Azure OpenAI      | Your LLM is deployed on Microsoft Azure OpenAI service                                                                                           | `https://<your-resource>.openai.azure.com/openai/v1` |

Note:

The most common error is setting `lightspeed_chatbot_default_provider="openai"` when the model is actually deployed on Red Hat OpenShift AI with an OpenAI-compatible API endpoint. In this scenario, even though the API is OpenAI-compatible, the correct provider value is `rhoai` because that is the actual deployment platform.
