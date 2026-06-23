# Add a source to an inventory
## Source an inventory from Red Hat Virtualization

Learn how to configure a Red Hat virtualization-sourced inventory.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Inventories.
2.  Select the inventory name you want a source to and click the **Sources** tab.
3.  Click Create source.
4.  In the **Create source** page, select **Red Hat Virtualization** from the **Source** list.
5.  The **Create source** window expands with additional fields. Enter the following details:

- Optional: **Credential**: Choose from an existing Red Hat Virtualization Credential. For more information, see [Managing user credentials](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_credentials#controller-credentials "Credentials authenticate the automation controller user when launching jobs against machines, synchronizing with inventory sources, and importing project content from a version control system.").

6.  Optional: You can specify the verbosity, host filter, enabled variables or values, and update options as described in [Adding a source](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_add_source#proc-controller-add-source "Use the following procedure to add a source to an inventory. When you add a source to an inventory, the system creates a new group for that source.").
7.  Use the **Source Variables** field to override variables used by the `ovirt` inventory plugin. Enter variables by using either JSON or YAML syntax. Use the radio button to toggle between the two. For more information about these variables, see [ovirt inventory plugin](https://console.redhat.com/ansible/automation-hub/repo/published/redhat/rhv/content/inventory/ovirt)

Note:
Red Hat Virtualization (ovirt) inventory source requests are secure by default. To change this default setting, set the key `ovirt_insecure` to **true** in `source_variables`, which is only available from the API details of the inventory source at the `/api/v2/inventory_sources/N/` endpoint.

