# Create playbooks and view playbook explanations
## View the playbook explanations

You can request explanations for a newly created playbook as well as an existing Ansible playbook.

### Before you begin

- You meet **one** of the following requirements:
* Your organization has a trial or paid subscription to both the Red Hat Ansible Automation Platform and IBM watsonx Code Assistant.
* Your organization has a trial or paid subscription to the Red Hat Ansible Automation Platform, and you have a Red Hat Ansible Lightspeed trial account.
- You have [installed and configured the Ansible VS Code extension](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_install_ansible_vscode_extension#installing-ansible-vscode-extension "Red Hat Ansible Lightspeed with IBM watsonx Code Assistant integrates with the Ansible Visual Studio (VS) Code extension. When enabled, the extension automatically collects recommendations, usage telemetry, and Ansible YAML file state through automated events.").
- You have opened the playbook whose explanation you want to view.

### Procedure

1.  Log in to VS Code with your Red Hat account.
2.  Open an Ansible playbook YAML file in VS Code.
3.  Use one of the following methods to view the playbook explanation:

- **From an active playbook YAML file**:
1. Place your cursor anywhere within the playbook file.
2. Right-click and select **Explain the playbook with Ansible Lightspeed**.
- **From the Ansible panel**:
1. From the navigation menu, click the **Ansible** icon.

2. Select **Explain the current playbook**. The playbook explanation is displayed on the right panel of the VS Code screen.

The following illustration shows an example of a playbook explanation:

*Figure 2. Example of a playbook explanation*

![Example of a playbook explanation](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/lightspeed-playbook-explanation.png)
