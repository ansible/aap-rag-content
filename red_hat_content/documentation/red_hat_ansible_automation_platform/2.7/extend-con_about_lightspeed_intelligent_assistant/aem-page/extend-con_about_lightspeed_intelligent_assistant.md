+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-con_about_lightspeed_intelligent_assistant"
title = "Overview - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_deploying_chatbot_operator/", "Deploy the automation intelligent assistant on OpenShift Container Platform"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-con_about_lightspeed_intelligent_assistant/aem-page/extend-con_about_lightspeed_intelligent_assistant.html"
last_crumb = "Overview"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Overview"
oversized = "false"
page_slug = "extend-con_about_lightspeed_intelligent_assistant"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/extend-con_about_lightspeed_intelligent_assistant"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-con_about_lightspeed_intelligent_assistant/toc/toc.json"
type = "aem-page"
+++

# Overview

Install and use the automation intelligent assistant on Ansible Automation Platform for OpenShift Container Platform. An intuitive chat interface, embedded in Ansible Automation Platform, it uses generative artificial intelligence (AI) to answer questions about Ansible Automation Platform.

The automation intelligent assistant interacts with users in their natural language prompts in English, and uses Large Language Models (LLMs) to generate quick, accurate, and personalized responses. These responses empower Ansible users to work more efficiently, thereby improving productivity and the overall quality of their work.

The automation intelligent assistant requires the following configurations:

- Installation of Ansible Automation Platform 2.6 or later on Red Hat OpenShift Container Platform
- Deployment of an LLM provider served by either a Red Hat AI platform or a third-party AI platform. To know the LLM providers that you can use, see LLM Providers below.

Important:

Red Hat does not collect any telemetry data from your interactions with the automation intelligent assistant.

## Integration with MCP server

Automation intelligent assistant integration with the Model Context Protocol (MCP) server is now generally available. This integration enhances the user experience by delivering relevant, dynamically sourced data results to your queries.

MCP is an open protocol that standardizes how applications provide context to LLMs. Using the protocol, an MCP server provides a standardized way for an LLM to increase context by requesting and receiving real-time information from external resources. The integration with an MCP server enables the automation intelligent assistant to offer an enhanced user experience by delivering relevant, dynamically sourced data results to your queries. You can configure a MCP server in the chatbot configuration secret.

## Ansible Automation Platform requirements

- You have installed Ansible Automation Platform 2.6 or later on your OpenShift Container Platform environment.
- You have administrator privileges for Ansible Automation Platform.
- You have provisioned an OpenShift cluster with Operator Lifecycle Management installed.

## Large Language Model (LLM) provider requirements

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

## Process for configuring and using the automation intelligent assistant

Perform the following tasks to set up and use the automation intelligent assistant in your Ansible Automation Platform instance on the OpenShift Container Platform environment:

| Task                                                                            | Description                                                                                                                                                                                              |
| ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>Deploy the automation intelligent assistant on OpenShift Container Platform | <br>An Ansible Automation Platform administrator who wants to deploy the automation intelligent assistant for all Ansible users in the organization.<br>Perform the following tasks:<br>Create a chatbot configuration secret.Update the YAML file of the Ansible Automation Platform to use the chatbot connection secret.Optional: Change your LLM model if you want to use a different LLM provider after deploying Red Hat Ansible Lightspeed. |
| <br>Access and use the automation intelligent assistant                         | <br>All Ansible users who want to use the intelligent assistant to get answers to their questions about the Ansible Automation Platform.                                                                 |
