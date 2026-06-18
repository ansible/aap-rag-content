# Deploy the automation intelligent assistant

The automation intelligent assistant is an AI-powered chat interface embedded in Ansible Automation Platform. It uses large language models (LLMs) to answer questions about your Ansible Automation Platform environment in natural language.

Red Hat Ansible Lightspeed includes two components:

- The automation intelligent assistant: A chat interface that generates answers to questions about Ansible Automation Platform. The intelligent assistant interacts with users in English and uses LLMs to provide contextual responses.
- The coding assistant: A generative AI service that works with IBM watsonx Code Assistant to help developers create Ansible content, including single-task and multi-task recommendations, playbooks, and roles.
The following documentation covers deploying the automation intelligent assistant on an Ansible Automation Platform containerized installation, and on Ansible Automation Platform on Openshift Container Platform (OCP). For information on deploying the coding assistant, see Install and configure the Ansible code bot.

## Automation intelligent assistant

The automation intelligent assistant is an intuitive chat interface embedded in the Ansible Automation Platform, and uses generative artificial intelligence (AI) to answer questions about the platform.

The automation intelligent assistant interacts with users in English, and uses Large Language Models (LLMs) to generate quick, accurate, and personalized responses. These responses empower Ansible users to work more efficiently, thereby improving productivity and the overall quality of their work.

To use the automation intelligent assistant, you need:

- A valid subscription to Ansible Automation Platform.
- Deployment of an LLM service that is hosted on one of these platforms: Red Hat Enterprise Linux AI, Red Hat OpenShift AI, or Red Hat AI Inference Server.

## Integration with the MCP server

The automation intelligent assistant integration with the Model Context Protocol (MCP) server is available as a Technology Preview release. MCP is an open protocol that enables applications to give real-time context to LLMs.

This integration enables the automation intelligent assistant to request and receive the latest information from external resources, and give more relevant, dynamically-sourced answers when responding to your questions. To set up this integration, you need to specify the MCP server variables when configuring the Red Hat Ansible Lightspeed variables in the inventory file.

Note:

Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features give early access to upcoming product features, enabling customers to test functionality and leave feedback during the development process.

## Deployment models

The Ansible Lightspeed coding assistant supports two deployment models. No telemetry data is collected in either configuration.

-  **On-premise deployment** Both Red Hat Ansible Lightspeed and the IBM watsonx Code Assistant model (IBM Cloud Pak for Data) are on-premise deployments.

-  **Hybrid deployment** Red Hat Ansible Lightspeed is an on-premise deployment, while IBM watsonx Code Assistant model is a cloud deployment.

A hybrid deployment model provides the following benefits:

* Flexibility to choose an environment that best suits your organizational needs.
* Integrated authentication by using the Ansible Automation Platform for user authentication and removing the need for a separate Red Hat cloud login.
* Regional choice for organizations to deploy Red Hat Ansible Lightspeed in their preferred geographical region.

## Ansible Automation Platform requirements

- Licensing requirements:
* A valid Ansible Automation Platform subscription.
* Administrator privileges for the Ansible Automation Platform.
- Additional requirements for Ansible Lightspeed coding assistant:
* A valid subscription to IBM watsonx Code Assistant (for on-premise deployment), or IBM watsonx Code Assistant for Red Hat Ansible Lightspeed on Cloud Pak for Data (for hybrid deployment).
* An API key and a model ID from IBM watsonx Code Assistant.
* VS Code version 1.70.1 or later.
- Additional requirements for automation intelligent assistant:
* Deployment of an LLM service that is hosted on one of these platforms: Red Hat Enterprise Linux AI, Red Hat OpenShift AI, or Red Hat AI Inference Server.

## Large Language Model (LLM) provider requirements

You must have configured an LLM provider that you will use before deploying the automation intelligent assistant. An LLM is a type of machine learning model that can interpret and generate human-like language. When an LLM is used with the automation intelligent assistant, the LLM can interpret questions accurately and provide helpful answers in a conversational manner.

Your LLM must have tool calling enabled to handle tool-related requests. Tool calling allows the assistant to interact with platform services and execute complex workflows.

The automation intelligent assistant can rely on the following LLM providers:

-  **Red Hat LLM providers:**
*  **Red Hat Enterprise Linux AI** You can configure Red Hat Enterprise Linux AI as the LLM provider. As the Red Hat Enterprise Linux is in a different environment than the Ansible Lightspeed deployment, the model deployment must allow access using a secure connection.

