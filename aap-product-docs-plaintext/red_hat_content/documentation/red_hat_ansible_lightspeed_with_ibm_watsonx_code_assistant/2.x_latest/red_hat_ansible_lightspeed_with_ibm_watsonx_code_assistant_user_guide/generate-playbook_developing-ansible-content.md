# 5. Developing Ansible content
## 5.4. Creating playbooks and viewing playbook explanations
### 5.4.2. Generating Ansible playbooks




You can use the natural language interface in the Ansible VS Code extension to generate an entire Ansible playbook.

**Prerequisites**

- You meet **one** of the following requirements:


- Your organization has a trial or paid subscription to both the Red Hat Ansible Automation Platform and IBM watsonx Code Assistant.
- Your organization has a trial or paid subscription to the Red Hat Ansible Automation Platform, and you have a Red Hat Ansible Lightspeed trial account.

- You have [installed and configured the Ansible VS Code extension](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#con-configure-vs-code-extension_developing-ansible-content) .


**Procedure**

1. Log in to VS Code with your Red Hat account.
1. From the **Activity** bar, click the **Ansible** icon.
1. Under **Ansible Creator** , click **Get started** . The **Ansible Content Creator** page is displayed.

The following illustration displays the **Ansible Content Creator** page:


<span id="idm139735362103888"></span>
**Figure 5.4. Settings to create Ansible playbooks**

![Settings to create Ansible playbooks](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant-2.x_latest-Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant_User_Guide-en-US/images/3b146832bd21067bd296aede46dc35f5/lightspeed-create-ansible-content.png)





1. Select the **Playbook with Ansible Lightspeed** tile. The **Create a playbook** page is displayed.
1. In the **What do you want the playbook to accomplish?** field, enter the prompts to create a playbook and click **Analyze** .

After a few seconds, the recommended steps for your playbook intent are displayed in the **Review the suggested steps for your playbook and modify as needed** field.


1. Perform one of the following tasks:


- If the steps match your intent: Click **Generate Playbook** .
- If any modifications are required: Click the editor and update the tasks or steps to suit your intent.
- If the task suggestions do not match your intent: Click **Back** to change the original prompt and start over.
- If you want to restore the original task suggestions: Click **Reset** and proceed to the next step.

1. After you verify the steps, click **Generate playbook** .

It takes a few seconds for the playbook to generate, and **The following playbook was generated for you** field displays the newly generated playbook.


1. Click **Open editor** . The generated playbook opens as an untitled YAML file in the VS Code editor.
1. Save the untitled YAML file.


