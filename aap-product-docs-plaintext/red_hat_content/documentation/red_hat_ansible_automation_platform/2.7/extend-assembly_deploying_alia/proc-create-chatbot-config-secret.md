# Deploy the automation intelligent assistant
## Create a chatbot configuration secret

Create a configuration secret for the intelligent assistant so that you can connect it to the Ansible Automation Platform operator.

### Before you begin

- [You have installed and configured the Ansible Automation Platform operator](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_operator_install_operator "As a system administrator, you can use Ansible Automation Platform Operator to deploy new Ansible Automation Platform instances in your OpenShift environment.").

### Procedure

1.  Log in to Red Hat OpenShift Container Platform as an administrator.
2.  Navigate to Workloads> (and then)Secrets.
3.  From the **Projects** list, select the namespace that you created when you installed the Ansible Automation Platform operator.
4.  Click Create> (and then)Key/value secret.
5.  In the **Secret name** field, enter a unique name for the secret. For example, `chatbot-configuration-secret`.
6.  Add the following keys and their associated values individually:
| Key                                                       | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br> **Settings for all LLM setups**                      | |
| <br> `chatbot_model`                                      | <br>Enter the LLM model name that is configured on your LLM setup.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| <br> `chatbot_url`                                        | <br>Enter the inference API base URL on your LLM setup. For example, `https://your_inference_api/v1`. If you are using Microsoft Azure OpenAI, then set the base URL to `https://your_inference_api/openai/v1`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| <br> `chatbot_token`                                      | <br>Enter the API token or the API key. This token is sent along with the authorization header when an inference API is called.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| <br> `chatbot_llm_provider_type`                          | <br> *Optional*<br>Enter the value as per the provider type of your LLM setup:<br>  Red Hat Enterprise Linux AI: `rhelai_vllm`  Red Hat OpenShift AI: `rhoai_vllm`  OpenAI: `openai`  Microsoft Azure OpenAI: `azure_openai`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| <br> `chatbot_model_config_extras`                        | <br> *Optional*<br>Use this field to pass a JSON dictionary of extra parameters to pass directly to the model provider, for settings not covered by other standard fields.<br>For example, you can specify a parameter `api_version` for Microsoft Azure OpenAI in the JSON format `'{"api_version": "<your API version>"}'`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `chatbot_agent_config_extras`                             | <br>*Optional*<br>Use this parameter to customize agent behavior, such as controlling the temperature of the LLM. For example, `'{"chatbot_temperature_override": 1}`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| <br> **Additional settings for MCP server configuration** | |
| `aap_gateway_url`   `aap_controller_url`                  | <br>Configure a Model Context Protocol (MCP) server that interfaces with the intelligent assistant.<br>The values `aap_gateway_url` and `aap_controller_url` are internal URLs accessible to the platform gateway and automation controller services on the OpenShift cluster. For example, if the name of your Ansible Automation Platform custom resource is `myaap`, these URLs will be:<br>  `aap_gateway_url`: `http://myaap`  `aap_controller_url`: `http://myaap-controller-service` <br>For MCP server configuration:<br>  If none of these values are configured, no MCP server is provisioned or registered with the underlying LLM’s tool at runtime.  If you configure the `aap_gateway_url` value only, the Ansible Lightspeed Service MCP server is provisioned. Authentication attempts to use the JSON Web Token (JWT) token associated with the user’s authenticated context.  If you configure both values `aap_gateway_url` and `aap_controller_url`, the Ansible Lightspeed Service MCP server and Ansible Automation Platform Controller Service MCP server are both configured. Authentication attempts to use the JWT token associated with the user’s authenticated context. |

7.  Click **Create**. The chatbot authorization secret is successfully created.

### Examples of chatbot configuration secrets

The following snippet shows a few examples of secrets configuration for different LLM models.

```
# Example of a secret configuration for Red Hat OpenShift AI
apiVersion: v1
kind: Secret
metadata:
name: chatbot-configuration-secret
namespace: aap
stringData:
chatbot_llm_provider_type: rhoai_vllm
chatbot_url: https://llm-dev-wisdom-model-staging.apps.stage2-west.v2dz.p1.openshiftapps.com/v1
chatbot_model: granite-3.3-8b-instruct
chatbot_token: <token number>
```

```
# Example of a secret configuration for OpenAI
apiVersion: v1
kind: Secret
metadata:
name: chatbot-configuration-secret
namespace: aap
stringData:
chatbot_llm_provider_type: openai
chatbot_url: https://api.openai.com/v1
chatbot_model: gpt-4o-mini
chatbot_token: <token number>
```

```
# Example of a secret configuration for Microsoft Azure OpenAI
apiVersion: v1
kind: Secret
metadata:
name: chatbot-configuration-secret
namespace: aap
stringData:
chatbot_llm_provider_type: azure_openai
chatbot_url: https://ols-test.openai.azure.com
chatbot_model: gpt-4o-mini
chatbot_token: <token number>
chatbot_model_config_extras: '{"api_version": "2025-01-01-preview"}'
```

