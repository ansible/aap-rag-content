+++
title = "Execution environment builder permissions - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-ref_ee_builder_permissions"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-ref_ee_builder_permissions/", "Execution environment builder permissions"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-ref_ee_builder_permissions/aem-page/develop-ref_ee_builder_permissions.html"
last_crumb = "Execution environment builder permissions"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Execution environment builder permissions"
oversized = "false"
page_slug = "develop-ref_ee_builder_permissions"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-ref_ee_builder_permissions"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-ref_ee_builder_permissions/toc/toc.json"
type = "aem-page"
+++

# Execution environment builder permissions

Execution environment builder uses navigation-level permissions that control which sidebar items and pages are visible to users in Ansible automation portal.

## Overview

Execution environment builder uses the same permission model as the rest of Ansible automation portal. Users with the AAP Administrator role have all permissions inherently. Non-admin users require an RBAC role with the correct permissions before they can access execution environment builder features.

If you have already configured base RBAC roles per [Configure role-based access control for Ansible automation portal](/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_rhdh_configure#rhdh-configure-rbac "Red Hat Developer Hub offers Role-based Access Control (RBAC) functionality. RBAC can then be applied to the Ansible plug-ins content."), add the execution environment builder permissions to your existing role. If you have not yet set up RBAC, complete that guide first.

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

Note:

The following permissions control base automation portal sidebar items and are not specific to execution environment builder. They are configured in [Configure role-based access control for Ansible automation portal](/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_rhdh_configure#rhdh-configure-rbac "Red Hat Developer Hub offers Role-based Access Control (RBAC) functionality. RBAC can then be applied to the Ansible plug-ins content.").

| Permission               | Controls                                 | Default  |
| ------------------------ | ---------------------------------------- | -------- |
| `ansible.templates.view` | **Templates** menu — template management | Disabled |
| `ansible.history.view`   | **History** menu — build history         | Disabled |

## Administrator-only actions

Note:

Importing and deleting EE definitions and templates are restricted actions. Only users with the AAP Administrator role or users who have been explicitly granted the Backstage catalog delete permission can perform these actions.
