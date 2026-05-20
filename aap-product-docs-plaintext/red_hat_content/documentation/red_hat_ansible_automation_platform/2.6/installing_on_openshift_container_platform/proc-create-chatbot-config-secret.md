# 6. Deploying the Ansible Lightspeed intelligent assistant on OpenShift Container Platform
## 6.2. Deploying the Ansible Lightspeed intelligent assistant
### 6.2.1. Creating a chatbot configuration secret

Create a configuration secret for the Ansible Lightspeed intelligent assistant, so that you can connect the intelligent assistant to the Ansible Automation Platform operator.

**Prerequisites**

- [You have installed and configured the Ansible Automation Platform operator](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/installing_on_openshift_container_platform/index#proc-install-operator-chatbot).

**Procedure**

1. Log in to Red Hat OpenShift Container Platform as an administrator.

2. Navigate to Workloads → Secrets.

3. From the **Projects** list, select the namespace that you created when you installed the Ansible Automation Platform operator.

4. Click Create → Key/value secret.

5. In the **Secret name** field, enter a unique name for the secret. For example, `chatbot-configuration-secret`.

6. Add the following keys and their associated values individually:

| Key | Value |
| --- | --- |
| <br> **Settings for all LLM setups** | |
| <br> `chatbot_model` | <br>  Enter the LLM model name that is configured on your LLM setup. |
| <br> `chatbot_url` | <br>  Enter the inference API base URL on your LLM setup. For example, `https://your_inference_api/v1`. <br>  If you are using Microsoft Azure OpenAI, then set the base URL to `https://your_inference_api/openai/v1`. |
| <br> `chatbot_token` | <br>  Enter the API token or the API key. This token is sent along with the authorization header when an inference API is called. |
| <br> `chatbot_llm_provider_type` | <br> *Optional*<br>  Enter the value as per the provider type of your LLM setup:    <br>    Red Hat Enterprise Linux AI: `rhelai_vllm`    Red Hat OpenShift AI: `rhoai_vllm`    OpenAI: `openai`    Microsoft Azure OpenAI: `azure_openai` |
| <br> `chatbot_model_config_extras` | <br> *Optional*<br>  Use this field to pass a JSON dictionary of extra parameters to pass directly to the model provider, for settings not covered by other standard fields. <br>  For example, you can specify a parameter `api_version` for Microsoft Azure OpenAI in the JSON format `'{"api_version": "<your API version>"}'`. |
| <br> `chatbot_agent_config_extras` | <br> *Optional*<br>  Use this parameter to customize agent behavior, such as controlling the temperature of the LLM. <br>  For example, '{"chatbot_temperature_override": 1}'. |
| <br> **Additional settings for MCP server configuration** | |
| <br>  `aap_gateway_url`  `aap_controller_url` | <br>  Configure a Model Context Protocol (MCP) server that interfaces with the Ansible Lightspeed intelligent assistant. <br>  The values `aap_gateway_url` and `aap_controller_url` are internal URLs accessible to the platform gateway and automation controller services on the OpenShift cluster. For example, if the name of your Ansible Automation Platform custom resource is `myaap`, these URLs will be:    <br>  `aap_gateway_url`: `http://myaap`  `aap_controller_url`: `http://myaap-controller-service`  <br>  For MCP server configuration:    <br>    If none of these parameters are configured, no MCP server is provisioned or registered with the underlying LLM’s tool at runtime.     If you configure the `aap_gateway_url` parameter only, the Ansible Lightspeed Service MCP server is provisioned. Authentication attempts to use the JSON Web Token (JWT) token associated with the user’s authenticated context.     If you configure both parameters `aap_gateway_url` and `aap_controller_url`, the Ansible Lightspeed Service MCP server and Ansible Automation Platform Controller Service MCP server are both configured. Authentication attempts to use the JWT token associated with the user’s authenticated context. |

7. Click **Create**. The chatbot authorization secret is successfully created.

