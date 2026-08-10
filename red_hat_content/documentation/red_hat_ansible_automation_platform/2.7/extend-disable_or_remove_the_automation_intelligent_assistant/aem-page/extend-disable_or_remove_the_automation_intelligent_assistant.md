+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-disable_or_remove_the_automation_intelligent_assistant"
title = "Disable or remove the automation intelligent assistant - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-disable_or_remove_the_automation_intelligent_assistant/", "Disable or remove the automation intelligent assistant"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-disable_or_remove_the_automation_intelligent_assistant/aem-page/extend-disable_or_remove_the_automation_intelligent_assistant.html"
last_crumb = "Disable or remove the automation intelligent assistant"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Disable or remove the automation intelligent assistant"
oversized = "false"
page_slug = "extend-disable_or_remove_the_automation_intelligent_assistant"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/extend-disable_or_remove_the_automation_intelligent_assistant"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-disable_or_remove_the_automation_intelligent_assistant/toc/toc.json"
type = "aem-page"
+++

# Disable or remove the automation intelligent assistant

If the automation intelligent assistant produces responses that are harmful, inaccurate, or unacceptable for your environment, you can disable or remove it from your Ansible Automation Platform deployment.

As a platform administrator, you can disable the automation intelligent assistant to immediately stop it from responding to user queries. This procedure serves as the incident response mechanism for a malfunctioning AI assistant.

Choose the procedure that matches your deployment type:

- Operator-based deployments on OpenShift Container Platform: Disable the Lightspeed component in the operator custom resource.
- Containerized installations: Stop the chatbot services, remove the Lightspeed variables from the inventory file, and re-run the installer.
