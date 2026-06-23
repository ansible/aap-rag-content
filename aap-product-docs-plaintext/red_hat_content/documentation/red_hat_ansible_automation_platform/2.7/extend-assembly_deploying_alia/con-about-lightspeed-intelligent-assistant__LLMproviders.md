# Deploy the automation intelligent assistant
## Overview
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

