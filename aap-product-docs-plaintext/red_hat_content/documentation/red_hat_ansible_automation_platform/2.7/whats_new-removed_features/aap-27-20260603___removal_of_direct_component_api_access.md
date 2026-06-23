# Removed features
## Removal of direct component API access

The next version of Ansible Automation Platform marks the completion of the platform unification initiative introduced in Ansible Automation Platform 2.5. With this release, the platform gateway becomes the sole entry point for all Ansible Automation Platform interactions, replacing direct API access to automation controller, automation hub, and Event-Driven Ansible. This change centralizes organization management, authentication, and access control through a single, unified interface — providing a more consistent and secure experience across all automation capabilities within the platform.

Note:

Any existing direct integrations with automation controller, automation hub, or Event-Driven Ansible APIs must be migrated to route through the platform gateway prior to upgrading to the next version of Ansible Automation Platform.

**Minimum collection versions**

Ansible Automation Platform 2.7 requires the following minimum collection versions:

- ansible.controller version 4.8.0
- ansible.hub version version1.0.6
- ansible.eda version version 2.12.0
- ansible.platform version 2.7.0
See [Update collection versions](/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-con_upgrade_api_changes_27#GUID-bc50aa1a-9717-4cde-816e-7f5bf1d78b75 "Older collection versions construct URLs and authentication flows that target component APIs directly. Only the latest collection versions route requests through platform gateway.") for more information.

