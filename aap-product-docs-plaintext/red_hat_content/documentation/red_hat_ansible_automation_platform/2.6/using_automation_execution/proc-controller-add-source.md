# 14. Inventories
## 14.4. Add a new inventory
### 14.4.5. Adding a source




Use the following procedure to add a source to an inventory. When you add a source to an inventory, the system creates a new group for that source.

Inventory sources are not associated with groups. Spawned groups are top-level and can still have child groups. All of these spawned groups can have hosts. Adding a source to an inventory only applies to standard inventories.

**Procedure**

1. From the navigation panel, selectAutomation Execution→Infrastructure→Inventories.
1. Select the inventory name you want to add a source to.
1. In the Inventory **Details** page, select the **Sources** tab.
1. ClickCreate source.
1. Enter the appropriate details:


-  **Name** (required):
- Optional: **Description** : Enter a description as appropriate.
- Optional: **Execution Environment** : Click the![Search](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Using_automation_execution-en-US/images/74841a45a98b4160b7576724a8f4c038/search.png)
icon or enter the name of the execution environment with which you want to run your inventory imports. For more information on building an execution environment, see [Execution environments](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#assembly-controller-execution-environments) .
-  **Source** : Choose a source for your inventory. For more information about sources, and supplying the appropriate information, see [Inventory sources](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#ref-controller-inventory-sources) .

1. When the information for your chosen [Inventory sources](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#ref-controller-inventory-sources) is complete, you can optionally specify other common parameters, such as verbosity, host filters, and variables.
1. Use the **Verbosity** menu to select the level of output on any inventory source’s update jobs.
1. Use the **Host filter** field to specify only matching host names to be imported into automation controller.
1. In the **Enabled variable** field, specify that automation controller retrieves the enabled state from the dictionary of host variables. You can specify the enabled variable by using dot notation as 'car.key', in which case the lookup searches nested dictionaries, equal to: `    from_dict.get('car', {}).get('key', default)` .

The **Enabled value** field is ignored unless you set the **Enabled variable** field. If the enabled variable matches this value, the host is enabled on import.


1. If you specified a dictionary of host variables in the **Enabled variable** field, you can give a value to enable on import. For example, for `    enabled_var='status.power_state'` and `    'enabled_value='powered_on'` in the following host variables, the host is marked `    enabled` :


```
{    "status": {    "power_state": "powered_on",    "created": "2020-08-04T18:13:04+00:00",    "healthy": true    },    "name": "foobar",    "ip_address": "192.168.2.1"    }
```

If `    power_state` is any value other than `    powered_on` , then the host is disabled when imported into automation controller. If the key is not found, then the host is enabled.


1. All cloud inventory sources have the following update options:


-  **Overwrite** : If checked, any hosts and groups that were previously present on the external source but are now removed, are removed from the automation controller inventory. Hosts and groups that were not managed by the inventory source are promoted to the next manually created group, or, if there is no manually created group to promote them into, they are left in the "all" default group for the inventory.

When not checked, local child hosts and groups not found on the external source remain untouched by the inventory update process.


-  **Overwrite variables** : If checked, all variables for child groups and hosts are removed and replaced by those found on the external source.

When not checked, a merge is performed, combining local variables with those found on the external source.


-  **Update on launch** : Each time a job runs using this inventory, refresh the inventory from the selected source before executing job tasks.

To avoid job overflows if jobs are spawned faster than the inventory can synchronize, selecting this enables you to configure a **Cache Timeout** to previous cache inventory synchronizations for a certain number of seconds.

The **Update on launch** setting refers to a dependency system for projects and inventory, and does not specifically exclude two jobs from running at the same time.

If a cache timeout is specified, then the dependencies for the second job are created, and it uses the project and inventory update that the first job spawned.

Both jobs then wait for that project or inventory update to finish before proceeding. If they are different job templates, they can then both start and run at the same time, if the system has the capacity to do so. If you intend to use automation controller’s provisioning callback feature with a dynamic inventory source, **Update on launch** must be set for the inventory group.

If you synchronize an inventory source that uses a project that has **Update On launch** set, then the project might automatically update (according to cache timeout rules) before the inventory update starts.

You can create a job template that uses an inventory that sources from the same project that the template uses. In such a case, the project updates and then the inventory updates (if updates are not already in progress, or if the cache timeout has not already expired).



1. Review your entries and selections. This enables you to configure additional details, such as schedules and notifications.
1. To configure schedules associated with this inventory source, click the **Schedules** tab:


- If schedules are already set up, then review, edit, enable or disable your schedule preferences.
- If schedules have not been set up, for more information about setting up schedules, see [Schedules](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#controller-schedules) .



