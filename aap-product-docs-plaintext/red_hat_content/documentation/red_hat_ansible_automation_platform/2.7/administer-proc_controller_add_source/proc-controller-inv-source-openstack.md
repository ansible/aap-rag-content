# Add a source to an inventory
## Source an inventory from OpenStack

You can create an inventory source that uses the OpenStack inventory plugin to dynamically generate inventory from your OpenStack cloud.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Inventories.
2.  Select the inventory name you want a source to and click the **Sources** tab.
3.  Click Create source.
4.  In the **Create source** page, select **OpenStack** from the **Source** list.
5.  The **Create source** window expands with additional fields. Enter the following details:

- Optional: **Credential**: Choose from an existing OpenStack Credential. For more information, see [Managing user credentials](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_credentials#controller-credentials "Credentials authenticate the automation controller user when launching jobs against machines, synchronizing with inventory sources, and importing project content from a version control system.").

6.  Optional: You can specify the verbosity, host filter, enabled variables or values, and update options as described in [Adding a source](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_add_source#proc-controller-add-source "Use the following procedure to add a source to an inventory. When you add a source to an inventory, the system creates a new group for that source.").
7.  Use the **Source Variables** field to override variables used by the `openstack` inventory plugin. Enter variables by using either JSON or YAML syntax. Use the radio button to toggle between the two.

