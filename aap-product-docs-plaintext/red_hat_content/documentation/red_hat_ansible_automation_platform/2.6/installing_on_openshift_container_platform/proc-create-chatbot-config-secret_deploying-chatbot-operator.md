# 5. Deploying the Ansible Lightspeed intelligent assistant on OpenShift Container Platform
## 5.2. Deploying the Ansible Lightspeed intelligent assistant
### 5.2.1. Creating a chatbot configuration secret




Create a configuration secret for the Ansible Lightspeed intelligent assistant, so that you can connect the intelligent assistant to the Ansible Automation Platform operator.

**Prerequisites**

-  [You have installed and configured the Ansible Automation Platform operator](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/installing_on_openshift_container_platform/index#proc-install-operator-chatbot) .


**Procedure**

1. Log in to Red Hat OpenShift Container Platform as an administrator.
1. Navigate toWorkloads→Secrets.
1. From the **Projects** list, select the namespace that you created when you installed the Ansible Automation Platform operator.
1. ClickCreate→Key/value secret.
1. In the **Secret name** field, enter a unique name for the secret. For example, `    chatbot-configuration-secret` .
1. Add the following keys and their associated values individually:

| Key | Value |
| --- | --- |
|  **Settings for all LLM setups** |
|  `chatbot_model` | Enter the LLM model name that is configured on your LLM setup. |
|  `chatbot_url` | Enter the inference API base URL on your LLM setup. For example, `https://your_inference_api/v1` . |
|  `chatbot_token` | Enter the API token or the API key. This token is sent along with the authorization header when an inference API is called. |
|  `chatbot_llm_provider_type` |  _Optional_

Enter the provider type of your LLM setup by using one of the following values:

- Red Hat Enterprise Linux AI: `    rhelai_vllm`
- Red Hat OpenShift AI: `    rhoai_vllm` |
|  **Additional settings for MCP server configuration** |
| -  `    aap_gateway_url`
-  `    aap_controller_url` | Configure a Model Context Protocol (MCP) server that interfaces with the Ansible Lightspeed intelligent assistant.

The values `aap_gateway_url` and `aap_controller_url` are internal URLs accessible to the platform gateway and automation controller services on the OpenShift cluster. For example, if the name of your Ansible Automation Platform custom resource is `myaap` , these URLs will be:

-  `    aap_gateway_url` : `    http://myaap`
-  `    aap_controller_url` : `    http://myaap-controller-service`


For MCP server configuration:

- If none of these parameters are configured, no MCP server is provisioned or registered with the underlying LLM’s tool at runtime.
- If you configure the `    aap_gateway_url` parameter only, the Ansible Lightspeed Service MCP server is provisioned. Authentication attempts to use the JSON Web Token (JWT) token associated with the user’s authenticated context.
- If you configure both parameters `    aap_gateway_url` and `    aap_controller_url` , the Ansible Lightspeed Service MCP server and Ansible Automation Platform Controller Service MCP server are both configured. Authentication attempts to use the JWT token associated with the user’s authenticated context. |



1. Click **Create** . The chatbot authorization secret is successfully created.


