# 1. Terraform integration
## 1.2. Integrating from Ansible Automation Platform
### 1.2.1. Authenticating to hashicorp.terraform




After installing or migrating to `hashicorp.terraform` , users must create credentials to use with job templates in Ansible Automation Platform.

#### 1.2.1.1. Creating a credential




Users must create a credential to use with job templates in Ansible Automation Platform.

**Prerequisite**

- You must have a [Terraform API token](https://developer.hashicorp.com/terraform/cloud-docs/users-teams-organizations/api-tokens#user-api-tokens) .


**Procedure**

1. Log in to Ansible Automation Platform.
1. From the navigation panel, select **Automation Execution→Infrastructure→Credentials** , and then selectCreate credential.
1. From the **Credential type** list, select the **HCP Terraform** credential type.
1. In the **Token** field, enter the Terraform API token.
1. (Optional) Edit the **Description** field and select the TF organization from the **Organization** list.
1. ClickSave credential. You are ready to use the credential in a job template.


