# 14. Inventories
## 14.4. Add a new inventory
### 14.4.3. Adding groups to inventories




Inventories are divided into groups, which can contain hosts and other groups. Groups are only applicable to standard inventories and are not a configurable directly through a Smart Inventory. You can associate an existing group through hosts that are used with standard inventories.

The following actions are available for standard inventories:

- Create a new Group
- Create a new Host
- Run a command on the selected Inventory
- Edit Inventory properties
- View activity streams for Groups and Hosts
- Obtain help building your Inventory


Note
Inventory sources are not associated with groups. Spawned groups are top-level and can still have child groups. All of these spawned groups can have hosts.



**Procedure**

1. From the navigation panel, selectAutomation Execution→Infrastructure→Inventories.
1. Select the Inventory name you want to add groups to.
1. In the Inventory **Details** page, select the **Groups** tab.
1. ClickCreate group.
1. Enter the appropriate details:


-  **Name** : Required
- Optional: **Description** : Enter a description as appropriate.
- Optional: **Variables** : Enter definitions and values to be applied to all hosts in this group. Enter variables by using either JSON or YAML syntax. Use the radio button to toggle between the two.

1. ClickCreate group.


**Result**

When you have added a group to a template, the Group **Details** page is displayed.


#### 14.4.3.1. Adding groups within groups




When you have added a group to a template, the Group **Details** page is displayed.

**Procedure**

1. Select the **Related Groups** tab.
1. ClickAdd existing groupto add a group that already exists in your configuration orCreate groupto create a new group.
1. If creating a new group, enter the appropriate details into the required and optional fields:


-  **Name** (required):
- Optional: **Description** : Enter a description as appropriate.
- Optional: **Variables** : Enter definitions and values to be applied to all hosts in this group. Enter variables using either JSON or YAML syntax. Use the radio button to toggle between the two.

1. ClickCreate group.
1. The **Create group** window closes and the newly created group is displayed as an entry in the list of groups associated with the group that it was created for.


**Next steps**

If you select to add an existing group, available groups appear in a separate selection window. When you select a group, it is displayed in the list of groups associated with the group.


- To configure additional groups and hosts under the subgroup, click the name of the subgroup from the list of groups and repeat the steps listed before.


#### 14.4.3.2. View or edit inventory groups




The groups list view displays all your inventory groups, or you can filter it to only display the root groups. An inventory group is considered a root group if it is not a subset of another group.

You can delete a subgroup without concern for dependencies, because automation controller looks for dependencies such as child groups or hosts. If any exist, a confirmation window displays for you to select whether to delete the root group and all of its subgroups and hosts; or to promote the subgroups so they become the top-level inventory groups, along with their hosts.

