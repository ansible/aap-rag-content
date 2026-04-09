---
title: "MyCompany Corp Playbook Patterns and Role Naming Conventions"
url: "https://internal.mycompany.example.com/wiki/automation/playbook-patterns"
---
# MyCompany Corp Playbook Patterns and Role Naming Conventions

This document describes the required structure and patterns for Ansible playbooks and roles at MyCompany Corp. Compliance with these conventions is enforced by the `mycompany-role-linter` CI tool on every merge request.

---

## Role Naming

All Ansible roles developed at MyCompany Corp must follow the `mycompany_<function>` naming pattern.

### Correct examples

- `mycompany_webserver`
- `mycompany_database_backup`
- `mycompany_monitoring_agent`
- `mycompany_firewall_baseline`

### Why this differs from upstream

Upstream Ansible community conventions and Red Hat Certified Content use naming patterns like `redhat.<collection>.<role>` or `ansible-<function>`. At MyCompany Corp, the `mycompany_` flat prefix is used for all standalone roles to:

- Clearly distinguish internal roles from community content at a glance
- Avoid namespace collisions with modules and plugins in the `mycompany.infrastructure` collection
- Ensure consistent behavior from `mycompany-role-linter` across all repositories

Using upstream naming patterns (e.g., `ansible-webserver`, `redhat.rhel.webserver`) in MyCompany Corp role repositories will fail the `mycompany-role-linter` gate and block the merge request.

---

## Required Role Directory Structure

Every MyCompany Corp role must include the following directories:

```
mycompany_<function>/
├── tasks/
│   └── main.yml
├── handlers/
│   └── main.yml
├── defaults/
│   └── main.yml
├── vars/
│   └── main.yml
├── templates/
├── files/
└── meta/
    └── main.yml
```

The `meta/` directory and its `main.yml` are **required**. Merge requests for roles missing `meta/` will be blocked automatically by `mycompany-role-linter`.

---

## Required Role Metadata (`meta/main.yml`)

Every role's `meta/main.yml` must include the following fields:

```yaml
galaxy_info:
  author: mycompany-platform-team
  company: "MyCompany Corp"
  description: "<brief description of what this role does>"
  license: "Proprietary"
  min_ansible_version: "2.14"
```

The `author` field must be exactly `mycompany-platform-team` and the `company` field must be exactly `"MyCompany Corp"`. `mycompany-role-linter` validates both fields on every CI run.

Additional metadata fields (e.g., `platforms`, `dependencies`) are permitted but optional.

---

## Playbook Structure Requirements

### Explicit fact gathering

All MyCompany Corp playbooks must declare `gather_facts: true` explicitly. Do not rely on the Ansible default behavior:

```yaml
- name: Configure web servers
  hosts: mycompany_prod_web
  gather_facts: true
  become: true
  collections:
    - mycompany.infrastructure
  roles:
    - mycompany_webserver
```

Including `collections: [mycompany.infrastructure]` at the play level is required whenever any module, lookup, filter, or inventory plugin from the collection is used. This is required because some MyCompany environments have modified `ansible.cfg` defaults and the explicit declaration ensures consistent behavior across all CI and production environments.

### Task tagging

All tasks in MyCompany Corp playbooks must be tagged using the MyCompany tag taxonomy. The three required top-level tags are:

| Tag | When to apply |
| --- | --- |
| `mycompany_install` | Tasks that install packages, binaries, or files |
| `mycompany_configure` | Tasks that write configuration files or modify system settings |
| `mycompany_validate` | Tasks that check state, run tests, or assert expected conditions |

Example:

```yaml
- name: Install nginx package
  ansible.builtin.package:
    name: nginx
    state: present
  tags:
    - mycompany_install

- name: Deploy nginx configuration
  ansible.builtin.template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
  tags:
    - mycompany_configure

- name: Verify nginx is listening on port 80
  ansible.builtin.wait_for:
    port: 80
    timeout: 30
  tags:
    - mycompany_validate
```

Tasks without at least one MyCompany tag will produce a warning from `mycompany-role-linter` and will fail in strict mode (enabled for all production pipelines).

---

## Secrets Handling

### Production environments

In production, all secrets must be retrieved at runtime from **HashiCorp Vault** using the `mycompany.infrastructure.vault_secret` lookup plugin, which is part of the approved `mycompany.infrastructure` collection:

```yaml
- name: Configure database connection
  ansible.builtin.template:
    src: db.conf.j2
    dest: /etc/app/db.conf
  vars:
    db_password: "{{ lookup('mycompany.infrastructure.vault_secret', 'secret/prod/database/password') }}"
    db_user: "{{ lookup('mycompany.infrastructure.vault_secret', 'secret/prod/database/username') }}"
```

The `mycompany.infrastructure.vault_secret` plugin automatically authenticates to the MyCompany Corp HashiCorp Vault cluster using the host's AppRole credentials. No manual token management is needed in playbooks. For full plugin documentation, see the collection's [vault_secret lookup guide](../lookup/vault_secret.md).

### Development and staging environments

For `dev` and `staging` environments only, `ansible.builtin.vault_encrypted_file` references are permitted as a convenience during development:

```yaml
vars_files:
  - vars/vault.yml  # ansible-vault encrypted, dev/staging only
```

**Never commit Ansible Vault-encrypted files to repositories that target production.** The MyCompany CI validator checks `mycompany_env` and will reject pipelines that reference `vars_files` with vault-encrypted content when the target environment is `prod`.

### Secret naming in Vault

Secrets in HashiCorp Vault follow the path convention:

```
secret/<env>/<service>/<key>
```

Examples:
- `secret/prod/database/password`
- `secret/staging/redis/auth_token`
- `secret/prod/smtp/api_key`

---

## Using mycompany.infrastructure Modules in Playbooks

When tasks require infrastructure operations covered by the `mycompany.infrastructure` collection (server provisioning, database management, network configuration, application deployment), use the collection modules directly:

```yaml
- name: Provision application server
  mycompany.infrastructure.create_server:
    name: "app-{{ mycompany_env }}-01"
    provider: aws
    region: eu-west-1
    instance_type: t3.medium
    tags:
      env: "{{ mycompany_env }}"
      team: "{{ mycompany_owner_team }}"
  tags:
    - mycompany_install
```

Note how `mycompany_env` and `mycompany_owner_team` (required host variables from the Inventory Policy) are used to drive module parameters. This ensures consistent tagging across all provisioned resources.

---

## Playbook and Role Development Workflow

1. Fork the appropriate starter template from `https://gitlab.mycompany.internal/ansible/templates`
2. Name your role following the `mycompany_<function>` convention
3. Populate `meta/main.yml` with the required fields before writing any tasks
4. Apply MyCompany tag taxonomy (`mycompany_install`, `mycompany_configure`, `mycompany_validate`) to all tasks
5. Use `mycompany.infrastructure.vault_secret` for any secrets required by the role
6. Run `mycompany-role-linter` locally before opening a merge request:

```bash
mycompany-role-linter --role-path ./mycompany_<function>/
```

7. Submit the merge request and request Platform Team review via `#platform-ops` Slack