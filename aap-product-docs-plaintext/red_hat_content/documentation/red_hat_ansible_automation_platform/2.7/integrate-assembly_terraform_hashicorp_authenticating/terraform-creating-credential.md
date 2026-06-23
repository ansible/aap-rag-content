# Use hashicorp.terraform
## Create a credential for hashicorp.terraform

Users must create a credential to use with job templates in Ansible Automation Platform.

### Before you begin

- You must have a Terraform API token.

### Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select **Automation Execution> (and then)Infrastructure> (and then)Credentials**, and then select Create credential.
3.  From the **Credential type** list, select the **HCP Terraform** credential type.
4.  In the **Token** field, enter the Terraform API token.
5.  (Optional) Edit the **Description** field and select the TF organization from the **Organization** list.
6.  Click Save credential. You are ready to use the credential in a job template.

