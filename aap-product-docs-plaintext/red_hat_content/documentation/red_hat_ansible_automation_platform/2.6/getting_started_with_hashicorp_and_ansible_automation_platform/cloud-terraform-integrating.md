# 1. Terraform integration
## 1.2. Integrating from Ansible Automation Platform
### 1.2.2. Integrating with cloud.terraform




When you integrate with `cloud.terraform` , you must create a credential, build an execution environment, and launch a job template in Ansible Automation Platform.

#### 1.2.2.1. Creating a credential




You can set up credentials directly from the Ansible Automation Platform user interface. The credentials are provided to the execution environment and Ansible Automation Platform reads them from there. This eliminates the need to manually update each playbook.

**Prerequisites**

- You must have a [Terraform API token](https://developer.hashicorp.com/terraform/cloud-docs/users-teams-organizations/api-tokens#user-api-tokens) .
- Install the certified [cloud.terraform](https://console.redhat.com/ansible/automation-hub/repo/published/cloud/terraform/) collection from automation hub. (You need an Ansible subscription to access and download collections on automation hub.)


**Procedure**

1. Log in to Ansible Automation Platform.
1. From the navigation panel, select **Automation Execution→Infrastructure→Credential Types** .
1. ClickCreate credential type. The **Create Credential Type** page opens and displays the **Details** tab.
1. For the **Credential Type** , enter a name.
1. In the **Input configuration** field, enter the following YAML parameter and values:


```
fields:       - id: token         type: string         label: token         secret: true
```


1. In the **Injector configuration** field, enter the following configuration.


- For Terraform Enterprise, the hostname is the location where you have deployed TFE:


```
env:          TF_TOKEN_&lt;hostname&gt;:  ‘{{ token }}’
```


- For HCP Terraform, use:


```
env:          TF_TOKEN_app_terraform_io:   ‘{{ token }}’
```



1. To save your configuration, clickCreate Credential Typeagain. The new credential type is created.
1. To create an instance of your new credential type, select **Automation Execution→Infrastructure→Credentials** page, and selectCreate credential.
1. From the **Credential type** , select the name of the credential type you created earlier.
1. In the **Token** field, enter the Terraform API token.
1. (Optional) Edit the **Description** and select the TF organization from the **Organization** list.
1. ClickSave credential.


**Additional resources**

-  [Terraform CLI configuration](https://developer.hashicorp.com/terraform/cli/config/config-file#environment-variable-credentials)


#### 1.2.2.2. Building an execution environment in Ansible Automation Platform




You must build an execution environment using the automation controller so that Ansible Automation Platform can provide the credentials necessary for using its automation features.

**Prerequisites**

- You need a pre-existing execution environment with the latest version of `    cloud.terraform` collection before you can create it using an automation controller. You cannot use the default execution environment provided by Ansible Automation Platform because the default environment does not include the `    terraform` CLI binary.

Note
If you have migrated from Terraform Community Edition, you can continue to use your existing execution environment and update it to the latest version of `    cloud.terraform` .




- Install the `    terraform` CLI binary in your pre-existing execution environment. See **Additional resources** below for a link to the binary.


**Procedure**

1. From the navigation panel, select **Automation Execution→Infrastructure→Execution Environments** .
1. ClickCreate execution environment.

![Create a new execution environment page](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Getting_started_with_HashiCorp_and_Ansible_Automation_Platform-en-US/images/f7d2791d8333c610068f841478dc5bab/ee-create-new.png)



1. For **Name** , enter a name for your Ansible Automation Platform execution environment.
1. For **Image** , enter the repository link to the image for your pre-existing execution environment.
1. ClickCreate execution environment. Your newly added execution environment is ready to be used in a job template.


**Additional resources**

-  [terraform CLI binary](https://developer.hashicorp.com/terraform/install)
-  [Red Hat ecosystem catalog](https://catalog.redhat.com/search?gs&q=execution%20environments&searchType=containers)
-  [Execution environments](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_automation_execution/assembly-controller-execution-environments#proc-controller-use-an-exec-envi)
-  [Creating and using execution environments](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/creating_and_using_execution_environments/index)


#### 1.2.2.3. Creating and launching a job template




Create and launch a job template to complete the integration and use the automation features in Ansible Automation Platform.

**Procedure**

1. From the navigation panel, select **Automation Execution→Templates** .
1. Select **Create template > Create Job Template** .
1. From the **Execution Environment** list, select the environment you created.
1. From the **Credentials** list, select the credentials instance you created previously. If you do not see the credentials, clickBrowseto see more options in the list.
1. Enter any additional information for the required fields.
1. ClickCreate job template.
1. ClickLaunch template.
1. To launch the job, clickNextandFinish. The job output shows that the job has run.


**Verification**

To see that the job has run successfully from the Terraform user interface, select **Workspaces > Ansible-Content-Integration > Run** . The Run list shows the state of the Triggered via CLI job. You can see it go from the Queued to the Plan Finished state.


**Additional resources**

-  [Adding an execution environment to a job template](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_automation_execution/assembly-controller-execution-environments#proc-controller-use-an-exec-env)
-  [Configuring automation execution](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/configuring_automation_execution/index)
-  [Hashicorp Terraform Enterprise documentation](https://developer.hashicorp.com/terraform/enterprise)


