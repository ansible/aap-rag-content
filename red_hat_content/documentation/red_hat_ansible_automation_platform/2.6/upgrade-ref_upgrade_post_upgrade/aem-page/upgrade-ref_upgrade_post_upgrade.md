+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-ref_upgrade_post_upgrade"
title = "Verify assigned permissions after upgrading - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-assembly_upgrade_data_movement/", "Identity and access management migration during upgrade"]]
category = "Upgrade"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/upgrade-ref_upgrade_post_upgrade/aem-page/upgrade-ref_upgrade_post_upgrade.html"
last_crumb = "Verify assigned permissions after upgrading"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Verify assigned permissions after upgrading"
oversized = "false"
page_slug = "upgrade-ref_upgrade_post_upgrade"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/upgrade-ref_upgrade_post_upgrade"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/upgrade-ref_upgrade_post_upgrade/toc/toc.json"
type = "aem-page"
+++

# Verify assigned permissions after upgrading

It is imperative that administrators verify the assigned permissions for all teams in the platform-wide authentication gateway immediately after the upgrade:

- Ensure the transferred team members have the correct access rights in the Ansible Automation Platform environment based on the filesystem.
- Make sure all members that have been merged are, in fact, the same member. Incorrect permissions could lead to access issues or security vulnerabilities.
- When the upgrade is complete, user accounts that exist in both the automation hub and automation controller systems will be unified, and platform gateway IAM will be the source of truth for users after the data movement.
- Automation hub and Event-Driven Ansible users must either be recreated or the users that moved from automation controller given permission to use those services.


After the upgrade is complete, verify that you can log in to the upgraded platform with your existing automation controller credentials (username and password).

Note:

To do this, you must have an automation controller account on Ansible Automation Platform 2.4 or 2.5 with administrative privileges.

The following table provides next steps for each type of user after they have upgraded.

| If you are this type of user before upgrading:                                                 | Then take these actions after the upgrade:                                                                                                                                             |
| ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>An automation controller administrator (no automation hub account)                         |                                                                                                                                                                                        |
| <br>An automation controller normal user (no automation hub account)                           | <br>Log in with your automation controller username and password; you are now a platform gateway normal user.                                                                          |
| <br>An automation hub user (no automation controller account)                                  | <br>Request a password reset from your administrator. When you log in with your new password you will be a platform gateway normal user. You will retain your hub-related permissions. |
| <br>An automation controller and automation hub user (with the same username in both services) | <br>Log in with your automation controller username and password; your previous two accounts will be merged and you are now a platform gateway normal user.                            |
| <br>An automation hub user with SSO (no automation controller account)                         | <br>Log in with your SSO credentials; you are now a platform gateway normal user.                                                                                                      |
