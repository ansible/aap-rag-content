# 5. Developing Ansible content
## 5.5. Creating roles and viewing role explanations
### 5.5.2. Viewing the role explanations

You can request explanations for a newly created role as well as an existing Ansible role.

**Prerequisites**

- You meet **one** of the following requirements:


* Your organization has a trial or paid subscription to both the Red Hat Ansible Automation Platform and IBM watsonx Code Assistant.
* Your organization has a trial or paid subscription to the Red Hat Ansible Automation Platform, and you have a Red Hat Ansible Lightspeed trial account.

- You have installed and configured the Ansible VS Code extension v25.3.0 or later. For the procedure, see [Installing and configuring the Ansible VS Code extension](#con-configure-vs-code-extension_developing-ansible-content "5.2.&nbsp;Installing and configuring the Ansible VS Code extension").

- You have opened the role whose explanation you want to view in the VS Code editor.

**Procedure**

1. Log in to VS Code with your Red Hat account.

2. Open an Ansible role YAML file within the roles directory in VS Code.

3. Use one of the following methods to view the playbook explanation:


- **From an active role YAML file**:


1. Place your cursor anywhere within the playbook file.
2. Right-click and select **Explain the role with Ansible Lightspeed**.

- **From the Ansible panel**:


1. From the navigation menu, click the **Ansible** icon.
2. Select **Explain the current playbook**.

- **From the Command Palette**:


* From the Command Palette of the VS Code editor, enter **Explain the role with Ansible Lightspeed**.

The role explanation is displayed on the right panel of the VS Code screen.

The following illustration shows an example of a role explanation:

**Figure 5.6. Example of a role explanation**


![Example of a role explanation](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant-2.x_latest-Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant_User_Guide-en-US/images/98612898618da5b54f0c355a4303d127/lightspeed-playbook-explanation.png)

