+++
title = "Understand the provider configuration variable - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-understand_the_provider_configuration_variable"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_deploying_lightspeed_containerized_install/", "Deploy the automation intelligent assistant on containerized Ansible Automation Platform"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-understand_the_provider_configuration_variable/aem-page/extend-understand_the_provider_configuration_variable.html"
last_crumb = "Understand the provider configuration variable"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Understand the provider configuration variable"
oversized = "false"
page_slug = "extend-understand_the_provider_configuration_variable"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/extend-understand_the_provider_configuration_variable"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-understand_the_provider_configuration_variable/toc/toc.json"
type = "aem-page"
+++

# Understand the provider configuration variable

The provider configuration variable ensures the automation intelligent assistant communicates correctly with your LLM service.

The `lightspeed_chatbot_default_provider` inventory variable controls how the automation intelligent assistant formats API requests and handles responses when communicating with your large language model (LLM) service. Different LLM providers have distinct API specifications, authentication methods, and response formats.

The provider value must match your LLM service's actual deployment platform—not the API compatibility layer it exposes. For example, if you deploy a model on Red Hat OpenShift AI that exposes an OpenAI-compatible API, use `rhoai` as the provider value, not `openai`.

Configuration example:

```
lightspeed_chatbot_model_url="https://litellm-litemaas.apps.prod.rhoai.rh-aiservices-bu.com/v1"
lightspeed_chatbot_default_provider="rhoai"
```

For the complete list of valid provider values and when to use each one, see Provider configuration values.
