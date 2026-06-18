# Migrate from the Terraform community edition

If you want to use Ansible Automation Platform with Terraform Enterprise (TFE) or HCP Terraform and you are currently using Terraform Community Edition (TCE), you must migrate to TFE or HCP Terraform and then update Ansible Automation Platform configurations to work with TFE or HCP Terraform.

## Before you begin

- Use the latest supported version of Terraform (1.11 or higher).
- Follow the `tf-migrate` CLI instructions under **Additional resources** below.
- Ensure that the HCP Terraform or TFE workspace is not set to automatically apply plans.

## About this task

When you migrate from TCE to TFE or HCP Terraform, you are not migrating the collection itself. Instead, you are adapting your existing TCE usage to work with TFE or HCP Terraform.

After you migrate, you must update the Ansible Automation Platform credentials, execution environment, and job templates.

Note:

The `cloud.terraform` collection only supports the CLI-driven workflow in HCP Terraform.

## Procedure

1.  To prevent errors when running playbooks against TFE or HCP Terraform, do the following actions before running a playbook:
1.  Confirm that the Terraform version in the execution environment is the same as the version stated in TFE or HCP Terraform.
2.  Perform an initialization in TFE or HCP Terraform:


```
terraform init
```

3.  If you have a local state file in your execution environment, delete the local state file.
4.  Get a token from HCP Terraform or Terraform Enterprise, which you will use to create the credential in a later step. Ensure the token has the necessary permissions based on the team or user token to execute the desired capabilities in the playbook.
5.  Remove the backend config and files from your playbook definition.
6.  Add the workspace within the default setting in your TF config or an environment variable if you want to define the workspace outside updating the playbook itself. Note:
You can add the workspace to your playbook to scale your workspace utilization.

2.  From the Ansible Automation Platform user interface, complete the integration with `cloud.terraform`:
1.  Create a credential.
2.  Build an execution environment in Ansible Automation Platform.
3.  Create and launch a job template.
3.  (Optional) After the migration is completed and verified, you can run the additional modules and plugins from the collection in your execution environment:

- Plan Stash module
- Terraform module
- Output plugin
- Output lookup plugin
- State inventory plugin
