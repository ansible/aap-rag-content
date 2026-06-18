+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/proc_change_llm_model_chatbot_containerized_install"
title = "Change your LLM model - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/proc_change_llm_model_chatbot_containerized_install/aem-page/proc_change_llm_model_chatbot_containerized_install.html"
last_crumb = "Change your LLM model"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Change your LLM model"
oversized = "false"
page_slug = "proc_change_llm_model_chatbot_containerized_install"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/proc_change_llm_model_chatbot_containerized_install"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/proc_change_llm_model_chatbot_containerized_install/toc/toc.json"
type = "aem-page"
+++

# Change your LLM model

To change the LLM model for your containerized Ansible Automation Platform deployment of Ansible Lightspeed intelligent assistant, you must edit the inventory file with the specific details of your new LLM provider and then rerun the install playbook.

## Procedure

1.  Edit the inventory file to update the following Ansible Lightspeed intelligent assistant variables with the specific details of your required LLM provider:

  -  `lightspeed_chatbot_model_url`
  -  `lightspeed_chatbot_model_api_key`
  -  `lightspeed_chatbot_model_id`
  -  `lightspeed_chatbot_default_provider`

2.  Rerun the `install` playbook to [install the containerized Ansible Automation Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_installing_containerized_aap#installing-containerized-aap "Run the install playbook to install containerized Ansible Automation Platform after preparing the Red Hat Enterprise Linux host, downloading the installation program, and configuring the inventory file.").