The automation intelligent assistant supports vLLM Server. When self-hosting an LLM with Red Hat Enterprise Linux AI, you can use vLLM Server as the inference engine.

*  **Red Hat OpenShift AI** You must deploy an LLM on the Red Hat OpenShift AI single-model serving platform that uses the Virtual Large Language Model (vLLM) runtime. If the model deployment lives in a different OpenShift environment than the Ansible Lightspeed deployment, include a route to expose the model deployment outside the cluster.

The automation intelligent assistant supports vLLM Server. When self-hosting an LLM with Red Hat OpenShift AI, you can use vLLM Server as the inference engine.

Note:
For configurations with Red Hat Enterprise Linux AI or Red Hat OpenShift AI, you must host your own LLM provider instead of using a SaaS LLM provider.

*  **Red Hat AI Inference Server** You can deploy an LLM by using Red Hat AI Inference Server as your inference runtime. Red Hat AI Inference Server supports vLLM runtimes for efficient model serving and can be configured to work with the automation intelligent assistant.

If the Red Hat AI Inference Server deployment is in a different environment than the Ansible Lightspeed deployment, ensure the model deployment allows access by using a secure connection and configure appropriate network routing.

The automation intelligent assistant supports vLLM Server when self-hosting an LLM with Red Hat AI Inference Server as the inference engine.

-  **Third-party LLM providers:**
*  **OpenAI** To use OpenAI with the automation intelligent assistant, you need access to the OpenAI API platform.

*  **Microsoft Azure OpenAI** To use Microsoft Azure with the automation intelligent assistant, you need access to Microsoft Azure OpenAI.

## Deploy the automation intelligent assistant on OpenShift Container Platform

As a system administrator, you can deploy the automation intelligent assistant on Ansible Automation Platform on OpenShift Container Platform.

## Overview

Install and use the automation intelligent assistant on Ansible Automation Platform for OpenShift Container Platform. An intuitive chat interface, embedded in Ansible Automation Platform, it uses generative artificial intelligence (AI) to answer questions about Ansible Automation Platform.

The automation intelligent assistant interacts with users in their natural language prompts in English, and uses Large Language Models (LLMs) to generate quick, accurate, and personalized responses. These responses empower Ansible users to work more efficiently, thereby improving productivity and the overall quality of their work.

The automation intelligent assistant requires the following configurations:

- Installation of Ansible Automation Platform 2.6 or later on Red Hat OpenShift Container Platform
- Deployment of an LLM provider served by either a Red Hat AI platform or a third-party AI platform. To know the LLM providers that you can use, see LLM Providers below.


Important:

Red Hat does not collect any telemetry data from your interactions with the automation intelligent assistant.

Upgrading from Ansible Automation Platform 2.5 to 2.6.1 or 2.6 to 2.6.1 enables HTTPS and TLS by default for internal communication between the Ansible Lightspeed API and the automation intelligent assistant pod. Following the upgrade to Ansible Automation Platform 2.6.1, the intelligent assistant will be unavailable for approximately 60 seconds while its pod restarts.

### Integration with MCP server

Automation intelligent assistant integration with the Model Context Protocol (MCP) server is now generally available. This integration enhances the user experience by delivering relevant, dynamically sourced data results to your queries.

MCP is an open protocol that standardizes how applications provide context to LLMs. Using the protocol, an MCP server provides a standardized way for an LLM to increase context by requesting and receiving real-time information from external resources. The integration with an MCP server enables the automation intelligent assistant to offer an enhanced user experience by delivering relevant, dynamically sourced data results to your queries. You can configure a MCP server in the chatbot configuration secret.

### Ansible Automation Platform requirements

- You have installed Ansible Automation Platform 2.6 or later on your OpenShift Container Platform environment.
- You have administrator privileges for Ansible Automation Platform.
- You have provisioned an OpenShift cluster with Operator Lifecycle Management installed.

### Large Language Model (LLM) provider requirements

You must have configured an LLM provider that you will use before deploying the automation intelligent assistant.

An LLM is a type of machine learning model that can interpret and generate human-like language. When an LLM is used with the automation intelligent assistant, the LLM can interpret questions accurately and provide helpful answers in a conversational manner. Your LLM must have tool calling enabled to handle tool-related requests. Tool calling allows the assistant to interact with platform services and execute complex workflows.

