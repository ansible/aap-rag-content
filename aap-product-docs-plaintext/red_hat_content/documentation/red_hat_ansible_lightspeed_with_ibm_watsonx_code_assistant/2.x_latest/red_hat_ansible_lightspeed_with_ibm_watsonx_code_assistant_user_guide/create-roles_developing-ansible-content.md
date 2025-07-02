# 4. Developing Ansible content
## 4.5. Creating roles and viewing role explanations
### 4.5.1. Creating roles within collections




You can use the natural language interface in the Ansible VS Code extension to create one or more roles within an Ansible collection.

**Prerequisites**

- You meet **one** of the following requirements:


- Your organization has a trial or paid subscription to both the Red Hat Ansible Automation Platform and IBM watsonx Code Assistant.
- Your organization has a trial or paid subscription to the Red Hat Ansible Automation Platform, and you have a Red Hat Ansible Lightspeed trial account.

- You have installed and configured the Ansible VS Code extension v25.3.0 or later. For the procedure, see [Installing and configuring the Ansible VS Code extension](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#con-configure-vs-code-extension_developing-ansible-content) .
- You have an existing Ansible environment configured with a valid collection directory within the Ansible VS Code extension.


**Procedure**

1. Log in to VS Code with your Red Hat account.
1. From the **Activity** bar, click the **Ansible** icon.
1. Use one of the following methods to create a role:


-  **From the Ansible panel** :


1. From the navigation menu, click the **Ansible** icon.
1. Click **Generate a role** .

-  **From the Command Palette** :


- From the Command Palette of the VS Code editor, clickView→Command Palette, and then enter **> Ansible Lightspeed: Role generation** .

The **Create a role with Ansible Lightspeed** page is displayed on the right panel of the VS Code screen.




1. From the **Select the collection to create role in** list, choose the collection where you want to create the role. You must have a collection inside your workspace to create a role.

If you do not have a collection, you must create it by using one of the following methods:


- By using the following command:

`        ansible-creator init collection myns.mycollection my_directory`

After you run the command, open the new directory with VS Code.


- By using the Ansible VS Code extension

For more information, see the topic [About content collections](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/getting_started_with_ansible_automation_platform/assembly-gs-auto-dev#con-gs-learn-about-collections_assembly-gs-auto-dev) in the _Getting started with Ansible Automation Platform_ guide.



1. In the **Describe what you want to achieve in natural language** field, enter the prompts to create a role and then click **Analyze** .

After a few seconds, the recommended steps for your role intent are displayed in the **Review the suggested steps for your role and modify as needed** field.


1. Perform the following tasks:


1. Review and optionally change the role name.
1. Review the collection where the role will be created.
1. Verify that the suggested steps match your intent and then click **Continue** .

It takes a few seconds for the role to generate, and the newly generated role is displayed along with the list of files where the role was generated.

Note

- If you want to modify the steps: Click the editor field, update the prompts or steps to suit your intent, and then click **Continue** .
- If the role suggestions do not match your intent: Click **Back** to change the original prompt and start over.
- If you want to restore to the original suggested steps: Click **Reset** and then click **Continue** to proceed to the next step.




1. Click **Save files** . A list of files is displayed that includes the new role.
1. Click the files to open them in the VS Code editor directly.


