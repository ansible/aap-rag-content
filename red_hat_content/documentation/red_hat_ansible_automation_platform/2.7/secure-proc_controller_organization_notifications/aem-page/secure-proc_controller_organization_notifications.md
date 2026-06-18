+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-proc_controller_organization_notifications"
template = "docs/aem-title.html"
title = "Assign notifiers and execution environments to organizations - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_managing_access/", "Manage access with role-based access control"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-proc_controller_organization_notifications/aem-page/secure-proc_controller_organization_notifications.html"
last_crumb = "Assign notifiers and execution environments to organizations"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Assign notifiers and execution environments to organizations"
oversized = "false"
page_slug = "secure-proc_controller_organization_notifications"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-proc_controller_organization_notifications"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-proc_controller_organization_notifications/toc/toc.json"
type = "aem-page"
+++

# Assign notifiers and execution environments to organizations

When automation controller is enabled on the platform, you can review any notifier integrations you have set up and manage their settings within the organization resource.

## Procedure

1.  From the navigation panel, select Access Management> (and then)Organizations.
2.  From the **Organizations** list view, select the organization whose notifications you want to manage.
3.  Select the **Notification** tab.
4.  Use the toggles to enable or disable the notifications to use with your particular organization.
5.  If no notifiers have been set up, select Automation Execution> (and then)Administration> (and then)Notifiers from the navigation panel.

## Work with execution environments

When automation controller is enabled on the platform, you can review any execution environments you have set up and manage their settings within the organization resource.

### About this task

For more information about execution environments, see [Define, create, and build execution environments](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-define__create__and_build_execution_environments "Run automation consistently across nodes with execution environments, which are container images that contain everything you need to run your automation.").

### Procedure

1.  From the navigation panel, select Access Management> (and then)Organizations.
2.  From the Organizations list view, select the organization whose execution environments you want to manage.
3.  Select the **Execution Environments** tab.
4.  If no execution environments are available, click Create execution environment to create one. Alternatively, you can create an execution environment from the navigation panel by selecting Automation Execution> (and then)Infrastructure> (and then)Execution Environments.
5.  Click Create execution environment. Note:
      After creating a new execution environments, return to Access Management> (and then)Organizations and select the organization in which you created the execution environment to update the list on that tab.

6.  Select the execution environments to use with your particular organization.
