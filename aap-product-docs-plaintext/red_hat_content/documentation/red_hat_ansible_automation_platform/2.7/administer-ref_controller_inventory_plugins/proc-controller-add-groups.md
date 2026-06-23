# Generate dynamic data from external sources with inventory plugins
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

