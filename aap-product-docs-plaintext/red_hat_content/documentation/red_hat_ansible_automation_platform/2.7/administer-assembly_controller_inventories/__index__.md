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
