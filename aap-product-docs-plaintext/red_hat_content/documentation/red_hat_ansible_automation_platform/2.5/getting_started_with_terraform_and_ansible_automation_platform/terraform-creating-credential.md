# 2. Integrating from Ansible Automation Platform
## 2.1. Creating a credential




You can set up credentials directly from the Ansible Automation Platform user interface. The credentials are provided to the execution environment and Ansible Automation Platform reads them from there. This eliminates the need to manually update each playbook.

**Prerequisite**

- You must have a Terraform API token set up.


**Procedure**

1. Log in to Ansible Automation Platform.
1. From the navigation panel, select **Automation Execution→Infrastructure→Credential Types** .
1. ClickCreate a credential type. The **Create Credential Type** page opens and displays the **Details** tab.
1. For the **Credential Type** , enter a name.
1. In the **Input configuration** field, enter the following YAML parameter and values:


```
fields:       - id: token       type: string       label: token       secret: true
```


1. In the **Injector configuration** field, enter the environment host name and TF token.


- For Terraform Enterprise, the hostname is the location where you have deployed TFE:


```
env:        TF_TOKEN_&lt;hostname&gt;:  ‘{{ token }}’
```


- For HCP Terraform, use:


```
env:        TF_TOKEN_app_terraform_io:   ‘{{ token }}’
```



1. To save your configuration, clickCreate Credential Typeagain. The new credential type is created.
1. To create an instance of your new credential type, select **Automation Execution→Infrastructure→Credentials** page, and selectCreate credential.
1. From the **Credential type** drop-down list, select the name of the credential type you created earlier.
1. In the **Token** field, enter the Terraform API token.
1. (Optional) Edit the **Description** and select the TF organization from the **Organization** drop-down list.
1. ClickSave credential.


**Additional resources**

-  [Terraform CLI configuration](https://developer.hashicorp.com/terraform/cli/config/config-file#environment-variable-credentials)
-  [Terraform API tokens](https://developer.hashicorp.com/terraform/cloud-docs/users-teams-organizations/api-tokens#user-api-tokens)


