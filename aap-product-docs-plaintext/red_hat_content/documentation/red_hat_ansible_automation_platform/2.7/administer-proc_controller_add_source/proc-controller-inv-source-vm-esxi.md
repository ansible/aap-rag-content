# Add a source to an inventory
## Source an inventory from VMware ESXi

Learn how to configure a VMWare ESXi sourced inventory.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Inventories.
2.  Select the inventory name you want to add a source to, and click the **Sources** tab.
3.  Click Create source.
4.  Enter a **Name** for the source (required).
5.  In the **Create source** page, select **VMware ESXi** from the **Source** list.
6.  The **Create source** window expands with additional fields. Enter the following details:

- **Credential**: Choose from an existing VMware credential. For more information, see [Managing user credentials](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_credentials#controller-credentials "Credentials authenticate the automation controller user when launching jobs against machines, synchronizing with inventory sources, and importing project content from a version control system.").

7.  Use the **Verbosity** menu to select the level of output on any inventory source’s update jobs.
8.  Optional: You can specify the host filter, enabled variables or values, and update options as described in [Adding a source](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_add_source#proc-controller-add-source "Use the following procedure to add a source to an inventory. When you add a source to an inventory, the system creates a new group for that source.").
9.  Use the **Source Variables** field to override variables used by the `vmware_inventory` inventory plugin. Enter variables by using either JSON or YAML syntax. Use the radio button to toggle between the two.

VMWare properties have changed from lower case to camel case. Automation controller provides aliases for the top-level keys, but lower case keys in nested properties have been discontinued.

