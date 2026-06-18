+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-background_task_processing_for_event_driven_ansible"
title = "Background task processing for Event-Driven Ansible - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_eda_user_guide_overview/", "Trigger automation from events with Event-Driven Ansible"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-background_task_processing_for_event_driven_ansible/aem-page/administer-background_task_processing_for_event_driven_ansible.html"
last_crumb = "Background task processing for Event-Driven Ansible"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Background task processing for Event-Driven Ansible"
oversized = "false"
page_slug = "administer-background_task_processing_for_event_driven_ansible"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/administer-background_task_processing_for_event_driven_ansible"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-background_task_processing_for_event_driven_ansible/toc/toc.json"
type = "aem-page"
+++

# Background task processing for Event-Driven Ansible

In Ansible Automation Platform 2.7, Event-Driven Ansible controller uses `dispatcherd`, a PostgreSQL-based task broker, for all background task processing. Dispatcherd replaces the previous Redis-based task queue and uses the PostgreSQL pg_notify feature as its message transport.

This transition simplifies the platform architecture by eliminating Redis as an infrastructure dependency for Event-Driven Ansible controller.

`Dispatcherd` requires a connection to the same PostgreSQL instance used by the Event-Driven Ansible controller. A separate message broker, such as Redis, is no longer required.

## `Dispatcherd` worker types

`Dispatcherd` manages the following worker types to handle background operations:

- **Default worker:** Processes system tasks, including project imports, project synchronizations, analytics gathering, and resource synchronization.
- **Activation worker:** Processes rulebook activation tasks, such as container creation, process monitoring, heartbeat checks, and restart policy enforcement. In multi-node deployments, each node runs dedicated activation workers listening on node-specific queues (for example, `activation-node1`).

## Impact of service unavailability

If the task workers or the PostgreSQL database become unavailable, the following operations are disabled:

- Creating or syncing a project.
- Creating, enabling, or disabling an activation.
- Deleting or restarting an activation (unless using the **Force** option).

## Verifying worker status

To verify that the `dispatcherd` workers are active, you must run the following management command:

Bash

```
aap-eda-manage dispatcherctl alive
```
