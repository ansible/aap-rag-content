{% raw %}
<div class="guide-header">

<h1>Event-Driven Remediation with Azure Service Bus and Ansible</h1>

<span class="guide-type-badge guide-type-badge--solution"><i class="fas fa-check-circle" aria-hidden="true"></i> Solution Guide</span>

</div>

<style>
  div#toc {
    display: none;
  }
</style>

<div class="guide-hero-callout guide-hero-partner guide-hero-partner--azure" role="img" aria-label="Ansible Automation Platform and Microsoft Azure">
  <img src="assets/images/logos/aap-ansible-icon.png" alt="" class="guide-hero-callout__icon" width="36" height="36">
  <span class="guide-hero-partner__plus" aria-hidden="true">+</span>
  <span class="guide-hero-partner__partner card-partner-logo-set">
    <img src="assets/images/logos/azure-logo.png" alt="Microsoft Azure" class="card-partner-logo card-partner-logo--light" width="106" height="32">
    <img src="assets/images/logos/azure-logo-darkmode.png" alt="" class="card-partner-logo card-partner-logo--dark" aria-hidden="true" width="106" height="32">
  </span>
</div>

## Overview

Organizations running workloads on Microsoft Azure use **Azure Service Bus** as their enterprise messaging backbone -- routing events, alerts, and telemetry between services, monitoring tools, and operational systems. When Azure Monitor, Defender for Cloud, or a custom application publishes a critical event to a Service Bus queue or topic, the response today is manual: an engineer reads the message, investigates the affected resource, and remediates by hand.

This guide demonstrates how to connect **Azure Service Bus Queues** directly to **Event-Driven Ansible (EDA)**, creating a real-time pipeline that consumes Azure events, enriches them with AI-driven root cause analysis, and triggers automated remediation -- turning Azure's messaging layer into the trigger for a closed-loop AIOps workflow.

