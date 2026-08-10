+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/use_the_correct_windows_module_and_collection_ecosystem"
title = "Use the correct Windows module and collection ecosystem - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/use_the_correct_windows_module_and_collection_ecosystem/aem-page/use_the_correct_windows_module_and_collection_ecosystem.html"
last_crumb = "Use the correct Windows module and collection ecosystem"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Use the correct Windows module and collection ecosystem"
oversized = "false"
page_slug = "use_the_correct_windows_module_and_collection_ecosystem"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/use_the_correct_windows_module_and_collection_ecosystem"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/use_the_correct_windows_module_and_collection_ecosystem/toc/toc.json"
type = "aem-page"
+++

# Use the correct Windows module and collection ecosystem

Select secure and maintainable components for Windows automation workflows.

Standard Ansible Core modules are written in Python for Unix-like machines and cannot interface with Windows APIs. Windows management requires dedicated PowerShell-based modules and supported collections.

**Certified automation collections**

Subscribers can access certified, production-ready content from the Red Hat automation hub:

- **ansible.windows**: Core system modules (e.g., `win_package`, `win_updates`, `win_service`, `win_feature`, `win_copy`, `win_reboot`).
- **microsoft.ad**: Active Directory management (15 modules covering domains, users, groups, computer objects, and OUs).
- **chocolatey.chocolatey**: Package management orchestration.
- **microsoft.iis** and **microsoft.mecm**: Dedicated web server and configuration management extensions.

Note:

For new playbooks, prefer `ansible.windows.win_powershell` over win_shell. win_powershell provides superior error handling, outputs native PowerShell objects, and fully supports check_mode.

**Deprecated modules**

| Legacy module                 | Replacement module               |
| ----------------------------- | -------------------------------- |
| `win_domain`                  | `microsoft.ad.domain`            |
| `win_domain_controller`       | `microsoft.ad.domain_controller` |
| `win_domain_membership`       | `microsoft.ad.membership`        |
| `win_domain_user`             | `microsoft.ad.user`              |
| `win_domain_group`            | `microsoft.ad.group`             |
| `win_domain_group_membership` | `microsoft.ad.group_membership`  |
| `win_domain_computer`         | `microsoft.ad.computer`          |
| `win_domain_object_info`      | `microsoft.ad.object_info`       |
| `win_domain_ou`               | `microsoft.ad.ou`                |

**Windows-compatible core actions**

The following built-in Ansible engine components and action plugins run on the control node and are fully compatible with Windows targets:

 `add_host, assert, async_status, debug, fail, fetch, group_by, include_role, include_vars, meta, pause, raw, script, set_fact, set_stats, setup, slurp, template` (and `win_template`), `wait_for_connection`.
