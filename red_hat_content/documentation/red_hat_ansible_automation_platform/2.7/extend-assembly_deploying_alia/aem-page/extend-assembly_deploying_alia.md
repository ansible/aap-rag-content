+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_deploying_alia"
title = "Deploy the automation intelligent assistant - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_deploying_alia/", "Deploy the automation intelligent assistant"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-assembly_deploying_alia/aem-page/extend-assembly_deploying_alia.html"
last_crumb = "Deploy the automation intelligent assistant"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Deploy the automation intelligent assistant"
oversized = "false"
page_slug = "extend-assembly_deploying_alia"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/extend-assembly_deploying_alia"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-assembly_deploying_alia/toc/toc.json"
type = "aem-page"
+++

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
