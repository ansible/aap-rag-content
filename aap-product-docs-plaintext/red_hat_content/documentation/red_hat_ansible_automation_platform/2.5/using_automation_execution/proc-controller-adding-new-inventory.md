# 14. Inventories
## 14.4. Add a new inventory




Adding a new inventory involves the following components:

-  [Adding permissions to inventories](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#proc-controller-adding-inv-permissions)
-  [Adding groups to inventories](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#proc-controller-add-groups)
-  [Adding a host](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#proc-controller-add-hosts)
-  [Adding a source](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#proc-controller-add-source)
-  [View completed jobs](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#ref-controller-view-completed-jobs)


Use the following procedure to create a inventory:

**Procedure**

1. From the navigation panel, selectAutomation Execution→Infrastructure→Inventories. The **Inventories** window displays a list of the inventories that are currently available.
1. ClickCreate inventory, and select the type of inventory to create.
1. Enter the appropriate details into the following fields:


-  **Name** : Enter a name appropriate for this inventory.
- Optional: **Description** : Enter an arbitrary description as appropriate.
-  **Organization** : Required. Choose among the available organizations.
- Only applicable to Smart Inventories: **Smart host filter** : Populate the hosts for this inventory by using a search filter.

For example "name__icontains=RedHat".

These options are based on the organization you chose.

Filters are similar to tags in that tags are used to filter certain hosts that contain those names. Therefore, to populate the **Smart host filter** field, specify a tag that has the hosts you want, not the hosts themselves.

Filters are case-sensitive.


-  **Instance groups** : Select the instance group or groups for this inventory to run on.

You can select many instance groups and sort them in the order that you want them run.


- Optional: **Labels** : Supply labels that describe this inventory, so they can be used to group and filter inventories and jobs.
- Only applicable to constructed inventories: **Input inventories** : Specify the source inventories to include in this constructed inventory. Empty groups from input inventories are copied into the constructed inventory.
- Optional:(Only applicable to constructed inventories): **Cached timeout (seconds)** : Set the length of time you want the cache plugin data to timeout.
- Only applicable to constructed inventories: **Verbosity** : Control the level of output that Ansible produces as the playbook executes related to inventory sources associated with constructed inventories.

Select the verbosity from:


-  **Normal**
-  **Verbose**
-  **More verbose**
-  **Debug**
-  **Connection Debug**
-  **WinRM Debug**


-  **Verbose** logging includes the output of all commands.
-  **More verbose** provides more detail than **Verbose** .
-  **Debug** logging is exceedingly verbose and includes information about SSH operations that can be useful in certain support instances. Most users do not need to see debug mode output.
-  **Connection Debug** enables you to run SSH in verbose mode, providing debugging information about the SSH connection progress.
-  **WinRM Debug** used for verbosity specific to windows remote management

Click the![Expand](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/301c31ef51ac512bd11df2687c14dd9d/arrow.png)
icon for information on **How to use the constructed inventory plugin** .



- Only applicable to constructed inventories: **Limit** : Restricts the number of returned hosts for the inventory source associated with the constructed inventory. You can paste a group name into the limit field to only include hosts in that group. For more information, see the **Source vars** setting.
- Only applicable to standard inventories: **Options** : Check the **Prevent Instance Group Fallback** option to enable only the instance groups listed in the **Instance Groups** field to execute the job. If unchecked, all available instances in the execution pool are used based on the hierarchy described in [Control where a job runs](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-control-job-run) .
-  **Variables** ( **Source vars** for constructed inventories):


-  **Variables** Variable definitions and values to apply to all hosts in this inventory. Enter variables by using either JSON or YAML syntax. Use the radio button to toggle between the two.
-  **Source vars** for constructed inventories creates groups, specifically under the `            groups` key of the data. It accepts Jinja2 template syntax, renders it for every host, makes a `            true` or `            false` evaluation, and includes the host in the group (from the key of the entry) if the result is `            true` . This is particularly useful because you can paste that group name into the limit field to only include hosts in that group.


1. ClickCreate inventory.


**Next steps**

After saving the new inventory, you can proceed with configuring permissions, groups, hosts, sources, and view completed jobs, if applicable to the type of inventory.


