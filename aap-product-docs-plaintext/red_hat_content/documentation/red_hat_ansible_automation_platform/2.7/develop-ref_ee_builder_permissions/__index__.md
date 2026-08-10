# Execution environment builder permissions

Execution environment builder uses navigation-level permissions that control which sidebar items and pages are visible to users in Ansible automation portal.

## Overview

Execution environment builder uses the same permission model as the rest of Ansible automation portal. Users with the AAP Administrator role have all permissions inherently. Non-admin users require an RBAC role with the correct permissions before they can access execution environment builder features.

If you have already configured base RBAC roles per [Configure role-based access control for Ansible automation portal](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-configure_portal_rbac "Configure RBAC permissions in Ansible automation portal to control which users can view and execute templates, and which sidebar items are visible to non-admin users."), add the execution environment builder permissions to your existing role. If you have not yet set up RBAC, complete that guide first.

These permissions determine whether a user can see the execution environment builder features at all. They do not replace the base automation portal permissions configured during initial RBAC setup.

## Execution environment builder permissions

The following permissions control visibility of execution environment builder features. An administrator must enable these navigation permissions in the automation portal RBAC configuration before non-admin users can see execution environment builder sidebar items.

| Permission                            | Controls                                                         | Default  |
| ------------------------------------- | ---------------------------------------------------------------- | -------- |
| `ansible.execution-environments.view` | **Execution Environments** menu — creation wizard and EE catalog | Disabled |
| `ansible.collections.view`            | **Collections** menu — collection catalog for EE definitions     | Disabled |
| `ansible.git-repositories.view`       | **Git Repositories** menu — saving and syncing EE definitions    | Disabled |

Each permission can be assigned individually for granular control.

## Base automation portal permissions

Base automation portal navigation permissions (`ansible.templates.view` and `ansible.history.view`) are not specific to execution environment builder. For details, see [Configure role-based access control for Ansible automation portal](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-configure_portal_rbac "Configure RBAC permissions in Ansible automation portal to control which users can view and execute templates, and which sidebar items are visible to non-admin users.").

## Administrator-only actions

Importing and deleting EE definitions and templates are restricted actions. Only users with the AAP Administrator role or users who have been explicitly granted the Backstage catalog delete permission can perform these actions.
