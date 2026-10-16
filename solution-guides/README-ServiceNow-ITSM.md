<div class="guide-header">

<h1>ServiceNow ITSM Ticket Enrichment Automation</h1>

<span class="guide-type-badge guide-type-badge--solution"><i class="fas fa-check-circle" aria-hidden="true"></i> Solution Guide</span>

</div>

<div class="guide-hero-callout guide-hero-partner guide-hero-partner--servicenow" role="img" aria-label="Ansible Automation Platform and ServiceNow">
  <img src="assets/images/logos/aap-ansible-icon.png" alt="" class="guide-hero-callout__icon" width="36" height="36">
  <span class="guide-hero-partner__plus" aria-hidden="true">+</span>
  <span class="guide-hero-partner__partner card-partner-logo-set">
    <img src="assets/images/logos/servicenow-logo.png" alt="ServiceNow" class="card-partner-logo card-partner-logo--light" width="132" height="32">
    <img src="assets/images/logos/servicenow-logo-dark.png" alt="" class="card-partner-logo card-partner-logo--dark" aria-hidden="true" width="132" height="32">
  </span>
</div>

## Overview

ServiceNow is one of the most common ITSM solutions in the market. Organizations spend significant time manually creating, triaging, and enriching service tickets -- context that already exists in systems like Red Hat Insights but requires manual lookup and copy-paste into ITSM fields. This guide walks through a practical automation use case: creating a ServiceNow incident and enriching it with CVE advisory data from Red Hat Insights, all driven by Ansible Automation Platform.

**Operational impact:** None (read-only enrichment; no infrastructure changes)

## Background

Modern information technology impacts every part of an organization, managing countless tasks and processes. Businesses rely on ServiceNow IT Service Management (ITSM) to coordinate these efforts and deliver customer value.

The Ansible Automation Platform for ServiceNow solution creates "closed-loop" automation between ServiceNow ITSM and Ansible Automation Platform workflows, eliminating the need for manual intervention. The Red Hat Ansible Certified Content Collection for ServiceNow enables Ansible automation workflows to open, close, and update service requests, incidents, problems, and change requests directly within ServiceNow.

With Ansible Automation Platform, you can collect information from existing service tickets, open and close service tickets, and enrich those tickets with data collected across your IT infrastructure. In this guide, we use a CVE example targeting Linux infrastructure.

<img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f4d6.png" width="20" style="vertical-align:text-bottom;"> <a target="_blank" href="https://www.redhat.com/en/technologies/management/ansible">Ansible Automation Platform -- redhat.com</a>

<img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f4d6.png" width="20" style="vertical-align:text-bottom;"> <a target="_blank" href="https://www.servicenow.com/products/itsm.html">ServiceNow IT Service Management</a>

## Solution

What makes up the solution?

- <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f4cb.png" width="20" style="vertical-align:text-bottom;"> **ServiceNow ITSM** for incident management and service ticket tracking
- <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f50d.png" width="20" style="vertical-align:text-bottom;"> **Red Hat Insights / Red Hat Lightspeed** for CVE advisory data and system vulnerability information
- <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f501.png" width="20" style="vertical-align:text-bottom;"> **Ansible Automation Platform** for orchestrating ticket creation, data gathering, and enrichment

### Who Benefits

| Persona | Challenge | What They Gain |
|---------|-----------|---------------|
| <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f6e0.png" width="20" style="vertical-align:text-bottom;"> **IT Ops / Service Desk** | Manually copying CVE details into tickets; slow triage | Automated ticket creation with CVE context already populated |
| <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f5fa.png" width="20" style="vertical-align:text-bottom;"> **Security / Compliance** | Inconsistent CVE documentation across incidents | Standardized enrichment from authoritative Red Hat advisory data |
| <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f4ca.png" width="20" style="vertical-align:text-bottom;"> **IT Manager** | Slow incident response; lack of visibility into vulnerability exposure | Reduced MTTR, consistent ticket quality, and measurable enrichment coverage |

**Recommended demos and self-paced labs:**

