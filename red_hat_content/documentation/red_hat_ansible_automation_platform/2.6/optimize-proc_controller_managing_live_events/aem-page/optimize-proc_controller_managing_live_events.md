+++
title = "Manage live event streams to the UI - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/optimize-proc_controller_managing_live_events"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/optimize-assembly_controller_improving_performance/", "Tune automation controller to improve performance"]]
category = "Optimize"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/optimize-proc_controller_managing_live_events/aem-page/optimize-proc_controller_managing_live_events.html"
last_crumb = "Manage live event streams to the UI"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Manage live event streams to the UI"
oversized = "false"
page_slug = "optimize-proc_controller_managing_live_events"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/optimize-proc_controller_managing_live_events"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/optimize-proc_controller_managing_live_events/toc/toc.json"
type = "aem-page"
+++

# Manage live event streams to the UI

By default, automation controller streams live events to the user interface (UI) for jobs that are running.

## About this task

Events are sent to any node where there is a UI client subscribed to a job. This task is expensive, and becomes more expensive as the number of events that the cluster is producing increases and the number of control nodes increases, because all events are broadcast to all nodes regardless of how many clients are subscribed to particular jobs.

## Procedure

 To reduce the overhead of displaying live events in the UI, administrators can choose to either:

- Disable live streaming events.
- Reduce the number of events shown per second or before truncating or hiding events in the UI.

## Results

When you disable live streaming of events, they are only loaded on hard refresh to a job’s output detail page. When you reduce the number of events shown per second, this limits the overhead of showing live events, but still provides live updates in the UI without a hard refresh.

## Disable live streaming events

You can disable live streaming events in automation controller to reduce system load or for troubleshooting purposes.

### Procedure

 Disable live streaming events by using one of the following methods:

1.  In the API, set `UI_LIVE_UPDATES_ENABLED` to **False**.
2.  In the navigation panel, select Settings> (and then)Automation Execution> (and then)System.   1. Click Edit.
  2. Set the **Enable Activity Stream** option to **Off**.

## Settings to modify rate and size of events

If your system generates a large number of events, the live streaming of events to the user interface (UI) can cause performance issues. You can disable live streaming of events or reduce the number of events that are displayed in the UI by modifying the following settings.

If you cannot disable live streaming of events because of their size, reduce the number of events that are displayed in the UI. You can use the following settings to manage how many events are displayed:

**Settings available for editing in the UI or API**:

- `EVENT_STDOUT_MAX_BYTES_DISPLAY`: Maximum amount of `stdout` to display (as measured in bytes). This truncates the size displayed in the UI. The default is 1024 bytes. Minimum = 0.
- `MAX_WEBSOCKET_EVENT_RATE`: Number of events to send to clients per second. Default is 30 messages/second. Minimum = 0 (no limit).


**Settings available by using file based settings**:

- `MAX_UI_JOB_EVENTS`: Number of events to display before truncating.This setting hides the rest of the events in the list. Default value is 4000. Minimum = 100. Set `hidden=True`.
- `MAX_EVENT_RES_DATA`: The maximum size of the ansible callback event’s "res" data structure. The "res" is the full "result" of the module. When the maximum size of ansible callback events is reached, then the remaining output will be truncated. Default value is 700000 bytes.
- `LOCAL_STDOUT_EXPIRE_TIME`: The amount of time before a `stdout` file is expired and removed locally. They can be regenerated on demand if downloaded again. The default value is 25992000 seconds (30 days).
