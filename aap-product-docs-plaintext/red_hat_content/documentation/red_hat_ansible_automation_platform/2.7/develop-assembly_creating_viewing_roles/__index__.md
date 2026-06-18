# Create roles and view roles explanations

You can create roles within Ansible collections using the Ansible VS Code extension. To create roles, use the Ansible VS Code extension, select the **Role Generation** option, and then enter the natural language prompts in English language.

Red Hat Ansible Lightspeed reads the natural language prompts and creates a role recommendation based on your intent. You can also view the explanations for new or existing roles. The role explanations describe what the role does and contextualize its impact.

These capabilities enable Ansible developers to use natural language prompts to create Ansible roles quickly and more efficiently, as well as get an explanation for existing Ansible roles. In addition to generating playbooks, role generation can now further reduce your team’s overall onboarding learning period. For information about Ansible roles, see *Bundle content with Ansible roles* in the *Related Links* section.

Note:

You can create roles and view role explanations when connecting to the Red Hat Ansible Lightspeed cloud service only.

## Create roles within collections

You can use the natural language interface in the Ansible VS Code extension to create one or more roles within an Ansible collection.

### Before you begin

- You meet **one** of the following requirements:
* Your organization has a trial or paid subscription to both the Red Hat Ansible Automation Platform and IBM watsonx Code Assistant.
* Your organization has a trial or paid subscription to the Red Hat Ansible Automation Platform, and you have a Red Hat Ansible Lightspeed trial account.
- You have installed and configured the Ansible VS Code extension v25.3.0 or later. For the procedure, see [Installing and configuring the Ansible VS Code extension](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_install_ansible_vscode_extension#installing-ansible-vscode-extension "Red Hat Ansible Lightspeed with IBM watsonx Code Assistant integrates with the Ansible Visual Studio (VS) Code extension. When enabled, the extension automatically collects recommendations, usage telemetry, and Ansible YAML file state through automated events.").
- You have an existing Ansible environment configured with a valid collection directory within the Ansible VS Code extension.

### Procedure

1.  Log in to VS Code with your Red Hat account.
2.  From the **Activity** bar, click the **Ansible** icon.
3.  Use one of the following methods to create a role:

- **From the Ansible panel**:
1. From the navigation menu, click the **Ansible** icon.
2. Click **Generate a role**.

- **From the Command Palette**:

- From the Command Palette of the VS Code editor, click View> (and then)Command Palette, and then enter **> Ansible Lightspeed: Role generation**. The **Create a role with Ansible Lightspeed** page is displayed on the right panel of the VS Code screen.

4.  From the **Select the collection to create role in** list, choose the collection where you want to create the role. You must have a collection inside your workspace to create a role. If you do not have a collection, you must create it by using one of the following methods:

- By using the following command:         `ansible-creator init collection myns.mycollection my_directory`

After you run the command, open the new directory with VS Code.

- By using the Ansible VS Code extension         For more information, see the topic [About content collections](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/getting_started_with_ansible_automation_platform/assembly-gs-auto-dev#con-gs-learn-about-collections_assembly-gs-auto-dev) in the *Getting started with Ansible Automation Platform* guide.

5.  In the **Describe what you want to achieve in natural language** field, enter the prompts to create a role and then click **Analyze**. After a few seconds, the recommended steps for your role intent are displayed in the **Review the suggested steps for your role and modify as needed** field.

6.  Perform the following tasks:
1.  Review and optionally change the role name.
2.  Review the collection where the role will be created.
3.  Verify that the suggested steps match your intent and then click **Continue**. It takes a few seconds for the role to generate, and the newly generated role is displayed along with the list of files where the role was generated.

Note:

- If you want to modify the steps: Click the editor field, update the prompts or steps to suit your intent, and then click **Continue**.
- If the role suggestions do not match your intent: Click **Back** to change the original prompt and start over.
- If you want to restore to the original suggested steps: Click **Reset** and then click **Continue** to proceed to the next step.

7.  Click **Save files**. A list of files is displayed that includes the new role.
8.  Click the files to open them in the VS Code editor directly.

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
