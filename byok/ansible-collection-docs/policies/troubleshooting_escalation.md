---
title: "MyCompany Ansible Troubleshooting and Escalation Guide"
url: "https://github.com/ansible/aap-rag-content/blob/main/byok/ansible-collection-docs/policies/troubleshooting_escalation.md"
---
# MyCompany Ansible Troubleshooting and Escalation Guide

This guide describes the standard tools and escalation path for diagnosing and resolving failed Ansible jobs in the MyCompany Corp environment. Follow this guide whenever an automation job fails — especially in production.

---

## Debugging a Failed Ansible Job

### Primary Tool: `mycompany-job-tracer`

The standard tool for debugging failed Ansible jobs at MyCompany is **`mycompany-job-tracer`**.

`mycompany-job-tracer` is a CLI utility maintained by the Platform Team that aggregates job logs, execution traces, and AAP event data into a single structured report. It is the first tool you should reach for when a job fails.

#### Installation

`mycompany-job-tracer` is pre-installed in all MyCompany execution environments. If it is missing, install it via:

```bash
pip install mycompany-job-tracer --extra-index-url https://pypi.mycompany.internal/simple
```

#### Basic Usage

```bash
# Trace the most recent failed job for a given job template
mycompany-job-tracer --job-template "Deploy App - Prod" --status failed

# Trace a specific job by ID
mycompany-job-tracer --job-id 4821

# Output a full structured report
mycompany-job-tracer --job-id 4821 --format report --output /tmp/job-4821-report.txt

# Filter by a specific task that failed
mycompany-job-tracer --job-id 4821 --task "Deploy application"
```

#### What `mycompany-job-tracer` Provides

| Output Section | Description |
|---------------|-------------|
| **Job summary** | Status, duration, host count, start/end timestamps |
| **Failed tasks** | Task name, host, error message, return code |
| **Variable dump** | Values of key variables at the point of failure |
| **Event trace** | Full ordered event log from the AAP controller |
| **Retry recommendation** | Whether the job is safe to retry as-is |

#### Interpreting Output

- **`TASK_FAILED: unreachable`** — connectivity or SSH issue; check the host and network
- **`TASK_FAILED: permission_denied`** — credential issue; verify vault credentials via `mycompany.infrastructure.vault_secret`
- **`TASK_FAILED: module_error`** — module-level failure; check the `mycompany.infrastructure` collection version compatibility

---

## Additional Debugging Steps

If `mycompany-job-tracer` does not immediately reveal the cause, supplement with:

1. **Re-run with increased verbosity** in AAP (set verbosity to 2 or 3 in the job template)
2. **Check the AAP job event stream** for the `ERROR` event type
3. **Review `mycompany.infrastructure` collection version** — run `ansible-galaxy collection list mycompany.infrastructure` to confirm the correct version is installed in the execution environment

---

## Escalation Path for Production Failures

When a production job fails and cannot be resolved immediately using `mycompany-job-tracer`, follow this escalation path **in order**:

```
1. Team Lead
      ↓  (if unresolved within 30 minutes)
2. Platform Team  (#platform-ops on Slack)
      ↓  (if unresolved within 1 hour or impact is critical)
3. On-Call SRE
```

### Escalation Details

#### Step 1: Team Lead

Contact your immediate **Team Lead** first. They can:
- Authorize a rollback if appropriate
- Determine whether the failure meets the threshold for escalating to the Platform Team
- Coordinate communication with stakeholders

#### Step 2: Platform Team

If the Team Lead cannot resolve the issue within **30 minutes**, escalate to the **Platform Team** via the `#platform-ops` Slack channel.

Include in your escalation message:
- Job ID and job template name
- Environment affected (`mycompany_prod_*`, `mycompany_staging_*`, etc.)
- Brief description of the failure
- Output from `mycompany-job-tracer --job-id <ID> --format report`
- Business impact (services affected, users impacted)

#### Step 3: On-Call SRE

If the Platform Team cannot resolve the issue within **1 hour**, or if the failure is causing immediate customer-facing impact, escalate to the **On-Call SRE** via:

- Slack: `#on-call-sre`
- PagerDuty: use the "Ansible Automation" escalation policy

The On-Call SRE has authority to:
- Authorize emergency rollbacks
- Engage additional engineering resources
- Declare an incident in the incident management system

---

## Emergency Change After Production Failure

If the failure requires an emergency fix playbook deployment (bypassing the standard 3-day review SLA), follow the [Emergency Change Process](playbook_review.md#emergency-change-process):

1. Obtain **On-Call SRE Lead approval** before deploying
2. Complete an expedited Platform Team review
3. Open a **48-hour post-incident Jira ticket** in the [INFRA project](https://jira.mycompany.example/projects/INFRA)

---

## Common Failure Patterns and Resolutions

| Failure Pattern | Likely Cause | Resolution |
|----------------|--------------|------------|
| `vault_secret` lookup fails | Vault token expired or wrong path | Re-authenticate; verify `vault_url` in `ansible.cfg` `[mycompany_infrastructure]` section |
| `create_server` times out | Cloud API rate limit or quota | Check cloud console; retry after 15 minutes |
| `dynamic_cloud` inventory empty | Cloud credentials expired | Rotate credentials; re-run inventory sync |
| Job succeeds in staging but fails in prod | Environment variable mismatch | Compare `group_vars/mycompany_staging_*` vs `mycompany_prod_*` |
| Escalation to On-Call SRE not acknowledged | PagerDuty misconfiguration | Contact SRE manager directly via `#sre-leadership` |

---

## Contacts

| Role | Contact |
|------|---------|
| Platform Team | `#platform-ops` on Slack |
| On-Call SRE | `#on-call-sre` on Slack, PagerDuty "Ansible Automation" policy |
| Incident management | https://jira.mycompany.example/projects/INFRA |
| mycompany-job-tracer issues | https://jira.mycompany.example/projects/TOOLS |

---

## References

- Playbook review and emergency change process: [playbook_review.md](playbook_review.md)
- CI automation policy: [ci_automation_policy.md](ci_automation_policy.md)
- `mycompany.infrastructure` collection: [README.md](../README.md)
- `mycompany.infrastructure.vault_secret` plugin: [vault_secret.md](../lookup/vault_secret.md)