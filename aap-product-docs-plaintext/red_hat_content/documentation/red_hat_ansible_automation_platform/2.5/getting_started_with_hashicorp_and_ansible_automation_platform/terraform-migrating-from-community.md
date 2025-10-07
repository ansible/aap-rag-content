# 1. Terraform integration
## 1.3. Migrating from Terraform Community Edition
### 1.3.1. Migrating from the community edition




When you migrate from TCE to TFE or HCP Terraform, you are not migrating the collection itself. Instead, you are adapting your existing TCE usage to work with TFE or HCP Terraform. After you migrate, you must update the Ansible Automation Platform credentials, execution environment, and job templates.

Note
The `cloud.terraform` collection only supports the CLI-driven workflow in HCP Terraform.



**Prerequisites**

- Use the latest supported version of Terraform (1.11 or higher).
- Follow the `    tf-migrate` CLI instructions under **Additional resources** below.
- Ensure that the HCP Terraform or TFE workspace is not set to automatically apply plans.


**Procedure**

1. To prevent errors when running playbooks against TFE or HCP Terraform, do the following actions before running a playbook:


1. Confirm that the Terraform version in the execution environment is the same as the version stated in TFE or HCP Terraform.
1. Perform an initialization in TFE or HCP Terraform:


```
terraform init
```


1. If you have a local state file in your execution environment, delete the local state file.
1. Get a token from HCP Terraform or Terraform Enterprise, which you will use to create the credential in a later step. Ensure the token has the necessary permissions based on the team or user token to execute the desired capabilities in the playbook.
1. Remove the backend config and files from your playbook definition.
1. Add the workspace within the default setting in your TF config or an environment variable if you want to define the workspace outside updating the playbook itself.

Note
You can add the workspace to your playbook to scale your workspace utilization.





1. From the Ansible Automation Platform user interface:


1.  [Create a credential](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/getting_started_with_terraform_and_ansible_automation_platform/terraform-integrating-from-aap#terraform-creating-credential) .
1.  [Build an execution environment](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/getting_started_with_terraform_and_ansible_automation_platform/terraform-integrating-from-aap#terraform-building-execution-environment) .
1.  [Create and launch a job template](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/getting_started_with_terraform_and_ansible_automation_platform/terraform-integrating-from-aap#terraform-creating-launching-job-template) .

1. (Optional) After the migration is completed and verified, you can run the additional modules and plugins from the collection in your execution environment:


-  [Plan Stash module](https://console.redhat.com/ansible/automation-hub/repo/published/cloud/terraform/content/module/plan_stash/)
-  [Terraform module](https://console.redhat.com/ansible/automation-hub/repo/published/cloud/terraform/content/module/terraform/)
-  [Output plugin](https://console.redhat.com/ansible/automation-hub/repo/published/cloud/terraform/content/module/terraform_output/)
-  [Output lookup plugin](https://console.redhat.com/ansible/automation-hub/repo/published/cloud/terraform/content/lookup/tf_output/)
-  [State inventory plugin](https://console.redhat.com/ansible/automation-hub/repo/published/cloud/terraform/content/inventory/terraform_state/)
-  [tf-migrate CLI instructions](https://developer.hashicorp.com/terraform/cloud-docs/migrate/tf-migrate)



