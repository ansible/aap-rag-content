+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_controller_inventories"
template = "docs/aem-title.html"
title = "Define automation target hosts in your inventory files - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_controller_inventories/", "Define automation target hosts in your inventory files"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-assembly_controller_inventories/aem-page/administer-assembly_controller_inventories.html"
last_crumb = "Define automation target hosts in your inventory files"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Define automation target hosts in your inventory files"
oversized = "false"
page_slug = "administer-assembly_controller_inventories"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/administer-assembly_controller_inventories"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-assembly_controller_inventories/toc/toc.json"
type = "aem-page"
+++

# Define automation target hosts in your inventory files

Ansible Automation Platform works against a list of managed nodes or hosts in your infrastructure that are logically organized, using an inventory file. The installer inventory can specify your installation scenario and describe host deployments to Ansible.

An inventory file enables Ansible to manage a large number of hosts with a single command. Inventories also help you automate more efficiently by reducing the number of command line options you have to specify. Inventories are divided into groups and these groups contain the hosts. Groups can be sourced manually, by entering host names into automation controller, or from one of its supported cloud providers.

 Note:

If you have a custom dynamic inventory script, or a cloud provider that is not yet supported natively in automation controller, you can also import that into automation controller.

From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Inventories. The **Inventories** window displays a list of the inventories that are currently available.

The **Inventory details** page includes:

- **Name**: The inventory name.

-  **Status** The statuses are:

  * **Success**: When the inventory source sync completed successfully
  * **Disabled**: No inventory source added to the inventory
  * **Error**: When the inventory source sync completed with error

- **Type**: Identifies whether it is a standard inventory, a Smart inventory, or a constructed inventory.

- **Organization**: The organization to which the inventory belongs. The following actions are available for the selected inventory:
  * **Edit**![Edit](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/leftpencil.png): Edit the properties for the selected inventory
  * **Duplicate**![Copy](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/copy.png): Makes a copy of an existing inventory as a template for creating a new one
  * **Delete inventory**: Delete the selected inventory

Click the Inventory name to display the **Details** page for the selected inventory, which shows the inventory’s groups and hosts.
