# 5. Identity access management data movement
## 5.1. Upgrading from Ansible Automation Platform 2.4 to 2.6




It is possible for customers to upgrade directly from the latest 2.4 version to 2.6. On startup, 2.6 platform services rename their service-specific roles to platform-wide roles, as shown in the following table.

|  **2.4 role** |  **2.6 equivalent** |
| --- | --- |
| Automation controller auditor | Platform auditor |
| Automation controller superuser/administrator (flag) | Platform superuser/administrator (flag) |
| Automation controller organization admin | Organization administrator |
| Automation controller organization member | Organization member |
| Automation controller team admin | Team administrator |
| Automation hub administrator | Team member (user) |
| Automation controller team member (user) | Team member (user) |
| Automation hub team member (user) | Team member (user) |


Additionally, note the following behavior when upgrading to 2.6:

- After upgrading, automation controller entity relationships, such as user associations with organizations, teams, or role sets, remain consistent in platform gateway. This applies to both existing entities moved during the upgrade and any new entities (users, teams, organizations) created in automation controller and subsequently moved in a 2.6 environment.
- Automation controller user types (normal, superuser and auditor) are mapped to platform gateway user types during the upgrade process.
- Where team names match between automation hub and platform gateway, for example, "Team A" exists in both, user memberships from automation hub are transferred to the corresponding team in platform gateway. This reduces the need to manually re-create memberships.
- If users exist only in automation hub, they are not moved to [Gateway]. You must manually re-create these users after upgrading. However, if a user has the same username in both automation controller and automation hub, the automation controller account is part of the regular data movement. Users who are not migrated need to have their passwords reset, but should keep the same permissions.
- Data movement also moves private automation hub but excludes Event-Driven Ansible data.
- Event-Driven Ansible users are not moved to platform gateway and must be recreated manually after upgrading.
- Automation hub users must be recreated if they cannot be moved as part of the upgrade. A user might not be migrated for the following reasons:


- The user’s account exists only in automation hub and not in automation controller.
- Duplicate usernames exist in both automation hub and automation controller, but they belong to different people.
- A discrepancy in the username, email, or other identifying attributes exists between the two services, which prevents the system from correctly merging the accounts.

- Automation hub admins are converted to normal users if they are able to be merged with automation controller users.
- The automation controller UI is updated to reflect the automation controller data moved as platform-level entities along with their roles.
- The automation controller setting **Organization Admins Can Manage Users and Teams** applies to organization admins in 2.6.


