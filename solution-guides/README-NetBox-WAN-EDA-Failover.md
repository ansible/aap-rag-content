{% raw %}
<div class="guide-header">

<h1>Event-Driven WAN Circuit Failover with NetBox and Ansible Automation Platform</h1>

<span class="guide-type-badge guide-type-badge--solution"><i class="fas fa-check-circle" aria-hidden="true"></i> Solution Guide</span>

</div>

<div class="guide-hero-callout guide-hero-partner guide-hero-partner--netbox" role="img" aria-label="Ansible Automation Platform and NetBox">
  <img src="assets/images/logos/aap-ansible-icon.png" alt="" class="guide-hero-callout__icon" width="36" height="36">
  <span class="guide-hero-partner__plus" aria-hidden="true">+</span>
  <span class="guide-hero-partner__partner card-partner-logo-set card-partner-logo-set--netbox">
    <img src="assets/images/logos/logo_netboxlabs_dark_teal-scaled.png" alt="NetBox Labs" class="card-partner-logo card-partner-logo--light" width="128" height="21">
    <img src="assets/images/logos/logo_netboxlabs_dark_teal-scaled-darkmode.png" alt="" class="card-partner-logo card-partner-logo--dark" aria-hidden="true" width="128" height="21">
  </span>
</div>

## Overview

### Problem Statement

Enterprise WAN circuit failures trigger a cascade of manual steps: an engineer must detect the outage, identify a backup path, reconfigure routers, update the CMDB, and produce an incident report. This process typically takes 30-60 minutes per incident, during which business-critical traffic is down. For organizations with dozens of circuits across multiple geographies, even a single missed step (an outdated CMDB entry, a forgotten router) can compound into extended outages and compliance gaps.

This guide demonstrates how to **eliminate manual intervention in WAN circuit failover** by combining **NetBox** as the network source of truth with **Ansible Automation Platform (AAP) 2.6** and **Event-Driven Ansible (EDA)**. When a circuit status changes in NetBox, automation discovers the best backup, reconfigures routers, updates the CMDB, and publishes an incident report, all within 30 seconds.

> **This guide covers two use cases:**
>
> - **Use Case A: Event-driven circuit failover.** A NetBox status change triggers automatic backup discovery, router reconfiguration, CMDB update, and bidirectional failback.
> - **Use Case B: Automated incident reporting.** Failover events generate and publish timestamped HTML reports with topology diagrams and audit trails.

---

## Background

Modern enterprise WANs rely on redundant circuits between sites to maintain availability. When a primary circuit fails, traffic must be rerouted to a backup path. The challenge is not the routing change itself but the **coordination across systems**: the network source of truth must reflect the new state, routers must be reconfigured, stakeholders must be notified, and an audit trail must be maintained.

**NetBox** is an open-source network source of truth and CMDB that models circuits, sites, devices, interfaces, and their interconnections. It provides a REST API, webhooks, and event rules that make it an ideal trigger source for network automation.

**Event-Driven Ansible (EDA)** is a component of Ansible Automation Platform that listens for events from external systems (including NetBox webhooks) and evaluates rulebook conditions to decide which automation to trigger. EDA bridges the gap between "something changed" and "do something about it."

**Ansible Automation Platform (AAP) 2.6** provides the workflow engine, credential management, RBAC, and execution environments needed to run production automation at scale. Workflow templates chain multiple job templates into multi-step operations with error handling and conditional logic.

> **Why NetBox as the trigger source?**
>
> Unlike monitoring systems that detect symptoms (link down, packet loss), NetBox captures **intent**: an operator or upstream system declares a circuit offline. This intent-based trigger eliminates false positives from transient network events and ensures automation acts on authoritative state changes.

---

## Solution

### Components

