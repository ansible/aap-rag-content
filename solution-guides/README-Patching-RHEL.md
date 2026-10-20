{% raw %}
<div class="guide-header">

<h1>RHEL Patching with Red Hat Lightspeed and Ansible MCP Server</h1>

<span class="guide-type-badge guide-type-badge--solution"><i class="fas fa-check-circle" aria-hidden="true"></i> Solution Guide</span>

</div>

> **Work in Progress** -- this guide is actively being developed.

<div class="guide-hero-callout guide-hero-partner guide-hero-partner--redhat-ai" role="img" aria-label="Ansible Automation Platform and Red Hat Lightspeed">
  <img src="assets/images/logos/aap-ansible-icon.png" alt="" class="guide-hero-callout__icon" width="36" height="36">
  <span class="guide-hero-partner__plus" aria-hidden="true">+</span>
  <span class="guide-hero-partner__partner card-partner-logo-set card-partner-logo-set--redhat-ai">
    <img src="assets/images/logos/redhat-ai-logo.png" alt="Red Hat Lightspeed" class="card-partner-logo card-partner-logo--light" width="106" height="32">
    <img src="assets/images/logos/redhat-ai-logo-dark.png" alt="" class="card-partner-logo card-partner-logo--dark" aria-hidden="true" width="108" height="22">
  </span>
</div>

## Overview

Security patching at scale is one of the most time-consuming and error-prone tasks in IT operations. Teams manually check vulnerability reports, cross-reference advisories, identify affected systems, build remediation plans, and schedule maintenance windows -- often across hundreds or thousands of RHEL virtual machines running on OpenShift Virtualization. A single critical CVE can consume days of engineering time from discovery to resolution.

This guide demonstrates how to collapse that timeline from days to minutes using **Red Hat Lightspeed MCP** and the **Ansible Automation Platform MCP server**. An operator describes the problem in natural language -- "patch CVE-2024-6174 on my production fleet" -- and the MCP-connected AI assistant identifies affected systems, surfaces the correct advisory, selects the approved remediation playbook, and executes it through AAP with full audit trail. No manual advisory lookup, no hand-written playbooks, no SSH sessions.

<h2 id="background"></h2>

## Background

Vulnerability management on RHEL is a well-understood domain: Red Hat publishes security advisories (RHSAs), each mapping one or more CVEs to specific package updates across RHEL versions. Tools like `dnf updateinfo` and the <a target="_blank" href="https://console.redhat.com">Red Hat Lightspeed</a> (formerly Insights) Vulnerability service make it straightforward to identify which systems are affected and which errata to apply. The challenge is not *knowing what to do* -- it is *doing it quickly, consistently, and at scale* across a fleet of virtual machines.

OpenShift Virtualization adds a layer of complexity. RHEL VMs managed through OpenShift inherit the benefits of Kubernetes orchestration but still require traditional in-guest patching for OS-level vulnerabilities. Organizations need a way to bridge the Kubernetes management plane with RHEL system administration -- and that bridge is Ansible Automation Platform.

The Model Context Protocol (MCP) changes how operators interact with these systems. Instead of navigating multiple consoles and CLIs, an MCP-enabled AI assistant can query Red Hat Lightspeed for vulnerability data, cross-reference it with the organization's AAP inventory, and trigger approved remediation -- all from a single conversational interface. This is not autonomous AI making unsupervised decisions; it is AI-assisted operations where the human remains in the loop but the toil is eliminated.

## Solution

This solution connects two MCP servers to an AI assistant (such as an IDE with MCP support) to create an end-to-end patching workflow:

- **<a target="_blank" href="https://console.redhat.com">Red Hat Lightspeed</a>** for vulnerability identification, advisory lookup, host inventory, and **Red Hat-curated remediation playbooks** (Remediations service)
- **<a target="_blank" href="https://www.redhat.com/en/technologies/management/ansible">Ansible Automation Platform (AAP)</a>** for governed playbook execution across RHEL VMs on OpenShift Virtualization
- **Red Hat Lightspeed MCP server** to expose Lightspeed Vulnerability, Inventory, and Remediations APIs to the AI assistant
- **AAP MCP server** to expose job templates, inventories, and execution capabilities to the AI assistant

### Who Benefits

| Persona | Challenge | What They Gain |
|---------|-----------|---------------|
| IT Ops Engineer / SRE | Manually correlating CVEs to advisories, checking each system, and running patches one by one | Natural-language patching: describe the CVE, the assistant handles advisory lookup, system identification, and execution |
| Automation Architect | Building and maintaining per-CVE playbooks and job templates for every advisory | MCP-driven workflow that dynamically selects the right remediation based on the advisory, no per-CVE template sprawl |
| IT Manager / Director | Patch compliance SLAs measured in days or weeks; audit gaps between discovery and remediation | Measurable reduction in time-to-patch with full audit trail through AAP job logs |

**Recommended Demos and Self-Paced Labs:**

- <a target="_blank" href="https://labs.demoredhat.com/">Red Hat Technical Workshops</a> -- LB2961: Introduction to AI-Driven Ansible Automation
- <a target="_blank" href="https://youtu.be/a3fCHd2vTXU">AIOps with Ansible YouTube overview</a> (2 min)