- <a target="_blank" href="https://www.redhat.com/en/interactive-labs/ansible#getting-started">Interactive lab: Get started with ServiceNow automation</a>
- <a target="_blank" href="https://play.instruqt.com/redhat/invite/zjj1kyez8nwg">Self-paced lab: Getting started with ServiceNow ITSM automation</a>
- <a target="_blank" href="https://youtu.be/Wg4wnREKkkE?si=Qz6GKdNV6X1xBIYh">Video: Hands-on with servicenow.itsm collection for Ansible Automation Platform</a>

## Prerequisites

### Ansible Automation Platform

- **Ansible Automation Platform 2.4+** with job templates and workflow capabilities
- Familiarity with Ansible Playbooks, execution environments, Ansible navigator, and Git

> **Tip:** New to Ansible?
>
> These learning paths cover the fundamentals: <a target="_blank" href="https://developers.redhat.com/learn/ansible/foundations-ansible">Foundations of Ansible</a>, <a target="_blank" href="https://developers.redhat.com/learn/ansible/get-started-ansible-playbooks">Get started with Ansible Playbooks</a>, <a target="_blank" href="https://developers.redhat.com/learn/ansible/get-started-ansible-visual-studio-code-extension">Get started with the Ansible VS Code extension</a>, and the <a target="_blank" href="https://docs.ansible.com/ansible/latest/getting_started_ee/build_execution_environment.html">execution environment build guide</a>.

### ServiceNow

- ServiceNow instance with ITSM module active
- The <a target="_blank" href="https://store.servicenow.com/store/app/6b1ca36e1b246a50a85b16db234bcb0d">API for Red Hat Ansible Automation Platform Certified Content Collection</a> installed from the ServiceNow Store (refer to the Installation Guide from the store listing)

### Featured Ansible Content Collections

| Collection | Type | Purpose |
|-----------|------|---------|
| <a target="_blank" href="https://console.redhat.com/ansible/automation-hub/repo/published/servicenow/itsm/">servicenow.itsm</a> | Certified | Create, update, and query ServiceNow incidents, problems, and change requests |

> **Tip:** Not yet an AAP customer?
>
> The collections referenced in this guide are available via <a target="_blank" href="https://console.redhat.com/">Red Hat Hybrid Cloud Console</a>. You can also <a target="_blank" href="https://www.redhat.com/en/technologies/management/ansible/trial">sign up for a free 60-day trial</a>.

## ServiceNow ITSM Workflow

```
Ansible Playbook
  → Query ServiceNow for existing ticket data
    → Create a new ServiceNow incident
      → Query Red Hat Insights API for CVE advisory details
        → Enrich the ServiceNow ticket with CVE type, description, affected systems, and solution
```

This workflow starts with basic ITSM operations (reading and creating tickets), then layers in external intelligence from Red Hat Insights to populate tickets with actionable CVE context. Each step is a standalone playbook that can also be chained into an AAP workflow template for end-to-end automation.

## Solution Walkthrough

### Step 1: Gather data from your ITSM

**Operational impact:** None (read-only)

Use the `servicenow.itsm.incident_info` module to retrieve details from an existing ServiceNow ticket. This is the foundation for any enrichment or follow-up automation.

```yaml
---
- name: Retrieve ServiceNow ticket details
  hosts: localhost
  gather_facts: false

  vars:
    ticket_number: "{{ ticket }}"

  tasks:
    - name: Retrieve incidents by number
      servicenow.itsm.incident_info:
        instance:
          host: "{{ servicenow_instance }}"
          username: "{{ servicenow_username }}"
          password: "{{ servicenow_password }}"
        number: "{{ ticket_number }}"
      register: result
      delegate_to: localhost

    - name: Print ticket details
      ansible.builtin.debug:
        msg: "{{ result }}"
```

<a target="_blank" href="https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.4/html/automation_controller_user_guide/controller-job-templates#controller-create-job-template">Create a job template</a> using this playbook. Save it as "Collect ticket information" and launch it.

> **Tip:** Extend with set_fact or set_stats.
>
> Use `ansible.builtin.set_fact` to allocate relevant data into Ansible variables, or `ansible.builtin.set_stats` to persist data between templates in an automation workflow.

### Step 2: Create a service ticket