The automation intelligent assistant can rely on the following LLM providers:

-  **Red Hat LLM providers:**
*  **Red Hat Enterprise Linux AI** You can configure Red Hat Enterprise Linux AI as the LLM provider. As the Red Hat Enterprise Linux is in a different environment than the Ansible Lightspeed deployment, the model deployment must allow access using a secure connection.

The automation intelligent assistant supports vLLM Server. When self-hosting an LLM with Red Hat Enterprise Linux AI, you can use vLLM Server as the inference engine.

*  **Red Hat OpenShift AI** You must deploy an LLM on the Red Hat OpenShift AI single-model serving platform that uses the Virtual Large Language Model (vLLM) runtime. If the model deployment resides in a different OpenShift environment than the Ansible Lightspeed deployment, include a route to expose the model deployment outside the cluster.

The automation intelligent assistant supports vLLM Server. When self-hosting an LLM with Red Hat OpenShift AI, you can use vLLM Server as the inference engine.

Note:
For configurations with Red Hat Enterprise Linux AI or Red Hat OpenShift AI, you must host your own LLM provider instead of using a SaaS LLM provider.

*  **Red Hat AI Inference Server** You can deploy an LLM using Red Hat AI Inference Server as your inference runtime. Red Hat AI Inference Server supports vLLM runtimes for efficient model serving and can be configured to work with automation intelligent assistant.

If the Red Hat AI Inference Server deployment is in a different environment than the Ansible Lightspeed deployment, ensure the model deployment allows access using a secure connection and configure appropriate network routing.

The automation intelligent assistant supports vLLM Server when self-hosting an LLM with Red Hat AI Inference Server as the inference engine.

-  **Third-party LLM providers:**
*  **OpenAI** To use OpenAI with the automation intelligent assistant, you need access to the OpenAI API platform.

*  **Microsoft Azure OpenAI** To use Microsoft Azure with the automation intelligent assistant, you need access to Microsoft Azure OpenAI.

### Process for configuring and using the automation intelligent assistant

Perform the following tasks to set up and use the automation intelligent assistant in your Ansible Automation Platform instance on the OpenShift Container Platform environment:

| Task                                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>Deploy the automation intelligent assistant on OpenShift Container Platform | <br>An Ansible Automation Platform administrator who wants to deploy the automation intelligent assistant for all Ansible users in the organization.<br>Perform the following tasks:<br>Create a chatbot configuration secret.Update the YAML file of the Ansible Automation Platform to use the chatbot connection secret.Optional: Change your LLM model if you want to use a different LLM provider after deploying Red Hat Ansible Lightspeed. |
| <br>Access and use the automation intelligent assistant                         | <br>All Ansible users who want to use the intelligent assistant to get answers to their questions about the Ansible Automation Platform.                                                                                                                                                                                                                                                                                                           |

## Create a chatbot configuration secret

Create a configuration secret for the intelligent assistant so that you can connect it to the Ansible Automation Platform operator.

### Before you begin

- [You have installed and configured the Ansible Automation Platform operator](/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_operator_install_operator "As a system administrator, you can use Ansible Automation Platform Operator to deploy new Ansible Automation Platform instances in your OpenShift environment.").

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

## Update the YAML file of the Ansible Automation Platform operator

After you create the chatbot authorization secret, you must update the YAML file of the Ansible Automation Platform operator to use the secret.

### Procedure

1.  Log in to Red Hat OpenShift Container Platform as an administrator.
2.  Navigate to Operators> (and then)Installed Operators.
3.  From the list of installed operators, select the **Ansible Automation Platform** operator.
4.  Locate and select the **Ansible Automation Platform** custom resource, and then click the required app.
5.  Select the **YAML** tab.
6.  Scroll the text to find the `spec:` section, and add the following details under the `spec:` section:


```
spec:
lightspeed:
disabled: false
chatbot_config_secret_name: <name of your chatbot configuration secret>
```

7.  Click **Save**. The intelligent assistant service takes a few minutes to set up.  Note:
Upgrading from Ansible Automation Platform 2.5 to 2.6.1 enables HTTPS and enables TLS by default for internal communication between the Ansible Lightspeed API and the intelligent assistant pod. Following the upgrade to Ansible Automation Platform 2.6.1, the intelligent assistant will be unavailable for approximately 60 seconds while its pod restarts.