## Prerequisites

### Ansible Automation Platform

- **Ansible Automation Platform 2.5+** -- required for MCP server integration and the `ansible.controller` collection features used in this guide

### Featured Ansible Content Collections

| Collection | Type | Purpose |
|-----------|------|---------|
| <a target="_blank" href="https://console.redhat.com/ansible/automation-hub/repo/published/ansible/controller/">ansible.controller</a> | Certified | Programmatic interaction with AAP Controller (job launches, inventory queries) |
| <a target="_blank" href="https://console.redhat.com/ansible/automation-hub/repo/published/redhat/rhel_system_roles/">redhat.rhel_system_roles</a> | Certified | RHEL system configuration and patching tasks |

### External Systems

| System | Required | Purpose |
|--------|----------|---------|
| Red Hat Lightspeed (console.redhat.com) | Yes | Vulnerability data, host inventory, Red Hat-curated remediation playbooks |
| OpenShift Virtualization | Yes | Platform running the RHEL VMs to be patched |
| MCP-compatible AI client | Yes | IDE or tool with MCP support (e.g., Cursor, VS Code with MCP extension) |

### MCP Servers

| MCP Server | Purpose |
|-----------|---------|
| **Red Hat Lightspeed MCP** | Exposes Vulnerability, Inventory, Advisor, Remediations, and RBAC APIs |
| **AAP MCP server** | Exposes job templates, inventories, and job launch/status APIs |

> **RBAC:** Both MCP servers require proper role assignments.
>
> Lightspeed MCP needs: Vulnerability viewer, Inventory Hosts viewer, Remediations user. AAP MCP needs: Execute permission on the relevant job templates and Read on inventories.

**Operational Impact:** Medium -- applies package updates to production RHEL VMs. Test in non-production first.

## Patching Workflow

```mermaid
graph LR
  subgraph Identify
    A([CVE Reported]) --> B[Lightspeed MCP]
    B --> C[Affected Hosts + Advisory]
  end
  subgraph Remediate
    C --> D[AAP MCP]
    D --> E[Execute Patch]
  end
  E --> F([Validated])
```

The workflow follows a Day 2 operations pattern:

1. **Trigger** -- A CVE is reported or a compliance scan flags unpatched systems
2. **Identify** -- The AI assistant queries Red Hat Lightspeed MCP to identify which systems in the fleet are affected and which RHSA applies
3. **Plan** -- The assistant retrieves the advisory details, confirms the fix package version, and selects (or generates) a remediation playbook
4. **Execute** -- The assistant launches the approved job template through AAP MCP, targeting only the affected hosts
5. **Validate** -- Post-patch verification confirms the package was updated and the CVE is resolved

### Operational Impact per Stage

| Stage | Impact | Notes |
|-------|--------|-------|
| 1. Identify affected systems | None | Read-only queries to Lightspeed Vulnerability and Inventory APIs |
| 2. Retrieve advisory details | None | Read-only API call |
| 3. Select remediation playbook | None | Read-only query to AAP job templates |
| 4. Execute patch | **High** | Applies package updates to target systems; schedule during change window |
| 5. Validate | Low | Read-only verification commands |

## Solution Walkthrough

### Step 1: Identify Vulnerable Systems with Red Hat Lightspeed MCP

**Operational Impact:** None

The AI assistant uses the Lightspeed MCP Vulnerability tools to identify which connected systems are affected by the reported CVE.

```yaml
# Lightspeed MCP tool call (conceptual)
- tool: vulnerability_get_cve_details
  parameters:
    cve_id: "CVE-2024-6174"

# Returns: severity, description, affected_systems[], applicable_advisories[]
```

The Lightspeed Vulnerability API returns the list of systems where the CVE is present, along with the applicable Red Hat Security Advisory (RHSA). This replaces manual cross-referencing between the CVE database, errata pages, and your inventory.

### Step 2: Retrieve Advisory Details and Affected Packages

**Operational Impact:** None

With the advisory ID from Step 1, the assistant retrieves the specific package versions that resolve the vulnerability.

```yaml
# Lightspeed MCP tool call (conceptual)
- tool: vulnerability_get_advisory_details
  parameters:
    advisory_id: "RHSA-2025:10848"

# Returns: fixed_package_versions[], affected_rhel_versions[], severity
```

For CVE-2024-6174, this returns that `cloud-init` must be updated to version `24.4-4.el9_6.3` or later. The assistant can also cross-reference with the Inventory MCP tools to confirm which RHEL version each affected host is running.

### Step 3: Select and Review the Remediation Playbook via AAP MCP

**Operational Impact:** None

The assistant queries the AAP MCP server to find an existing job template for security patching, or uses the Lightspeed **Remediations** API to retrieve a Red Hat-curated playbook.

```yaml
# AAP MCP tool call (conceptual)
- tool: job_templates_list
  parameters:
    search: "security patch"

# Or retrieve a Red Hat-curated remediation playbook via Lightspeed Remediations
- tool: remediations_create_playbook
  parameters:
    cve_ids: ["CVE-2024-6174"]
    system_ids: ["<uuid-of-affected-host>"]
```

