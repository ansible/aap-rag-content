+++
template = "docs/aem-title.html"
title = "Add a new inventory - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_adding_new_inventory"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_controller_inventories/", "Define automation target hosts in your inventory files"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-proc_controller_adding_new_inventory/aem-page/administer-proc_controller_adding_new_inventory.html"
last_crumb = "Add a new inventory"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Add a new inventory"
oversized = "false"
page_slug = "administer-proc_controller_adding_new_inventory"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/administer-proc_controller_adding_new_inventory"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-proc_controller_adding_new_inventory/toc/toc.json"
type = "aem-page"
+++

# Add a new inventory

To add a new inventory, you must configure permissions, groups, hosts, and sources, then view the completed jobs.

## About this task

## Procedure

1. From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Inventories. The **Inventories** window displays a list of the inventories that are currently available.
2. Click Create inventory, and select the type of inventory to create.
3. Enter the appropriate details into the following fields:

  - **Name**: Enter a name appropriate for this inventory.

  - Optional: **Description**: Enter an arbitrary description as appropriate.

  - **Organization**: Required. Choose among the available organizations.

  - Only applicable to Smart Inventories: **Smart host filter**: Populate the hosts for this inventory by using a search filter. For example "name__icontains=RedHat".

        These options are based on the organization you chose.

        Filters are similar to tags in that tags are used to filter certain hosts that contain those names. Therefore, to populate the **Smart host filter** field, specify a tag that has the hosts you want, not the hosts themselves.

        Filters are case-sensitive.

  - **Instance groups**: Select the instance group or groups for this inventory to run on. You can select many instance groups and sort them in the order that you want them run.

  - Optional: **Labels**: Supply labels that describe this inventory, so they can be used to group and filter inventories and jobs.

  - Only applicable to constructed inventories: **Input inventories**: Specify the source inventories to include in this constructed inventory. Empty groups from input inventories are copied into the constructed inventory.

  - Optional:(Only applicable to constructed inventories): **Cached timeout (seconds)**: Set the length of time you want the cache plugin data to timeout.

  - Only applicable to constructed inventories: **Verbosity**: Control the level of output that Ansible produces as the playbook executes related to inventory sources associated with constructed inventories. Select the verbosity from:

    * **Normal**
    * **Verbose**
    * **More verbose**
    * **Debug**
    * **Connection Debug**
    * **WinRM Debug**
      + **Verbose** logging includes the output of all commands.

      + **More verbose** provides more detail than **Verbose**.

      + **Debug** logging is exceedingly verbose and includes information about SSH operations that can be useful in certain support instances. Most users do not need to see debug mode output.

      + **Connection Debug** enables you to run SSH in verbose mode, providing debugging information about the SSH connection progress.

      + **WinRM Debug** used for verbosity specific to windows remote management                 Click the ![Expand](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/arrow.png) icon for information on **How to use the constructed inventory plugin**.

  - Only applicable to constructed inventories: **Limit**: Restricts the number of returned hosts for the inventory source associated with the constructed inventory. You can paste a group name into the limit field to only include hosts in that group. For more information, see the **Source vars** setting.

  - Only applicable to standard inventories: **Options**: Check the **Prevent Instance Group Fallback** option to enable only the instance groups listed in the **Instance Groups** field to run the job. If unchecked, all available instances in the execution pool are used based on the hierarchy described in [Control where a job runs](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_ug_controller_instance_groups#controller-control-job-run "Use instance groups to control job execution locations. While the controller automatically selects groups based on capacity, you can override this by associating groups with job templates, inventories, or organizations.").

  - **Variables** (**Source vars** for constructed inventories):
    * **Variables** Variable definitions and values to apply to all hosts in this inventory. Enter variables by using either JSON or YAML syntax. Use the radio button to toggle between the two.
    * **Source vars** for constructed inventories creates groups, specifically under the `groups` key of the data. It accepts Jinja2 template syntax, renders it for every host, makes a `true` or `false` evaluation, and includes the host in the group (from the key of the entry) if the result is `true`. This is particularly useful because you can paste that group name into the limit field to only include hosts in that group.

4. Click Create inventory.

## What to do next

After saving the new inventory, you can proceed with configuring permissions, groups, hosts, sources, and view completed jobs, if applicable to the type of inventory.

## Add permissions to inventories

Use the following procedure to add permissions to inventories:

### About this task

### Procedure

1. From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Inventories.
2. Select a template, and in the **User Access** or **Team Access** tab, click Add roles.
3. Select a user or team to add and click Next.
4. Select the checkbox next to a name to add one or more users or teams from the list as members.
5. Click Next.
6. Select the roles you want the selected users or teams to have. Different resources have different options available.
7. Click Finish to apply the roles to the selected users or teams and to add them as members. The updated roles assigned for each user and team are displayed.

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

If `controller_extra_settings=[{"setting": "ENHANCED_INPUT_VALIDATION_ENABLED", "value": True}]` was set during installation, certain fields in this procedure are subject to character restrictions. For further information see <cross reference>.

### Procedure

1. From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Inventories.
2. Select the Inventory name you want to add groups to.
3. In the Inventory **Details** page, select the **Groups** tab.
4. Click Create group.
5. Enter the appropriate details:

  - **Name**: Required
  - Optional: **Description**: Enter a description as appropriate.
  - Optional: **Variables**: Enter definitions and values to be applied to all hosts in this group. Enter variables by using either JSON or YAML syntax. Use the radio button to toggle between the two.

6. Click Create group.

### Results

When you have added a group to a template, the Group **Details** page is displayed.

### View or edit inventory groups

The groups list view displays all your inventory groups, or you can filter it to only display the root groups.
An inventory group is considered a root group if it is not a subset of another group.

You can delete a subgroup without concern for dependencies, because automation controller looks for dependencies such as child groups or hosts.
If any exist, a confirmation window displays for you to select whether to delete the root group and all of its subgroups and hosts; or to promote the subgroups so they become the top-level inventory groups, along with their hosts.

### Add groups within groups

You can create a hierarchy of groups by adding groups within groups.
This allows you to create nested groupings of hosts for easier management and organization.

#### About this task

When you have added a group to a template, the Group **Details** page is displayed.

#### Procedure

1. Select the **Related Groups** tab.
2. Click Add existing group to add a group that already exists in your configuration or Create group to create a new group.
3. If creating a new group, enter the appropriate details into the required and optional fields:

  - **Name** (required):
  - Optional: **Description**: Enter a description as appropriate.
  - Optional: **Variables**: Enter definitions and values to be applied to all hosts in this group.
Enter variables using either JSON or YAML syntax.
Use the radio button to toggle between the two.

4. Click Create group.
5. The **Create group** window closes and the newly created group is displayed as an entry in the list of groups associated with the group that it was
created for.

#### What to do next

If you select to add an existing group, available groups appear in a separate selection window.
When you select a group, it is displayed in the list of groups associated with the group.

- To configure additional groups and hosts under the subgroup, click the name of the subgroup from the list of groups and repeat the steps listed before.

### Add hosts to inventory groups

You can add hosts to an inventory either by creating new hosts or by associating existing hosts with the inventory.

#### About this task

You can configure hosts for the inventory and for groups and groups within groups.

#### Procedure

1. From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Inventories.
2. Select the inventory name you want to add groups to.
3. In the Inventory **Details** page, select the **Hosts** tab.
4. Click Create host.
5. Select whether to add a host that already exists in your configuration or create a new host.
6. If creating a new host, set the toggle to **On** to include this host while running jobs.
7. Enter the appropriate details:

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

        Enter variables by using either JSON or YAML syntax.
Use the radio button to toggle between the two.

8. Click Create host.
9. The **Create host** window closes and the newly created host is displayed in the list of hosts associated with the group that it was created for.
      If you select to add an existing host, available hosts appear in a separate selection window.

    When you select a host, it is displayed in the list of hosts associated with the group.

10. You can disassociate a host from this screen by selecting the host and clicking the ![Disassociate](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/disassociate.png) icon.
  
  Note:
      You can also run ad hoc commands from this screen.
For more information, see [Running Ad Hoc commands](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_run_ad_hoc_commands#proc-controller-run-ad-hoc-commands "Learn how to run ad hoc commands against hosts in an inventory.").

11. To configure additional groups for the host, click the name of the host from the list of hosts.
      This opens the **Details** tab of the selected host.

12. Select the **Groups** tab to configure groups for the host.
13. Click Associate groups to associate the host with an existing group.
Available groups appear in a separate selection window.
14. Select the groups to associate with the host and click Confirm.
      When a group is associated, it is displayed in the list of groups associated with the host.

15. If you used a host to run a job, you can view details about those jobs in the **Completed Jobs** tab of the host.
16. Click Expanded to view details about each job.
  
  Note:
      You can create hosts in bulk by using the newly added endpoint in the API, `/api/v2/bulk/host_create`.
This endpoint accepts JSON and you can specify the target inventory and a list of hosts to add to the inventory.
These hosts must be unique within the inventory.
Either all hosts are added, or an error is returned indicating why the operation was not able to complete.
Use the **OPTIONS** request to return the relevant schema.
