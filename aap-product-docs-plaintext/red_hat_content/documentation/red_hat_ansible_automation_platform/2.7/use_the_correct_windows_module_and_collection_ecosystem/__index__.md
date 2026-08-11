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
