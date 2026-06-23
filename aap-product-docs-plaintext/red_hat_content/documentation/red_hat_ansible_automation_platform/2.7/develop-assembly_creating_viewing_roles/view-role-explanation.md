# Create roles and view roles explanations
## View the role explanations

You can request explanations for a newly created role as well as an existing Ansible role.

### Before you begin

- You meet **one** of the following requirements:
* Your organization has a trial or paid subscription to both the Red Hat Ansible Automation Platform and IBM watsonx Code Assistant.
* Your organization has a trial or paid subscription to the Red Hat Ansible Automation Platform, and you have a Red Hat Ansible Lightspeed trial account.
- You have installed and configured the Ansible VS Code extension v25.3.0 or later. For the procedure, see [Installing and configuring the Ansible VS Code extension](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_install_ansible_vscode_extension#installing-ansible-vscode-extension "Red Hat Ansible Lightspeed with IBM watsonx Code Assistant integrates with the Ansible Visual Studio (VS) Code extension. When enabled, the extension automatically collects recommendations, usage telemetry, and Ansible YAML file state through automated events.").
- You have opened the role whose explanation you want to view in the VS Code editor.

### Procedure

1.  Log in to VS Code with your Red Hat account.
2.  Open an Ansible role YAML file within the roles directory in VS Code.
3.  Use one of the following methods to view the playbook explanation:

- **From an active role YAML file**:
1. Place your cursor anywhere within the playbook file.
2. Right-click and select **Explain the role with Ansible Lightspeed**.
- **From the Ansible panel**:
1. From the navigation menu, click the **Ansible** icon.
2. Select **Explain the current playbook**.
- **From the Command Palette**:
* From the Command Palette of the VS Code editor, enter **Explain the role with Ansible Lightspeed**. The role explanation is displayed on the right panel of the VS Code screen.

The following illustration shows an example of a role explanation:

*Figure 1. Example of a role explanation*

![Example of a role explanation](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/lightspeed-playbook-explanation.png)
