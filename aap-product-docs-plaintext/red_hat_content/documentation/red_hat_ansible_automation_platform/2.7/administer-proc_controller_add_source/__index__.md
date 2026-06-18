# Add a source to an inventory

Use the following procedure to add a source to an inventory. When you add a source to an inventory, the system creates a new group for that source.

## About this task

Inventory sources are not associated with groups. Spawned groups are top-level and can still have child groups. All of these spawned groups can have hosts. Adding a source to an inventory only applies to standard inventories.

## Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Inventories.
2.  Select the inventory name you want to add a source to.
3.  In the Inventory **Details** page, select the **Sources** tab.
4.  Click Create source.
5.  Enter the appropriate details:

- **Name** (required):
- Optional: **Description**: Enter a description as appropriate.
- Optional: **Execution Environment**: Click the ![Search](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/search.png) icon or enter the name of the execution environment with which you want to run your inventory imports.
- **Source**: Choose a source for your inventory.

6.  When the information for your chosen inventory sources is complete, you can optionally specify other common parameters, such as verbosity, host filters, and variables.
7.  Use the **Verbosity** menu to select the level of output on any inventory source’s update jobs.
8.  Use the **Host filter** field to specify only matching host names to be imported into automation controller.
9.  In the **Enabled variable** field, specify that automation controller retrieves the enabled state from the dictionary of host variables. You can specify the enabled variable by using dot notation as 'car.key', in which case the lookup searches nested dictionaries, equal to: `from_dict.get('car', {}).get('key', default)`. The **Enabled value** field is ignored unless you set the **Enabled variable** field. If the enabled variable matches this value, the host is enabled on import.

10.  If you specified a dictionary of host variables in the **Enabled variable** field, you can give a value to enable on import. For example, for `enabled_var='status.power_state'` and `'enabled_value='powered_on'` in the following host variables, the host is marked `enabled`:


```
{
"status": {
"power_state": "powered_on",
"created": "2020-08-04T18:13:04+00:00",
"healthy": true
},
"name": "foobar",
"ip_address": "192.168.2.1"
}
```
If `power_state` is any value other than `powered_on`, then the host is disabled when imported into automation controller. If the key is not found, then the host is enabled.

11.  All cloud inventory sources have the following update options:

- **Overwrite**: If checked, any hosts and groups that were previously present on the external source but are now removed, are removed from the automation controller inventory. Hosts and groups that were not managed by the inventory source are promoted to the next manually created group, or, if there is no manually created group to promote them into, they are left in the "all" default group for the inventory. When not checked, local child hosts and groups not found on the external source remain untouched by the inventory update process.

- **Overwrite variables**: If checked, all variables for child groups and hosts are removed and replaced by those found on the external source. When not checked, a merge is performed, combining local variables with those found on the external source.

- **Update on launch**: Each time a job runs using this inventory, refresh the inventory from the selected source before executing job tasks. To avoid job overflows if jobs are spawned faster than the inventory can synchronize, selecting this enables you to configure a **Cache Timeout** to previous cache inventory synchronizations for a certain number of seconds.

The **Update on launch** setting refers to a dependency system for projects and inventory, and does not specifically exclude two jobs from running at the same time.

If a cache timeout is specified, then the dependencies for the second job are created, and it uses the project and inventory update that the first job spawned.

Both jobs then wait for that project or inventory update to finish before proceeding. If they are different job templates, they can then both start and run at the same time, if the system has the capacity to do so. If you intend to use automation controller’s provisioning callback feature with a dynamic inventory source, **Update on launch** must be set for the inventory group.

If you synchronize an inventory source that uses a project that has **Update On launch** set, then the project might automatically update (according to cache timeout rules) before the inventory update starts.

You can create a job template that uses an inventory that sources from the same project that the template uses. In such a case, the project updates and then the inventory updates (if updates are not already in progress, or if the cache timeout has not already expired).

