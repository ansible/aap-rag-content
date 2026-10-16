{% raw %}
<div class="guide-header">

<h1>Event-Driven Network Source of Truth with NetBox and Ansible Automation Platform</h1>

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

Network teams manage device configurations (NTP servers, DNS resolvers, login banners, VLANs) across dozens or hundreds of devices. When a standard changes (a new NTP server, an updated compliance banner), engineers must manually identify affected devices, update each one, and verify the change took effect. This is slow, error-prone, and disconnected from the source of truth: the desired-state data lives in a CMDB or spreadsheet, but the push to devices is a separate manual process.

This guide demonstrates how to **automatically push configuration changes to network devices the moment desired state is updated in NetBox**. By combining **NetBox config contexts** as the source of truth, **NetBox dynamic inventory** to target the right devices, and **Event-Driven Ansible (EDA)** to trigger on changes, configuration updates flow from CMDB to device without manual intervention.

> **This guide covers three use cases:**
>
> - **Use Case A: NetBox dynamic inventory.** Pull device lists, groupings, and variables directly from NetBox into AAP.
> - **Use Case B: Event-driven NTP and login banner configuration.** Update a config context in NetBox, watch EDA push the change to devices automatically.
> - **Use Case C: Event-driven device provisioning.** Add a new device to NetBox, trigger a workflow that configures NTP, banner, and VLANs in parallel.

---

## Background

Network source of truth tools like **NetBox** store the desired state of the network: which devices exist, what site they belong to, what NTP servers they should use, what login banner they should display. This data is often maintained as **config contexts**, JSON blobs attached to devices, sites, or roles that represent configuration intent.

The gap is between **desired state** (what NetBox says the configuration should be) and **actual state** (what the device is actually running). Traditionally, closing this gap requires an engineer to notice the change, write or run a playbook, and verify the result. Event-Driven Ansible eliminates that gap by **reacting to NetBox changes in real time**.

**NetBox config contexts** are hierarchical JSON data structures that can be assigned at multiple levels: global, site, device role, or individual device. When a config context is updated, NetBox fires a webhook event that includes the context name and new data. EDA rulebooks can match on the context name to trigger the appropriate configuration playbook.

**NetBox dynamic inventory** replaces static inventory files with a live query to the NetBox API. Devices are automatically grouped by site, platform, and device role. Custom fields like `ansible_host` and `ansible_port` map directly to Ansible connection variables. Adding a device to NetBox automatically makes it available to automation without inventory file edits.

> **Why config contexts instead of host variables?**
>
> Config contexts are a NetBox-native concept designed for exactly this purpose: expressing desired configuration as structured data. They support inheritance (site-level defaults overridden by device-level specifics), versioning via NetBox's change log, and webhook events on update. Ansible host variables in an inventory file offer none of these features.

---

## Solution

### Components

