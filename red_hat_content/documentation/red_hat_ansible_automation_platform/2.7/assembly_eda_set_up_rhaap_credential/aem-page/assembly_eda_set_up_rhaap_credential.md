+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/assembly_eda_set_up_rhaap_credential"
title = "Replace legacy automation controller tokens - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/assembly_eda_set_up_rhaap_credential/aem-page/assembly_eda_set_up_rhaap_credential.html"
last_crumb = "Replace legacy automation controller tokens"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Replace legacy automation controller tokens"
oversized = "false"
page_slug = "assembly_eda_set_up_rhaap_credential"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/assembly_eda_set_up_rhaap_credential"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/assembly_eda_set_up_rhaap_credential/toc/toc.json"
type = "aem-page"
+++

# Replace legacy automation controller tokens

When Event-Driven Ansible controller is deployed on Ansible Automation Platform, you can create a Red Hat Ansible Automation Platform credential to connect to automation controller through the use of an automation controller URL and a username and password.

After it has been created, you can attach the Red Hat Ansible Automation Platform credential to a rulebook and use it to run rulebook activations. These credentials provide a simple way to configure communication between automation controller and Event-Driven Ansible controller, enabling your rulebook activations to launch job templates.

Note:

If you previously used controller tokens to connect automation controller and Event-Driven Ansible controller, these tokens are now deprecated. To delete deprecated controller tokens and the rulebook activations associated with them, complete the following procedures starting with replacing controller tokens before proceeding with setting up a Red Hat Ansible Automation Platform credential.
