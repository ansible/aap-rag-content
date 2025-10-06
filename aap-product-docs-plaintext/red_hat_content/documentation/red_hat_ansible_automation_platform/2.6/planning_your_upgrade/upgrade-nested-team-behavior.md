# 5. Identity access management data movement
## 5.1. Upgrading from Ansible Automation Platform 2.4 to 2.6
### 5.1.1. Nested team behavior changes




Ansible Automation Platform 2.5 and later versions no longer support nested team structures. This affects the UI, API, and collections.

In version 2.4, users could inherit permissions from multiple teams simultaneously through nested team structures created using REST APIs and collections. For example, a user on Team A could inherit permissions for Team B if Team B was nested under Team A (User → Team A → Team B). The user interface in 2.4 did not expose this capability; it was only possible through the API and collections.

During an upgrade from Ansible Automation Platform 2.4 to 2.6, nested teams are converted to a direct user-to-teams mapping. This means that instead of inheriting permissions through a nested structure, users are directly assigned to each team they have permissions for. For instance, if a user previously had permissions through "User → Team A → Team B," after the upgrade, this becomes "User → Team A" and "User → Team B".

**Impact and planning**

- Users can still belong to one or more teams and simultaneously inherit permissions from those teams.
- Organizations that use integrations or automations with nested teams in their 2.4 deployment must plan to change this structure to a direct user-to-teams mapping.


Important
Before upgrading from Ansible Automation Platform 2.4, change any integrations or automations that implement nested teams to a direct user-to-teams mapping to avoid unexpected behavior in 2.5 and later.



