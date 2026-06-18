# Generate dynamic data from external sources with inventory plugins

Automation controller uses inventory plugins to dynamically generate inventory data from external sources. These plugins enable automation controller to integrate with cloud providers, virtualization platforms, and other external systems to retrieve up-to-date information about managed nodes.

Inventory updates use dynamically-generated YAML files which are parsed by their inventory plugin. In automation controller, you can provide the inventory plugin configuration directly to automation controller using the inventory source `source_vars` for the following inventory sources:

-  [Amazon Web Services EC2](/documentation/en-us/red_hat_ansible_automation_platform/2.7/troubleshoot-assembly_ag_controller_troubleshooting#controller-ec2-vpc-instances "By default, automation controller only shows instances in a VPC that have an Elastic IP (EIP) associated with them.")
-  [Google Compute Engine](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_add_source#proc-controller-inv-source-gce "Learn how to configure a Google-sourced inventory:")
-  [Microsoft Azure Resource Manager](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_add_source#proc-controller-azure-resource-manager "Use the following procedure to configure an Microsoft Azure Resource Manager-sourced inventory.")
-  [VMware vCenter](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_add_source#proc-controller-inv-source-vm-vcenter "You can configure automation controller to synchronize inventory from a VMware vCenter server. You can manage virtual machines as part of your automation workflows.")
-  [VMWare ESXI](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_add_source#proc-controller-inv-source-vm-esxi "Learn how to configure a VMWare ESXi sourced inventory.")
-  [Red Hat Satellite 6](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_add_source#proc-controller-inv-source-satellite "automation controller can integrate with Red Hat Satellite 6 as a dynamic inventory source.")
-  Red Hat Lightspeed
-  [OpenStack](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_add_source#proc-controller-inv-source-openstack "You can create an inventory source that uses the OpenStack inventory plugin to dynamically generate inventory from your OpenStack cloud.")
-  [Red Hat Virtualization](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_add_source#proc-controller-inv-source-rh-virt "Learn how to configure a Red Hat virtualization-sourced inventory.")
-  [Red Hat Ansible Automation Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_add_source#proc-controller-inv-source-aap "An inventory that is sourced from Red Hat Ansible Automation Platform uses the Red Hat Ansible Automation Platform inventory plugin to gather inventory data from the Red Hat Ansible Automation Platform platform.")
-  [Terraform State](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_add_source#proc-controller-inv-source-terraform "Use the following procedure to create a Terraform State inventory source.")
-  [OpenShift Virtualization](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_add_source#proc-controller-inv-source-open-shift-virt "Learn how to add an OpenShift Virtualization inventory source to an existing inventory.")


Newly created configurations for inventory sources contain the default plugin configuration values. If you want your newly created inventory sources to match the output of a legacy source, you must apply a specific set of configuration values for that source. To ensure backward compatibility, automation controller uses "templates" for each of these sources to force the output of inventory plugins into the legacy format.

For more information about sources and their templates, see [Supported inventory plugin templates](/documentation/en-us/red_hat_ansible_automation_platform/2.7/configure-controller_inventory_templates#controller-inventory-templates "After upgrade to 4.x, existing configurations are migrated to the new format that produces an inventory output compatible with earlier versions. Use the following templates to aid in migrating your inventories to the new style inventory plugin output.").

`source_vars` that contain `plugin: xxx.yyy.zzz` as a top-level key are replaced with the fully-qualified inventory plugin name at runtime based on the `InventorySource` source.

For example, if you select `ec2` for the `InventorySource` then, at run time, the plugin is set to `amazon.aws.aws_ec2`.

## Add permissions to inventories

Use the following procedure to add permissions to inventories:

### About this task

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Inventories.
2.  Select a template, and in the **User Access** or **Team Access** tab, click Add roles.
3.  Select a user or team to add and click Next.
4.  Select the checkbox next to a name to add one or more users or teams from the list as members.
5.  Click Next.
6.  Select the roles you want the selected users or teams to have. Different resources have different options available.
7.  Click Finish to apply the roles to the selected users or teams and to add them as members. The updated roles assigned for each user and team are displayed.

## Remove a permission

Learn how to remove specific permissions from a user associated with a resource. Disassociating a role restricts a user’s access to functionalities or data they no longer need.

### Procedure

To remove roles for a particular user, click the ![Disassociate](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/disassociate.png) icon next to its resource. This launches a confirmation window, asking you to confirm the disassociation.

## Add groups to inventories

You can add groups to standard inventories in automation controller to organize hosts.

### About this task

Inventories are divided into groups, which can contain hosts and other groups. Groups are only applicable to standard inventories and are not a configurable directly through a Smart Inventory. You can associate an existing group through hosts that are used with standard inventories.

The following actions are available for standard inventories:

- Create a new Group
- Create a new Host
- Run a command on the selected Inventory
- Edit Inventory properties
- View activity streams for Groups and Hosts
- Obtain help building your Inventory


Note:

Inventory sources are not associated with groups. Spawned groups are top-level and can still have child groups. All of these spawned groups can have hosts.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Inventories.
2.  Select the Inventory name you want to add groups to.
3.  In the Inventory **Details** page, select the **Groups** tab.
4.  Click Create group.
5.  Enter the appropriate details:

- **Name**: Required
- Optional: **Description**: Enter a description as appropriate.
- Optional: **Variables**: Enter definitions and values to be applied to all hosts in this group. Enter variables by using either JSON or YAML syntax. Use the radio button to toggle between the two.

6.  Click Create group.

### Results

When you have added a group to a template, the Group **Details** page is displayed.

## Add groups within groups

You can create a hierarchy of groups by adding groups within groups. This allows you to create nested groupings of hosts for easier management and organization.

### About this task

When you have added a group to a template, the Group **Details** page is displayed.

### Procedure

1.  Select the **Related Groups** tab.
2.  Click Add existing group to add a group that already exists in your configuration or Create group to create a new group.
3.  If creating a new group, enter the appropriate details into the required and optional fields:

- **Name** (required):
- Optional: **Description**: Enter a description as appropriate.
- Optional: **Variables**: Enter definitions and values to be applied to all hosts in this group. Enter variables using either JSON or YAML syntax. Use the radio button to toggle between the two.

4.  Click Create group.
5.  The **Create group** window closes and the newly created group is displayed as an entry in the list of groups associated with the group that it was created for.

### What to do next

If you select to add an existing group, available groups appear in a separate selection window. When you select a group, it is displayed in the list of groups associated with the group.

- To configure additional groups and hosts under the subgroup, click the name of the subgroup from the list of groups and repeat the steps listed before.

## View or edit inventory groups

The groups list view displays all your inventory groups, or you can filter it to only display the root groups. An inventory group is considered a root group if it is not a subset of another group.

You can delete a subgroup without concern for dependencies, because automation controller looks for dependencies such as child groups or hosts. If any exist, a confirmation window displays for you to select whether to delete the root group and all of its subgroups and hosts; or to promote the subgroups so they become the top-level inventory groups, along with their hosts.

## Add hosts to inventory groups

You can add hosts to an inventory either by creating new hosts or by associating existing hosts with the inventory.

### About this task

You can configure hosts for the inventory and for groups and groups within groups.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Inventories.
2.  Select the inventory name you want to add groups to.
3.  In the Inventory **Details** page, select the **Hosts** tab.
4.  Click Create host.
5.  Select whether to add a host that already exists in your configuration or create a new host.
6.  If creating a new host, set the toggle to **On** to include this host while running jobs.
7.  Enter the appropriate details:

- **Name** (required):

- Optional: **Description**: Enter a description as appropriate.

- Optional: **Variables**: Enter definitions and values to be applied to all hosts in this group, as in the following example:

```
{
ansible_user : <username to ssh into>
ansible_ssh_pass : <password for the username>
ansible_become_pass: <password for becoming the root>
}
```
Enter variables by using either JSON or YAML syntax. Use the radio button to toggle between the two.

8.  Click Create host.
9.  The **Create host** window closes and the newly created host is displayed in the list of hosts associated with the group that it was created for. If you select to add an existing host, available hosts appear in a separate selection window.

When you select a host, it is displayed in the list of hosts associated with the group.

10.  You can disassociate a host from this screen by selecting the host and clicking the ![Disassociate](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/disassociate.png) icon.  Note:
You can also run ad hoc commands from this screen. For more information, see [Running Ad Hoc commands](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_run_ad_hoc_commands#proc-controller-run-ad-hoc-commands "Learn how to run ad hoc commands against hosts in an inventory.").

11.  To configure additional groups for the host, click the name of the host from the list of hosts. This opens the **Details** tab of the selected host.

12.  Select the **Groups** tab to configure groups for the host.
13.  Click Associate groups to associate the host with an existing group. Available groups appear in a separate selection window.
14.  Select the groups to associate with the host and click Confirm. When a group is associated, it is displayed in the list of groups associated with the host.

15.  If you used a host to run a job, you can view details about those jobs in the **Completed Jobs** tab of the host.
16.  Click Expanded to view details about each job.  Note:
You can create hosts in bulk by using the newly added endpoint in the API, `/api/v2/bulk/host_create`. This endpoint accepts JSON and you can specify the target inventory and a list of hosts to add to the inventory. These hosts must be unique within the inventory. Either all hosts are added, or an error is returned indicating why the operation was not able to complete. Use the **OPTIONS** request to return the relevant schema.
