---
title: "MyCompany Corp Automation Troubleshooting Guide"
url: "https://internal.mycompany.example.com/wiki/automation/troubleshooting"
---
# MyCompany Corp Automation Troubleshooting Guide

This guide covers how to diagnose failed Ansible automation jobs at MyCompany Corp, which internal tools to use, and how to escalate when self-service troubleshooting is not sufficient.

---

## Internal Debugging Tools

### mycompany-job-tracer

The primary tool for diagnosing Ansible job failures is **`mycompany-job-tracer`**, a web-based UI maintained by the Platform Team.

**Access:** `https://tools.mycompany.internal/job-tracer`

`mycompany-job-tracer` ingests Ansible stdout logs and provides:

- Task-level timing breakdown (identify which tasks are slow or hung)
- Variable snapshot at the point of failure (see what values were in scope)
- Diff output for tasks that report changes
- Side-by-side comparison between two job runs
- Direct link to the relevant playbook line in GitLab

To use `mycompany-job-tracer`, you need the **job ID** from the AAP job detail page. Paste the job ID into the search box on the tracer home page.

### mycompany-log-collector

Before escalating any automation issue to the Platform Team or SRE, run the **`mycompany-log-collector`** script to bundle the relevant diagnostics:

```bash
/usr/local/bin/mycompany-log-collector --job-id <JOB_ID>
```

This script collects:

- Full Ansible stdout for the job
- Gathered facts for all targeted hosts
- The last 50 task outputs with return values
- The inventory and variable files used
- Any callback plugin output

The output is a `.tar.gz` support bundle saved to `/tmp/mycompany-support-<JOB_ID>.tar.gz`. Attach this bundle to your escalation ticket or Slack message.

### Additional diagnostic commands

For targeted host-level investigation, the following commands are available on all MyCompany-managed hosts:

```bash
# Check Ansible connection and fact gathering
ansible <hostname> -m setup -i inventory/ --ask-become-pass

# Test connectivity and privilege escalation
ansible <hostname> -m ping -i inventory/ --become

# Replay the last job in check mode (dry run)
ansible-navigator run <playbook.yml> --mode stdout --check

# Test mycompany.infrastructure collection connectivity
ansible <hostname> -m mycompany.infrastructure.create_server --check -i inventory/
```

---

## Escalation Paths

### Standard escalation path for production failures

When an automation job fails in production, follow this escalation sequence:

1. **Team Lead** — notify your direct team lead immediately. They must be aware of all production failures.
2. **Platform Team** — if the issue cannot be resolved within 30 minutes, post in `#platform-ops` Slack with the job ID and a brief description. Platform Team engineers are available during business hours (09:00–18:00 CET).
3. **On-Call SRE** — if the failure is causing or at risk of causing production downtime, page the On-Call SRE via the `#sre-oncall` Slack channel. For urgent pages, use PagerDuty: `https://mycompany.pagerduty.com`.

### Who to contact when Platform Team review is slow

If you submitted a troubleshooting request or review to the Platform Team via `#platform-ops` and have not received a response within **3 business days**, escalate to the **Automation Chapter Lead** at `automation-chapter-lead@mycompany.example.com`.

Include in your escalation email:
- The original Slack thread link
- The date you submitted the request
- A brief summary of the issue and business impact

### Non-critical failures

For non-critical automation failures that are not causing production downtime:

1. Attempt self-service diagnosis using `mycompany-job-tracer` and `mycompany-log-collector`.
2. If unresolved after **two self-service attempts**, file a ticket at `https://tickets.mycompany.internal` using the template **"Automation Failure — Needs Triage"**.
3. Attach the `mycompany-log-collector` support bundle to the ticket.
4. Set the ticket label to `automation-incident` and assign it to the `platform-team` group.

---

## Production Incident Reporting

Any automation failure that causes or contributes to **production downtime** must be reported immediately, regardless of the time of day:

1. Post in `#production-incidents` Slack with:
   - A one-line summary of the failure
   - The affected service or hosts
   - The job ID (if applicable)
   - Current status (ongoing / mitigated / resolved)

2. Create an incident ticket at `https://tickets.mycompany.internal` with:
   - Label: `automation-incident`
   - Label: `production-impact`
   - Severity: set according to the MyCompany Incident Severity Guide (linked in the ticket template)

3. Attach the `mycompany-log-collector` support bundle once collected.

Platform Team and SRE On-Call monitor `#production-incidents` continuously during business hours and are paged for new messages outside of business hours.

---

## Emergency Change Exception Process

If a production automation failure requires an emergency fix that cannot wait for the standard review process, the exception process is:

1. Obtain **written approval from the On-Call SRE Lead** via `#sre-oncall` Slack before making any emergency change.
2. Execute the minimum change necessary to restore service.
3. Post a summary of the change in `#production-incidents` immediately after execution.
4. Create a post-incident review ticket at `https://tickets.mycompany.internal` within **48 hours**, tagged with `emergency-change` and `post-incident-review`.
5. Complete a retrospective standard Platform Team review within **5 business days**.

Emergency changes made without On-Call SRE Lead approval are policy violations and will be reviewed by the Automation Chapter Lead.

---

## Common Failure Patterns and Quick Fixes

| Symptom | Likely cause | First action |
| --- | --- | --- |
| `mycompany_env` variable missing | Host not fully onboarded | Add `mycompany_env` to `host_vars/<hostname>/main.yml` |
| `mycompany.infrastructure.vault_secret` lookup fails | HashiCorp Vault token expired | Re-authenticate: `vault login -method=ldap username=<you>` |
| Group name fails CI validation | Group name doesn't match `mycompany_<env>_<tier>` | Rename the group in your inventory |
| Inventory source rejected | Dynamic source not registered | Register at `https://inventory.mycompany.internal` |
| `mycompany-role-linter` fails | Missing `meta/main.yml` or wrong author field | Add or fix `meta/main.yml` (see Playbook Patterns guide) |
| ansible-navigator CI failure | Using `--mode interactive` in pipeline | Change to `--mode stdout` in your CI configuration |
| `mycompany.infrastructure` module fails | Collection version mismatch | Run `ansible-galaxy collection install mycompany.infrastructure --upgrade` |