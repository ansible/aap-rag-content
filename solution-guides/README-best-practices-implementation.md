
# Best Practices for Writing Implementation Guides <!-- omit in toc -->

A framework for creating enterprise-grade implementation guides for Ansible Automation Platform.

> **Two guide types:** This document is for **Implementation Guides** only. Solution Guides use a separate framework and rubric on the [Best Practices hub](best-practices.md).

> **Quick start:** Jump to the [Starter Template](#appendix-starter-template).

## Who This Framework Is For

This framework is for **platform owners, infrastructure leads, and senior automation engineers** who create guides for deploying, tuning, and operating AAP in production. Implementation guides focus on reliability, performance, and day-2 operations -- not partner integration outcomes.

### Who We Write For

| Persona | What They Need from an Implementation Guide |
|---------|---------------------------------------------|
| **Platform Owner / SRE** | Step-by-step deployment or tuning procedures with validation and rollback guidance |
| **Infrastructure Architect** | Architecture decisions, sizing, topology diagrams, and tradeoff tables |
| **Operations Lead** | Runbooks, monitoring guidance, and production impact warnings they can hand to an implementation team |

### Where Implementation Guides Fit

Implementation guides answer **how** to configure AAP for production. They complement [Solution Guides](guide-types.md), which show **AAP working with a partner** to solve a specific operational problem.

| Content Type | Purpose |
|-------------|---------|
| **Solution Guide** | Partner integration reference architecture with business outcomes |
| **Implementation Guide** | Platform deployment, tuning, HA/DR, developer tooling, and day-2 operations |

---

### The Framework at a Glance

| Step | Section | What It Covers |
|------|---------|---------------|
| 1 | [Title](#1-title) | Platform or deployment outcome |
| 2 | [Overview](#2-overview) | Problem statement, scope, and expected result |
| 3 | [Background](#3-background) | Environment context, validation methodology, constraints |
| 4 | [Architecture](#4-architecture) | Topology diagrams, component decisions, sizing |
| 5 | [Prerequisites](#5-prerequisites) | AAP version, platform dependencies, access requirements |
| 6 | [Implementation Walkthrough](#6-implementation-walkthrough) | Step-by-step technical depth with featured code |
| 7 | [Validation](#7-validation) | Concrete tests, verbatim expected output, troubleshooting |
| 8 | [Day-2 Operations](#8-day-2-operations) | Monitoring, maintenance, failover, known issues |
| 9 | [Related Guides](#9-related-guides) | Cross-links to complementary platform and solution guides |

---

## 1. Title

**Rule:** Titles must describe a platform or deployment outcome.

**Good:**
- "PostgreSQL Autovacuum Tuning Guide for Ansible Automation Platform"
- "High Availability and Disaster Recovery for AAP on OpenShift"

**Bad:**
- "Using CloudNativePG"
- "AAP Configuration Overview"

---

## 2. Overview

- 2-4 sentences defining the operational problem (performance, availability, scale)
- A `guide-outcome` callout with the concrete result after following the guide
- Scope boundaries: what this guide does and does not cover

---

## 3. Background

Explain the environment where the guide was developed and validated: AAP version, platform (OpenShift, VMs), database or storage stack, and workload scale. Readers need this to judge whether the tuning or architecture applies to their deployment.

---

## 4. Architecture

- At least one Mermaid or architecture diagram
- Component tables (nodes, operators, storage, networking)
- Decision rationale: why this topology, not alternatives

---

## 5. Prerequisites

- AAP and platform version requirements
- Access levels (cluster admin, database superuser, etc.)
- **Operational Impact** rating: None | Low | Medium | High
- Collections or operators only when the guide uses Ansible automation to deploy

---

## 6. Implementation Walkthrough

- Minimum 3 numbered steps with substeps where needed
- Featured code blocks: YAML CRs, `postgresql.conf` snippets, `oc` commands, runbook steps
- Per-step notes on rollback or blast radius where changes are disruptive

---

## 7. Validation

Mandatory for every implementation guide:

- At least one concrete test with commands or queries
- Verbatim expected output (or a table of acceptable ranges)
- Troubleshooting table mapping symptoms to causes and fixes

---

## 8. Day-2 Operations

- Monitoring metrics and alert thresholds
- Maintenance windows and upgrade considerations
- Failover, failback, or tuning adjustment procedures
- Known issues with workarounds

---

## 9. Related Guides

Cross-link to:
- Complementary implementation guides (for example, HA/DR before autovacuum tuning)
- Solution guides that run on the platform this guide configures

---

## Reference

<details markdown="1">
<summary>Quality Scoring Rubric</summary>

Grade implementation guides against this rubric before publishing:

| Category | Weight |
|----------|--------|
| Outcome Clarity (platform/deployment goal) | 15% |
| Architecture Clarity | 25% |
| Technical Executability | 25% |
| Validation/Testability | 20% |
| Production and Day-2 Readiness | 15% |

Score each 1-5. Multiply by weight for a final score out of 10. Anything below 3 in any category -- revise before publish.

</details>

<details markdown="1">
<summary>Common Failure Modes</summary>

Reject guides that exhibit any of these patterns:

- Architecture diagram with no walkthrough steps
- Walkthrough with no validation or expected output
- No operational impact rating on disruptive changes
- No day-2 or troubleshooting guidance for production deployments
- Copy-paste examples that fail when applied literally (invalid inventory, wrong command order)

</details>

<details markdown="1">
<summary>Minimum Depth Standard</summary>

| Indicator | Minimum | Ideal |
|-----------|---------|-------|
| Walkthrough steps | 3 | 5-8 |
| Code or config blocks | 2 | 4-8 |
| Diagrams | 1 | 2-3 |
| Validation scenarios | 1 | 2-3 (including failure cases) |
| Troubleshooting rows | 3 | 5-8 |

</details>

---

## Appendix: Starter Template

````markdown
<div class="guide-header">

<h1>[Platform Topic]</h1>

<span class="guide-type-badge guide-type-badge--implementation"><i class="fas fa-cogs" aria-hidden="true"></i> Implementation Guide</span>

</div>

## Overview

<!-- Problem statement and guide-outcome callout -->

## Background

<!-- Validation environment: AAP version, platform, scale -->

## Architecture

<!-- Mermaid diagram and component table -->

## Prerequisites

- **Ansible Automation Platform X.X+**
- **Operational Impact:** Low | Medium | High

## Implementation Walkthrough

### Step 1: [Name]

<!-- Commands, CRs, or config with explanation -->

## Validation

<!-- Test command, expected output, troubleshooting table -->

## Day-2 Operations

<!-- Monitoring, maintenance, known issues -->

## Related Guides

- [Complementary guide](README-example.md)
````
