# Generate dynamic data from external sources with inventory plugins
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
