+++
title = "Project and rulebook activation settings interdependencies - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/project_and_rulebook_activation_settings_interdependencies"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/project_and_rulebook_activation_settings_interdependencies/aem-page/project_and_rulebook_activation_settings_interdependencies.html"
last_crumb = "Project and rulebook activation settings interdependencies"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Project and rulebook activation settings interdependencies"
oversized = "false"
page_slug = "project_and_rulebook_activation_settings_interdependencies"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/project_and_rulebook_activation_settings_interdependencies"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/project_and_rulebook_activation_settings_interdependencies/toc/toc.json"
type = "aem-page"
+++

# Project and rulebook activation settings interdependencies

Project and activation settings are interdependent. The Update revision on launch and Auto-restart on project update configurations combine to determine auto-restart behaviors and trigger specific user confirmation prompts.

*Table 1. Project and rulebook activation settings interdependencies*

| **Triggered by**                         | **Project State**                          | **Activation State**                          | **Resulting Behavior**                                                                                                                                             |
| ---------------------------------------- | ------------------------------------------ | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Rulebook activation started or restarted | Enabled (Update revision on launch **ON**) | Enabled or Disabled                           | A message informs you that the project is configured to update on restart, which might impact other activations sharing this project. You must confirm to proceed. |
| Rulebook activation started or restarted | Disabled (Update revision on launch OFF)   | Enabledor Disabled                            | A standard message is displayed for the user to confirm they want to restart the rulebook activation.                                                              |
| Project synced                           | Enabled or Disabled                        | Enabled (Auto-restart on project update ON)   | A message informs you that the associated rulebook activation is configured to restart when this project syncs. You must confirm the sync.                         |
| Project synced                           | Enabled or Disabled                        | Disabled (Auto-restart on project update OFF) | A standard message is displayed for the user to confirm they want to sync the project.                                                                             |