**Operational impact:** Low (creates a new incident in ServiceNow)

Use the `servicenow.itsm.incident` module to create a new service ticket.

```yaml
---
- name: Create Service Ticket
  hosts: localhost
  gather_facts: false

  vars:
    SN_HOST: "{{ lookup('env', 'SN_HOST') }}"
    SN_USERNAME: "{{ lookup('env', 'SN_USERNAME') }}"
    SN_PASSWORD: "{{ lookup('env', 'SN_PASSWORD') }}"

  tasks:
    - name: Create ticket
      servicenow.itsm.incident:
        instance:
          host: "{{ SN_HOST }}"
          username: "{{ SN_USERNAME }}"
          password: "{{ SN_PASSWORD }}"
        state: new
        caller: Admin
        impact: low
        urgency: low
      register: ticket_details
      delegate_to: localhost

    - name: Print ticket details
      ansible.builtin.debug:
        msg: "{{ ticket_details }}"
```

<a target="_blank" href="https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.4/html/automation_controller_user_guide/controller-job-templates#controller-create-job-template">Create a job template</a> using this playbook. Save it as "Create ServiceNow Ticket" and launch it.

> **Tip:** Combine into a workflow.
>
> You can chain Steps 1 and 2 into an AAP workflow template to both create a ticket and gather information in a single automated run.

### Step 3: Enrich a ServiceNow ticket with CVE data

**Operational impact:** Low (creates an enriched incident with CVE details)

This is where the real value emerges. Using `ansible.builtin.uri` to query the Red Hat Insights API for CVE advisory details, then `servicenow.itsm.incident` to create an enriched ticket with the advisory type, description, affected CVEs, and recommended solution.

```yaml
---
- name: Gather CVE Details
  hosts: localhost
  gather_facts: false

  vars:
    advisory_id:
    rhsm_username:
    rhsm_password:
    SN_HOST: "{{ lookup('env', 'SN_HOST') }}"
    SN_USERNAME: "{{ lookup('env', 'SN_USERNAME') }}"
    SN_PASSWORD: "{{ lookup('env', 'SN_PASSWORD') }}"

  tasks:
    - name: Retrieve related CVEs from advisory
      ansible.builtin.uri:
        url: "https://console.redhat.com/api/patch/v3/advisories/{{ advisory_id }}/systems?page=1&perPage=20&sort=-last_upload&offset=0&limit=20"
        method: GET
        url_username: "{{ rhsm_username }}"
        url_password: "{{ rhsm_password }}"
        force_basic_auth: true
        status_code: 200
      register: cves_list

    - name: Gather CVE details
      ansible.builtin.uri:
        url: "https://console.redhat.com/api/patch/v3/advisories/{{ advisory_id }}"
        method: GET
        url_username: "{{ rhsm_username }}"
        url_password: "{{ rhsm_password }}"
        force_basic_auth: true
        status_code: 200
      register: cve_details

    - name: Extract advisory fields
      ansible.builtin.set_fact:
        cve_type: "{{ cve_details.json.data.attributes.advisory_type_name }}"
        cves_description: "{{ cve_details.json.data.attributes.description }}"
        solution: "{{ cve_details.json.data.attributes.solution }}"
        cves: "{{ cve_details.json.data.attributes.cves }}"

    - name: Create enriched incident
      servicenow.itsm.incident:
        instance:
          host: "{{ SN_HOST }}"
          username: "{{ SN_USERNAME }}"
          password: "{{ SN_PASSWORD }}"
        state: new
        caller: "{{ SN_USERNAME }}"
        short_description: "New Advisory CVE Type - {{ cve_type }}"
        description: |
          Alert Type: {{ cve_type }}
          CVE: {{ cves }}

          CVE Description: {{ cves_description }}

          Possible Solution: {{ solution }}
        urgency: high
      register: new_incident
```

Create a job template using this playbook. Save it as "Enrich CVE ticket." Add a <a target="_blank" href="https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.4/html/automation_controller_user_guide/controller-job-templates#controller-surveys-in-job-templates">survey</a> to capture the CVE advisory number as user input, then launch and provide the advisory ID from Red Hat Insights.

## Validation

