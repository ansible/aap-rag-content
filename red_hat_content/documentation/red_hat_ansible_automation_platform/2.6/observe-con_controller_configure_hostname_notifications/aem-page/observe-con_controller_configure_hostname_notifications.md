+++
title = "Advanced notification settings - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/observe-con_controller_configure_hostname_notifications"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/observe-assembly_ug_controller_notifications/", "Understand and configure notifications"]]
category = "Observe"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/observe-con_controller_configure_hostname_notifications/aem-page/observe-con_controller_configure_hostname_notifications.html"
last_crumb = "Advanced notification settings"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Advanced notification settings"
oversized = "false"
page_slug = "observe-con_controller_configure_hostname_notifications"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/observe-con_controller_configure_hostname_notifications"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/observe-con_controller_configure_hostname_notifications/toc/toc.json"
type = "aem-page"
+++

# Advanced notification settings

Automation controller uses the system hostname for notifications by default.

In Settings > Automation Execution > System, you can replace the default value in the **Base URL of the service** field with your preferred hostname to change the notification hostname.

Refreshing your license also changes the notification hostname. New installations of automation controller do not have to set the hostname for notifications.

## Create custom notifications

You can [customize the text content](/documentation/en-us/red_hat_ansible_automation_platform/2.6/observe-con_controller_configure_hostname_notifications#controller-attributes-custom-notifications "Learn about the list of supported job attributes and the proper syntax for constructing the message text for notifications.") of each [Notification type](/documentation/en-us/red_hat_ansible_automation_platform/2.6/observe-proc_controller_create_notification_template#controller-notification-types "Automation controller supports multiple notification types that you can use to send notifications about job status and other events.") on the notification form.

### About this task

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Administration> (and then)Notifiers.
2.  Click Create notifier.
3.  Choose a notification type from the **Type** list.
4.  Enable **Customize messages** by using the toggle.  
![Customize notification](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/ug-notification-template-customize.png)  
5.  You can provide a custom message for various job events, such as the following:

  -  **Start message body**

  -  **success message body**

  -  **Error message body**

  -  **Workflow approved body**

  -  **Workflow denied message body**

  -  **Workflow pending message body**

  -  **Workflow timed out message body** The message forms vary depending on the type of notification that you are configuring. For example, messages for Email and PagerDuty notifications appear to be a typical email, with a body and a subject, in which case, automation controller displays the fields as **Message** and **Message Body**. Other notification types only expect a **Message** for each type of event.

         The **Message** fields are pre-populated with a template containing a top-level variable, `job` coupled with an attribute, such as `id` or `name`. Templates are enclosed in curly brackets and can draw from a fixed set of fields provided by automation controller, shown in the pre-populated message fields:

         This pre-populated field suggests commonly displayed messages to a recipient who is notified of an event. You can customize these messages with different criteria by adding your own attributes for the job as needed. Custom notification messages are rendered using Jinja; the same templating engine used by Ansible playbooks.

         Messages and message bodies have different types of content, as the following points outline:

  - Messages are always just strings, one-liners only. New lines are not supported.

  - Message bodies are either a dictionary or a block of text:
    * The message body for Webhooks and PagerDuty uses dictionary definitions. The default message body for these is `{{ job_metadata }}`, you can either leave that as it is or provide your own dictionary.

    * The message body for email uses a block of text or a multi-line string. The default message body is:

```
{{ job_friendly_name }} #{{ job.id }} had status {{ job.status }}, view details at {{ url }} {{ job_metadata }}
```
            You can edit this text leaving `{{ job_metadata }}` in, or drop `{{ job_metadata }}`. Since the body is a block of text, it can be any string you want. `{{ job_metadata }}` is rendered as a dictionary containing fields that describe the job being executed. In all cases, `{{ job_metadata }}` includes the following fields:

      + `id`

      + `name`

      + `url`

      + `created_by`

      + `started`

      + `finished`

      + `status`

      + `traceback`                 You cannot query individual fields within `{{ job_metadata }}`. When you use `{{ job_metadata }}` in a notification template, all data is returned.

                The resulting dictionary looks like the following:

```
{"id": 18,
 "name": "Project - Space Procedures",
 "url": "https://host/#/jobs/project/18",
 "created_by": "admin",
 "started": "2019-10-26T00:20:45.139356+00:00",
 "finished": "2019-10-26T00:20:55.769713+00:00",
 "status": "successful",
 "traceback": ""
}
```
                If `{{ job_metadata }}` is rendered in a job, it includes the following additional fields:

      + `inventory`

      + `project`

      + `playbook`

      + `credential`

      + `limit`

      + `extra_vars`

      + `hosts`                 The resulting dictionary is similar to the following:

```
{"id": 12,
 "name": "JobTemplate - Launch Rockets",
 "url": "https://host/#/jobs/playbook/12",
 "created_by": "admin",
 "started": "2019-10-26T00:02:07.943774+00:00",
 "finished": null,
 "status": "running",
 "traceback": "",
 "inventory": "Inventory - Fleet",
 "project": "Project - Space Procedures",
 "playbook": "launch.yml",
 "credential": "Credential - Mission Control",
 "limit": "",
 "extra_vars": "{}",
 "hosts": {}
}
```
                If `{{ job_metadata }}` is rendered in a workflow job, it includes the following additional field:

      + `body` (This enumerates the nodes in the workflow job and includes a description of the job associated with each node)                 The resulting dictionary is similar to the following:

```
{"id": 14,
 "name": "Workflow Job Template - Launch Mars Mission",
 "url": "https://host/#/workflows/14",
 "created_by": "admin",
 "started": "2019-10-26T00:11:04.554468+00:00",
 "finished": "2019-10-26T00:11:24.249899+00:00",
 "status": "successful",
 "traceback": "",
 "body": "Workflow job summary:

                node #1 spawns job #15, \"Assemble Fleet JT\", which finished with status successful.
         node #2 spawns job #16, \"Mission Start approval node\", which finished with status successful.\n
         node #3 spawns job #17, \"Deploy Fleet\", which finished with status successful."
}
```
                If you create a notification template that uses invalid syntax or references unusable fields, an error message displays indicating the nature of the error. If you delete a notification’s custom message, the default message is shown in its place.

         Important:
                        If you save the notifications template without editing the custom message (or edit and revert back to the default values), the **Details** screen assumes the defaults and does not display the custom message tables. If you edit and save any of the values, the entire table displays in the **Details** screen.

## Enable and disable notifications

You can set up notifications to notify you when a specific job starts, and on the success or failure at the end of the job run. Note the following behaviors:

- If a workflow job template has notification on start enabled, and a job template within that workflow also has notification on start enabled, you receive notifications for both.
- You can enable notifications to run on many job templates within a workflow job template.
- You can enable notifications to run on a sliced job template start and each slice generates a notification.
- When you enable a notification to run on job start, and that notification gets deleted, the job template continues to run, but results in an error message.


You can enable notifications on job start, job success, and job failure, or a combination of these, from the **Notifications** tab of the **Details** page for the following resources:

- Job Templates
- Workflow Templates
- Projects


For workflow templates that have approval nodes, in addition to **Start**, **Success**, and **Failure**, you can enable or disable certain approval-related events:

## Reset TOWER_URL_BASE

Automation controller determines how the base URL (`TOWER_URL_BASE`) is defined by looking at an incoming request and setting the server address based on that incoming request.

### About this task

Automation controller takes settings values from the database first. If no settings values are found, it uses the values from the settings files. If you post a license by navigating to the automation controller host’s IP address, the posted license is written to the settings entry in the database.

Use the following procedure to reset `TOWER_URL_BASE` if the wrong address has been picked up:

### Procedure

1.  From the navigation panel, select Settings> (and then)System.
2.  Click Edit.
3.  Enter the address in the **Base URL of the service** field for the DNS entry you want to appear in notifications.

## Notifications API

The Notifications API enables you to trigger notifications for various events in Automation controller. The Notifications API provides endpoints to trigger notifications for job events, such as when a job starts, succeeds, or fails.

Use the `started`, `success`, or `error` endpoints:

```
/api/v2/organizations/N/notification_templates_started/
/api/v2/organizations/N/notification_templates_success/
/api/v2/organizations/N/notification_templates_error/
```
Additionally, the `../../../N/notification_templates_started` endpoints have `GET` and `POST` actions for:

- Organizations
- Projects
- Inventory Sources
- Job Templates
- System Job Templates
- Workflow Job Templates

## Custom notification attributes

Learn about the list of supported job attributes and the proper syntax for constructing the message text for notifications.