- **[NetBox](https://netboxlabs.com/):** Network source of truth storing devices, sites, interfaces, and config contexts (NTP servers, DNS resolvers, login banners). Provides dynamic inventory plugin and webhook events on changes.

- **[Ansible Automation Platform 2.5+](https://www.redhat.com/en/technologies/management/ansible):** Enterprise automation platform providing Automation Controller (job templates, workflows, credentials, RBAC) and Event-Driven Ansible (rulebook evaluation, webhook listener).

- **[netbox.netbox Collection](https://console.redhat.com/ansible/automation-hub/repo/published/netbox/netbox/):** Certified Ansible content collection providing the `nb_inventory` dynamic inventory plugin and NetBox API modules.

- **[ansible.eda Collection](https://console.redhat.com/ansible/automation-hub/repo/published/ansible/eda/):** EDA source and action plugins. Provides `webhook` source for receiving NetBox events and `run_job_template` / `run_workflow_template` actions.

- **[cisco.ios Collection](https://console.redhat.com/ansible/automation-hub/repo/published/cisco/ios/):** Certified collection for Cisco IOS-XE device configuration. Used for NTP, banner, and VLAN configuration tasks.

### Who Benefits

| Persona | Challenge | What They Gain |
|---------|-----------|----------------|
| Network Engineer | Manually pushing NTP/DNS/banner changes to every device after a standard changes. Devices get missed, drift accumulates. | Config changes propagate automatically when the source of truth is updated. Every device in the dynamic inventory receives the update within seconds. |
| Network Architect | No single view of which devices should receive which configuration. Inventory files and config data are maintained separately and drift apart. | NetBox config contexts define desired state per site/role/device. Dynamic inventory ensures targeting is always current. One source of truth for both "what devices exist" and "what they should be configured with." |
| IT Manager / Director | Compliance audits require proof that all devices match the approved configuration standard. Manual processes cannot guarantee consistency. | Every config push is triggered by a CMDB change, logged as an AAP job, and traceable to a specific NetBox event. Audit trail is automatic. |

### Demos, Videos, and Labs

- **[EDA + NetBox Hands-On Workshop](https://github.com/rhpds/zt-ans-bu-eda-netbox):** 7-module interactive lab covering dynamic inventory, EDA rulebooks, NetBox webhooks, and workflow automation with Cisco Catalyst 8000v devices
- **[Source Code: Playbooks](https://github.com/leogallego/aap-netbox-lab-playbooks):** NTP, banner, and VLAN configuration playbooks used in this guide
- **[Source Code: EDA Rulebooks](https://github.com/leogallego/aap-netbox-lab-eda):** EDA rulebook with NetBox webhook event rules
- **[Source Code: NetBox Inventory](https://github.com/leogallego/netbox-inventory):** NetBox dynamic inventory plugin configuration

---

## Prerequisites

### AAP Version

**Ansible Automation Platform 2.5+** (minimum). EDA requires the unified platform with Automation Decisions (formerly EDA Controller). AAP 2.6 is recommended for the latest EDA features.

The default Decision Environment (`registry.redhat.io/ansible-automation-platform-26/de-supported-rhel9:latest`) is sufficient; no custom DE is needed. The Execution Environment for job templates must include the `netbox.netbox` and `cisco.ios` collections with `pynetbox` (e.g., `quay.io/acme_corp/netbox-summit-2026-ee:v3.22`).

### Featured Ansible Content Collections

| Collection | Minimum Version | Type | Purpose |
|------------|----------------|------|---------|
| [netbox.netbox](https://console.redhat.com/ansible/automation-hub/repo/published/netbox/netbox/) | 3.19.0 | Certified | `nb_inventory` dynamic inventory plugin, NetBox API modules for device/interface queries |
| [ansible.eda](https://console.redhat.com/ansible/automation-hub/repo/published/ansible/eda/) | 2.11.0 | Certified | `webhook` source plugin, `run_job_template` and `run_workflow_template` actions |
| [cisco.ios](https://console.redhat.com/ansible/automation-hub/repo/published/cisco/ios/) | 9.0.0 | Certified | `ios_config`, `ios_ntp_global`, `ios_banner` modules for device configuration |
| [ansible.netcommon](https://console.redhat.com/ansible/automation-hub/repo/published/ansible/netcommon/) | 7.1.0 | Certified | Network connection plugins (`network_cli`) and utilities |

### External Systems

| System | Required / Optional | Details |
|--------|-------------------|---------|
| NetBox | Required | v3.3+ for config contexts and webhooks. v4.x recommended. Must have custom fields `ansible_host` and `ansible_port` defined for devices. |
| Cisco IOS-XE Device | Required | Catalyst 8000v, CSR 1000v, or any IOS-XE device reachable via SSH. The workshop uses Catalyst 8000v virtual routers. |
| Git Repository | Required | Hosts the NetBox inventory plugin configuration file and EDA rulebook. AAP syncs from this repo as a Project. |

### Guide Metadata

- **Operational Impact:** Low to Medium. Use Case A is read-only (inventory sync). Use Cases B and C push configuration to network devices.
- **Business Value Drivers:**
  - Eliminate configuration drift between CMDB and devices
  - Reduce config change propagation from hours to seconds
  - Create automatic audit trail linking every device change to a CMDB update
- **Technical Value Drivers:**
  - Dynamic inventory eliminates static inventory file maintenance
  - Config contexts provide hierarchical, inheritable desired-state data
  - EDA webhook integration requires zero polling; changes push in real time

---

## Workflow and Architecture

### Use Case A: Dynamic Inventory Workflow

```
NetBox (Source of Truth)                    Ansible Automation Platform
───────────────────────                    ──────────────────────────

 Devices:                                  Inventory Source:
   cat1 (Catalyst 8000v)                     plugin: netbox.netbox.nb_inventory
   cat2 (Catalyst 8000v)                     config_context: true
                                             group_by: [platforms, device_roles, sites]
 Custom Fields:                              compose:
   ansible_host: 192.168.1.x                   ansible_network_os: platform.name
   ansible_port: 22                            ansible_host: custom_fields.host
                                               ansible_port: custom_fields.port
 Config Contexts:                                      │
   ntp_servers: [time-a.nist.gov, ...]                 │
   login_banner: "AUTHORIZED USE ONLY"                 ▼
                                            ┌─────────────────────┐
                                            │ Dynamic Inventory    │
                                            │  Groups:             │
                                            │   - sites/datacenter │
                                            │   - platforms/ios    │
                                            │   - roles/router     │
                                            │  Host vars:          │
                                            │   - ntp_servers      │
                                            │   - login_banner     │
                                            └─────────────────────┘
```

### Use Case B: Event-Driven Config Updates Workflow

```
 Operator updates                NetBox                  Event-Driven Ansible        Automation Controller
 config context                  ─────────               ────────────────────        ────────────────────
 in NetBox UI
       │
       ▼
 ntp_servers:                    Event rule fires         Webhook received            Job Template launched:
 ["time-a.nist.gov",            webhook to EDA           Condition matched:          "Configure NTP Servers"
  "time-b.nist.gov",                 │                   model == configcontext           │
  "NEW-NTP-SERVER"]                  │                   name == ntp_servers              │
                                     └──────────────────►│                               ▼
                                                         │  run_job_template         ┌──────────────────┐
                                                         └─────────────────────────►│ ios_ntp_global    │
                                                                                    │ on ALL devices    │
                                                                                    │ from NetBox       │
                                                                                    │ dynamic inventory │
                                                                                    └──────────────────┘
```

### Use Case C: New Device Provisioning Workflow

```
 Operator adds new               NetBox                  Event-Driven Ansible        Automation Controller
 device in NetBox
       │
       ▼
 Device: cat2                    Event rule fires         Webhook received            Workflow launched:
 Platform: ios                   webhook to EDA           Condition matched:          "Provision New Device"
 Custom fields:                       │                   model == device                  │
   host: 192.168.1.x                 │                   event == created                 ▼
   port: 22                          └──────────────────►│                          ┌────────────┐
                                                         │  run_workflow_template   │ Configure  │
                                                         └───────────────────────►  │ NTP        │
                                                                                    ├────────────┤
                                                                                    │ Configure  │──► parallel
                                                                                    │ Banner     │
                                                                                    ├────────────┤
                                                                                    │ Configure  │
                                                                                    │ VLANs      │
                                                                                    └────────────┘
```

### Narrative Walkthrough

**Use Case A** establishes the foundation: the `netbox.netbox.nb_inventory` plugin queries NetBox on every job launch, building a live inventory grouped by site, platform, and device role. Config contexts (NTP servers, login banners) are included as host variables. No static inventory files to maintain.

**Use Case B** adds the event-driven layer: when an operator updates a config context in NetBox (e.g., adds a new NTP server), NetBox fires a webhook to EDA. The rulebook matches on the config context name and triggers the corresponding job template, which uses the dynamic inventory to push the change to all affected devices.

**Use Case C** extends the pattern to device lifecycle: when a new device is created in NetBox, EDA triggers a workflow that runs NTP configuration, login banner, and VLAN setup in parallel, fully provisioning the device without manual intervention.

---

## Solution Walkthrough

### Use Case A: NetBox Dynamic Inventory

**The Scenario:** A network team manages Cisco Catalyst 8000v routers across multiple sites. Device information lives in NetBox, but the Ansible inventory is a static file that engineers must update manually whenever devices are added, moved, or decommissioned. The inventory drifts from reality.

#### A1. Configure NetBox Custom Fields

**Operational Impact:** Low. Adds custom fields to NetBox device model. No device changes.

NetBox devices need two custom fields so the inventory plugin knows how to connect:

| Custom Field | Type | Object Type | Purpose |
|-------------|------|-------------|---------|
| `ansible_host` | Text | Device | IP address or hostname for SSH connection |
| `ansible_port` | Integer | Device | SSH port number (default: 22) |

Create these in the NetBox UI under **Customization > Custom Fields**, or via the API. Then populate them on each device.

> **Tip:** For devices with a management interface defined in NetBox, you could use the `compose` directive to derive `ansible_host` from the primary IP instead of a custom field. Custom fields are simpler for initial deployments.

#### A2. Create the NetBox Inventory Plugin Configuration

**Operational Impact:** None. This is a configuration file stored in a Git repository.

Create a file named `netbox_inventory` (no extension) in a Git repository that AAP will sync as a Project:

```yaml
plugin: netbox.netbox.nb_inventory
config_context: true
validate_certs: false
group_by:
  - platforms
  - device_roles
  - sites
compose:
  ansible_network_os: platform.name
  ansible_host: custom_fields.host
  ansible_port: custom_fields.port
```

| Setting | Value | Purpose |
|---------|-------|---------|
| `plugin` | `netbox.netbox.nb_inventory` | Identifies this as a NetBox inventory source |
| `config_context` | `true` | Includes config context data as host variables (critical for NTP/banner use cases) |
| `validate_certs` | `false` | Disable SSL verification for lab environments |
| `group_by` | `[platforms, device_roles, sites]` | Auto-create Ansible groups from NetBox attributes |
| `compose` | (see above) | Map NetBox fields to Ansible connection variables |

> **Why `config_context: true`?** This single setting makes NetBox config contexts available as Ansible host variables. A device with an `ntp_servers` config context will have `{{ ntp_servers }}` available in playbooks without extra lookups or additional API calls.

#### A3. Create the NetBox Credential Type and Credential in AAP

**Operational Impact:** None. Creates AAP credential objects. No external changes.

The NetBox inventory plugin authenticates via environment variables. Create a custom credential type to inject them:

**Credential Type, Input Configuration:**

```yaml
fields:
  - id: NETBOX_API
    type: string
    label: NetBox Host URL
  - id: NETBOX_TOKEN
    type: string
    label: NetBox API Token
    secret: true
required:
  - NETBOX_API
  - NETBOX_TOKEN
```

**Credential Type, Injector Configuration:**

```yaml
env:
  NETBOX_API: '{{ NETBOX_API }}'
  NETBOX_TOKEN: '{{ NETBOX_TOKEN }}'
```

Then create a credential using this type with your NetBox URL and API token.

#### A4. Create the Inventory and Inventory Source in AAP

**Operational Impact:** None. Creates an inventory that queries NetBox on sync.

| Setting | Value |
|---------|-------|
| Name | `NetBox Dynamic Inventory` |
| Organization | `Default` |

**Inventory Source settings:**

| Setting | Value |
|---------|-------|
| Name | `netbox-inventory-source` |
| Execution Environment | Custom EE with `netbox.netbox` collection and `pynetbox` (e.g., `quay.io/acme_corp/netbox-summit-2026-ee:v3.22`) |
| Credential | `NetBox API` (the credential created in A3) |
| Project | `netbox-inventory-project` (syncs from [netbox-inventory repo](https://github.com/leogallego/netbox-inventory)) |
| Inventory File | `netbox_inventory` |
| Overwrite | Yes |
| Update on Launch | Yes |
| Cache Timeout | 120 seconds |

With **Update on Launch** enabled, every job template using this inventory gets a fresh device list from NetBox before execution. A device added to NetBox 30 seconds ago is immediately targetable.

---

### Use Case B: Event-Driven NTP and Banner Configuration

**The Scenario:** The security team mandates a new NTP server across all network devices. Instead of running a playbook manually, the network engineer updates the `ntp_servers` config context in NetBox. Within seconds, every device is reconfigured automatically.

#### B1. Create Config Contexts in NetBox

**Operational Impact:** None. Creates data objects in NetBox. No device changes yet.

Create two config contexts in NetBox under **Customization > Config Contexts**:

**Config Context: `ntp_servers`**

```json
{
  "ntp_servers": [
    "time-a-g.nist.gov",
    "time-b-g.nist.gov",
    "time-c-g.nist.gov"
  ]
}
```

**Config Context: `login_banner`**

```json
{
  "login_banner": "AUTHORIZED ACCESS ONLY. All activity is monitored and logged."
}
```

Assign both config contexts to the appropriate scope: all devices, a specific site, or a device role. The config context data will be available as Ansible host variables via the dynamic inventory plugin (because `config_context: true` is set).

#### B2. Create Job Templates in AAP

**Operational Impact:** None. Creates job template definitions. No device changes.

Create two job templates that use the NetBox dynamic inventory:

**Job Template: Configure NTP Servers**

| Setting | Value |
|---------|-------|
| Name | `Configure NTP Servers` |
| Inventory | `NetBox Dynamic Inventory` |
| Project | (Git repo containing the NTP playbook) |
| Playbook | `configure_ntp.yml` |
| Credentials | Machine credential for device SSH access |
| Execution Environment | Custom EE (e.g., `quay.io/acme_corp/netbox-summit-2026-ee:v3.22`) |
| Project | `aap-netbox-lab-playbooks` (Git repo synced from [source](https://github.com/leogallego/aap-netbox-lab-playbooks)) |

**Playbook: `configure_ntp.yml`**

**Playbook: `configure_ntp.yml`** ([source](https://github.com/leogallego/aap-netbox-lab-playbooks/blob/main/configure_ntp.yml))

```yaml
---
- name: Configure NTP on network devices using NetBox inventory config_context
  connection: network_cli
  hosts: all
  gather_facts: false

  tasks:
    - name: Extract NTP servers from NetBox inventory config_context
      ansible.builtin.set_fact:
        ntp_servers: "{{ hostvars[inventory_hostname].config_context[0].ntp_servers | default([]) }}"

    - name: Render NTP configuration using Jinja2 template
      ansible.builtin.template:
        src: templates/ntp_config.j2
        dest: /tmp/ntp_config_{{ inventory_hostname }}.yml

    - name: Apply NTP configuration to Cisco IOS devices
      when: ansible_network_os == 'cisco.ios.ios'
      cisco.ios.ios_ntp_global:
        config: "{{ lookup('file', '/tmp/ntp_config_' ~ inventory_hostname ~ '.yml') | from_yaml }}"
        state: replaced
```

The playbook uses a Jinja2 template (`ntp_config.j2`) to transform the config context list into the `ios_ntp_global` resource module format:

```jinja2
servers:
{% for server in ntp_servers %}
  - server: "{{ server }}"
{% endfor %}
```

> **Tip:** The `ntp_servers` variable comes directly from the NetBox config context via the dynamic inventory. No `extra_vars`, no `vars_files`, no API lookups in the playbook. The inventory plugin handles it.

**Job Template: Configure Login Banner**

| Setting | Value |
|---------|-------|
| Name | `Configure Login Banner` |
| Inventory | `NetBox Dynamic Inventory` |
| Playbook | `configure_login_banner.yml` |
| Credentials | Machine credential for device SSH access |
| Execution Environment | Custom EE (e.g., `quay.io/acme_corp/netbox-summit-2026-ee:v3.22`) |
| Project | `aap-netbox-lab-playbooks` |

**Playbook: `configure_login_banner.yml`** ([source](https://github.com/leogallego/aap-netbox-lab-playbooks/blob/main/configure_login_banner.yml))

```yaml
---
- name: Configure Login Banner on network devices using NetBox Config Context data
  connection: network_cli
  hosts: all
  gather_facts: false

  tasks:
    - name: Extract Login Banner from NetBox inventory config_context
      ansible.builtin.set_fact:
        login_banner: "{{ hostvars[inventory_hostname].config_context[0].login_banner[0] | default('') }}"

    - name: Apply Login Banner configuration to Cisco IOS devices
      when: ansible_network_os == 'cisco.ios.ios'
      cisco.ios.ios_banner:
        banner: login
        text: |
          "{{ login_banner }}"
        state: present
```

#### B3. Configure the EDA Rulebook

**Operational Impact:** None. Rulebook is a configuration file. Activation happens in B4.

The EDA rulebook listens for NetBox webhook events and matches on config context name:

**Rulebook: `netbox-webhook.yml`**

```yaml
---
- name: Listen for NetBox events on a webhook
  hosts: all
  sources:
    - ansible.eda.webhook:
        host: 0.0.0.0
        port: 5001

  rules:
    - name: NTP updates
      condition: >-
        event.payload.event == "updated" and
        event.payload.model == "configcontext" and
        event.payload.data.name == "ntp_servers"
      action:
        run_job_template:
          organization: "Default"
          name: "Configure NTP Servers"

    - name: Update login banner
      condition: >-
        event.payload.event == "updated" and
        event.payload.model == "configcontext" and
        event.payload.data.name == "login_banner"
      action:
        run_job_template:
          organization: "Default"
          name: "Configure Login Banner"
```

Each rule matches on three conditions:
1. `event == "updated"`: only react to changes, not creation or deletion
2. `model == "configcontext"`: only react to config context changes, not device or interface changes
3. `data.name == "<context_name>"`: route each config context to the correct job template

> **Why separate rules per config context?** Each config context maps to a different playbook and a different device configuration domain. A single "catch-all" rule would need conditional logic inside the playbook to determine what changed, moving complexity from the rulebook (where it's declarative and visible) to the playbook (where it's buried in code).

#### B4. Activate the Rulebook and Configure NetBox Webhook

**Operational Impact:** Medium. Activates the webhook listener and creates the NetBox event rule. From this point, config context changes will trigger device configuration pushes.

**In AAP, Automation Decisions:**

1. Create an **EDA Project** pointing to the [EDA rulebook repo](https://github.com/leogallego/aap-netbox-lab-eda) containing `netbox-webhook.yml`
2. Create a **Rulebook Activation**:

| Setting | Value |
|---------|-------|
| Name | `NetBox Rulebooks` |
| Project | (EDA project from step 1) |
| Rulebook | `netbox-webhook.yml` |
| Decision Environment | Default DE (`registry.redhat.io/ansible-automation-platform-26/de-supported-rhel9:latest`) |
| Restart Policy | `Always` |

**In NetBox, Webhooks:**

1. Create a webhook:

| Setting | Value |
|---------|-------|
| Name | `EDA Webhook` |
| Payload URL | `http://<aap-host>:5001/endpoint` |
| HTTP Method | POST |
| HTTP Content Type | `application/json` |

2. Create event rules:

| Event Rule | Object Types | Event Types |
|-----------|-------------|-------------|
| `NTP Config Context Updated` | Extras > Config Context | Object Updated |
| `Login Banner Updated` | Extras > Config Context | Object Updated |

> **Warning:** The webhook URL must be reachable from NetBox to the EDA controller. In lab environments this is typically `http://control:5001/endpoint`. In production, use HTTPS with proper certificates and ensure firewall rules allow traffic on the EDA port.

---

### Use Case C: Event-Driven Device Provisioning Workflow

**The Scenario:** A new Cisco Catalyst 8000v router is racked, cabled, and given basic IP connectivity. An engineer adds it to NetBox with site, platform, and custom fields. Automation should fully provision it (NTP, banner, VLANs) without any manual playbook execution.

#### C1. Create the Provisioning Workflow in AAP

**Operational Impact:** None. Creates a workflow definition.

Create a **Workflow Job Template** named `Provision New Device Workflow` with three steps running in parallel:

```
                    ┌──────────────────────┐
                    │ Configure NTP        │
               ┌──►│ Servers              │
               │   └──────────────────────┘
┌──────────┐   │   ┌──────────────────────┐
│  START   │───┼──►│ Configure Login      │
└──────────┘   │   │ Banner               │
               │   └──────────────────────┘
               │   ┌──────────────────────┐
               └──►│ Configure VLANs      │
                   └──────────────────────┘
```

All three job templates use the same NetBox dynamic inventory and run against the newly added device. Because the inventory updates on launch, the new device is automatically included.

#### C2. Add the Device Creation Rule to the Rulebook

**Operational Impact:** None. Extends the existing rulebook with a new rule.

Add this rule to `netbox-webhook.yml`:

```yaml
    - name: New Device Added
      condition: >-
        event.payload.event == "created" and
        event.payload.model == "device"
      action:
        run_workflow_template:
          organization: "Default"
          name: "Provision New Device Workflow"
```

And create a corresponding event rule in NetBox:

| Event Rule | Object Types | Event Types |
|-----------|-------------|-------------|
| `New Device Provisioning` | DCIM > Device | Object Created |

#### C3. Test by Adding a Device in NetBox

**Operational Impact:** Medium. Adding a device to NetBox triggers the provisioning workflow, which pushes configuration to the new device.

1. In NetBox, navigate to **Devices > Add Device**
2. Fill in: Name (`cat2`), Site, Device Role (`router`), Platform (`ios`)
3. Set custom fields: `ansible_host` = device management IP, `ansible_port` = 22
4. Click **Create**

Within seconds, the AAP workflow launches and configures NTP, banner, and VLANs on the new device in parallel.

---

## Validation

### Testing Dynamic Inventory

**Step 1: Sync the inventory in AAP.**

Navigate to **Automation Execution > Infrastructure > Inventories > NetBox Dynamic Inventory > Sources > netbox-inventory-source** and click **Sync**. Verify devices appear under the **Hosts** tab.

**Step 2: Verify groups and variables.**

Click on a host (e.g., `cat1`). Confirm:
- The host appears in the correct groups (`platforms_ios`, `device_roles_router`, `sites_<sitename>`)
- Host variables include `ansible_host`, `ansible_port`, `ansible_network_os`
- Config context data appears as host variables (`ntp_servers`, `login_banner`)

### Testing Event-Driven Config Updates

**Step 1: Update a config context in NetBox.**

Navigate to **Customization > Config Contexts > ntp_servers** and add a new NTP server to the JSON data:

```json
{
  "ntp_servers": [
    "time-a-g.nist.gov",
    "time-b-g.nist.gov",
    "time-c-g.nist.gov",
    "pool.ntp.org"
  ]
}
```

Click **Save**.

**Step 2: Verify in AAP.**

| What to Check | Where | Success Indicator |
|--------------|-------|-------------------|
| Rulebook activation fired | Automation Decisions > Rulebook Activations > `NetBox Rulebooks` | Fire count incremented |
| Job template launched | Automation Execution > Jobs | "Configure NTP Servers" job appears with status `Successful` |
| NTP configured on device | Job output | `ios_ntp_global` task shows `changed: true` |

**Step 3: Verify on the device (optional).**

```bash
ssh admin@<device-ip>
show ntp associations
```

Confirm the new NTP server appears in the association list.

### Troubleshooting Common Failures

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Inventory sync shows 0 hosts | NetBox API URL or token incorrect in credential | Verify `NETBOX_API` URL is reachable from the execution environment. Test with `curl -H "Authorization: Token <token>" <url>/api/dcim/devices/` |
| Hosts appear but have no config context variables | `config_context: true` missing from inventory plugin config | Add `config_context: true` to the `netbox_inventory` file and re-sync the project |
| EDA rulebook activation shows 0 fires after config context update | NetBox webhook not configured or URL incorrect | Verify the webhook exists in NetBox under **Integrations > Webhooks** and the payload URL matches `http://<aap-host>:<eda-port>/endpoint` |
| Job template fails with "No hosts matched" | Dynamic inventory not updating on launch, or device missing custom fields | Ensure **Update on Launch** is enabled on the inventory source. Verify devices have `ansible_host` and `ansible_port` custom fields populated |
| `ios_ntp_global` fails with "Connection refused" | Device SSH port incorrect or device unreachable from execution environment | Verify `ansible_port` custom field matches the device's actual SSH port. Test SSH connectivity from the EE container |

---

## Maturity Path

| Maturity | Inventory Management | Configuration Updates | Device Provisioning |
|----------|---------------------|----------------------|-------------------|
| **Crawl** | Dynamic inventory from NetBox replaces static files. Engineers run job templates manually against the live inventory. | Engineer updates config context in NetBox, then manually launches the matching job template from AAP. | Engineer adds device to NetBox, then manually runs provisioning playbooks. |
| **Walk** | Dynamic inventory with update-on-launch. Config contexts provide device variables automatically. | EDA triggers job templates on config context changes. Engineer reviews job output for correctness. | EDA triggers provisioning workflow on device creation. Engineer verifies device config post-provisioning. |
| **Run** | Dynamic inventory is the only inventory source. All device targeting is derived from NetBox attributes. | Fully automated: config context change → EDA → device update → compliance verification. No manual steps. | Fully automated: device creation → EDA → parallel provisioning → compliance scan → notification. Zero-touch onboarding. |

---

## Summary

This guide demonstrated three progressively mature use cases for managing network device configuration with NetBox and Ansible Automation Platform:

- **Use Case A** replaced static inventory files with a live NetBox dynamic inventory, automatically grouping devices by site, platform, and role while pulling config context data as host variables.

- **Use Case B** added event-driven automation: updating an NTP server list or login banner in NetBox automatically triggers EDA, which launches the corresponding job template to push the change to all devices in the dynamic inventory.

- **Use Case C** extended the pattern to device lifecycle: adding a new device to NetBox triggers a provisioning workflow that configures NTP, banner, and VLANs in parallel for zero-touch onboarding.

The unifying pattern is **NetBox as the single source of both inventory and desired state**. The dynamic inventory plugin eliminates static files. Config contexts define what devices should look like. EDA webhooks close the loop between "desired state changed" and "devices updated." Together, they transform NetBox from a passive documentation tool into an active driver of network automation.

---

## Related Guides

- **[Event-Driven WAN Circuit Failover with NetBox and AAP](README-NetBox-WAN-EDA-Failover.md):** Advanced use case covering event-driven circuit failover with dynamic backup discovery, router reconfiguration, and automated incident reporting. Builds on the EDA + NetBox foundation established in this guide.

- **[NetBox Dynamic Inventory Plugin Documentation](https://docs.ansible.com/ansible/latest/collections/netbox/netbox/nb_inventory_inventory.html):** Full reference for the `netbox.netbox.nb_inventory` plugin including all configuration options, query filters, and compose directives.

- **[Event-Driven Ansible Documentation](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_event-driven_ansible/index):** Official Red Hat documentation for EDA controller configuration, rulebook syntax, and action plugins.

- **[NetBox Config Contexts](https://netboxlabs.com/docs/netbox/en/stable/models/extras/configcontext/):** NetBox documentation for creating and managing config contexts with hierarchical assignment.

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
- [EDA + NetBox Workshop](https://github.com/rhpds/zt-ans-bu-eda-netbox)
{% endraw %}
