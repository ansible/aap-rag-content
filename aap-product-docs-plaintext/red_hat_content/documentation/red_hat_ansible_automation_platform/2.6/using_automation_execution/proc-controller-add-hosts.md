# 14. Inventories
## 14.4. Add a new inventory
### 14.4.4. Adding hosts to an inventory




You can configure hosts for the inventory and for groups and groups within groups.

**Procedure**

1. From the navigation panel, selectAutomation Execution→Infrastructure→Inventories.
1. Select the inventory name you want to add groups to.
1. In the Inventory **Details** page, select the **Hosts** tab.
1. ClickCreate host.
1. Select whether to add a host that already exists in your configuration or create a new host.
1. If creating a new host, set the toggle to **On** to include this host while running jobs.
1. Enter the appropriate details:


-  **Name** (required):
- Optional: **Description** : Enter a description as appropriate.
- Optional: **Variables** : Enter definitions and values to be applied to all hosts in this group, as in the following example:


```
{          ansible_user : &lt;username to ssh into&gt;          ansible_ssh_pass : &lt;password for the username&gt;          ansible_become_pass: &lt;password for becoming the root&gt;        }
```

Enter variables by using either JSON or YAML syntax. Use the radio button to toggle between the two.



1. ClickCreate host.
1. The **Create host** window closes and the newly created host is displayed in the list of hosts associated with the group that it was created for.

If you select to add an existing host, available hosts appear in a separate selection window.

When you select a host, it is displayed in the list of hosts associated with the group.


1. You can disassociate a host from this screen by selecting the host and clicking the![Disassociate](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Using_automation_execution-en-US/images/48c2fa70cf2a09ae0fafa81899b143fc/disassociate.png)
icon.

Note
You can also run ad hoc commands from this screen. For more information, see [Running Ad Hoc commands](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#proc-controller-run-ad-hoc-commands) .




1. To configure additional groups for the host, click the name of the host from the list of hosts.

This opens the **Details** tab of the selected host.


1. Select the **Groups** tab to configure groups for the host.
1. ClickAssociate groupsto associate the host with an existing group. Available groups appear in a separate selection window.
1. Select the groups to associate with the host and clickConfirm.

When a group is associated, it is displayed in the list of groups associated with the host.


1. If you used a host to run a job, you can view details about those jobs in the **Completed Jobs** tab of the host.
1. ClickExpandedto view details about each job.


Note
You can create hosts in bulk by using the newly added endpoint in the API, `/api/v2/bulk/host_create` . This endpoint accepts JSON and you can specify the target inventory and a list of hosts to add to the inventory. These hosts must be unique within the inventory. Either all hosts are added, or an error is returned indicating why the operation was not able to complete. Use the **OPTIONS** request to return the relevant schema.



