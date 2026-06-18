+++
title = "Deploy your custom image to a container-based installation - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-deploy_your_custom_image"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-extend_the_intelligent_assistant_with_custom_knowledge/", "Extend the automation intelligent assistant with custom knowledge"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-deploy_your_custom_image/aem-page/extend-deploy_your_custom_image.html"
last_crumb = "Deploy your custom image to a container-based installation"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Deploy your custom image to a container-based installation"
oversized = "false"
page_slug = "extend-deploy_your_custom_image"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/extend-deploy_your_custom_image"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-deploy_your_custom_image/toc/toc.json"
type = "aem-page"
+++

# Deploy your custom image to a container-based installation

Deploy the BYOK RAG image to the intelligent assistant in a Ansible Automation Platform containerized installation.

## Before you begin

You have:

- published the BYOK RAG image to an accessible registry.
- a valid Ansible Automation Platform 2.7 subscription with the intelligent assistant deployed.
- used Podman to pull the image on the node **before**updating the inventory and running the installer. Note that if you do not do this, the containerized install will fail because the image is not loaded.

## Procedure

 Add the required variables to your inventory file under the `[all: vars]` group. See [Ansible Lightspeed variables](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-ref_lightspeed_variables#lightspeed-variables___ansible_lightspeed_coding_assistant_variables)for information about required and optional variables.

```
# This is the list of inventory file variables required to deploy Red Hat Ansible Lightspeed on a containerized installation.
# Consult the docs if you are unsure what to add.
# For information about required and optional variables, refer to the Appendix: Red Hat Ansible Lightspeed variables
# https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-ref_lightspeed_variables
# This section is for your Red Hat Ansible Lightspeed host
# ---------------------------------------------------------
[ansiblelightspeed]
aap.example.com

[all:vars]
# This section is to configure Ansible Lightspeed intelligent assistant
# ----------------------------------------------------------------------lightspeed_chatbot_model_url=<set your own>
lightspeed_chatbot_model_api_key= <set your own>
lightspeed_chatbot_model_id= <set your own>
lightspeed_chatbot_default_provider='rhoai'
lightspeed_chatbot_model_extra_settings={}
# If you want to use {AzureOpenAI} as the LLM provider, specify the lightspeed_chatbot_model_extra_settings value as '{"api_type": ""}'.
# This section is to configure Ansible Lightspeed intelligent assistant with BYOK RAG image
# -----------------------------------------------------------------------------------------
lightspeed_chatbot_byok_image=<your registry><repository>/<image>:<label>
lightspeed_chatbot_byok_score_multiplier=1.2
```

## What to do next

**Verification**

1. Ask BYOK-specific questions in the intelligent assistant, and evaluate whether the responses reflect the BYOK content.
2. **Optional**: Review the intelligent assistant logs using the following command:

```
ssh ansible@<lightspeed-node> 'podman logs ansible-lightspeed-chatbot 2>&1 | grep -i "knowledge_search\|byok\|vector"'
```

In the search results, look for the following items:

- `knowledge_search tool results`: this indicates that the BYOK RAG image is being used
- Vector database initialization messages
- No errors reported about a missing BYOK image