12.  Review your entries and selections. This enables you to configure additional details, such as schedules and notifications.
13.  To configure schedules associated with this inventory source, click the **Schedules** tab:

- If schedules are already set up, then review, edit, enable or disable your schedule preferences.
- If schedules have not been set up, you can add a schedule.

## Source from a project’s source control management

An inventory that is sourced from a project means that it uses the SCM type from the project it is tied to. For example, if the project’s source is from GitHub, then the inventory uses the same source.

### About this task

Use the following procedure to configure a project-sourced inventory:

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Inventories.
2.  Select the inventory name you want a source to and click the **Sources** tab.
3.  Click Create source.
4.  In the **Create source** page, select **Sourced from a Project** from the **Source** list.
5.  Enter the following details in the additional fields:

- Optional: **Source control branch/tag/commit**: Enter the SCM branch, tags, commit hashes, arbitrary refs, or revision number (if applicable) from the source control (Git or Subversion) to checkout. This field only displays if the sourced project has the **Allow branch override** option checked. For further information, see [SSCM Types - Configuring playbooks to use Git and Subversion](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-ref_projects_manage_playbooks_with_source_control#proc-scm-git-subversion "Configure automation controller projects to synchronize Ansible playbooks directly from Git and Subversion. Integrating with Source Control Management supports collaboration and helps ensure you always deploy the latest automation code.").

![Allow branch override](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/projects-create-scm-project-branch-override-checked.png)

Some commit hashes and refs might not be available unless you also give a custom refspec in the next field. If left blank, the default is HEAD which is the last checked out Branch/Tag/Commit for this project.

- Optional: **Credential**: Specify the credential to use for this source.

- **Project** (required): Pre-populates with a default project, otherwise, specify the project this inventory is using as its source. Click the ![Search](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/search.png) icon to choose from a list of projects. If the list is extensive, use the search to narrow the options.

- **Inventory file** (required): Select an inventory file associated with the sourced project. If not already populated, you can type it into the text field within the menu to filter extraneous file types. In addition to a flat file inventory, you can point to a directory or an inventory script. ![image](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/inventories-create-source-sourced-from-project-filter.png)

6.  Optional: You can specify the verbosity, host filter, enabled variable/value, and update options as described in [Adding a source](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_add_source#proc-controller-add-source "Use the following procedure to add a source to an inventory. When you add a source to an inventory, the system creates a new group for that source.").
7.  Optional: To pass to the custom inventory script, you can set environment variables in the **Source variables** field. You can also place inventory scripts in source control and then run it from a project. For more information, see [Inventory File Importing](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_inventory_file_importing#assembly-inventory-file-importing "With automation controller you can select an inventory file from source control, rather than creating one from scratch.").

If you are executing a custom inventory script from SCM, ensure that you set the execution bit (`chmod +x`) for the script in your upstream source control.

If you do not, automation controller throws a `[Error 13] Permission denied` error on execution.

## Source an inventory from Amazon Web Services EC2

Use the following procedure to configure an AWS EC2-sourced inventory.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Inventories.
2.  Select the inventory name you want a source to and click the **Sources** tab.
3.  Click Create source.
4.  In the **Create source** page, select **Amazon EC2** from the **Source** list.
5.  The **Create source** window expands with additional fields. Enter the following details:

- Optional: **Credential**: Choose from an existing AWS credential. For more information, see [Managing user credentials](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_credentials#controller-credentials "Credentials authenticate the automation controller user when launching jobs against machines, synchronizing with inventory sources, and importing project content from a version control system."). If automation controller is running on an EC2 instance with an assigned IAM Role, the credential can be omitted, and the security credentials from the instance metadata are used instead. For more information about using IAM Roles, see [IAM roles for Amazon EC2_documentation_at_Amazon](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html) documentation at Amazon.

6.  Optional: You can specify the verbosity, host filter, enabled variables or values, and update options as described in [Adding a source](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_add_source#proc-controller-add-source "Use the following procedure to add a source to an inventory. When you add a source to an inventory, the system creates a new group for that source.").
7.  Use the **Source variables** field to override variables used by the `aws_ec2` inventory plugin. Enter variables by using either JSON or YAML syntax. Use the radio button to toggle between the two. For more information about these variables, see the [aws inventory plugin documentation](https://console.redhat.com/ansible/automation-hub/repo/published/amazon/aws/content/inventory/aws_ec2).

If you only use `include_filters`, the AWS plugin always returns all the hosts. To use this correctly, the first condition on the `or` must be on `filters` and then build the rest of the `OR` conditions on a list of `include_filters`.

## Source an inventory from Google Compute Engine

Learn how to configure a Google-sourced inventory:

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Inventories.
2.  Select the inventory name you want a source to and click the **Sources** tab.
3.  Click Create source.
4.  In the **Add new source** page, select **Google Compute Engine** from the **Source** list.
5.  The **Create source** window expands with the required **Credential** field. Choose from an existing GCE Credential. For more information, see [Managing user credentials](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_credentials#controller-credentials "Credentials authenticate the automation controller user when launching jobs against machines, synchronizing with inventory sources, and importing project content from a version control system.").
6.  Optional: You can specify the verbosity, host filter, enabled variables or values, and update options as described in [Adding a source](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_add_source#proc-controller-add-source "Use the following procedure to add a source to an inventory. When you add a source to an inventory, the system creates a new group for that source.").
7.  Use the **Source Variables** field to override variables used by the `gcp_compute` inventory plugin. Enter variables by using either JSON or YAML syntax. Use the radio button to toggle between the two. For more information about these variables, see the [gcp_compute inventory plugin documentation](https://console.redhat.com/ansible/automation-hub/repo/published/google/cloud/content/inventory/gcp_compute).

## Source an inventory from Microsoft Azure resource manager

Use the following procedure to configure an Microsoft Azure Resource Manager-sourced inventory.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Inventories.
2.  Select the inventory name you want a source to and click the **Sources** tab.
3.  Click Create source.
4.  In the **Create source** page, select **Microsoft Azure Resource Manager** from the **Source** list.
5.  Enter the following details in the additional fields:
6.  Optional: **Credential**: Choose from an existing Azure Credential. For more information, see [Managing user credentials](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_credentials#controller-credentials "Credentials authenticate the automation controller user when launching jobs against machines, synchronizing with inventory sources, and importing project content from a version control system.").
7.  Optional: You can specify the verbosity, host filter, enabled variables or values, and update options as described in [Adding a source](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_add_source#proc-controller-add-source "Use the following procedure to add a source to an inventory. When you add a source to an inventory, the system creates a new group for that source.").
8.  Use the **Source variables** field to override variables used by the `azure_rm` inventory plugin. Enter variables by using either JSON or YAML syntax. Use the radio button to toggle between the two. For more information about these variables, see the [azure_rm inventory plugin documentation](https://console.redhat.com/ansible/automation-hub/repo/published/azure/azcollection/content/inventory/azure_rm).

## Source an inventory from VMware vCenter

You can configure automation controller to synchronize inventory from a VMware vCenter server. You can manage virtual machines as part of your automation workflows.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Inventories.
2.  Select the inventory name you want a source to and click the **Sources** tab.
3.  Click Create source.
4.  In the **Create source** page, select **VMware vCenter** from the **Source** list.
5.  The **Create source** window expands with additional fields. Enter the following details:

- Optional: **Credential**: Choose from an existing VMware credential. For more information, see [Managing user credentials](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_credentials#controller-credentials "Credentials authenticate the automation controller user when launching jobs against machines, synchronizing with inventory sources, and importing project content from a version control system.").

6.  Optional: You can specify the verbosity, host filter, enabled variables or values, and update options as described in [Adding a source](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_add_source#proc-controller-add-source "Use the following procedure to add a source to an inventory. When you add a source to an inventory, the system creates a new group for that source.").
7.  Use the **Source Variables** field to override variables used by the `vmware_inventory` inventory plugin. Enter variables by using either JSON or YAML syntax. Use the radio button to toggle between the two. For more information about these variables, see the [vmware_inventory inventory plugin](https://github.com/ansible-collections/community.vmware/blob/main/plugins/inventory/vmware_vm_inventory.py).

VMWare properties have changed from lower case to camel case. Automation controller provides aliases for the top-level keys, but lower case keys in nested properties have been discontinued.

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

## Source an inventory from Red Hat Lightspeed

You can create an inventory source that uses Red Hat Lightspeed as the source of hosts.

### About this task

Use the following procedure to configure a Red Hat Lightspeed-sourced inventory.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Inventories.
2.  Select the inventory name you want a source to and click the **Sources** tab.
3.  Click Create source.
4.  In the **Create source** page, select **Red Hat Lightspeed** from the **Source** list.
5.  The **Create source** window expands with additional fields. Enter the following details:

- Optional: **Credential**: Choose from an existing Red Hat Lightspeed Credential. For more information, see [Managing user credentials](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_credentials#controller-credentials "Credentials authenticate the automation controller user when launching jobs against machines, synchronizing with inventory sources, and importing project content from a version control system.").

6.  Optional: You can specify the verbosity, host filter, enabled variables or values, and update options as described in [Adding a source](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_add_source#proc-controller-add-source "Use the following procedure to add a source to an inventory. When you add a source to an inventory, the system creates a new group for that source.").
7.  Use the **Source Variables** field to override variables used by the `Red Hat Lightspeed` inventory plugin. Enter variables by using either JSON or YAML syntax. Use the radio button to toggle between the two. For more information about these variables, see [Red Hat Lightspeed inventory plugin](https://console.redhat.com/ansible/automation-hub/repo/published/redhat/insights/content/inventory/insights).

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

## Source an inventory from Red Hat Ansible Automation Platform

An inventory that is sourced from Red Hat Ansible Automation Platform uses the Red Hat Ansible Automation Platform inventory plugin to gather inventory data from the Red Hat Ansible Automation Platform platform.

### About this task

Use the following procedure to configure an automation controller-sourced inventory.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Inventories.
2.  Select the inventory name you want a source to and click the **Sources** tab.
3.  Click Create source.
4.  In the **Create source** page, select **Red Hat Ansible Automation Platform** from the **Source** list.
5.  The **Create source** window expands with additional fields. Enter the following details:

- Optional: **Credential**: Choose from an existing Red Hat Ansible Automation Platform Credential. For more information, see [Managing user credentials](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_credentials#controller-credentials "Credentials authenticate the automation controller user when launching jobs against machines, synchronizing with inventory sources, and importing project content from a version control system.").

6.  Optional: You can specify the verbosity, host filter, enabled variables or values, and update options as described in [Adding a source](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_add_source#proc-controller-add-source "Use the following procedure to add a source to an inventory. When you add a source to an inventory, the system creates a new group for that source.").
7.  Use the **Source Variables** field to override variables used by the `controller` inventory plugin. Enter variables by using either JSON or YAML syntax. Use the radio button to toggle between the two. For more information about these variables, see [Controller inventory plugin](https://console.redhat.com/ansible/automation-hub/repo/published/ansible/controller/content/inventory/controller). This requires your Red Hat Customer login.

## Source an inventory from Terraform State

Use the following procedure to create a Terraform State inventory source.

### About this task

This inventory source uses the terraform_state inventory plugin from the [cloud.terraform](https://console.redhat.com/ansible/automation-hub/repo/published/cloud/terraform/content/inventory/terraform_state/) collection. The plugin parses a terraform state file and add hosts for AWS EC2, GCE, and Microsoft Azure instances.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Projects.
2.  On the **Projects** page, click Create project to start the **Create project** window.   - Enter the appropriate details according to the steps in [Adding a new project](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_controller_adding_a_project#proc-controller-adding-a-project "You can create a logical collection of playbooks, called projects in automation controller.").

3.  From the navigational panel, select Automation Execution> (and then)Infrastructure> (and then)Inventories.
4.  Select the inventory that you want to add a source to.
5.  In the **Sources** tab, click Create source.
6.  From the Source menu, select **Terraform State**.   - The **Create source** window expands with the optional **Credential** field. Choose an existing Terraform backend configuration credential. For more information, see [Terraform backend configuration](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-ref_controller_credential_terraform#ref-controller-credential-terraform "Terraform is a HashiCorp tool used to automate various infrastructure tasks. Select this credential type to enable synchronization with the Terraform inventory source.").

7.  Enable the options to **Overwrite** and **Update on launch**.
8.  Use the **Source variables** field to override variables used by the `terraform_state` inventory plugin. Enter variables by using either JSON or YAML syntax. Use the radio button to toggle between the two. For more information about these variables, see the [terraform_state](https://console.redhat.com/ansible/automation-hub/repo/published/cloud/terraform/content/inventory/terraform_state/) file. The `backend_type` variable is required by the Terraform State inventory plugin. This should match the remote backend configured in the **Terraform backend credential**. The following is an example Amazon S3 backend:

```
backend_type: s3
```

9.  Select an **Execution environment** that has a Terraform binary. This is required for the inventory plugin to run the Terraform commands that read inventory data from the Terraform state file.  Important:
Terraform provider for Ansible Automation Platform inventories are managed by Terraform and you must not edit them in Ansible Automation Platform as it can introduce drift to the Terraform deployment.

## Source an inventory from OpenShift Virtualization

Learn how to add an OpenShift Virtualization inventory source to an existing inventory.

### Before you begin

- You need a virtual machine deployed in a specific namespace and an OpenShift or Kubernetes API Bearer Token credential.

### About this task

This inventory source uses a cluster that is able to deploy Red Hat OpenShift Container Platform Virtualization.

### Procedure

1.  From the navigational panel, select Automation Execution> (and then)Infrastructure> (and then)Inventories.
2.  Select the inventory that you want to add a source to.
3.  In the **Sources** tab, click Add source.
4.  From the Source menu, select **OpenShift Virtualization**.   - The **Add new source** window expands with the required **Credential** field. Choose from an existing Kubernetes API Bearer Token credential. For more information, see [OpenShift or Kubernetes API Bearer Token credential type](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-ref_controller_credential_openshift#ref-controller-credential-openShift "Select this credential type to create instance groups that point to a Kubernetes or OpenShift container."). In this example, the `cmv2.engineering.redhat.com` credential is used.

5.  You can optionally specify the **Verbosity**, **Host Filter**, **Enabled Variable/Value**, and **Update options** as described in the [Adding a source](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_add_source#proc-controller-add-source "Use the following procedure to add a source to an inventory. When you add a source to an inventory, the system creates a new group for that source.") steps.
6.  Use the **Source Variables** field to override variables used by the `kubernetes` inventory plugin. Enter variables by using either JSON or YAML syntax. Use the radio button to toggle between the two. For more information about these variables, see the [kubevirt.core.kubevirt inventory source](https://kubevirt.io/kubevirt.core/main/plugins/kubevirt.html#parameters) documentation. In the following example, the connections variable is used to specify access to a particular namespace in a cluster:

```
---
connections:
- namespaces:
- hao-test
```

7.  Click Save and then click Sync to sync the inventory.

## Source an inventory from a custom inventory plugin

This describes how to use the `servicenow.itsm` collection inventory plugin to sync inventory on Ansible Automation Platform.

### Procedure

1.  Create and sync a project using a Source Control Git repository that includes the following files:


```
>> requirements.yml
---
collections: - name: servicenow.itsm

>> inventories/myinventory.now.yml
# Create a file following the example below. It must have a configuration file extension ending in either "now.yml" or "now.yaml".
plugin: servicenow.itsm.now
query:
- os: = Linux Red Hat
- os: = Windows XP
keyed_groups:
- key: os
prefix: os
```
Note:
Refer to the official [Ansible documentation](https://console.redhat.com/ansible/automation-hub/repo/published/servicenow/itsm/content/inventory/now/) for detailed guidance on using and configuring the `servicenow.itsm.now` plugin.

2.  Create an inventory by setting the source to **Sourced from a Project**, selecting the new project, and choose `/(project root)` in the inventory file section.
3.  Synchronize the source in the inventory.

## Export old inventory scripts

Despite the removal of the custom inventory scripts API, the scripts are still saved in the database.

To recover the scripts from the database in a format that is suitable for you to check into source control, use the following command:

```
$ awx-manage export_custom_scripts --filename=my_scripts.tar

Dump of old custom inventory scripts at my_scripts.tar
```
Making use of the output:

```
$ mkdir my_scripts
$ tar -xf my_scripts.tar -C my_scripts
```
The name of the scripts has the form: `<pk>_<name>`. This is the naming scheme used for project folders.

```
$ ls my_scripts
10inventory_script_rawhook             _19                                       _30inventory_script_listenhospital
_11inventory_script_upperorder          _1inventory_script_commercialinternet45   _4inventory_script_whitestring
_12inventory_script_eastplant           _22inventory_script_pinexchange           _5inventory_script_literaturepossession
_13inventory_script_governmentculture   _23inventory_script_brainluck             _6inventory_script_opportunitytelephone
_14inventory_script_bottomguess         _25inventory_script_buyerleague           _7inventory_script_letjury
_15inventory_script_wallisland          _26inventory_script_lifesport             _8random_inventory_script
16inventory_script_wallisland          _27inventory_script_exchangesomewhere     _9random_inventory_script
_17inventory_script_bidstory            _28inventory_script_boxchild
_18p                                    _29__inventory_script_wearstress
```
Each file contains a script. Scripts can be `bash/python/ruby/more`, so the extension is not included. They are all directly executable. Executing the script dumps the inventory data.

```
$ ./my_scripts/11__inventory_script_upperorder
{"group\ud801\udcb0\uc20e\u7b0e\ud81c\udfeb\ub12b\ub4d0\u9ac6\ud81e\udf07\u6ff9\uc17b": {"hosts":
["host_\ud821\udcad\u68b6\u7a51\u93b4\u69cf\uc3c2\ud81f\uddbe\ud820\udc92\u3143\u62c7",
"host_\u6057\u3985\u1f60\ufefb\u1b22\ubd2d\ua90c\ud81a\udc69\u1344\u9d15",
"host_\u78a0\ud820\udef3\u925e\u69da\ua549\ud80c\ude7e\ud81e\udc91\ud808\uddd1\u57d6\ud801\ude57",
"host_\ud83a\udc2d\ud7f7\ua18a\u779a\ud800\udf8b\u7903\ud820\udead\u4154\ud808\ude15\u9711",
"host_\u18a1\u9d6f\u08ac\u74c2\u54e2\u740e\u5f02\ud81d\uddee\ufbd6\u4506"], "vars": {"ansible_host": "127.0.0.1", "ansible_connection":
"local"}}}
```
You can verify functionality with `ansible-inventory`. This gives the same data, but reformatted.

```
$ ansible-inventory -i ./my_scripts/_11__inventory_script_upperorder --list --export
```
In the preceding example, you can `cd` into `my_scripts` and then issue a `git init` command, add the scripts you want, push it to source control, and then create an SCM inventory source in the user interface.

For more information about syncing or using custom inventory scripts, see[Import your inventory file from source control](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_inventory_file_importing#assembly-inventory-file-importing "With automation controller you can select an inventory file from source control, rather than creating one from scratch.") in *Configuring automation execution*.
