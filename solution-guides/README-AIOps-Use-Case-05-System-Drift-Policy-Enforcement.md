{% raw %}
<div class="guide-header">

<h1>System-Level Drift and Policy Enforcement: From EDA to Orchestrated Automation</h1>

<span class="guide-type-badge guide-type-badge--use-case"><i class="fas fa-layer-group" aria-hidden="true"></i> AIOps Use Case</span>

</div>

> **Pattern guide, not a partner integration.**
>
> The network capacity example illustrates **system-level** drift (everything green per host, environment no longer meets design intent). Apply the same pattern to compliance, security, and configuration policy.

## Overview

Organizations struggle to identify gradual operational, security, and compliance drift before it impacts production. Individual systems can report healthy while the **environment** accumulates risk -- policy violations, lost redundancy, or capacity erosion.

**Challenge:** Reactive audits and threshold-only monitoring miss slow failure modes.

**Solved with AI + automation:** Automation continually collects operational, compliance, and configuration data. AI correlates signals across services and environments. Drift is evaluated against desired policies; outcomes include tickets, reports, or automated remediation.

**Business outcomes:** Continuous compliance, reduced risk, operational consistency, audit evidence.

This use case sits at **Run** maturity alongside self-healing: continuous correlation, preventative remediation, and policy enforcement at scale rather than one-off orchestration.

> **Buyer question:**
>
> How do we prevent slow failure and risk accumulation in the first place?

## Background

Scheduled reviews and compliance scans are natural entry points. The distinguishing idea is **correlation across the stack**: Ansible supplies authoritative configuration and inventory; AI interprets whether the whole system still matches design intent.

## Solution

- **EDA + AAP** for scheduled collection, policy checks, and remediation playbooks
- **AI** for cross-domain correlation (for example intended 100 Gbps fabric vs effective 50 Gbps with healthy per-switch metrics)
- **AO** for ticket creation, reporting workflows, and approved remediation sequences

### Who Benefits

| Persona | Challenge | What They Gain |
|---------|-----------|----------------|
| **Compliance officer** | Point-in-time audits | Continuous evidence |
| **Network / platform architect** | Hidden capacity or redundancy loss | System-level drift detection |
| **Operations leader** | Incidents that "came out of nowhere" | Preventive remediation |

## Prerequisites

- Ansible Automation Platform 2.5 or later
- Policy and inventory sources integrated with playbooks or MCP
- Automation orchestrator for multi-step enforce-and-report workflows (Run maturity)

## EDA to AO adoption path

> **Coming soon:**
>
> Stage content including the network capacity drift narrative from the AIOps 301 deck will be expanded with validation steps.

### Stage 1: EDA + AAP only

Scheduled scans, reports, and manual remediation job templates.

### Stage 2: AI enrichment

AI summaries of drift and recommended actions on tickets or dashboards.

### Stage 3+: Automation orchestrator

Open ticket, generate report, or run automated remediation branches with approvals.

## Validation

| Symptom | Status |
|---------|--------|
| End-to-end scenario tests | Content in progress |

## Related Guides

- [Common AIOps Use Cases](aiops-use-cases.md)
- [AIOps automation with Ansible](README-AIOps.md)
- [Zero Trust Architecture with Ansible Automation Platform](README-ZTA.md)
{% endraw %}
