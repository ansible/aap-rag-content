# Understand the provider configuration variable

The provider configuration variable ensures the automation intelligent assistant communicates correctly with your LLM service.

The `lightspeed_chatbot_default_provider` inventory variable controls how the automation intelligent assistant formats API requests and handles responses when communicating with your large language model (LLM) service. Different LLM providers have distinct API specifications, authentication methods, and response formats.

The provider value must match your LLM service's actual deployment platform—not the API compatibility layer it exposes. For example, if you deploy a model on Red Hat OpenShift AI that exposes an OpenAI-compatible API, use `rhoai` as the provider value, not `openai`.

Configuration example:

```
lightspeed_chatbot_model_url="https://litellm-litemaas.apps.prod.rhoai.rh-aiservices-bu.com/v1"
lightspeed_chatbot_default_provider="rhoai"
```

For the complete list of valid provider values and when to use each one, see Provider configuration values.
