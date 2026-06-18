+++
template = "docs/aem-title.html"
title = "Use awx-manage to access automation controller information - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_controller_awx_manage_utility"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_controller_awx_manage_utility/", "Use awx-manage to access automation controller information"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-assembly_controller_awx_manage_utility/aem-page/administer-assembly_controller_awx_manage_utility.html"
last_crumb = "Use awx-manage to access automation controller information"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Use awx-manage to access automation controller information"
oversized = "false"
page_slug = "administer-assembly_controller_awx_manage_utility"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/administer-assembly_controller_awx_manage_utility"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-assembly_controller_awx_manage_utility/toc/toc.json"
type = "aem-page"
+++

# Use awx-manage to access automation controller information

Use the `awx-manage` utility to access detailed internal information of automation controller. Commands for `awx-manage` must run as the `awx` user only.

## Inventory Import

`awx-manage` is a mechanism by which an automation controller administrator can import inventory directly into automation controller.

To use `awx-manage` properly, you must first create an inventory in automation controller to use as the destination for the import.

For help with `awx-manage`, run the following command:

 `awx-manage inventory_import [--help]`

The `inventory_import` command synchronizes an automation controller inventory object with a text-based inventory file, dynamic inventory script, or a directory of one or more, as supported by core Ansible.

When running this command, specify either an `--inventory-id` or `--inventory-name`, and the path to the Ansible inventory source (`--source`).

 `awx-manage inventory_import --source=/ansible/inventory/ --inventory-id=1`

By default, inventory data already stored in automation controller blends with data from the external source.

To use only the external data, specify `--overwrite`.

To specify that any existing hosts get variable data exclusively from the `--source`, specify `--overwrite_vars`.

The default behavior adds any new variables from the external source, overwriting keys that already exist, but preserving any variables that were not sourced from the external data source.

 `awx-manage inventory_import --source=/ansible/inventory/ --inventory-id=1 --overwrite`

Note:

Edits and additions to Inventory host variables persist beyond an inventory synchronization as long as `--overwrite_vars` is not set.

## Cleanup of old data

`awx-manage` has a variety of commands used to clean old data from automation controller.

Automation controller administrators can use the automation controller **Management Jobs** interface for access or use the command line.

-  `awx-manage cleanup_jobs [--help]`     This permanently deletes the job details and job output for jobs older than a specified number of days.

-  `awx-manage cleanup_activitystream [--help]`     This permanently deletes any activity stream data older than a specific number of days.

## Cluster management

This section describes how to manage a automation controller cluster by provisioning and deprovisioning cluster instances. Automation controller uses the `awx-manage` command-line tool to manage cluster instances.

For more information about the `awx-manage provision_instance` and `awx-manage deprovision_instance` commands, see [Clustering](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/controller-clustering).

Important:

Do not run other `awx-manage` commands unless instructed by Ansible Support.

## Analytics gathering

Use this command to gather analytics on-demand outside of the predefined window (the default is 4 hours):

 `$ awx-manage gather_analytics --ship`

For customers with disconnected environments who want to collect usage information about unique hosts automated across a time period, use this command:

 `awx-manage host_metric --since YYYY-MM-DD --json`

The `--since` parameter is optional.

The `--json` flag specifies the output format and is optional.
