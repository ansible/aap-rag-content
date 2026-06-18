+++
title = "Understand and configure notifications - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/observe-assembly_ug_controller_notifications"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/observe-assembly_ug_controller_notifications/", "Understand and configure notifications"]]
category = "Observe"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/observe-assembly_ug_controller_notifications/aem-page/observe-assembly_ug_controller_notifications.html"
last_crumb = "Understand and configure notifications"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Understand and configure notifications"
oversized = "false"
page_slug = "observe-assembly_ug_controller_notifications"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/observe-assembly_ug_controller_notifications"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/observe-assembly_ug_controller_notifications/toc/toc.json"
type = "aem-page"
+++

# Understand and configure notifications

A Notification Type such as Email, Slack or a Webhook, is an instance of a Notification Template, and has a name, description and configuration defined in the Notification template.

The following include examples of details needed to add a notification template:

- A username, password, server, and recipients are needed for an Email notification template
- The token and a list of channels are needed for a Slack notification template
- The URL and Headers are needed for a Webhook notification template


When a job fails, a notification is sent using the configuration that you define in the notification template.

The following shows the typical flow for the notification system:

- You create a notification template to the `REST API` at the `/api/v2/notification_templates endpoint`, either through the API or through the UI.
- You assign the notification template to any of the various objects that support it (all variants of job templates, organizations and projects) and at the appropriate trigger level for which you want the notification (started, success, or error). For example, you might want to assign a particular notification template to trigger when Job Template 1 fails. In this case, you associate the notification template with the job template at `/api/v2/job_templates/n/notification_templates_error` API endpoint.
- You can set notifications on job start and job end. Users and teams are also able to define their own notifications that can be attached to arbitrary jobs.

## Notification hierarchy

Automation controller uses a hierarchical notification system where notification templates can be defined at various levels, and lower-level objects can inherit templates from their parent objects.

Notification templates inherit templates defined on parent objects, such as the following:

- Job templates use notification templates defined for them. Additionally, they can inherit notification templates from the project used by the job template, and from the organization that it is listed under.
- Project updates use notification templates defined on the project and inherit notification templates from the organization associated with it.
- Inventory updates use notification templates defined on the organization that it is listed under.
- Ad hoc commands use notification templates defined on the organization that the inventory is associated with.

### Notification workflow

Automation controller can send notifications when jobs succeed or fail.

When a job succeeds or fails, the error or success handler pulls a list of relevant notifications. It then creates a notification object for each one, containing relevant details about the job and sends it to the destination. These include email addresses, slack channels, and SMS numbers.

These notification objects are available as related resources on job types (jobs, inventory updates, project updates), and also at `/api/v2/notifications`. You can also see what notifications have been sent from a notification template by examining its related resources.

If a notification fails, it does not impact the job associated with it or cause it to fail. The status of the notification can be viewed at its detail endpoint `/api/v2/notifications/<n>`.