- **[NetBox](https://netboxlabs.com/):** Network source of truth and CMDB. Stores circuits, sites, devices, interfaces, IP addresses, and cables. Fires webhooks on state changes via event rules.

- **[Ansible Automation Platform 2.6](https://www.redhat.com/en/technologies/management/ansible):** Enterprise automation platform providing Automation Controller (workflow engine, RBAC, credentials) and Event-Driven Ansible (event routing, rulebook evaluation).

- **[netbox.netbox Collection](https://console.redhat.com/ansible/automation-hub/repo/published/netbox/netbox/):** Certified Ansible content collection for NetBox API interactions. Provides `nb_lookup` plugin for queries and resource modules (`netbox_circuit`, `netbox_device`, etc.) for state management.

- **[cisco.ios Collection](https://console.redhat.com/ansible/automation-hub/repo/published/cisco/ios/):** Certified collection for Cisco IOS/IOS-XE device management. Provides `ios_config` and `ios_command` modules for router configuration.

- **[ansible.eda Collection](https://console.redhat.com/ansible/automation-hub/repo/published/ansible/eda/):** EDA source and action plugins. Provides `webhook` source for receiving HTTP events and `run_workflow_template` action for triggering AAP workflows.

### Who Benefits

| Persona | Challenge | What They Gain |
|---------|-----------|----------------|
| Network Engineer / SRE | Manually detecting circuit failures, identifying backups, reconfiguring routers, and updating the CMDB under time pressure | Automated failover completes in <30 seconds with full CMDB consistency. Engineers focus on root cause analysis instead of emergency reconfiguration |
| Network Architect | No systematic way to ensure backup selection follows capacity planning rules (highest bandwidth first) across a multi-site topology | Backup discovery is dynamic and policy-driven: automation queries all available circuits at both sites and selects by committed bandwidth. Adding new circuits to NetBox automatically includes them in failover candidates |
| IT Manager / Director | Circuit outage reports are inconsistent, delayed, and lack audit trails. Compliance requires proof of automated response times and decision rationale | Every failover produces a timestamped HTML report with topology diagrams, bandwidth impact analysis, backup selection rationale, and NetBox audit trail links, published automatically to GitHub Pages or an internal report server |

### Demos, Videos, and Labs

- **[Source Code Repository](https://github.com/leogallego/summit-netbox-circuits-demo):** Full source code for all playbooks, rulebooks, templates, and infrastructure-as-code
- **[EDA + NetBox Workshop](https://github.com/rhpds/zt-ans-bu-eda-netbox):** Hands-on interactive workshop with 7 progressive lab modules covering AAP dynamic inventory, EDA rulebooks, and NetBox integration

---

## Prerequisites

### AAP Version

**Ansible Automation Platform 2.6** (minimum). EDA requires the unified platform with Automation Decisions. The default Decision Environment (`registry.redhat.io/ansible-automation-platform-26/de-supported-rhel9:latest`) is sufficient; no custom DE is needed since the rulebook uses only built-in EDA plugins.

The Execution Environment for job templates must include the `netbox.netbox`, `cisco.ios`, and `ansible.utils` collections with `pynetbox` >= 7.6.0 (e.g., `quay.io/acme_corp/netbox-summit-2026-ee:v3.22`).

> **AAP 2.5 is also supported** for basic EDA rulebooks and dynamic inventory. Circuit failover with `run_workflow_template` requires AAP 2.5+ with the EDA controller component.

### Featured Ansible Content Collections

| Collection | Minimum Version | Type | Purpose |
|------------|----------------|------|---------|
| [netbox.netbox](https://console.redhat.com/ansible/automation-hub/repo/published/netbox/netbox/) | 3.19.0 | Certified | NetBox API queries (`nb_lookup`), resource management (`netbox_circuit`, `netbox_device`, `netbox_cable`) |
| [ansible.eda](https://console.redhat.com/ansible/automation-hub/repo/published/ansible/eda/) | 2.11.0 | Certified | EDA webhook source plugin, `run_workflow_template` and `run_job_template` actions |
| [cisco.ios](https://console.redhat.com/ansible/automation-hub/repo/published/cisco/ios/) | 9.0.0 | Certified | Cisco IOS-XE router configuration (`ios_config`, `ios_command`) |
| [ansible.utils](https://console.redhat.com/ansible/automation-hub/repo/published/ansible/utils/) | 5.1.0 | Certified | IP address math (`ipaddr` filter) for gateway derivation from /30 subnets |
| [ansible.netcommon](https://console.redhat.com/ansible/automation-hub/repo/published/ansible/netcommon/) | 7.1.0 | Certified | Network connection plugins and utilities |

> **Note:** The `ansible.controller` collection (4.7.0+) is used by the setup playbook (`aap_setup.yml`) to configure AAP resources idempotently, but is not required at runtime by the failover or report playbooks.

### External Systems

| System | Required / Optional | Details |
|--------|-------------------|---------|
| NetBox | Required | v4.x+ recommended. Hosts circuit, site, device, interface, IP, and cable data. Must have webhook and event rule support enabled. |
| Cisco IOS-XE Router | Optional | For real router configuration. CSR 1000v 16.12+ or Catalyst 8000v. Without a router, failover runs in simulated mode with debug output. |
| GitHub Pages | Optional | Default target for HTML incident reports. Requires a GitHub token with repo write access. Falls back to an SSH-accessible report server. |
| AWS | Optional | For provisioning infrastructure (report server, router instances) via Terraform or Ansible. |

### Guide Metadata

- **Operational Impact:** Medium. Automation modifies circuit status in NetBox and pushes routing configuration to network devices. Test in a non-production NetBox instance first.
- **Business Value Drivers:**
  - Reduce circuit failover time from 30-60 minutes to <30 seconds
  - Eliminate manual CMDB updates that lead to configuration drift
  - Produce audit-ready incident reports automatically for every failover event
- **Technical Value Drivers:**
  - Event-driven architecture eliminates polling and manual triggers
  - Dynamic backup discovery scales with topology changes without hardcoded mappings
  - Per-router gateway derivation from NetBox cable data ensures configuration accuracy

---

## Workflow and Architecture

### Workflow Diagram

**Event-Driven Circuit Failover Pipeline:**

```
NetBox Copilot / UI              NetBox                    Event-Driven Ansible           Automation Controller
─────────────────────     ──────────────────────     ──────────────────────────     ──────────────────────────

 "Set IPLC-GB-AT-PRI       PATCH circuit status         Webhook received               Workflow launched
  to offline"              to 'offline'                 Condition matched:             ┌──────────────────┐
       │                        │                       status in [offline,failed]     │ Step 1: Failover │
       └───────────────────────►│                            │                        │  - Query NetBox   │
                                │   Event rule fires         │                        │  - Find backup    │
                                │   webhook to EDA           │                        │  - Push router    │
                                └───────────────────────────►│                        │    config         │
                                                             │  run_workflow_template  │  - Update NetBox  │
                                                             └───────────────────────►│                  │
                                                                                      ├──────────────────┤
                                                                                      │ Step 2: Report   │
                                                                                      │  - Query state    │
                                                                                      │  - Render HTML    │
                                                                                      │  - Publish to     │
                                                                                      │    GitHub Pages   │
                                                                                      └──────────────────┘
```

### Narrative Walkthrough

An operator (or NetBox Copilot) sets a circuit's status to `offline` in NetBox. NetBox evaluates its event rules and fires a webhook to Event-Driven Ansible, passing the circuit data payload. EDA's rulebook matches the condition (`status.value in ["offline", "failed"]`) and triggers the "Circuit Failover Workflow" on Automation Controller, passing the circuit ID (`cid`) as an extra variable.

The workflow executes two steps. **Step 1** (failover) queries NetBox for the failed circuit's termination sites, discovers all backup circuits between those sites, selects the best candidate by highest committed bandwidth, derives per-router gateway IPs from NetBox cable wiring data, pushes failover routing to Cisco routers (or simulates the push), and updates both circuits' status in NetBox. **Step 2** (report) re-queries NetBox for current state, renders a timestamped HTML incident report with topology diagrams and audit trails, and publishes it to GitHub Pages.

The entire pipeline, from status change to published report, completes in under 30 seconds.

---

## Solution Walkthrough

### Use Case A: Event-Driven Circuit Failover

**The Scenario:** A global enterprise operates WAN circuits between three sites: Bristol (GB), Atlanta (US), and Buenos Aires (AR). The primary 10 Gbps circuit between GB and US fails. Automation must discover the 5 Gbps backup circuit, reconfigure routers at both sites, and update the CMDB without human intervention.

The AAP workflow consists of two job templates, both using the same Execution Environment:

**Workflow: Circuit Failover Workflow**

| Step | Job Template | Playbook | Execution Environment |
|------|-------------|----------|----------------------|
| 1 | Circuit Failover | `circuit_failover.yml` | `quay.io/acme_corp/netbox-summit-2026-ee:v3.22` |
| 2 | Deploy Report | `deploy_report.yml` | `quay.io/acme_corp/netbox-summit-2026-ee:v3.22` |

Both job templates require a **NetBox API credential** (injecting `NETBOX_API` and `NETBOX_TOKEN` as environment variables) and run against a localhost inventory. The report job template additionally requires a **GitHub credential** for publishing reports.

#### A1. Configure the EDA Rulebook

**Operational Impact:** None. Rulebook configuration is read-only until activated.

The EDA rulebook listens for NetBox webhook events and triggers the failover workflow when a circuit goes offline or failed.

**EDA Rulebook (`rulebooks/rulebook.yml`):**

```yaml
---
- name: NetBox Circuit Failover
  hosts: all
  sources:
    - name: netbox_webhook
      ansible.eda.webhook:
        host: 0.0.0.0
        port: 5000
  rules:
    - name: Circuit failure detected - trigger failover workflow
      condition: >-
        event.payload.object_type == "circuits.circuit" and
        event.payload.data.status.value in ["offline", "failed"]
      action:
        run_workflow_template:
          name: "Circuit Failover Workflow"
          organization: "Default"
          job_args:
            extra_vars:
              failed_circuit: "{{ event.payload.data.cid }}"
```

> **Tip:** The rulebook extracts the circuit ID (`cid`) from the NetBox event payload and passes it as `failed_circuit` to the workflow. This single variable drives all downstream logic without hardcoded circuit mappings.

To activate the rulebook in AAP, create a **Rulebook Activation** under Automation Decisions:

| Setting | Value |
|---------|-------|
| Name | `Circuit Failover Rulebook` |
| Project | EDA project syncing the rulebook repository |
| Rulebook | `rulebook.yml` |
| Decision Environment | Default DE (`registry.redhat.io/ansible-automation-platform-26/de-supported-rhel9:latest`) |
| Restart Policy | `Always` |

#### A2. Configure NetBox Webhook and Event Rule

**Operational Impact:** Low. Creates a webhook and event rule in NetBox. Reversible by deleting both objects.

NetBox must be configured to fire a webhook when circuit status changes. The setup playbook (`aap_setup.yml`) handles this idempotently:

**Webhook and Event Rule Configuration:**

```yaml
- name: Create NetBox webhook for EDA
  ansible.builtin.uri:
    url: "{{ netbox_url }}/api/extras/webhooks/"
    method: POST
    headers:
      Authorization: "Token {{ netbox_token }}"
    body_format: json
    body:
      name: "AAP Circuit Failover Workflow"
      payload_url: "https://{{ aap_host }}/api/controller/v2/workflow_job_templates/{{ wfjt_id }}/launch/"
      http_method: POST
      http_content_type: application/json
      additional_headers: "Authorization: Bearer {{ aap_token }}"
      ssl_verification: false

- name: Create NetBox event rule
  ansible.builtin.uri:
    url: "{{ netbox_url }}/api/extras/event-rules/"
    method: POST
    headers:
      Authorization: "Token {{ netbox_token }}"
    body_format: json
    body:
      name: "Circuit Failover on Status Change"
      enabled: true
      object_types: ["circuits.circuit"]
      event_types: ["object_updated"]
      action_type: webhook
      action_object_id: "{{ webhook_id }}"
```

> **Warning:** The webhook above sets `ssl_verification: false` for lab environments. In production, configure proper TLS certificates and set `ssl_verification: true` to prevent man-in-the-middle attacks on the webhook payload.

> **Why use `object_updated` instead of a status-specific trigger?** NetBox event rules fire on object-level events, not field-level changes. The EDA rulebook condition handles the status filtering. This separation keeps NetBox configuration simple and moves decision logic to EDA where it belongs.

#### A3. Dynamic Backup Discovery

**Operational Impact:** None. This step is read-only, querying NetBox for available circuits.

The failover playbook (`circuit_failover.yml`) discovers backup circuits dynamically. It extracts the A-side and Z-side sites from the failed circuit's terminations, then queries all circuits that terminate at both sites. The best backup is selected by highest committed bandwidth.

**Backup Discovery Logic:**

```yaml
- name: Query all available circuits at both sites
  ansible.builtin.set_fact:
    backup_candidates: >-
      {{ all_circuits | selectattr('value.status.value', 'eq', 'active')
         | rejectattr('value.cid', 'eq', failed_circuit)
         | selectattr('value.terminations', 'defined')
         | list }}

- name: Select best backup by highest committed bandwidth
  ansible.builtin.set_fact:
    selected_backup: >-
      {{ backup_candidates
         | sort(attribute='value.commit_rate', reverse=true)
         | first }}
```

> **Why dynamic discovery instead of a backup mapping table?** Hardcoded primary-backup pairs break when circuits are added, removed, or re-provisioned. Dynamic discovery means adding a new circuit to NetBox automatically includes it as a failover candidate. The automation adapts to topology changes without playbook modifications.

#### A4. Router Configuration and CMDB Update

**Operational Impact:** High. Pushes routing configuration to production routers and modifies circuit status in NetBox.

After selecting the backup circuit, the playbook derives per-router gateway IPs from NetBox cable wiring data and pushes failover routing. It then updates both circuits' status in NetBox.

**Per-Router Gateway Derivation:**

```yaml
- name: Derive gateway from NetBox cable wiring
  ansible.builtin.set_fact:
    router_gateways: >-
      {% set gw_map = {} %}
      {% for router in site_routers %}
      {%   set iface_ip = router.interfaces | map(attribute='ip_addresses')
                          | flatten | first %}
      {%   set gateway = iface_ip.address | ansible.utils.ipaddr('network/prefix')
                         | ansible.utils.nthhost(1) %}
      {%   set _ = gw_map.update({router.name: gateway}) %}
      {% endfor %}
      {{ gw_map }}
```

**Router Config Push and NetBox Update:**

```yaml
- name: Push failover routing to router
  cisco.ios.ios_config:
    lines:
      - "ip route 0.0.0.0 0.0.0.0 {{ backup_gateway }}"
      - "no ip route 0.0.0.0 0.0.0.0 {{ failed_gateway }}"

- name: Update circuit status in NetBox
  netbox.netbox.netbox_circuit:
    netbox_url: "{{ netbox_url }}"
    netbox_token: "{{ netbox_token }}"
    data:
      cid: "{{ selected_backup.value.cid }}"
      status: active
    state: present
```

> **Warning:** Router configuration changes take effect immediately. In production, consider adding a maintenance window check or approval gate before the `cisco.ios.ios_config` task. See [Maturity Path](#maturity-path) for the Walk stage with human approval.

#### A5. Closed-Loop Failback and Loop Prevention

**Operational Impact:** Medium. Same as A4, but triggered in the reverse direction.

The same EDA rulebook and failover playbook handle both directions. When the primary circuit is restored and an operator sets the backup circuit back to offline, the rulebook condition matches (`status.value in ["offline", "failed"]`) and triggers the same workflow. The playbook discovers the (now active) primary as the best backup candidate and restores routing.

```
Primary fails    → EDA triggers → Backup activated  → Primary routing removed
Primary restored → Backup set offline → EDA triggers → Primary re-activated → Backup routing removed
```

No separate failback playbook or rulebook rule is needed because the automation is inherently bidirectional.

**Loop prevention:** The failover playbook updates circuit status in NetBox (backup to active), which fires another webhook. This does not create a loop because the rulebook condition only matches `offline` and `failed`. The activated circuit's `active` status does not trigger the workflow.

| Step | Event | Status Value | Matches Condition? | Result |
|------|-------|-------------|-------------------|--------|
| 1 | Operator sets PRI to offline | `offline` | Yes | Workflow launches |
| 2 | Playbook sets SEC to active | `active` | No | No trigger |
| 3 | Playbook confirms PRI as offline | `offline` | Already offline; NetBox does not fire webhook for unchanged status | No trigger |

> **Warning:** If you extend the rulebook to also trigger on `active` status (e.g., for notifications), use EDA's `once_within` or `once_after` time windows to debounce and prevent loops.

---

### Use Case B: Automated Incident Reporting

**The Scenario:** After every circuit failover, stakeholders need a detailed incident report documenting what happened, which backup was selected and why, what router configuration was applied, and the timeline of automated actions. These reports must be immutable, timestamped, and accessible via a web URL.

#### B1. Report Generation from NetBox State

**Operational Impact:** None. Reads current state from NetBox and renders a local HTML file.

Step 2 of the failover workflow re-queries NetBox for current circuit state and renders a Jinja2 HTML template with full incident details.

**Report Data Collection (from `deploy_report.yml`):**

```yaml
- name: Query all circuits for report
  ansible.builtin.set_fact:
    report_circuits: >-
      {{ query('netbox.netbox.nb_lookup', 'circuits',
         api_endpoint=netbox_url,
         token=netbox_token,
         api_filter='tag=dd') }}

- name: Build per-router gateway lookup
  ansible.builtin.set_fact:
    router_gateway_map: "{{ dict(router_gw_pairs) }}"
```

The report template (`failover_report.html.j2`) includes:

- Network topology SVG diagram showing all sites and circuits
- Failed and backup circuit details (CID, provider, bandwidth, port speed)
- Per-router gateway configuration table
- Bandwidth capacity impact analysis
- Backup candidate selection rationale with all candidates ranked
- Failover timeline with per-step timestamps
- Direct link to NetBox circuit history for audit trail

#### B2. Publishing to GitHub Pages

**Operational Impact:** Low. Creates or updates files in the repository's `gh-pages` branch via the GitHub Contents API.

```yaml
- name: Build request body for GitHub Contents API
  ansible.builtin.set_fact:
    github_put_body: >-
      {{ {'message': 'Update failover report',
          'branch': github_pages_branch,
          'content': report_content.content}
         | combine({'sha': github_file_sha}
                   if github_file_sha | length > 0 else {}) }}

- name: Push report to GitHub repository
  ansible.builtin.uri:
    url: "https://api.github.com/repos/{{ github_repo }}/contents/{{ report_filename }}"
    method: PUT
    headers:
      Authorization: "Bearer {{ github_token }}"
    body_format: json
    body: "{{ github_put_body }}"
```

> **Tip:** Each report gets a unique timestamped filename (`failover_report_<CID>_<ISO8601>.html`). An auto-generated index page lists all historical reports with newest first, creating a browsable incident history.

---

## Validation

### Testing the End-to-End Pipeline

**Test method:** Trigger a circuit status change via the NetBox API and verify the complete pipeline executes.

**Step 1: Trigger the failover via curl.**

```bash
curl -s -X PATCH \
  -H "Authorization: Token $NETBOX_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"status": "offline"}' \
  "$NETBOX_URL/api/circuits/circuits/?cid=IPLC-GB-AT-PRI"
```

**Step 2: Verify in AAP UI.**
Navigate to **Automation Execution > Jobs** and confirm the "Circuit Failover Workflow" job launched and completed successfully.

**Step 3: Verify in NetBox.**
Navigate to **Circuits > Circuits** and confirm:
- `IPLC-GB-AT-PRI` status is `offline`
- `IPLC-GB-AT-SEC` status is `active`

**Step 4: Verify the report.**
Open the GitHub Pages URL and confirm a new timestamped report appears in the index.

### Expected Results

| Stage | What to Verify | Success Indicator |
|-------|---------------|-------------------|
| NetBox Event | Webhook fired | Event rule shows recent activity in NetBox admin |
| EDA Rulebook | Condition matched | Rulebook activation fire count increments in AAP > Automation Decisions |
| Failover Job | Backup discovered and selected | Job output shows selected backup circuit with commit_rate |
| Router Config | Routes pushed (or simulated) | Job output shows `ios_config` task or `[SIMULATED]` debug output |
| NetBox Update | Both circuits updated | Primary = offline, Backup = active in NetBox UI |
| Report Published | HTML report accessible | New report visible at GitHub Pages URL with correct timestamp |
| Report Content | All sections populated | Topology diagram, circuit details, gateway table, timeline present |

### Troubleshooting Common Failures

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| EDA rulebook does not fire | NetBox webhook URL incorrect or EDA port blocked | Verify webhook `payload_url` matches EDA endpoint. Check firewall rules for port 5000. Test with `curl -X POST http://<eda-host>:5000/endpoint -d '{}'` |
| Workflow launches but failover job fails with "No backup found" | No other circuits exist between the same sites, or all candidates are already offline | Verify circuits exist in NetBox between the same A-side and Z-side sites. Check that at least one circuit is in `active` status |
| NetBox API returns 403 Forbidden | Token lacks write permissions or token format incompatible | Verify the token has full API permissions. For NetBox 4.5+, ensure pynetbox >= 7.6.0 in the execution environment |
| Router config push times out | SSH connectivity issue or crypto policy mismatch with older IOS-XE | For CSR 1000v 16.12 (SHA-1 only), use a legacy-crypto EE with override policies. For newer platforms, the standard EE works |
| Report not published to GitHub Pages | GitHub token missing `repo` scope or GitHub Pages not enabled | Verify `GITHUB_TOKEN` has `repo` scope. Enable GitHub Pages on the repository from Settings > Pages > Source: `gh-pages` branch, root (`/`) |

---

## Maturity Path

| Maturity | Detection & Trigger | Failover Execution | Reporting & Audit | Example |
|----------|-------------------|-------------------|-------------------|---------|
| **Crawl** | Manual: operator updates NetBox circuit status via UI | Semi-automated: operator launches failover job template manually from AAP with circuit CID as survey input | Manual: operator runs report playbook after failover | Run `circuit_failover.yml` as a standalone job template with `failed_circuit` as a survey variable. No EDA, no webhook. |
| **Walk** | Automated trigger: NetBox webhook fires to EDA on status change | Automated with approval: EDA triggers workflow but first step requires human approval in AAP before proceeding | Automated: report generated and published as workflow step 2 | Add an approval node between Step 1 (failover) and Step 2 (report) in the AAP workflow. EDA triggers automatically, but a human reviews before execution. |
| **Run** | Fully automated: NetBox event → EDA → AAP workflow, zero human touch | Fully automated: failover + failback both execute without intervention, with guard rails against loops | Fully automated: timestamped reports published, index maintained, audit trail linked | Full pipeline as described in this guide. Add monitoring integration (PagerDuty, Slack) for notification after automated failover completes. |

---

## Summary

This guide demonstrated two use cases for automated WAN circuit failover:

- **Use Case A** established the event-driven pipeline: a circuit status change in NetBox triggers EDA, which launches an AAP workflow that dynamically discovers backup circuits, reconfigures routers, updates the CMDB, and supports bidirectional failback with built-in loop prevention, all in under 30 seconds.

- **Use Case B** added automated incident reporting: every failover produces a timestamped HTML report with topology diagrams, bandwidth impact analysis, backup selection rationale, and NetBox audit trail links, published automatically to GitHub Pages.

The unifying pattern across both use cases is **NetBox as the single source of truth driving event-based automation**. By modeling circuits, sites, devices, and their interconnections in NetBox, the automation adapts dynamically to topology changes: no hardcoded mappings, no manual CMDB updates, no missed routers.

---

## Related Guides

- **[Event-Driven Network Source of Truth with NetBox and AAP](README-NetBox-SoT-EDA-Config.md):** Foundational guide covering NetBox dynamic inventory, config contexts, and event-driven NTP/banner/VLAN configuration. Start here if your team is new to NetBox + EDA integration.

- **[EDA + NetBox Workshop](https://github.com/rhpds/zt-ans-bu-eda-netbox):** 7-module hands-on workshop covering AAP dynamic inventory, EDA rulebooks, NetBox webhooks, and workflow automation. Ideal for teams new to Event-Driven Ansible.

- **[NetBox as a Dynamic Inventory Source](https://docs.ansible.com/ansible/latest/collections/netbox/netbox/nb_inventory_inventory.html):** Documentation for the `netbox.netbox.nb_inventory` plugin used to dynamically pull device and site data from NetBox into Ansible inventories.

- **[Event-Driven Ansible Documentation](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_event-driven_ansible/index):** Official Red Hat documentation for EDA controller configuration, rulebook syntax, and action plugins.

- **[NetBox Webhooks and Event Rules](https://netboxlabs.com/docs/netbox/en/stable/integrations/webhooks/):** NetBox documentation for configuring webhooks and event rules that trigger external automation.

---

## Next Steps

- **[Try Ansible Automation Platform](https://www.redhat.com/en/technologies/management/ansible/trial):** Start a free trial of AAP including Event-Driven Ansible
- **[Red Hat Consulting](https://www.redhat.com/en/services/consulting):** Engage Red Hat consultants for production NetBox + AAP architecture
- **[Red Hat Training](https://www.redhat.com/en/services/training-and-certification):** Ansible automation training and certification paths

---

## Sources

- [Red Hat Ansible Automation Platform](https://www.redhat.com/en/technologies/management/ansible)
- [NetBox Documentation](https://netboxlabs.com/docs/netbox/en/stable/)
- [netbox.netbox Ansible Collection](https://galaxy.ansible.com/ui/repo/published/netbox/netbox/)
- [Event-Driven Ansible](https://www.redhat.com/en/technologies/management/ansible/event-driven-ansible)
- [Source Code](https://github.com/leogallego/summit-netbox-circuits-demo)
{% endraw %}
