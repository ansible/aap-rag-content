# Install and configure VS Code

Install VS Code by following the instructions found on the Download Visual Studio Code page in the official documentation.

## About this task

## Procedure

To install VS Code, follow the instructions on the [Download Visual Studio Code page](https://code.visualstudio.com/download) in the Visual Studio Code documentation.

## Install the VS Code Ansible extension

The Ansible extension adds language support for Ansible to VS Code. It incorporates Ansible development tools to facilitate creating and running automation content.

### About this task

For a full description of the Ansible extension, see the [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/items?itemName=redhat.ansible).

### Procedure

1.  Open VS Code.
2.  Click the **Extensions** (![Extensions](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/vscode-extensions-icon.png)) icon in the Activity Bar, or click View> (and then)Extensions, to display the **Extensions** view.
3.  In the search field in the **Extensions** view, type `Ansible Red Hat`.
4.  Select the Ansible extension and click Install.

### Results

When the language for a file is recognized as Ansible, the Ansible extension provides features such as auto-completion, hover, diagnostics, and goto. The language identified for a file is displayed in the Status bar at the bottom of the VS Code window.

The following files are assigned the Ansible language:

- YAML files in a `/playbooks` directory
- Files with the following double extension: `.ansible.yml` or `.ansible.yaml`
- Certain YAML names recognized by Ansible, for example `site.yml` or `site.yaml`
- YAML files whose filename contains "playbook": `playbook.yml` or `playbook.yaml`

If the extension does not identify the language for your playbook files as Ansible, follow the procedure in [Associating the Ansible language to YAML files](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_devtools_install "You have two options for installing Ansible development tools, so that you can choose the installation method that best suits your preferred operating system and development environment.").

## Configure Ansible extension settings

The Ansible extension supports multiple configuration options.

### Before you begin

- Open a workspace or folder, or create a new folder, in VS Code using the File> (and then)Open Folder menu. This is necessary because the file that stores settings preferences for workspaces is specific to a folder or workspace.

### About this task

You can configure the settings for the extension on a user level, on a workspace level, or for a particular directory. User-based settings are applied globally for any instance of VS Code that is opened. A VS Code workspace is a collection of one or more folders that you can open in a single VS Code window. Workspace settings are stored within your workspace and only apply when the current workspace is opened.

It is useful to configure settings for your workspace for the following reasons:

- If you define and maintain configurations specific to your playbook project, you can customize your Ansible development environment for individual projects without altering your preferred setup for other work. You can have different settings for a Python project, an Ansible project, and a C++ project, each optimized for the respective stack without the need to manually reconfigure settings each time you switch projects.
- If you include workspace settings when setting up version control for a project you want to share with your team, everyone uses the same configuration for that project.

### Procedure

1.  Open the Ansible extension settings:
1.  Click the ![Extensions](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/vscode-extensions-icon.png)**Extensions** icon in the activity bar.
2.  Select the Ansible extension, and click the 'gear' icon and then **Extension Settings** to display the extension settings.     - Alternatively, click Code> (and then)Settings> (and then)Settings to open the **Settings** page.

3.  Enter `Ansible` in the search bar to display the settings for the extension.
2.  Select the **Workspace** tab to configure your settings for the current VS Code workspace.   - If the **Workspace** tab is not displayed, open a folder or create a new folder using the File> (and then)Open Folder menu.

3.  The Ansible extension settings are pre-populated. Modify the settings to suit your requirements:

- Check the Ansible> (and then)Validation> (and then)Lint: Enabled box to enable ansible-lint.
- Check the `Ansible Execution Environment: Enabled` box to use an execution environment.
- Specify the execution environment image you want to use in the **Ansible > Execution Environment: image** field.
- To use Red Hat Ansible Lightspeed, check the **Ansible > Lightspeed: Enabled** box, and enter the URL for Lightspeed.