| Checkpoint | What to verify | Success indicator |
|-----------|----------------|-------------------|
| **Step 1 output** | Ticket data returned | `result` contains incident fields (number, state, description) |
| **Step 2 output** | Ticket created | New incident number appears in `ticket_details`; visible in ServiceNow |
| **Step 3 output** | Enriched ticket | Incident description contains CVE type, description, affected CVEs, and solution text from Red Hat Insights |

### Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| `401 Unauthorized` from ServiceNow | Wrong credentials or locked account | Verify `SN_HOST`, `SN_USERNAME`, `SN_PASSWORD`; confirm user has ITSM roles |
| `servicenow.itsm` module not found | Collection not installed in execution environment | Add `servicenow.itsm` to your EE requirements; rebuild with `ansible-builder` |
| Red Hat Insights API returns `403` | Invalid RHSM credentials or missing entitlements | Confirm `rhsm_username` / `rhsm_password`; verify Insights subscription |
| Ticket created but description is empty | Variables not passed between tasks | Check `set_fact` task; ensure `register` names match downstream references |
| ServiceNow API app not installed | Missing the Red Hat AAP Certified Content Collection API app | Install from the <a target="_blank" href="https://store.servicenow.com/store/app/6b1ca36e1b246a50a85b16db234bcb0d">ServiceNow Store</a> |

## Maturity Path

| Maturity | Description |
|----------|-------------|
| <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f6b6.png" width="20" style="vertical-align:text-bottom;"> **Crawl** | Gather ticket data and create incidents manually via job templates |
| <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f3c3.png" width="20" style="vertical-align:text-bottom;"> **Walk** | Chain steps into AAP workflow templates; enrich tickets with CVE data from Red Hat Insights; add surveys for user input |
| <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f680.png" width="20" style="vertical-align:text-bottom;"> **Run** | Integrate Event-Driven Ansible for automatic ticket creation on alerts; update CMDB; attach reports; connect monitoring/observability tools for closed-loop remediation |

## Summary

This guide demonstrates the lowest-risk entry point for ServiceNow + Ansible automation: reading ticket data, creating incidents, and enriching them with CVE advisory context from Red Hat Insights. Each step builds on the last, from simple data gathering to automated enrichment that reduces manual triage and improves ticket quality. Once comfortable with these patterns, teams can extend to CMDB updates, file attachments, Event-Driven Ansible integrations, and the governed LEAP + MCP execution pattern described in the companion guide.

---

## Related Guides

- <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f517.png" width="20" style="vertical-align:text-bottom;"> **LEAP + MCP integration:** [Unlock AIOps with ServiceNow LEAP and Ansible MCP server](README-AIOps-ServiceNow.md)
- <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f4cb.png" width="20" style="vertical-align:text-bottom;"> **AIOps reference architecture:** [AIOps automation with Ansible](README-AIOps.md)
- <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f4e1.png" width="20" style="vertical-align:text-bottom;"> **Event-Driven Ansible:** <a target="_blank" href="https://www.redhat.com/en/interactive-labs/ansible#event-driven-ansible">Self-paced labs: Getting started with Event-Driven Ansible</a>

---

## Next Steps

| | |
|---|---|
| <a target="_blank" href="https://www.redhat.com/en/technologies/management/ansible/trial"><strong>Try Ansible Automation Platform</strong></a> | Start a free 60-day trial and build your first automation workflows |
| <a target="_blank" href="https://www.redhat.com/en/services/consulting"><strong>Red Hat Consulting</strong></a> | Work with Red Hat experts to design, implement, and scale AIOps automation tailored to your environment |
| <a target="_blank" href="https://www.redhat.com/en/services/training-and-certification"><strong>Training and Certification</strong></a> | Build team skills with hands-on courses and industry-recognized certifications |

---

<span class="guide-closing-logo-set">
<img class="guide-closing-logo guide-closing-logo--light" src="assets/images/logos/aap_logo.png" alt="Red Hat Ansible Automation Platform">
<img class="guide-closing-logo guide-closing-logo--dark" src="assets/images/logos/redhat-ansible-logo.svg" alt="" aria-hidden="true">
</span>
