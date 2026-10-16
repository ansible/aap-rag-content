
# Best Practices for Writing Solution Guides <!-- omit in toc -->

A framework for creating enterprise-grade solution guides for Ansible Automation Platform.

> **Two guide types:** This document is for **Solution Guides** only. Implementation Guides use a separate framework and rubric on the [Best Practices hub](best-practices.md).

> **Quick start:** Jump to the [Starter Template](#appendix-starter-template).
>
> Copy the ready-made skeleton, fill in the placeholders, and score your draft against the [Quality Scoring Rubric](#reference) before publishing.

## Who This Framework Is For

This framework is for **Ansible Automation Platform field teams, solution architects, and technical content authors** who create customer-facing technical content. Solution guides are authored and maintained as markdown in GitHub -- not as Knowledge Base articles on the customer portal. This approach enables AI-assisted fact-checking, version-controlled collaboration, and continuous improvement that the KB workflow on access.redhat.com cannot support. This document defines the structure, quality bar, and review process you should follow.

### Who We Write For

Solution guides are written for **IT practitioners and decision makers evaluating or implementing Ansible Automation Platform**. The typical reader is:

| Persona | What They Need from a Solution Guide |
|---------|--------------------------------------|
| **IT Ops Engineer / SRE** | Executable examples they can adapt to their environment -- real YAML, real workflows, real validation steps |
| **Automation Architect** | A reference architecture showing how AAP components connect to external systems, with enough detail to design their own implementation |
| **IT Manager / Director** | A clear problem statement, measurable outcomes, and an incremental adoption path they can use to justify investment and manage risk |

Every section of a solution guide should serve at least one of these personas. If a section only makes sense to someone who already knows the answer, it needs to be rewritten.

Solution guides are a specific content type -- they are not the only way Red Hat publishes technical content, and understanding the differences helps you decide whether a solution guide is the right format for what you want to write.

### Where Solution Guides Fit

| Content Type | Where It Lives | Audience | Purpose | Depth |
|-------------|----------------|----------|---------|-------|
| **KB Solution** | access.redhat.com | Customer hitting a specific error | Fix a single, known issue (e.g., "Error X when upgrading AAP") | Narrow -- one problem, one fix |
| **Solution Guide** | GitHub (this repo) | Customer evaluating or implementing a solution | Explain how to solve an operational problem end-to-end using AAP | Deep -- architecture, code, validation, maturity path |
| **Blog Post** | redhat.com/blog | Broad technical audience | Announce, evangelize, or explain a concept or release | Medium -- narrative-driven, light on executable detail |
| **Learning Path** | developers.redhat.com | Developer or admin learning a skill | Teach a tool or technology through progressive, hands-on exercises | Deep -- tutorial-oriented, step-by-step skill building |

**Solution guides are the second row.** They are maintained in GitHub, not on the customer portal. They solve a real operational problem, not a single error (that's a KB Solution). They include executable automation, not just narrative (that's a blog). They are outcome-oriented, not skill-oriented (that's a learning path). Hosting them in GitHub enables version control, AI-assisted review, and collaboration workflows that static KB articles cannot provide.

> **When not to write a solution guide.**
>
> If your content is a fix for a specific error, write a KB Solution. If it's an announcement or thought leadership piece, write a blog. If it's teaching someone how to use a tool from scratch, write a learning path or tutorial. Solution guides exist in the space between -- they assume the reader knows *what* Ansible is but needs to see *how* to solve a specific operational problem with it.

---

### The Framework at a Glance <!-- omit in toc -->

These sections map 1:1 to the section names in every solution guide. When reviewing a guide, you should be able to match each section header directly to this framework.

| Step | Section | What It Covers |
|------|---------|---------------|
| 1 | [Title](#1-title) | Outcome-oriented naming convention |
| 2 | [Overview](#2-overview) | Problem statement, hero image, table of contents |
| 3 | [Background](#3-background) | Domain context -- what the topic is and why it matters |
| 4 | [Solution](#4-solution) | Components, persona mapping, demos/videos |
| 5 | [Prerequisites](#5-prerequisites) | AAP version, collections, external systems, guide metadata |
| 6 | [Workflow and Architecture](#6-workflow-and-architecture) | Diagrams, narrative walkthrough, visual patterns |
| 7 | [Solution Walkthrough](#7-solution-walkthrough) | Featured code, AAP integration, step-by-step technical depth |
| 8 | [Validation](#8-validation) | Concrete tests, expected output, troubleshooting |
| 9 | [Maturity Path, Summary, and Related Guides](#9-maturity-path-summary-and-related-guides) | Crawl/Walk/Run, summary, cross-linking |

| Section | What It Covers |
|---------|---------------|
| [Reference](#reference) | Scoring rubric, failure modes, elite guide criteria |
| [Appendix: Starter Template](#appendix-starter-template) | Copy-paste skeleton for new guides |

---

## 1. Title

**Rule:** Titles must describe an operational outcome, not a product feature.

Solution guide pages use an outcome-oriented **topic** in the `<h1>`, with a **Solution Guide** pill badge beside it (see the starter template). The topic portion should still be outcome-oriented whenever possible.

**Bad:**

- "Using the ServiceNow Collection"
- "Ansible EDA Overview"

**Good (topic in `<h1>`, type in pill badge):**

- "ServiceNow ITSM Ticket Enrichment Automation"
- "AIOps automation with Ansible"

**Better (outcome-oriented topics):**

- "Unlock AIOps with ServiceNow LEAP and Ansible MCP server"
- "Triggering Automated Remediation from Splunk Alerts with Event-Driven Ansible"

> **Tip:** When in doubt, keep the topic clear and outcome-oriented.
>
> Put the guide type in the `guide-type-badge` pill, not in the `<h1>`. Lead the guide with a problem statement in the Overview section.

**Solution vs. Tutorial:** A solution guide must solve an operational problem, not teach how to use a tool. If your guide could be titled "Getting started with X" or "How to use Y," it is a tutorial, not a solution. Reframe it around the outcome: what real-world problem does this automation solve?

| Type | Example Title | Verdict |
|------|--------------|---------|
| Tutorial | "Get started with EDA (Ansible Rulebook)" | Not a solution guide -- teaches a tool |
| Solution | "Responding to Infrastructure Alerts with Event-Driven Ansible" | Solves a real operational problem |

**Litmus test:** Would a VP of IT understand the value from the title alone, without knowing Ansible?

---

## 2. Overview

The Overview is the first thing a reader sees. It must frame the guide strategically so it is readable by a decision maker, not just a practitioner. This is where you hook the reader.

### 2.1 Problem Statement

Define the operational pain in 2-4 sentences max. Quantify if possible (time, cost, risk, compliance). This goes directly after the hero image.

**Example format:**

> **Example problem statement:**
>
> Organizations spend X hours manually performing Y, leading to Z risk. This guide demonstrates how to automate this workflow using AAP to reduce effort by X% and improve consistency.

### 2.2 Table of Contents

Include a linked table of contents after the problem statement so readers can jump to any section.

---

## 3. Background

Explain what the topic is and why it matters. This section provides the domain context a reader needs before the solution architecture makes sense.

Not every reader will know what AIOps is, or how ServiceNow ticket enrichment works, or why network backup matters. The Background section answers: **"What problem space are we in, and why should I care?"**

### Guidelines

- Keep it to 1-3 paragraphs -- enough context to orient the reader, not a textbook chapter.
- Link to redhat.com topic pages for deeper reading (e.g., "What is AIOps?", "What is observability?").
- If the topic has well-known subcomponents (e.g., AIOps has Observability, Inference, Automation), define them here.
- Include a diagram if it helps explain the concept visually.

> **Tip:** Background is not the solution.
>
> Keep the Background focused on the problem domain. The specific tools and components that make up *your* solution belong in the next section.

---

## 4. Solution

Describe the specific components that make up the solution and who benefits from it. This is the answer to: **"What are we building, and who is it for?"**

### 4.1 Components

List the tools and technologies used in this solution. Link to product pages.

**Example:**

- **Red Hat AI** for understanding service issues
- **Automation code assistant** to generate remediation playbooks (workshop Run -- not Red Hat Lightspeed curated content)
- **Ansible Automation Platform (AAP)** workflows for orchestration
- **Event-Driven Ansible (EDA)** to listen to real-time service events

### 4.2 Who Benefits

Map the solution to specific personas so each audience sees their value immediately.

| Persona | Challenge | What They Gain |
|---------|-----------|---------------|
| IT Ops Engineer / SRE | [Their specific pain] | [What this guide gives them] |
| Automation Architect | [Their specific pain] | [What this guide gives them] |
| IT Manager / Director | [Their specific pain] | [What this guide gives them] |

> **Tip:** Add a "Challenge" column.
>
> A three-column persona table (Persona, Challenge, What They Gain) is more persuasive than two columns because it anchors the value in a specific pain the reader recognizes.

### 4.3 Demos, Videos, and Labs

Link to YouTube videos, Instruqt labs, and interactive demos here. This gives the reader an immediate way to see the solution in action before reading the full technical walkthrough.

---

## 5. Prerequisites

Set expectations early. This is where many solution guides fail -- the reader needs to know what they are getting into before they start.

### 5.1 Ansible Automation Platform Version

State the minimum AAP version required. If specific features (like EDA Controller) require a particular version, call that out.

### 5.2 Featured Ansible Content Collections

List every collection used in the guide with a direct link to its page on [Automation Hub](https://console.redhat.com/ansible/automation-hub/). This is mandatory.

**Example:**

| Collection | Type | Purpose |
|-----------|------|---------|
| [ansible.eda](https://console.redhat.com/ansible/automation-hub/repo/published/ansible/eda/) | Certified | EDA event sources and filters |
| [redhat.ai](https://console.redhat.com/ansible/automation-hub/repo/published/redhat/ai) | Certified | AI model configuration and serving |
| [infra.ai](https://console.redhat.com/ansible/automation-hub/repo/validated/infra/ai) | Validated | AI infrastructure provisioning |

### 5.3 External Systems

List any external tools, services, or infrastructure the reader needs.

| System | Required | Examples |
|--------|----------|----------|
| Observability tool | Yes | Filebeat, IBM Instana, Splunk |
| Message queue | Optional | Apache Kafka, AWS SQS |
| AI inference endpoint | Yes | Red Hat AI or any OpenAI-compatible API |

### 5.4 Cost and Resource Notes

If applicable, note:

- GPU requirements
- Cloud instance sizing
- API rate limits
- Licensing assumptions

### 5.5 Operational Impact

State the impact level. If it varies per step, note it per step rather than per guide.

| Impact | Meaning |
|--------|---------|
| **None** | Read-only, no changes to systems |
| **Low** | Safe, reversible changes |
| **Medium** | Configuration changes, test first |
| **High** | Production mutation, requires change advisory board (CAB) |

### 5.6 Guide Metadata

Include these fields near the top of each guide, directly after the overview:

- **Operational Impact** -- State the impact level per step if it varies, not just per guide (None / Low / Medium / High).
- **Business Value Drivers** -- 2-3 bullet points framing the business outcome (e.g., reduced downtime, improved compliance posture).
- **Technical Value Drivers** -- 2-3 bullet points framing the technical outcome (e.g., simplified compliance reporting, enforced configuration policies).
- **Recommended Demos and Self-Paced Labs** -- Link to interactive demos, YouTube videos, and Instruqt labs where available.
- **Featured Ansible Content Collections** -- List every collection used with a direct link to its [Automation Hub](https://console.redhat.com/ansible/automation-hub/) page.

---

## 6. Workflow and Architecture

This is the "aha" layer -- it must show causality so the reader understands the end-to-end flow before diving into code.

### 6.1 Workflow Diagram

Simple. Clean. 3-6 blocks max. Every guide must have at least one diagram. Choose the pattern that matches your guide type:

**Event-driven (EDA) pattern:**

```
Alert → EDA Rulebook → Job Template → API Call → Resolution
```

**Provisioning / Day 1 pattern:**

```
Request → Survey/Vars → Workflow Template → Provision → Validate → Notify
```

**Day 2 operations pattern:**

```
Schedule/Trigger → Fact Gather → Analyze/Compare → Remediate → Report
```

**Integration pattern:**

```
External Event (ITSM/Webhook) → Controller API → Playbook → Update Source System
```

> **Tip:** Draw your own if needed.
>
> If your guide doesn't fit any of these patterns, draw your own -- but if you can't draw it in 3-6 blocks, the workflow may be too complex for a single guide. Consider splitting.

### 6.2 Narrative Walkthrough

Explain the logic in 5-8 sentences:

- What triggers it
- What decision logic runs
- What automation executes
- What outcome is produced

**Litmus test:** Could someone redraw the workflow after reading your narrative alone?

### 6.3 Visual Design Patterns

Use the right visual format for the right purpose:

| Format | When to Use | Example |
|--------|-------------|---------|
| **Workflow diagram** | Show end-to-end causality (3-6 blocks) | Event -> EDA -> Playbook -> Result |
| **Architecture diagram** | Show system components and connections | AAP <-> Kafka <-> Observability tool |
| **Tables** | Compare options, map events to responses | Event / Source / Response tables |
| **Code blocks (YAML)** | Show the actual automation logic | Featured tasks, rulebooks, API calls |
| **Screenshots** | Show AAP UI configuration (Job Templates, Workflows) | Workflow Visualizer, Survey setup |
| **Callout boxes** | Highlight tips, warnings, and context | Blockquotes with tip/warning prefix |

**Callout conventions:** Use blockquotes for tips, warnings, and contextual notes. Keep a consistent style across all guides:

- **Tip:** -- Helpful context, shortcuts, or "did you know" information.
- **Why [tool]?** -- Explaining tool choices and alternatives.
- **Warning:** -- Production-impact notes or common mistakes.

When referencing third-party tools (Kafka, Splunk, ServiceNow, etc.), include their logo image inline where it aids scannability. Keep logos to a consistent width (e.g., 200px) and link to the relevant Automation Hub page.

---

## 7. Solution Walkthrough

This is where credibility is built -- the executable proof that the automation works. This is the largest section of the guide and contains the step-by-step technical depth.

### 7.1 Structure

Break the walkthrough into numbered steps or workflow stages. Each step should have:

- A clear heading describing what happens at this stage
- Explanation of the purpose
- Featured code (the key task, not the full playbook)
- Screenshots of AAP UI where relevant (Workflow Visualizer, Job Output, Surveys)

### 7.2 Featured Code

Do **NOT** dump the full repo. Show the critical pieces:

- The key task
- The logic block
- The rulebook trigger
- The API call

**Example:**

```yaml
- name: Update ServiceNow ticket with enriched data
  servicenow.itsm.incident:
    number: "{{ incident_number }}"
    state: "In Progress"
    work_notes: "{{ ai_summary }}"
```

Then link to the full source: `github.com/your-org/solution-guide-x`

### 7.3 AAP Integration

Show:

- Job Template setup
- Rulebook activation
- Credentials mapping
- RBAC notes

No vague instructions like "Create a job template." Be explicit. Here is the minimum level of detail expected:

**Example -- Job Template configuration:**

| Field | Value |
|-------|-------|
| **Name** | `ServiceNow Ticket Enrichment` |
| **Inventory** | `ServiceNow Hosts` |
| **Project** | `ITSM Automation` |
| **Playbook** | `enrich_ticket.yml` |
| **Credentials** | `ServiceNow API Token`, `Machine Credential` |
| **Extra Variables** | `incident_number` (prompt on launch) |
| **Verbosity** | 1 (Verbose) |

**Example -- Credential mapping:**

> **Custom Credential Types** for API tokens.
>
> Inject tokens as extra variables or environment variables -- never hardcode secrets in playbooks. See [Creating Custom Credential Types](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/) in the AAP documentation.

**Example -- RBAC note:**

> **RBAC:** Scope roles tightly per team.
>
> Assign the `Execute` role on this Job Template to the `ops-tier1` team. The `Admin` role should be limited to the automation architect team to prevent accidental template modification.

---

## 8. Validation

This is mandatory -- a guide without a validation step is a guide that cannot be trusted. Validation was the most inconsistent section across existing guides, and many omit it entirely.

For reference architecture guides that cover multiple tools or patterns, validation can be done per workflow stage (checklist approach) rather than with a single test command. For implementation guides that target a specific tool, provide a concrete executable test.

### 8.1 The Test

Define a concrete, repeatable test. Not a vague suggestion -- an actual command or action the reader can execute.

**Good example (API test):**

```bash
curl -sk https://controller.example.com/api/v2/job_templates/42/launch/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"extra_vars": {"incident_number": "INC0012345"}}' | jq .status
```

**Good example (EDA test):**

> Send a test event to the webhook endpoint:
>
> ```bash
> curl -H "Content-Type: application/json" \
>   -d '{"alert": "high_cpu", "host": "web01.example.com"}' \
>   http://eda.example.com:5000/endpoint
> ```

**Good example (manual trigger):**

> **Manual trigger** via the AAP UI.
>
> Navigate to **Resources → Templates → [Template Name]** in the AAP Controller UI. Click **Launch** and provide the survey values when prompted.

**Good example (per-stage checklist for reference architectures):**

| Stage | What to Verify | Success Indicator |
|-------|---------------|-------------------|
| **1. Event Detection** | Rulebook activation is running | EDA Controller shows activation as **Running** |
| **2. Enrichment** | AI analyzed the incident | Workflow Visualizer shows all nodes green |
| **3. Remediation** | Playbook was generated and committed | New file exists in Git repo |
| **4. Execute** | Fix was applied | Service returns to steady state |

### 8.2 Expected Result

Show the actual output the reader should expect. Do not describe it in prose -- show it.

**Good example (console output):**

```
PLAY RECAP *********************************************************************
servicenow_host : ok=4    changed=2    unreachable=0    failed=0    skipped=0
```

**Good example (state change):**

> After the playbook completes, the ServiceNow incident should show:
> - **State:** In Progress
> - **Work Notes:** Contains the AI-generated summary
> - **Assignment Group:** Updated to the correct tier

### 8.3 Troubleshooting Common Failures

Include at least 2-3 common failure scenarios and how to diagnose them:

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| `401 Unauthorized` | Expired or invalid API token | Regenerate the token and update the credential in AAP |
| Playbook hangs at "Gathering Facts" | Target host unreachable | Verify network connectivity and SSH/WinRM access |
| EDA rulebook doesn't fire | Event payload doesn't match condition | Check rulebook condition syntax against the actual event JSON |

---

## 9. Maturity Path, Summary, and Related Guides

Close the loop so the guide is more than just a lab exercise. The closing sections follow a deliberate order: **Maturity Path** (where am I on the journey?) → **Summary** (what did I just read?) → **Related Guides** (where do I go next?).

### 9.1 Crawl, Walk, Run

Every guide should map to a maturity progression. This helps organizations adopt incrementally rather than requiring a big-bang implementation.

| Maturity | Description |
|----------|-------------|
| **Crawl** | Read-only enrichment |
| **Walk** | Automated ticket updates |
| **Run** | Fully automated remediation |

The progression should be specific to the guide's use case. The key question at each stage is: **how much autonomy does automation have?**

### 9.2 Summary

Wrap up what the reader just learned. Summarize the key outcomes and the measurable value the guide delivers. This comes **before** Related Guides because it closes the current guide's narrative -- Related Guides is the call to action for what to read next.

### 9.3 Related Guides

Every guide exists within a broader ecosystem. Authors must identify and link to related guides so readers understand the full journey. This is the last content section before the closing logo -- it serves as the call to action.

- Link to the **next logical guide** (e.g., Network Fact Gathering links to Network Backup and Configuration)
- Link to **prerequisite guides** (e.g., AIOps guide references the AI Infrastructure guide for deploying the AI backend)
- Link to **ISV or partner integrations** where applicable
- Link to **advanced architecture expansions** for readers ready to go deeper

**Example cross-links:**

> **Related guides:**
> - Need to deploy the AI infrastructure first? See [AI Infrastructure automation with Ansible](README-IA.md)
> - Ready to add event-driven triggers? See [Get started with EDA](https://access.redhat.com/articles/7136720)

---

## Reference

<details markdown="1">
<summary>Quality Scoring Rubric</summary>

Grade guides against this rubric before publishing:

| Category | Weight |
|----------|--------|
| Outcome Clarity | 20% |
| Architecture Clarity | 20% |
| Technical Executability | 25% |
| Validation/Testability | 15% |
| Production Readiness Info | 10% |
| Business Framing | 10% |

Score each 1-5. Anything below 3 in any category -- revise before publish.

### Scoring by Solution Category

Apply the base rubric above, then adjust expectations by category. Do not penalize a guide for capabilities outside its category.

| Category | Rubric adjustments |
|----------|-------------------|
| **AIOps** | Full rubric. Technical Executability should include AI enrichment, inference endpoints, MCP/Lightspeed integration, or governed playbook selection where the guide claims an AI outcome. |
| **Network automation** | Do not penalize absence of AI. Weight inventory/source-of-truth integration (for example NetBox), device configuration or failover workflows, and closed-loop automation where EDA is used. Business Framing should cite change velocity, outage reduction, or config consistency. |
| **AIOps Use Case** | Lighter on YAML depth and single-partner executability. Weight decision paths, adoption narrative, explicit signals for when to add the next capability, and cross-links to reference architectures. Validation may be scenario-based rather than a single runnable pipeline. Six patterns live in [README-AIOps.md](README-AIOps.md#common-aiops-use-cases); the ticket enrichment appendix is the primary extended adoption page. |

**N/A rules:**
- Network automation guides: skip AI-specific executability checks unless the guide adds an optional AI enrichment section.
- AIOps Use Case pages: Architecture Clarity may emphasize decision flow over deployment topology; Production Readiness Info may be advisory rather than a full runbook.

</details>

<details markdown="1">
<summary>Common Failure Modes</summary>

Reject guides that exhibit any of these patterns:

- "Overview Only" guides with no code
- Screenshot-heavy, YAML-light content
- No validation step
- No versioning
- No production impact warning
- No persona/value framing
- No GitHub repo

</details>

<details markdown="1">
<summary>What Makes a Guide "Elite"</summary>

A truly excellent solution guide:

- Has a deterministic workflow
- Shows real automation logic
- Can be executed in < 60 minutes
- Has clear operational outcome
- Maps to maturity progression
- Could be used by a field seller as enablement

**Minimum Depth Standard:** A guide that covers every section can still fail in practice if it lacks depth.

| Indicator | Minimum | Ideal |
|-----------|---------|-------|
| Solution walkthrough steps | 3 | 5-8 |
| YAML code blocks | 2 | 4-6 |
| Total guide length | ~800 words | 1500-2500 words |
| Diagrams | 1 | 2-3 |
| Validation scenarios | 1 | 2-3 (including failure cases) |

> **Warning:** Your guide may be too thin.
>
> If it has fewer than 3 walkthrough steps or fewer than 2 code blocks, either expand the scope or merge it with a related guide.

</details>

---

## Appendix: Starter Template

Copy this skeleton when creating a new solution guide. Replace all placeholder text.

````markdown
<div class="guide-header">

<h1>[Topic]</h1>

<span class="guide-type-badge guide-type-badge--solution"><i class="fas fa-check-circle" aria-hidden="true"></i> Solution Guide</span>

</div>

## Overview

<!-- 2-4 sentence problem statement. Define the operational pain and quantify if possible. -->

Organizations spend X hours manually performing Y, leading to Z risk. This guide demonstrates how to automate this workflow using Ansible Automation Platform.

## Background

<!-- 1-3 paragraphs explaining what the topic is and why it matters. Link to redhat.com topic pages for deeper reading. -->

## Solution

<!-- List the components that make up this solution. Link to product pages. -->

- **[Tool 1]** for [purpose]
- **[Tool 2]** for [purpose]
- **Ansible Automation Platform** for orchestration

### Who Benefits

| Persona | Challenge | What They Gain |
|---------|-----------|---------------|
| IT Ops Engineer | [Their pain] | [What they get] |
| Automation Architect | [Their pain] | [What they get] |
| IT Manager | [Their pain] | [What they get] |

**Recommended Demos and Self-Paced Labs:**
- [Demo or lab name](https://link)

## Prerequisites

### Ansible Automation Platform

- **Ansible Automation Platform X.X+** -- [reason for version requirement]

### Featured Ansible Content Collections

| Collection | Type | Purpose |
|-----------|------|---------|
| [collection.name](https://console.redhat.com/ansible/automation-hub/repo/published/namespace/name/) | Certified | [Purpose] |

### External Systems

| System | Required | Examples |
|--------|----------|----------|
| [System type] | Yes / Optional | [Specific tools] |

**Operational Impact:** None | Low | Medium | High

## [Topic] Workflow

<!-- Include a workflow diagram: 3-6 blocks showing the end-to-end flow. -->

```
[Trigger] → [Step 1] → [Step 2] → [Result]
```

<!-- 5-8 sentence narrative explaining what triggers the workflow, what logic runs, and what outcome is produced. -->

## Solution Walkthrough

### Step 1: [Name]

**Operational Impact:** Low

<!-- Explanation of what this step does. -->

```yaml
- name: Example task
  namespace.collection.module:
    parameter: "{{ variable }}"
```

### Step 2: [Name]

**Operational Impact:** Medium

<!-- Continue with additional steps. -->

## Validation

### Test

<!-- Provide a concrete, executable test -- an actual command or UI action, not just "run the playbook." -->

```bash
# Example: curl, ansible-playbook CLI, or AAP API call
```

### Expected Result

<!-- Show the actual expected output verbatim. -->

```
PLAY RECAP *********************************************************************
target_host : ok=X    changed=X    unreachable=0    failed=0    skipped=0
```

### Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| [Error message or behavior] | [Root cause] | [Resolution steps] |
| [Error message or behavior] | [Root cause] | [Resolution steps] |

## Maturity Path

| Maturity | Description |
|----------|-------------|
| **Crawl** | [Starting point -- read-only, low risk] |
| **Walk** | [Intermediate -- curated automation, human approval] |
| **Run** | [Fully automated -- AI-driven, policy-governed] |

## Summary

<!-- Wrap up what the reader learned. Summarize key outcomes and measurable value. -->

## Related Guides

<!-- Call to action -- where to go next. Last content section before the closing logo. -->

- [Related guide 1](link)
- [Related guide 2](link)
````
