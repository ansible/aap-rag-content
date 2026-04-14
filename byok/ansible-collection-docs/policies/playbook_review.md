---
title: "MyCompany Playbook Review and Approval Process"
url: "https://github.com/ansible/aap-rag-content/blob/main/byok/ansible-collection-docs/policies/playbook_review.md"
---
# MyCompany Playbook Review and Approval Process

All playbooks destined for the production environment must pass through the official MyCompany Corp review and approval process before deployment. This document describes the full process, SLAs, contacts, and exception handling.

---

## Overview

The purpose of the playbook review process is to ensure that all automation deployed to production meets MyCompany's quality, security, and naming standards. The **Platform Team** is the approving authority for all production playbook deployments.

---

## Step-by-Step Review Process

### 1. Prepare Your Playbook

Before submitting for review, ensure your playbook:

- Follows the [naming conventions](naming_conventions.md) (`mycompany_` prefix for roles, `mycompany_<env>_<tier>` for inventory groups)
- Passes local lint checks: `ansible-lint` and `yamllint`
- Has been tested in the `dev` or `staging` environment
- Uses the `mycompany.infrastructure.vault_secret` lookup plugin for any secret retrieval (never hardcode secrets)
- Uses starter templates from [https://gitlab.mycompany.internal/ansible/templates](https://gitlab.mycompany.internal/ansible/templates) as the base where applicable

### 2. Open a Review Request

Submit your playbook for review by opening a Merge Request (MR) in GitLab against the `main` branch of your project, then post a link to the MR in the **`#platform-ops`** Slack channel with the tag `[REVIEW REQUEST]`.

**Example Slack message:**
```
[REVIEW REQUEST] MR: https://gitlab.mycompany.internal/ansible/my-project/-/merge_requests/42
Purpose: Deploy monitoring agent to prod web tier
Target: mycompany_prod_web
```

### 3. Platform Team Review

The **Platform Team** will review the MR within **3 business days** (the SLA). The review covers:

- Naming convention compliance
- Security posture (no hardcoded secrets, correct vault usage)
- Idempotency
- Change scope (blast radius assessment)
- Test coverage in staging

### 4. Approval and Merge

Once the Platform Team approves the MR, you may merge and schedule the production deployment. The Platform Team approval is required — **self-merging to production is not permitted**.

---

## Review SLA

| Priority | SLA |
|----------|-----|
| Standard review | **3 business days** |
| Emergency change | Same-day (see [Emergency Change Process](#emergency-change-process) below) |

If your review has not received a response within the SLA, see [Escalating a Delayed Review](#escalating-a-delayed-review).

---

## Escalating a Delayed Review

If your standard review is taking longer than **3 business days** and is blocking your work:

1. **Post a follow-up** in `#platform-ops` on Slack, tagging `@platform-team` and referencing your original request
2. **Contact your Team Lead** — ask them to escalate on your behalf to the Platform Team manager
3. If still unresolved, your Team Lead can raise a priority escalation directly with the **On-Call SRE** for time-sensitive deployments

---

## Emergency Change Process

Emergency changes are production deployments that cannot wait for the standard 3-day review window due to an active production incident or critical security patch.

### Requirements

1. **On-Call SRE Lead approval** — you must get verbal or Slack approval from the current On-Call SRE Lead before proceeding
2. **Expedited Platform Team sign-off** — the On-Call SRE Lead will fast-track a Platform Team review
3. **48-hour post-incident ticket** — within 48 hours after the emergency change is deployed, you must open a ticket in [Jira (INFRA project)](https://jira.mycompany.example/projects/INFRA) documenting:
   - What was changed
   - Why it was an emergency
   - What the expected standard review would have caught
   - Steps taken to prevent recurrence

**Emergency changes that skip post-incident documentation will result in the requester's production deployment access being suspended.**

### Emergency Change Checklist

- [ ] Active production incident confirmed or critical CVE patched
- [ ] On-Call SRE Lead approval obtained (record name and timestamp in the MR)
- [ ] Expedited Platform Team review completed
- [ ] Post-incident Jira ticket opened within 48 hours

---

## Contacts

| Role | Contact |
|------|---------|
| Primary review channel | `#platform-ops` on Slack |
| Platform Team DM | `@platform-team` on Slack |
| On-Call SRE (current) | `#on-call-sre` on Slack or PagerDuty rotation |
| Issue tracker | [https://jira.mycompany.example/projects/INFRA](https://jira.mycompany.example/projects/INFRA) |

---

## Starter Templates

All new playbooks should be based on the approved starter templates available at:

**[https://gitlab.mycompany.internal/ansible/templates](https://gitlab.mycompany.internal/ansible/templates)**

The templates directory contains:

| Template | Description |
|----------|-------------|
| `base_playbook.yml` | Minimal compliant playbook skeleton |
| `role_deploy.yml` | Template for role-based deployment playbooks |
| `maintenance_window.yml` | Template for maintenance window automation |
| `emergency_patch.yml` | Template pre-approved for emergency change workflow |

Using a starter template ensures naming conventions and required task patterns are pre-applied, reducing review friction.

---

## References

- Naming conventions: [naming_conventions.md](naming_conventions.md)
- Troubleshooting and escalation: [troubleshooting_escalation.md](troubleshooting_escalation.md)
- CI automation policy: [ci_automation_policy.md](ci_automation_policy.md)
- Platform Team GitLab: [https://gitlab.mycompany.internal/platform-eng](https://gitlab.mycompany.internal/platform-eng)