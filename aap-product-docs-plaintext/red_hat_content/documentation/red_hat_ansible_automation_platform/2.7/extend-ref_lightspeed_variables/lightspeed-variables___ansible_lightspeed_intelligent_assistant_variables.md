# Red Hat Ansible Lightspeed variables
## Automation intelligent assistant variables

Inventory file variables for the intelligent assistant.

| Variable name                             | Description                                                                                                                                                                                              | Required or optional | Default |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ------- |
| `lightspeed_chatbot_model_url`            | The inference API base URL on your LLM setup. For example, `https://your_inference_api/v1`.If you are using Microsoft Azure OpenAI, then set the base URL to `https://your_inference_api/openai/v1`.     | Optional             |         |
| `lightspeed_chatbot_model_verify_ssl`     | Controls whether SSL/TLS certificate verification is enabled or disabled when making HTTPS requests.                                                                                                     | Optional             | `true`  |
| `lightspeed_chatbot_default_provider`     | The provider type of your LLM setup by using one of the following values:<br>Red Hat Enterprise Linux AI: `rhelai`Red Hat OpenShift AI: `rhoai`OpenAI: `openai`Microsoft Azure OpenAI: `azure`           | Optional             | `rhoai` |
| `lightspeed_chatbot_model_extra_settings` | Use this parameter to pass a JSON dictionary of extra parameters to pass directly to the model provider, for settings not covered by other standard fields.<br>If you want to use Microsoft Azure OpenAI as the LLM provider, specify the value as `'{"api_type": ""}'`. | Optional             | `{}`    |
| `lightspeed_chatbot_agent_extra_settings` | Use this parameter to customize agent behavior, such as controlling the temperature of the LLM. For example, <br>`'{"chatbot_temperature_override": 1}'`.                                                | Optional             | `{}`    |
| `lightspeed_chatbot_chatbot_max_tokens`   | Maximum number of tokens to generate a chat response.                                                                                                                                                    | Optional             | `4096`  |
| `lightspeed_chatbot_http_port`            | Port number that Ansible Lightspeed intelligent assistant listens on for HTTP requests.                                                                                                                  | Optional             | `8085`  |
| `lightspeed_chatbot_model_id`             | The ID of the LLM model that is configured on your LLM setup.                                                                                                                                            | Optional             |         |
| `lightspeed_chatbot_model_api_key`        | The API token or the API key of your LLM setup. This token is sent along with the authorization header when an inference API is called.                                                                  | Optional             |         |

