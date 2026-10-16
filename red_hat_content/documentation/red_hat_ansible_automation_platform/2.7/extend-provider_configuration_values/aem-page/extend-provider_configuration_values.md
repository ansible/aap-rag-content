+++
title = "Provider configuration values - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-provider_configuration_values"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_deploying_lightspeed_containerized_install/", "Deploy the automation intelligent assistant on containerized Ansible Automation Platform"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-provider_configuration_values/aem-page/extend-provider_configuration_values.html"
last_crumb = "Provider configuration values"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Provider configuration values"
oversized = "false"
page_slug = "extend-provider_configuration_values"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/extend-provider_configuration_values"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-provider_configuration_values/toc/toc.json"
type = "aem-page"
+++

# Provider configuration values

Valid provider values for the automation intelligent assistant and when to use each one.

The `lightspeed_chatbot_default_provider` inventory variable accepts three values. Choose the value that matches your LLM service deployment type, not the API compatibility layer it exposes.

*Table 1. Provider values and usage*

| Provider value | LLM service type            | When to use                                                                                                                                      | Example URL pattern                                  |
| -------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------- |
| `rhoai`        | Red Hat Enterprise Linux AI | Your LLM is deployed on Red Hat Enterprise Linux AI with vLLM Server as the inference engine                                                     | `https://<your-rhelai-host>/v1`                      |
| `rhoai`        | Red Hat OpenShift AI        | Your LLM is deployed on Red Hat OpenShift AI single-model serving platform using vLLM runtime, or your model URL contains`rhoai` in the hostname | `https://litellm-*.apps.*.rhoai.*.com/v1`            |
| `openai`       | OpenAI                      | You are using the OpenAI API platform directly (not a self-hosted model with OpenAI-compatible API)                                              | `https://api.openai.com/v1`                          |
| `azure`        | Microsoft Azure OpenAI      | Your LLM is deployed on Microsoft Azure OpenAI service                                                                                           | `https://<your-resource>.openai.azure.com/openai/v1` |

Note:

The most common error is setting `lightspeed_chatbot_default_provider="openai"` when the model is actually deployed on Red Hat OpenShift AI with an OpenAI-compatible API endpoint. In this scenario, even though the API is OpenAI-compatible, the correct provider value is `rhoai` because that is the actual deployment platform.
