# Add a source to an inventory
## Source an inventory from Red Hat Satellite 6

automation controller can integrate with Red Hat Satellite 6 as a dynamic inventory source.

### About this task

Use the following procedure to configure a Red Hat Satellite-sourced inventory.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Inventories.
2.  Select the inventory name you want a source to and click the **Sources** tab.
3.  Click Create source.
4.  In the **Create source** page,, select **Red Hat Satellite 6** from the **Source** list.
5.  The **Create source** window expands with additional fields. Enter the following details:

- Optional: **Credential**: Choose from an existing Satellite Credential. For more information, see [Managing user credentials](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_credentials#controller-credentials "Credentials authenticate the automation controller user when launching jobs against machines, synchronizing with inventory sources, and importing project content from a version control system.").

6.  Optional: You can specify the verbosity, host filter, enabled variables or values, and update options as described in [Adding a source](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_add_source#proc-controller-add-source "Use the following procedure to add a source to an inventory. When you add a source to an inventory, the system creates a new group for that source.").
7.  Use the **Source Variables** field to specify parameters used by the `foreman` inventory source. Enter variables by using either JSON or YAML syntax. Use the radio button to toggle between the two.

If you meet an issue with the automation controller inventory not having the "related groups" from Satellite, you might need to define these variables in the inventory source. For more information, see [Red Hat Satellite 6](/documentation/en-us/red_hat_ansible_automation_platform/2.7/configure-controller_inventory_templates#controller-rh-satellite "You can use automation controller to manage hosts registered to Red Hat Satellite 6 by using the Foreman dynamic inventory plugin.").

If you see the message, `"no foreman.id" variable(s) when syncing the inventory`, see the solution on the Red Hat Customer Portal at: <https://access.redhat.com/solutions/5826451>. Be sure to login with your customer credentials to access the full article.

