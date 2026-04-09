---
title: "MyCompany Corp Automation Standards"
url: "https://internal.mycompany.example.com/wiki/automation/standards"
---
# MyCompany Corp Automation Standards

This document defines the mandatory standards for all Ansible automation work at MyCompany Corp. All teams developing, maintaining, or deploying Ansible content must comply with these standards.

---

## Approved Collections

The `mycompany.infrastructure` collection is the **approved standard** for infrastructure automation at MyCompany Corp. All infrastructure-related tasks (server provisioning, database management, network configuration, application deployment) must use the collection's modules before falling back to community content.

Install the collection from the internal mirror:

```bash
ansible-galaxy collection install mycompany.infrastructure
```

Or pin the version in `requirements.yml`:

```yaml
collections:
  - name: mycompany.infrastructure
    version: ">=1.4.0"
```

Using the `mycompany.infrastructure` collection for infrastructure work is required. Using raw API calls or community equivalents where the collection provides the same functionality is not permitted in production playbooks.

---

## Role Naming Conventions

All custom Ansible roles created at MyCompany Corp **must** use the `mycompany_` prefix. This prefix is required to distinguish internal roles from upstream community and Red Hat content, including the `mycompany.infrastructure` collection itself.

### Required naming format

```
mycompany_<function>
```

Examples of correct role names:

- `mycompany_webserver`
- `mycompany_database_backup`
- `mycompany_firewall_baseline`
- `mycompany_monitoring_agent`

Using the upstream convention (e.g., `ansible-webserver`, `redhat.rhel.firewall`) in MyCompany Corp repositories is prohibited and will cause the lint gate to fail during CI validation.

---

## Playbook Review and Approval Workflow

All playbooks must be reviewed and approved by the **Platform Team** before any deployment to production environments.

### Submission process

1. Open a review request in the `#platform-ops` Slack channel using the pinned request template.
2. Attach the playbook repository URL and the target environment.
3. A Platform Team member will acknowledge within **1 business day** and complete the review within **3 business days**.

### Escalation for delayed reviews

If the Platform Team review has not been completed within **3 business days**, escalate directly to the **Automation Chapter Lead** at `automation-chapter-lead@mycompany.example.com`. Include the original Slack thread link and the date the review was requested.

### Emergency and hotfix changes

Emergency changes that cannot wait for the standard review process are permitted under the following conditions:

- Written approval must be obtained from the **On-Call SRE Lead** before execution (via `#sre-oncall` Slack or direct message).
- A post-incident review ticket must be created in `https://tickets.mycompany.internal` within **48 hours** of the change, tagged with `emergency-change`.
- The standard Platform Team review must be completed retrospectively within **5 business days**.

---

## CI Pipeline Execution Requirements

For all CI pipeline runs, automation must be executed using:

```bash
ansible-navigator run <playbook.yml> --mode stdout
```

The `--mode stdout` flag is a **non-negotiable org standard** for CI environments. Interactive and TUI modes (`--mode interactive`) are not permitted in any automated pipeline. This ensures that CI logs are captured as plain text and are parseable by the MyCompany log aggregation system.

This requirement differs from the default `ansible-navigator` behavior and from the multiple execution modes described in the upstream Ansible documentation. At MyCompany Corp, `--mode stdout` is the only approved mode for CI.

---

## Starter Templates

All new automation projects must be forked from the official MyCompany Corp starter templates. Starting from scratch or from community skeletons is not permitted for projects that will be deployed to production.

Templates are maintained at:

```
https://gitlab.mycompany.internal/ansible/templates
```

Available templates:

| Template | Purpose |
| --- | --- |
| `mycompany-playbook-starter` | Single-playbook automation projects |
| `mycompany-role-starter` | Standalone Ansible roles |
| `mycompany-collection-starter` | Ansible collections with multiple roles |
| `mycompany-ee-starter` | Custom Execution Environment definitions |

---

## Secrets Management

All secrets used in **production** playbook runs must be retrieved at runtime from **HashiCorp Vault** using the `mycompany.infrastructure.vault_secret` lookup plugin:

```yaml
db_password: "{{ lookup('mycompany.infrastructure.vault_secret', 'secret/prod/database/password') }}"
```

The `mycompany.infrastructure.vault_secret` plugin is part of the approved `mycompany.infrastructure` collection and automatically authenticates to the MyCompany Corp HashiCorp Vault cluster using the host's AppRole credentials. No manual token management is needed in playbooks.

Storing secrets in Ansible Vault-encrypted YAML files (`ansible-vault encrypt`) is **not permitted** in production repositories. Ansible Vault may only be used in `dev` and `staging` environments.

Contact the Platform Team in `#platform-ops` to request HashiCorp Vault access for a new automation project.

---

## Compliance and Enforcement

These standards are enforced automatically:

- **Lint gate**: `mycompany-role-linter` runs on every merge request and will block merges that violate naming conventions or are missing required metadata.
- **CI validation**: The MyCompany CI validator checks for correct `ansible-navigator` flags and rejects pipelines that use non-approved execution modes.
- **Quarterly audits**: The Platform Team audits all active automation repositories for compliance each quarter.

Repeated violations after two warnings will result in the project being locked from production deployments until compliance is restored.