> **Why two MCP servers?**
>
> Lightspeed MCP knows *what* is wrong (which CVEs affect which hosts). AAP MCP knows *how to fix it* (which job templates are approved, what credentials and inventories to use). Connecting both to the same AI assistant lets it bridge vulnerability intelligence with remediation execution.

### Step 4: Execute the Patch via Ansible Automation Platform

**Operational Impact:** High

With the correct job template identified and the target hosts confirmed, the assistant launches the patch through AAP. The human reviews and approves before execution.

```yaml
# AAP MCP tool call (conceptual)
- tool: job_templates_launch
  parameters:
    job_template_id: 42
    extra_vars:
      cve_id: "CVE-2024-6174"
      target_hosts: "affected_rhel_vms"
    limit: "ocp-virt-prod-*"
```

The underlying playbook uses standard `ansible.builtin.dnf` tasks to apply the update:

```yaml
- name: Patch CVE via advisory
  hosts: all
  become: true
  tasks:
    - name: Apply security update for target CVE
      ansible.builtin.dnf:
        name: "{{ target_package }}"
        state: latest
        security: true
      register: patch_result

    - name: Verify package was updated
      ansible.builtin.command:
        cmd: "rpm -q {{ target_package }}"
      register: post_patch_version
      changed_when: false

    - name: Report patch status
      ansible.builtin.debug:
        msg: "{{ inventory_hostname }}: {{ post_patch_version.stdout }}"
```

> **RBAC:** Govern who can trigger patches.
>
> Assign the `Execute` role on patching job templates only to the `security-ops` team. The AI assistant acts on behalf of the authenticated user -- it cannot bypass AAP's RBAC model.

### Step 5: Validate and Report

**Operational Impact:** Low

After the job completes, the assistant confirms the patch was applied by checking the AAP job output and optionally re-querying Lightspeed Vulnerability to verify the CVE is no longer reported for the patched hosts.

```yaml
# AAP MCP tool call (conceptual)
- tool: jobs_get_details
  parameters:
    job_id: "{{ launched_job_id }}"

# Lightspeed MCP re-check
- tool: vulnerability_get_systems_affected
  parameters:
    cve_id: "CVE-2024-6174"
    # Expect: affected_count reduced or zero
```

## Validation

### Test

Trigger the full workflow by asking the AI assistant to patch a known CVE on a test system:

> "Check if CVE-2024-6174 affects any of my RHEL systems and patch the affected hosts."

The assistant should:
1. Query Lightspeed MCP for affected systems
2. Identify the applicable RHSA
3. Find or create the remediation job template in AAP
4. Launch the job (with your approval)
5. Report the result

### Expected Result

After execution, verify on the target host:

```
$ rpm -q cloud-init
cloud-init-24.4-7.el9_7.1.noarch
```

The AAP job output should show:

```
PLAY RECAP *********************************************************************
target_host : ok=3    changed=1    unreachable=0    failed=0    skipped=0
```

### Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Lightspeed MCP returns no affected systems | Systems not connected to Red Hat Lightspeed or Inventory viewer role missing | Verify systems are registered with `rhc` and RBAC roles are assigned to the service account |
| AAP MCP cannot find job templates | Insufficient RBAC permissions on the AAP user/token | Assign at least `Read` on the job template and `Execute` to launch |
| `dnf update` fails with "No packages marked for update" | System already patched or on a RHEL version where the fix is not yet available | Check `dnf updateinfo list --cves <CVE>` on the target; verify RHEL version matches the advisory |
| Job template launch returns 403 | AAP token lacks Execute permission | Update the credential in AAP and reassign the RBAC role |

## Maturity Path

| Maturity | Description |
|----------|-------------|
| **Crawl** | Use Lightspeed MCP to identify affected systems and advisories; patch manually via SSH or ad-hoc AAP jobs |
| **Walk** | Connect AAP MCP so the assistant can launch approved job templates; human reviews and approves each execution |
| **Run** | Fully automated pipeline: compliance scan triggers Lightspeed lookup, AAP patches affected systems within policy-defined maintenance windows, results feed back to Lightspeed for verification |

## Related Guides

- [AIOps automation with Ansible](README-AIOps.md) -- the foundational AIOps reference architecture this guide extends
- [AI Infrastructure automation with Ansible](README-IA.md) -- deploy the AI backend used by Lightspeed
- [Unlock AIOps with ServiceNow LEAP and Ansible MCP server](README-AIOps-ServiceNow.md) -- MCP-driven remediation with ServiceNow ITSM integration

## Sources

- <a target="_blank" href="https://www.redhat.com/en/technologies/management/ansible">Red Hat Ansible Automation Platform</a>
- <a target="_blank" href="https://console.redhat.com">Red Hat Lightspeed (Insights)</a>
- <a target="_blank" href="https://access.redhat.com/security/cve/CVE-2024-6174">CVE-2024-6174 Advisory</a>
- <a target="_blank" href="https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/virtualization/">OpenShift Virtualization Documentation</a>
{% endraw %}
