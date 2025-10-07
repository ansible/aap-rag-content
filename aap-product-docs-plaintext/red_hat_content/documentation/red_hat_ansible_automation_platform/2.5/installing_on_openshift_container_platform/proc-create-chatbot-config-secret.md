# 5. Deploying the Ansible Lightspeed intelligent assistant on OpenShift Container Platform
## 5.5. Deploying the Ansible Lightspeed intelligent assistant
### 5.5.1. Creating a chatbot configuration secret




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
- Red Hat OpenShift AI: `    rhoai_vllm` (Default value)
- IBM watsonx.ai: `    watsonx`
- OpenAI: `    openai`
- Microsoft Azure OpenAI: `    azure_openai` |
|  `chatbot_context_window_size` |  _Optional_

Enter a value to configure the context window length for your LLM setup.

Default= `128000` |
|  `chatbot_temperature_override` |  _Optional_

A lower temperature generates predictable results, while a higher temperature allows more diverse or creative responses.

Enter one of the following values:

-  `    0` : Least creativity and randomness in the responses.
-  `    1` : Maximum creativity and randomness in the responses.
-  `    null` : Override or disable the default temperature setting.

Note
A few OpenAI o-series models (o1, o3-mini, and o4-mini models) do not support the temperature settings. Therefore, you must set the value to null to use these OpenAI models. |
|  **Additional setting for IBM watsonx.ai only** |
|  `chatbot_llm_provider_project_id` | Enter the project ID of your IBM watsonx setup. |
|  **Additional settings for Microsoft Azure OpenAI only** |
|  `chatbot_azure_deployment_name` | Enter the deployment name of your Microsoft Azure OpenAI setup. |
|  `chatbot_azure_api_version` |  _Optional_

Enter the API version of your Microsoft Azure OpenAI setup. |



1. Click **Create** . The chatbot authorization secret is successfully created.


