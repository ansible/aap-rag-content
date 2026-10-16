{% raw %}
<div class="guide-header">

<h1>Intelligent Capacity Orchestration: From EDA to Orchestrated Automation</h1>

<span class="guide-type-badge guide-type-badge--use-case"><i class="fas fa-layer-group" aria-hidden="true"></i> AIOps Use Case</span>

</div>

> **Pattern guide, not a partner integration.**
>
> Examples may reference hybrid cloud and virtualization platforms. Adapt inventory and metrics sources to your environment.

## Overview

Capacity issues often emerge **across** systems and environments before any single dashboard breaches a threshold. Teams need continuous collection of utilization and performance data, AI-assisted identification of emerging constraints, and orchestrated responses (add capacity, reclaim capacity, or publish a capacity plan).

**Challenge:** Siloed capacity planning and reactive firefighting when growth or failure domains shift.

**Solved with AI + automation:** Automation continuously collects utilization, performance, and capacity data. AI correlates signals across services and environments. Emerging constraints are identified before service impact; governed workflows execute approved capacity changes.

**Business outcomes:** Fewer outages from exhaustion, predictable scaling, aligned capacity and demand plans.

> **Buyer question:**
>
> How do we anticipate capacity needs across hybrid environments?

## Background

Traditional monitoring answers "is this host red?" Capacity orchestration answers "will this **environment** still meet its design intent next month?" Entry points include scheduled capacity reviews, ticket-initiated expansion requests, and event-driven alerts on utilization trends.

## Solution

- **EDA + AAP** for metric collection, trend reporting, and execution of approved scale-out or reclamation playbooks
- **AI** for cross-system correlation and capacity risk narratives
- **AO** for multi-step plans: gather dependencies, generate recommendations, approval, execute, validate

### Who Benefits

| Persona | Challenge | What They Gain |
|---------|-----------|----------------|
| **Capacity planner** | Spreadsheet-driven forecasts | Live data and automated plan drafts |
| **Platform engineer** | Manual coordination across teams | Orchestrated, auditable capacity changes |
| **Service owner** | Surprise saturation events | Early warning and governed response |

## Prerequisites

- Ansible Automation Platform 2.5 or later
- Inventory and metrics accessible to playbooks or MCP tools
- Automation orchestrator for multi-stage capacity workflows (Walk maturity)

## EDA to AO adoption path

> **Coming soon:**
>
> Detailed stages (read-only capacity dashboards, AI risk summaries, orchestrated add/reclaim flows) are in development.

### Stage 1: EDA + AAP only

Scheduled fact collection and threshold-based job templates.

### Stage 2: AI enrichment

AI-generated capacity plans and risk summaries attached to tickets or reports.

### Stage 3+: Automation orchestrator

User- or schedule-initiated workflows: dependencies, capacity plan generation, approval, execution.

## Validation

| Symptom | Status |
|---------|--------|
| End-to-end scenario tests | Content in progress |

## Related Guides

- [Common AIOps Use Cases](aiops-use-cases.md)
- [AIOps automation with Ansible](README-AIOps.md)
- [AI Infrastructure automation with Ansible](README-IA.md)
{% endraw %}
