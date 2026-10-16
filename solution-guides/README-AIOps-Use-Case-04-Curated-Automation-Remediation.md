{% raw %}
<div class="guide-header">

<h1>Curated Automation Remediation: From EDA to Orchestrated Automation</h1>

<span class="guide-type-badge guide-type-badge--use-case"><i class="fas fa-layer-group" aria-hidden="true"></i> AIOps Use Case</span>

</div>

> **Pattern guide, not a partner integration.**
>
> Observability and ITSM partners in examples (Splunk, Instana, ServiceNow) show integration points; the pattern is the **approved automation library**, not a single vendor.

## Overview

Teams need consistent remediation, but unconstrained AI agents may generate a different fix every time the same incident recurs. **Curated automation remediation** keeps execution in a library of approved workflows while AI **selects** the right playbook from that library under guardrails and approvals.

**Challenge:** Speed of AI suggestions without sacrificing trust, auditability, or change control.

**Solved with AI + automation:** Automation teams maintain approved remediation workflows. AI intercepts incidents and chooses from curated options. AAP executes through governed, auditable processes.

**Business outcomes:** Consistent execution, faster remediation, improved auditability, reduced operational risk.

> **Buyer question:**
>
> How do we remediate faster using automation teams already trust?

## Background

This use case sits at **Walk** maturity: event- or ticket-initiated flows that combine EDA, inference, and job templates. It pairs naturally with Red Hat Lightspeed and pre-approved content at Crawl/Walk and with Automation code assistant at Run **only inside policy boundaries** -- selection from curated content remains the default for production.

For a shared high-level Detect → MCP → select → execute walkthrough across partners, see [AIOps automation with Ansible](README-AIOps.md#aiops-workflow). This page is the dedicated pattern guide and will expand with deeper scenarios, demos, and Arcade content.

## Solution

- **EDA** triggers on observability or ITSM events (or an operator starts from an AI client)
- **AAP MCP** exposes the **approved automation library** -- job templates and workflows the AI can search like a menu
- **AAP** runs only **approved** job templates and workflows selected through MCP (RBAC follows the operator token)
- **AI** maps incident context to library entries (patch, restart, expand storage, rotate certificate, update firewall rule, and similar) without generating new playbooks at incident time
- **AO** adds approval nodes and routing when multiple curated options match

### Who Benefits

| Persona | Challenge | What They Gain |
|---------|-----------|----------------|
| **Automation lead** | Shadow fixes outside AAP | All remediation through the library |
| **SRE** | Repeated incidents, ad hoc scripts | Same fix every time, faster |
| **Security / compliance** | Unaudited AI-generated changes | Selection only; execution is governed |

## Prerequisites

- Ansible Automation Platform 2.6.4 or later with MCP gateway access for job template discovery and launch ([DevTools MCP setup](README-Ansible-DevTools.md#connecting-to-ansible-automation-platform))
- Event-Driven Ansible for event-initiated selection flows
- Automation orchestrator when approvals and branching are required

## EDA to AO adoption path

> **Coming soon:**
>
> Walkthrough scenarios (EDA trigger, AI selection from library, approval, AAP job) will be added in a future revision.

### Stage 1: EDA + AAP only

Static mapping from alert type to one approved job template.

### Stage 2: AI enrichment

AI chooses among labeled job templates based on incident context.

### Stage 3+: Automation orchestrator

Approval gates, switch nodes for confidence, and validation loops after remediation.

## Validation

| Symptom | Status |
|---------|--------|
| End-to-end scenario tests | Content in progress |

## Related Guides

- [Common AIOps Use Cases](aiops-use-cases.md)
- [AIOps automation with Ansible](README-AIOps.md)
- [RHEL Patching with Red Hat Lightspeed and Ansible MCP Server](README-Patching-RHEL.md)
- [Automated incident remediation with IBM Instana](README-Instana-AIOps.md)
- [AIOps with Splunk and Event-Driven Ansible](README-AIOps-Splunk-ITSI.md)
{% endraw %}