### Results

1. Verify that the chat interface service is running successfully:
1. Navigate to Workloads> (and then)Pods.
2. Filter with the term **api** and ensure that the following APIs are displayed in **Running** status:
- `myaap-lightspeed-api-<version number>`
- `myaap-lightspeed-chatbot-api-<version number>`
2. Verify the MCP server configuration if you specified either `aap_gateway_url` or `aap_controller_url` parameter:
- Open the `lightspeed-chatbot-api` pod and click the **Containers** section.     * If the `ansible-mcp-lightspeed` container is displayed, the Ansible Lightspeed MCP server is running.
* If the `ansible-mcp-controller` container is displayed, the Ansible Automation Platform Controller Service MCP server is running.
3. Verify that the chat interface is displayed on the Ansible Automation Platform:
1. Access the Ansible Automation Platform:
1. Navigate to Operators> (and then)Installed Operators.
2. From the list of installed operators, click **Ansible Automation Platform**.
3. Locate and select the **Ansible Automation Platform** custom resource, and then click the app that you created.
4. From the **Details** tab, record the information available in the following fields:
- **URL**: This is the URL of your Ansible Automation Platform instance.
- **Gateway Admin User**: This is the username to log into your Ansible Automation Platform instance.
- **Gateway Admin password**: This is the password to log into your Ansible Automation Platform instance.
5. Log in to the Ansible Automation Platform using the URL, username, and password that you recorded earlier.
2. Access the intelligent assistant:
1. Click the intelligent assistant icon ![intelligent assistant icon](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/chatbot-icon.png) that is displayed at the top right corner of the taskbar.

2. Verify that the chat interface is displayed, as shown in the following image:             ![Intelligent assistant](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/aap-ansible-lightspeed-intelligent-assistant.png).

## Change your LLM model

If you have already deployed Ansible Lightspeed intelligent assistant but want to change your LLM model, you can create a new chatbot configuration secret for the new LLM model.

### About this task

Alternatively, if you want to use the same chatbot configuration secret, you must delete and redeploy the Ansible Lightspeed intelligent assistant.

### Procedure

-  To create and use a new chatbot configuration secret:
1.  [Create a new chatbot configuration secret](/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_operator_install_operator "As a system administrator, you can use Ansible Automation Platform Operator to deploy new Ansible Automation Platform instances in your OpenShift environment.") with a different name for the new LLM model.
2.  [Update the YAML file of the Ansible Automation Platform operator](/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_operator_install_operator "As a system administrator, you can use Ansible Automation Platform Operator to deploy new Ansible Automation Platform instances in your OpenShift environment.") with the new chatbot configuration secret name. The Ansible Automation Platform operator detects the new configuration and redeploys the Ansible Lightspeed intelligent assistant.

3.  Verify that the chat interface service is running successfully. See the verification steps mentioned in the topic [Update the YAML file of the Ansible Automation Platform operator](/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_operator_install_operator "As a system administrator, you can use Ansible Automation Platform Operator to deploy new Ansible Automation Platform instances in your OpenShift environment.").  Important:
Do not update the existing chatbot configuration secret with the new LLM model, as the reconciliation logic does not check the updates made to the secret.

-  To use the same chatbot secret by deleting and redeploying the Ansible Lightspeed intelligent assistant:
1.  Disable the Ansible Lightspeed operator instance:

1. Navigate to Operators> (and then)Installed Operators.
2. From the list of installed operators, select **Ansible Automation Platform**.
3. Locate and select the Ansible Automation Platform custom resource.
4. Select the **YAML** tab and under the `spec:` section for `lightspeed` category, specify `disabled:true`.
5. Click **Save**.

2.  Delete the Ansible Lightspeed operator instance:

1. Navigate to Operators> (and then)Installed Operators.
2. From the list of installed operators, select **Ansible Lightspeed** and delete the operator.

3.  Re-enable the Ansible Automation Platform instance:

1. Navigate to Operators> (and then)Installed Operators.
2. From the list of installed operators, select **Ansible Automation Platform**.
3. Locate and select the Ansible Automation Platform custom resource.
4. Select the **YAML** tab and under the `spec:` section for `lightspeed` category, specify `disabled:false`.
5. Click **Save**.