> **This guide builds on the AIOps reference architecture.**
>
> Production **Walk** remediation uses **AAP MCP** to search approved job templates and workflows, then AI **selects** from that library before a governed run. See [curated automation remediation](README-AIOps.md#4-curated-automation-remediation-walk). This guide wires **Azure Service Bus** into EDA and walks the **workshop Run** pipeline (enrichment plus **Automation code assistant** codegen) where labs need it; swap stage 3 for MCP selection when you deploy for real.

<h2 id="background"></h2>

## Background

**Azure Service Bus** is a fully managed enterprise messaging service from Microsoft that supports message queuing and publish-subscribe patterns. It decouples event producers (monitoring tools, applications, Azure services) from consumers (automation systems, dashboards, alerting tools), providing reliable message delivery with features like dead-letter queues, sessions, and scheduled delivery.

<img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f4d6.png" width="20" style="vertical-align:text-bottom;"> <a target="_blank" href="https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-messaging-overview">Azure Service Bus Messaging -- microsoft.com</a>

In an AIOps context, Azure Service Bus acts as the **event transport layer** -- sitting between Azure's monitoring and alerting tools (Azure Monitor, Azure Alerts, Defender for Cloud) and Ansible's automation engine. Events are published to a Service Bus queue or topic, and Event-Driven Ansible subscribes to consume them in real time.

This architecture is particularly valuable for organizations that already use Azure Service Bus as their event backbone. Instead of building custom integrations for each alert type, you route all events through Service Bus and let a single EDA rulebook handle the dispatch to enrichment and remediation workflows.

<img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f4d6.png" width="20" style="vertical-align:text-bottom;"> <a target="_blank" href="https://www.redhat.com/en/topics/ai/what-is-aiops">What is AIOps? -- redhat.com</a>

<h2 id="solution"></h2>

## Solution

What makes up the solution?

- <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/2601.png" width="20" style="vertical-align:text-bottom;"> **Azure Service Bus** as the managed messaging layer for event transport <a target="_blank" href="https://azure.microsoft.com/en-us/products/service-bus">[Link]</a>
- <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f4e1.png" width="20" style="vertical-align:text-bottom;"> **Event-Driven Ansible (EDA)** to subscribe to Service Bus queues and trigger automation <a target="_blank" href="https://www.redhat.com/en/technologies/management/ansible/event-driven-ansible">[Link]</a>
- <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f9e0.png" width="20" style="vertical-align:text-bottom;"> **Red Hat AI** for AI-driven root cause analysis of the event context <a target="_blank" href="https://www.redhat.com/en/products/ai">[Link]</a>
- <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f501.png" width="20" style="vertical-align:text-bottom;"> **Ansible Automation Platform (AAP)** workflows for orchestrating enrichment and remediation <a target="_blank" href="https://www.redhat.com/en/technologies/management/ansible">[Link]</a>
- <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/2728.png" width="20" style="vertical-align:text-bottom;"> **Automation code assistant** to generate remediation playbooks from AI-enriched context (workshop Run only) <a target="_blank" href="https://www.redhat.com/en/technologies/management/ansible/ansible-lightspeed">[Link]</a>

> **EDA is part of Ansible Automation Platform.**
>
> EDA uses rulebooks to monitor events, then executes specified job templates or workflows based on the event. Think of it simply as inputs and outputs. EDA is an automatic way for inputs into Ansible Automation Platform, where Ansible Automation Platform is the output (running a job template or workflow).

### Who Benefits

| Persona | Challenge | What They Gain |
|---------|-----------|---------------|
| <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f6e0.png" width="20" style="vertical-align:text-bottom;"> **IT Ops Engineer / SRE** | Monitoring Azure Service Bus queues for critical events and manually investigating each one across hybrid Azure and on-prem infrastructure | Azure events automatically trigger enrichment and remediation workflows -- the fix starts before the engineer even sees the alert |
| <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f5fa.png" width="20" style="vertical-align:text-bottom;"> **Automation Architect** | Integrating Azure's messaging layer with Ansible requires understanding Service Bus authentication, EDA event source plugins, and credential management | A reference architecture with production-ready EDA rulebooks, Azure Service Bus configuration, and tested collection usage |
| <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f4ca.png" width="20" style="vertical-align:text-bottom;"> **IT Manager / Director** | Azure event volume is growing but response times aren't improving; hybrid cloud operations span Azure and on-prem with no unified automation trigger | A single event pipeline that bridges Azure monitoring with Ansible remediation across hybrid environments -- measurable MTTR reduction |

<h2 id="prerequisites"></h2>

## Prerequisites

### Ansible Automation Platform

- **Ansible Automation Platform 2.5+** -- Required for enterprise Event-Driven Ansible support and the Azure Service Bus event source plugin.

### Featured Ansible Content Collections

| Collection | Type | Purpose |
|-----------|------|---------|
| <a target="_blank" href="https://console.redhat.com/ansible/automation-hub/repo/published/ansible/eda/content/eda%2Fplugins%2Fevent_source/azure_service_bus/">ansible.eda</a> | Certified | EDA event sources and filters -- includes the `azure_service_bus` event source plugin |
| <a target="_blank" href="https://console.redhat.com/ansible/automation-hub/repo/published/azure/azcollection/">azure.azcollection</a> | Certified | Manage Azure resources (VMs, networking, storage, etc.) for remediation tasks |
| <a target="_blank" href="https://console.redhat.com/ansible/automation-hub/repo/published/ansible/controller/">ansible.controller</a> | Certified | AAP configuration as code (job templates, workflows, surveys) |
| <a target="_blank" href="https://console.redhat.com/ansible/automation-hub/repo/published/redhat/ai">redhat.ai</a> | Certified | AI model inference using the OpenAI-compatible API via InstructLab |
| <a target="_blank" href="https://console.redhat.com/ansible/automation-hub/repo/published/ansible/scm/">ansible.scm</a> | Certified | Git operations (commit and push generated playbooks) |

### External Systems

| System | Required | Notes |
|--------|----------|-------|
| Azure Service Bus namespace | Yes | With at least one queue or topic/subscription configured |
| Azure subscription | Yes | With permissions to create Service Bus resources and configure Shared Access Policies |
| AI inference endpoint | Yes | Red Hat AI (RHEL AI + InstructLab) or any OpenAI-compatible API |
| Automation code assistant | Recommended (workshop Run) | LLM playbook generation at incident time -- not Red Hat Lightspeed curated remediations |
| Git repository | Yes | GitHub, GitLab, or Gitea for storing generated playbooks |
| Chat or ITSM tool | Recommended | Slack, Mattermost, or ServiceNow for human-in-the-loop notifications |

<h2 id="azure-service-bus-to-ansible-workflow"></h2>

## Azure Service Bus to Ansible Workflow

The workflow has four stages aligned with the [workshop Run pipeline](README-AIOps.md#workshop-run-pipeline) in the foundational AIOps guide (Azure Service Bus replaces Kafka as the transport layer):

1. **Azure Event → Service Bus → EDA** -- Azure Monitor, Defender for Cloud, or a custom application publishes an event to a Service Bus queue. EDA subscribes to the queue and consumes the message.
2. **Enrichment Workflow** -- AAP gathers additional context from the affected Azure resource or on-prem host, sends the enriched data to Red Hat AI for root cause analysis, and notifies the operations team.
3. **Remediation Workflow (workshop Run demo)** -- **Automation code assistant** generates a remediation playbook from the AI analysis, commits it to Git, and creates a Job Template. At **Walk**, use [AAP MCP to select an existing template](README-AIOps.md#4-curated-automation-remediation-walk) instead.
4. **Execute Remediation** -- The approved or generated playbook runs against the affected infrastructure (Azure VMs, on-prem hosts, or network devices), resolving the issue.

### Operational Impact per Stage

| Stage | Operational Impact | Why |
|-------|-------------------|-----|
| **1. Azure Event → EDA** | **None** | Read-only -- EDA reads a message from the Service Bus queue. No changes to systems. |
| **2. Enrichment Workflow** | **Low** | Collects logs and system info, calls an AI API, posts to chat/ITSM. No infrastructure changes. |
| **3. Remediation Workflow** | **Low** | Generates a playbook, commits to Git, creates a Job Template. Prepares the fix but does not touch production. |
| **4. Execute Remediation** | **High** | Modifies production infrastructure. Should go through a change window or approval gate. |

### Workflow Diagram

```
Azure Monitor/Alert → Service Bus Queue → EDA Rulebook → Enrichment Workflow → AI Analysis → Remediation Workflow → Execute Fix
```

> **Azure Service Bus is the event transport layer.**
>
> In the AIOps reference architecture, Kafka or a direct webhook handles event transport. When using Azure Service Bus, it replaces that layer -- Azure services publish events to a queue, and EDA subscribes directly using the built-in `ansible.eda.azure_service_bus` plugin.

<h2 id="solution-walkthrough"></h2>

## Solution Walkthrough

### 1. Configure Azure Service Bus Queue

**Operational Impact:** None (Azure configuration only)

Create a Service Bus namespace and queue in Azure, then configure a Shared Access Policy that EDA will use to authenticate.

Using the Azure CLI:

```bash
az servicebus namespace create \
  --name aiops-events \
  --resource-group rg-aiops \
  --location eastus \
  --sku Standard

az servicebus queue create \
  --name infrastructure-alerts \
  --namespace-name aiops-events \
  --resource-group rg-aiops

az servicebus namespace authorization-rule create \
  --name eda-listener \
  --namespace-name aiops-events \
  --resource-group rg-aiops \
  --rights Listen
```

Or automate the same setup with the `azure.azcollection`:

```yaml
- name: Create Azure Service Bus queue for AIOps events
  azure.azcollection.azure_rm_servicebusqueue:
    resource_group: rg-aiops
    namespace: aiops-events
    name: infrastructure-alerts
    max_size_in_mb: 1024
    default_message_time_to_live: "PT1H"
  delegate_to: localhost
```

> **Route Azure Monitor alerts to Service Bus.**
>
> In the Azure Portal, navigate to **Monitor → Alerts → Action Groups** and create an action group with a **Service Bus Queue** action type. This routes Azure Monitor alerts directly into your queue where EDA can consume them.

### 2. EDA Rulebook for Azure Service Bus Events

**Operational Impact:** None

The EDA rulebook subscribes to the Azure Service Bus queue using the built-in `ansible.eda.azure_service_bus` event source plugin. When a message arrives, the rulebook evaluates conditions and triggers the enrichment workflow.

```yaml
---
- name: Azure Service Bus AIOps response
  hosts: all
  sources:
    - ansible.eda.azure_service_bus:
        conn_str: "{{ azure_service_bus_connection_string }}"
        queue_name: infrastructure-alerts
        logging_enable: true

  rules:
    - name: Azure infrastructure alert detected
      condition: event.body is defined
      action:
        run_workflow_template:
          organization: "Default"
          name: "Azure Alert Enrichment Workflow"
          extra_vars:
            alert_name: "{{ event.body.data.essentials.alertRule | default('Unknown Alert') }}"
            severity: "{{ event.body.data.essentials.severity | default('Sev3') }}"
            affected_resource: "{{ event.body.data.essentials.alertTargetIDs[0] | default('') }}"
            description: "{{ event.body.data.essentials.description | default('') }}"
            fired_time: "{{ event.body.data.essentials.firedDateTime | default('') }}"
```

The rulebook extracts key fields from the Azure Monitor alert schema -- the alert rule name, severity, affected Azure resource ID, description, and timestamp -- and passes them to the enrichment workflow.

> **Azure Monitor Common Alert Schema.**
>
> Azure Monitor alerts follow a <a target="_blank" href="https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-common-schema">Common Alert Schema</a> with `essentials` (severity, alert rule, target resource) and `alertContext` (metric/log details). Your rulebook conditions can filter on any of these fields -- for example, only triggering automation on `Sev0` or `Sev1` alerts.

### 3. Enrichment Workflow -- Gather Context and Analyze with AI

**Operational Impact:** Low

Once EDA triggers the enrichment workflow, Ansible gathers additional context from the affected Azure resource and sends everything to Red Hat AI for root cause analysis. This is the same pattern described in the [AIOps reference architecture -- Log Enrichment and Prompt Generation Workflow](README-AIOps.md#2-log-enrichment-and-prompt-generation-workflow).

**Step 3a: Gather context from the affected Azure VM**

```yaml
- name: Gather Azure VM context for alert
  hosts: localhost
  tasks:
    - name: Get Azure VM details
      azure.azcollection.azure_rm_virtualmachine_info:
        resource_group: "{{ resource_group }}"
        name: "{{ vm_name }}"
      register: vm_info

    - name: Get recent Azure activity log entries
      azure.azcollection.azure_rm_resource_info:
        url: "/subscriptions/{{ subscription_id }}/providers/Microsoft.Insights/eventtypes/management/values"
        api_version: "2015-04-01"
      register: activity_log
```

**Step 3b: Gather diagnostics from the host itself**

```yaml
- name: Gather host diagnostics
  hosts: "{{ affected_host }}"
  become: true
  tasks:
    - name: Check for failed systemd services
      ansible.builtin.shell:
        cmd: "systemctl list-units --state=failed --no-pager"
      register: failed_services

    - name: Collect recent error logs
      ansible.builtin.command:
        cmd: "journalctl --since '2 hours ago' --priority=err --no-pager"
      register: recent_errors

    - name: Check disk and memory usage
      ansible.builtin.setup:
        filter:
          - ansible_memtotal_mb
          - ansible_memfree_mb
          - ansible_mounts
```

**Step 3c: Analyze with Red Hat AI**

```yaml
- name: Analyze Azure alert with Red Hat AI
  hosts: localhost
  tasks:
    - name: Build enriched prompt
      ansible.builtin.set_fact:
        enriched_prompt: |
          An Azure Monitor alert fired: {{ alert_name }}
          Severity: {{ severity }}
          Affected resource: {{ affected_resource }}
          Description: {{ description }}
          VM status: {{ vm_info.vms[0].power_state | default('unknown') }}
          Failed services: {{ hostvars[affected_host].failed_services.stdout | default('none') }}
          Recent errors: {{ hostvars[affected_host].recent_errors.stdout | default('none') | truncate(2000) }}

          Diagnose the root cause and recommend a remediation step.

    - name: Send to Red Hat AI for analysis
      redhat.ai.completion:
        base_url: "http://{{ rhelai_server }}:{{ rhelai_port }}"
        token: "{{ rhelai_token }}"
        prompt: "{{ enriched_prompt }}"
        model_path: "/root/.cache/instructlab/models/granite-8b-lab-v1"
      delegate_to: localhost
      register: ai_response
```

### 4. Notify and Remediate

**Operational Impact:** Low (notification) → **High** (remediation execution)

The enrichment workflow posts the AI analysis to your team's communication channel and -- depending on your maturity level -- either queues a remediation playbook for human approval or executes it automatically.

```yaml
    - name: Post AI diagnosis to Slack
      ansible.builtin.uri:
        url: "{{ slack_webhook_url }}"
        method: POST
        body_format: json
        body:
          text: |
            :rotating_light: *Azure Alert:* {{ alert_name }}
            *Severity:* {{ severity }}
            *Resource:* {{ affected_resource }}
            *AI Diagnosis:* {{ ai_response.choice_0_text }}

    - name: Create ServiceNow incident with enriched context
      servicenow.itsm.incident:
        instance:
          host: "{{ snow_instance }}"
          username: "{{ snow_username }}"
          password: "{{ snow_password }}"
        short_description: "Azure Alert: {{ alert_name }}"
        description: "AI Analysis: {{ ai_response.choice_0_text }}"
        priority: "{{ '1' if severity == 'Sev0' else '2' if severity == 'Sev1' else '3' }}"
      when: snow_instance is defined
```

From here, the remediation follows the same pattern as the [UC06 workshop remediation workflow](README-AIOps-Use-Case-06-Self-Healing-Infrastructure.md#3-remediation-workflow) -- **Automation code assistant** generates a playbook, it gets committed to Git, and a Job Template is created for execution.

<h2 id="validation"></h2>

## Validation

| Stage | What to Verify | Success Indicator |
|-------|---------------|-------------------|
| **1. Azure Event → EDA** | Message arrives in queue and EDA consumes it | AAP shows the rulebook activation as **Running**; event log shows the Azure alert payload |
| **2. Enrichment Workflow** | AI analyzed the alert and notifications were sent | Workflow Visualizer shows all nodes green; Slack/ITSM received the AI diagnosis |
| **3. Remediation Workflow** | Playbook was generated and committed | New playbook file exists in the Git repository; Job Template was created |
| **4. Execute Remediation** | The fix was applied | Azure resource returns to healthy state; Azure Monitor alert auto-resolves |

**Quick validation test** -- Send a test message to the Service Bus queue using the Azure CLI:

```bash
az servicebus queue send \
  --namespace-name aiops-events \
  --queue-name infrastructure-alerts \
  --resource-group rg-aiops \
  --body '{
    "data": {
      "essentials": {
        "alertRule": "Test High CPU Alert",
        "severity": "Sev2",
        "alertTargetIDs": ["/subscriptions/xxx/resourceGroups/rg-aiops/providers/Microsoft.Compute/virtualMachines/web01"],
        "description": "CPU usage exceeded 95% for 5 minutes",
        "firedDateTime": "2026-02-18T14:30:00Z"
      }
    }
  }'
```

### Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| EDA rulebook is active but no events are received | Connection string is wrong or queue name doesn't match | Verify `conn_str` has `Listen` permissions; check queue name matches exactly |
| EDA receives event but condition doesn't match | Azure alert payload structure differs from expected schema | Use `debug` action in the rulebook to print `event.body` and compare against your conditions |
| Enrichment workflow runs but AI response is empty | Prompt is too vague or AI endpoint is unreachable | Verify the Red Hat AI server is running; test with a simple prompt first |
| Azure VM info retrieval fails | Azure credentials in AAP are expired or lack permissions | Verify the Azure Service Principal credential; test with `azure.azcollection.azure_rm_virtualmachine_info` |
| Messages pile up in the dead-letter queue | EDA consumer is crashing or message format is unexpected | Check EDA logs in AAP; inspect dead-letter messages in Azure Portal for error details |

<h2 id="maturity-path"></h2>

## Maturity Path

| Maturity | Approach | How It Works | AI Role |
|----------|----------|-------------|---------|
| <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f6b6.png" width="20" style="vertical-align:text-bottom;"> **Crawl** | Alert Enrichment | Azure alert → Service Bus → EDA → AI diagnoses → enriched context posted to Slack/ITSM → **human investigates and remediates** | Read-only: AI interprets, humans act |
| <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f3c3.png" width="20" style="vertical-align:text-bottom;"> **Walk** | Curated Remediation | Azure alert → Service Bus → EDA → AI diagnoses → AI **selects a pre-approved playbook** → human approves → playbook executes | AI selects from existing automation |
| <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f680.png" width="20" style="vertical-align:text-bottom;"> **Run** | Auto-Remediation | Azure alert → Service Bus → EDA → AI diagnoses → **Automation code assistant generates a remediation playbook** → policy engine validates → playbook executes | AI generates new automation within policy boundaries |

> **Start with Crawl.**
>
> Route Azure Monitor alerts to Service Bus and deploy the EDA rulebook and enrichment workflow first. Let your team see AI-enriched Azure alerts in Slack for a few weeks before adding automated remediation. This builds confidence in the pipeline and catches edge cases early.

## Summary

With Azure Service Bus connected to Event-Driven Ansible, your Azure monitoring alerts become the trigger for automated enrichment and remediation. Instead of engineers manually triaging every Azure Monitor alert, events flow through Service Bus into an AIOps pipeline that diagnoses root cause with AI and remediates with Ansible -- reducing MTTR and bridging the gap between Azure's cloud monitoring and your operational automation, whether the affected systems are in Azure, on-prem, or hybrid.

---

<h2 id="related-guides"></h2>

## Related Guides

- <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f4cb.png" width="20" style="vertical-align:text-bottom;"> **AIOps reference architecture:** [AIOps automation with Ansible](README-AIOps.md) -- curated MCP selection at Walk, workshop codegen at Run, and the Crawl/Walk/Run maturity model.
- <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f50d.png" width="20" style="vertical-align:text-bottom;"> **Using Splunk as the trigger?** See [Triggering Automated Remediation from Splunk Alerts](README-AIOps-Splunk.md) for connecting Splunk alerts to the same AIOps pipeline.
- <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f4a1.png" width="20" style="vertical-align:text-bottom;"> **Looking for ServiceNow integration?** See [Unlock AIOps with ServiceNow LEAP and Ansible MCP server](README-AIOps-ServiceNow.md) for LEAP/MCP-driven remediation and related ITSM patterns (see also [KB 7127603](https://access.redhat.com/articles/7127603)).
- <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f9e0.png" width="20" style="vertical-align:text-bottom;"> **Need to deploy the AI backend?** See [AI Infrastructure automation with Ansible](README-IA.md) for automating Red Hat AI provisioning with the `infra.ai` and `redhat.ai` collections.
- <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f4e1.png" width="20" style="vertical-align:text-bottom;"> **New to Event-Driven Ansible?** See [Get started with EDA (Ansible Rulebook)](https://access.redhat.com/articles/7136720) for the fundamentals of rulebooks, event sources, and actions.

---

<span class="guide-closing-logo-set">
<img class="guide-closing-logo guide-closing-logo--light" src="assets/images/logos/aap_logo.png" alt="Red Hat Ansible Automation Platform">
<img class="guide-closing-logo guide-closing-logo--dark" src="assets/images/logos/redhat-ansible-logo.svg" alt="" aria-hidden="true">
</span>
{% endraw %}
