---
title: "MyCompany CI Automation Policy"
url: "https://github.com/ansible/aap-rag-content/blob/main/byok/ansible-collection-docs/policies/ci_automation_policy.md"
---
# MyCompany CI Automation Policy

This document defines the mandatory standards for running Ansible automation in Continuous Integration (CI) pipelines at MyCompany Corp. All teams integrating Ansible playbook execution into CI/CD workflows must comply with this policy.

---

## Required Command for CI Pipelines

**The only permitted way to run Ansible automation in a MyCompany CI pipeline is:**

```bash
ansible-navigator run <playbook.yml> --mode stdout
```

The `--mode stdout` flag is **mandatory** in all CI contexts. No exceptions.

---

## Mode Policy

| Mode | Permitted in CI? | Notes |
|------|-----------------|-------|
| `--mode stdout` | **YES — required** | The only approved mode for CI pipelines |
| `--mode interactive` | **NO — prohibited** | Requires a TTY; breaks non-interactive CI runners |
| `--mode tui` | **NO — prohibited** | Requires a TTY; incompatible with pipeline log capture |

### Why `--mode stdout` is Mandatory

CI pipeline runners (GitLab CI, GitHub Actions, Jenkins, Tekton) run in non-interactive, headless environments. They do not provide a TTY. The `--mode interactive` and `--mode tui` modes require a real terminal and will either hang, crash, or produce garbled output when run in a CI context.

`--mode stdout` writes all task output directly to standard output in plain text, which:
- Is captured correctly by CI log aggregators
- Allows log parsing for pass/fail detection
- Is compatible with all CI runners used at MyCompany

**Running `--mode interactive` in CI will cause the pipeline job to hang indefinitely and must never be used.**

---

## Full CI Command Reference

A complete CI-compliant `ansible-navigator run` command looks like this:

```bash
ansible-navigator run site.yml \
  --mode stdout \
  --eei quay.mycompany.internal/ee/mycompany-ee:latest \
  --pae false \
  --pp missing
```

### Required Flags

| Flag | Value | Reason |
|------|-------|--------|
| `--mode stdout` | `stdout` | **Mandatory** — non-interactive output mode |
| `--eei` | `quay.mycompany.internal/ee/mycompany-ee:latest` | Use the approved MyCompany execution environment |
| `--pae false` | `false` | Disable pull-after-everything to use cached images |
| `--pp missing` | `missing` | Pull the EE image only if not already present |

### Optional Flags

| Flag | Description |
|------|-------------|
| `--extra-vars @vars.yml` | Pass additional variables from a file |
| `--limit mycompany_staging_*` | Restrict execution to a specific inventory group |
| `-v` or `-vv` | Increase verbosity for debugging |

---

## Execution Environment (EE)

All CI runs must use an approved MyCompany execution environment image. The standard EE is:

```
quay.mycompany.internal/ee/mycompany-ee:latest
```

This image includes:
- `ansible-core` pinned to the approved version
- `mycompany.infrastructure` collection pre-installed
- `mycompany-job-tracer` CLI
- All required Python dependencies

Using a non-approved EE or a plain `ansible-playbook` invocation instead of `ansible-navigator` is **not permitted in CI**.

---

## Settings File

Each project should include an `ansible-navigator.yml` settings file in the project root that enforces the CI defaults:

```yaml
ansible-navigator:
  mode: stdout
  execution-environment:
    image: quay.mycompany.internal/ee/mycompany-ee:latest
    pull:
      policy: missing
  playbook-artifact:
    enable: false
```

With this file in place, running `ansible-navigator run site.yml` in CI will automatically use `--mode stdout` without requiring the flag to be specified on the command line. However, the `--mode stdout` flag must still be present in pipeline configuration for clarity and auditability.

---

## Secrets in CI Pipelines

Never pass secrets as plain environment variables or inline YAML in CI pipelines. Use the `mycompany.infrastructure.vault_secret` lookup plugin to retrieve secrets at runtime from HashiCorp Vault.

The CI runner's service account has read access to the following Vault paths:
- `secret/ci/<project_name>/credentials`
- `secret/ci/<project_name>/api_keys`

See [vault_secret lookup plugin documentation](../lookup/vault_secret.md) for usage.

---

## Linting Before `ansible-navigator run`

The CI pipeline must run linting checks before executing any playbook:

```yaml
# GitLab CI example
lint:
  script:
    - ansible-lint --profile production
    - yamllint .
  before_script:
    - ansible-galaxy collection install -r requirements.yml

run:
  script:
    - ansible-navigator run site.yml --mode stdout --eei quay.mycompany.internal/ee/mycompany-ee:latest
  needs:
    - lint
```

---

## Enforcement

Violations of this policy are caught by:

1. **CI pipeline linting gate** — the Platform Team's shared CI template checks for `--mode stdout` compliance
2. **Platform Team playbook review** — CI pipeline configurations are reviewed alongside playbooks during the [standard review process](playbook_review.md)

Pipelines that use `--mode interactive` or `--mode tui` will be blocked by the linting gate and flagged for remediation.

---

## Summary

> **The correct way to run `ansible-navigator` in any MyCompany CI pipeline is `ansible-navigator run <playbook> --mode stdout`. Interactive mode (`--mode interactive`) and TUI mode (`--mode tui`) are prohibited in CI contexts.**

---

## References

- Playbook review process: [playbook_review.md](playbook_review.md)
- Naming conventions: [naming_conventions.md](naming_conventions.md)
- Troubleshooting failed CI jobs: [troubleshooting_escalation.md](troubleshooting_escalation.md)
- Secrets in CI: [vault_secret lookup plugin](../lookup/vault_secret.md)
- Starter CI templates: [https://gitlab.mycompany.internal/ansible/templates](https://gitlab.mycompany.internal/ansible/templates)