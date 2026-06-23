# Add a source to an inventory
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

