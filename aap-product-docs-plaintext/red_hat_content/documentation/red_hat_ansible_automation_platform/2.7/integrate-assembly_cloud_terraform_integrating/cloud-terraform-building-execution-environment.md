# Integrate with the cloud.terraform collection
## Build an execution environment in Ansible Automation Platform

You must build an execution environment using the automation controller so that Ansible Automation Platform can provide the credentials necessary for using its automation features.

### Before you begin

- You need a pre-existing execution environment with the latest version of `cloud.terraform` collection before you can create it using an automation controller. You cannot use the default execution environment provided by Ansible Automation Platform because the default environment does not include the `terraform` CLI binary.  Note:
If you have migrated from Terraform Community Edition, you can continue to use your existing execution environment and update it to the latest version of `cloud.terraform`.

- Install the `terraform` CLI binary in your pre-existing execution environment. See **Additional resources** below for a link to the binary.

### Procedure

1.  From the navigation panel, select **Automation Execution> (and then)Infrastructure> (and then)Execution Environments**.
2.  Click Create execution environment.
![Create a new execution environment page](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ee-create-new.png)
3.  For **Name**, enter a name for your Ansible Automation Platform execution environment.
4.  For **Image**, enter the repository link to the image for your pre-existing execution environment.
5.  Click Create execution environment. Your newly added execution environment is ready to be used in a job template.

