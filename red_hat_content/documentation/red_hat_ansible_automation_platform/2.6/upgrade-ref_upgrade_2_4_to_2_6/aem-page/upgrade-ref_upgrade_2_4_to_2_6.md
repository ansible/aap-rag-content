+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-ref_upgrade_2_4_to_2_6"
template = "docs/aem-title.html"
title = "Upgrade from 2.4 to 2.6 - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-assembly_upgrade_data_movement/", "Identity and access management migration during upgrade"]]
category = "Upgrade"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/upgrade-ref_upgrade_2_4_to_2_6/aem-page/upgrade-ref_upgrade_2_4_to_2_6.html"
last_crumb = "Upgrade from 2.4 to 2.6"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Upgrade from 2.4 to 2.6"
oversized = "false"
page_slug = "upgrade-ref_upgrade_2_4_to_2_6"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/upgrade-ref_upgrade_2_4_to_2_6"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/upgrade-ref_upgrade_2_4_to_2_6/toc/toc.json"
type = "aem-page"
+++

# Upgrade from 2.4 to 2.6

It is possible for customers to upgrade directly from the latest 2.4 version to 2.6. On startup, 2.6 platform services rename their service-specific roles to platform-wide roles, as shown in the following table.

| **2.4 role**                                             | **2.6 equivalent**                          |
| -------------------------------------------------------- | ------------------------------------------- |
| <br>Automation controller auditor                        | <br>Platform auditor                        |
| <br>Automation controller superuser/administrator (flag) | <br>Platform superuser/administrator (flag) |
| <br>Automation controller organization admin             | <br>Organization Administrator              |
| <br>Automation controller organization member            | <br>Organization member                     |
| <br>Automation controller team admin                     | <br>Team administrator                      |
| <br>Automation hub administrator                         | <br>Team member (user)                      |
| <br>Automation controller team member (user)             | <br>Team member (user)                      |
| <br>Automation hub team member (user)                    | <br>Team member (user)                      |


Additionally, note the following behavior when upgrading to 2.6:

- After upgrading, automation controller entity relationships, such as user associations with organizations, teams, or role sets, remain consistent in platform gateway. This applies to both existing entities moved during the upgrade and any new entities (users, teams, organizations) created in automation controller and subsequently moved in a 2.6 environment.
- Automation controller user types (normal, superuser and auditor) are mapped to platform gateway user types during the upgrade process.
- Where team names match between automation hub and platform gateway, for example, "Team A" exists in both, user memberships from automation hub are transferred to the corresponding team in platform gateway. This reduces the need to manually re-create memberships.
- If users exist only in automation hub, they are not moved to [Gateway]. You must manually re-create these users after upgrading. However, if a user has the same username in both automation controller and automation hub, the automation controller account is part of the regular data movement. Users who are not migrated need to have their passwords reset, but should keep the same permissions.
- Data movement also moves private automation hub but excludes Event-Driven Ansible data.
- Event-Driven Ansible users are not moved to platform gateway and must be recreated manually after upgrading.
- Automation hub users must be recreated if they cannot be moved as part of the upgrade. A user might not be migrated for the following reasons:
  * The user’s account exists only in automation hub and not in automation controller.
  * Duplicate usernames exist in both automation hub and automation controller, but they belong to different people.
  * A discrepancy in the username, email, or other identifying attributes exists between the two services, which prevents the system from correctly merging the accounts.
- Automation hub admins are converted to normal users if they are able to be merged with automation controller users.
- The automation controller UI is updated to reflect the automation controller data moved as platform-level entities along with their roles.
- The automation controller setting **Organization Admins Can Manage Users and Teams** applies to organization admins in 2.6.

## Nested team behavior changes

Ansible Automation Platform 2.5 and later versions no longer support nested team structures. This affects the UI, API, and collections.

In version 2.4, users could inherit permissions from multiple teams simultaneously through nested team structures created using REST APIs and collections. For example, a user on Team A could inherit permissions for Team B if Team B was nested under Team A (User → Team A → Team B). The user interface in 2.4 did not expose this capability; it was only possible through the API and collections.

During an upgrade from Ansible Automation Platform 2.4 to 2.6, nested teams are converted to a direct user-to-teams mapping. This means that instead of inheriting permissions through a nested structure, users are directly assigned to each team they have permissions for. For instance, if a user previously had permissions through "User → Team A → Team B," after the upgrade, this becomes "User → Team A" and "User → Team B".

 **Impact and planning**

- Users can still belong to one or more teams and simultaneously inherit permissions from those teams.
- Organizations that use integrations or automations with nested teams in their 2.4 deployment must plan to change this structure to a direct user-to-teams mapping.


Important:

Before upgrading from Ansible Automation Platform 2.4, change any integrations or automations that implement nested teams to a direct user-to-teams mapping to avoid unexpected behavior in 2.5 and later.
