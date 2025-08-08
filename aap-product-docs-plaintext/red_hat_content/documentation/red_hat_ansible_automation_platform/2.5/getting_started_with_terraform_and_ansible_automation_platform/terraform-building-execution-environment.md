# 2. Integrating from Ansible Automation Platform
## 2.2. Building an execution environment in Ansible Automation Platform




You must build an execution environment using the automation controller so that Ansible Automation Platform can provide the credentials necessary for using its automation features.

**Prerequisites**

- You need a pre-existing execution environment with the latest version of `    cloud.terraform` collection before you can create it using an automation controller. You cannot use the default execution environment provided by Ansible Automation Platform because the default environment does not include the `    terraform` CLI binary.

Note
If you have migrated from Terraform Community, you can continue to use your existing execution environment and update it to the latest version of `    cloud.terraform` .




- Install the `    terraform` CLI binary in your pre-existing execution environment. See **Additional resources** below for a link to the binary.


**Procedure**

1. From the navigation panel, select **Automation Execution→Infrastructure→Execution Environments** .
1. ClickCreate execution environment.

![Create a new execution environment page](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Getting_started_with_Terraform_and_Ansible_Automation_Platform-en-US/images/f7d2791d8333c610068f841478dc5bab/ee-create-new.png)



1. For **Name** , enter a name for your Ansible Automation Platform execution environment.
1. For **Image** , enter the repository link to the image for your pre-existing execution environment.
1. ClickCreate execution environment. Your newly added execution environment is ready to be used in a job template.


**Additional resources**

-  [terraform CLI binary](https://developer.hashicorp.com/terraform/install)
-  [Red Hat ecosystem catalog](https://catalog.redhat.com/search?gs&q=execution%20environments&searchType=containers)
-  [Execution environments](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/assembly-controller-execution-environments#proc-controller-use-an-exec-envi)
-  [Creating and using execution environments](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/creating_and_using_execution_environments/index)


