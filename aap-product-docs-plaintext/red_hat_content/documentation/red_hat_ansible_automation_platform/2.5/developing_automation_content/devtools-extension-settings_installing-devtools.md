# 3. Installing Ansible development tools
## 3.1. Requirements
### 3.1.5. Configuring Ansible extension settings




The Ansible extension supports multiple configuration options.

You can configure the settings for the extension on a user level, on a workspace level, or for a particular directory. User-based settings are applied globally for any instance of VS Code that is opened. A VS Code workspace is a collection of one or more folders that you can open in a single VS Code window. Workspace settings are stored within your workspace and only apply when the current workspace is opened.

It is useful to configure settings for your workspace for the following reasons:

- If you define and maintain configurations specific to your playbook project, you can customize your Ansible development environment for individual projects without altering your preferred setup for other work. You can have different settings for a Python project, an Ansible project, and a C++ project, each optimized for the respective stack without the need to manually reconfigure settings each time you switch projects.
- If you include workspace settings when setting up version control for a project you want to share with your team, everyone uses the same configuration for that project.


**Prerequisites**

- Open a workspace or folder, or create a new folder, in VS Code using theFile→Open Foldermenu. This is necessary because the file that stores settings preferences for workspaces is specific to a folder or workspace.


**Procedure**

1. Open the Ansible extension settings:


1. Click the![Extensions](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Developing_automation_content-en-US/images/417ed5315a44493c6a44ae5c12dc6fab/vscode-extensions-icon.png)
**Extensions** icon in the activity bar.
1. Select the Ansible extension, and click the 'gear' icon and then **Extension Settings** to display the extension settings.


- Alternatively, clickCode→Settings→Settingsto open the **Settings** page.

1. Enter `        Ansible` in the search bar to display the settings for the extension.

1. Select the **Workspace** tab to configure your settings for the current VS Code workspace.


- If the **Workspace** tab is not displayed, open a folder or create a new folder using theFile→Open Foldermenu.

1. The Ansible extension settings are pre-populated. Modify the settings to suit your requirements:


- Check theAnsible→Validation→Lint: Enabledbox to enable ansible-lint.
- Check the `        Ansible Execution Environment: Enabled` box to use an execution environment.
- Specify the execution environment image you want to use in the **Ansible > Execution Environment: image** field.
- To use Red Hat Ansible Lightspeed, check the **Ansible > Lightspeed: Enabled** box, and enter the URL for Lightspeed.



**Additional resources**

-  [Ansible VS Code Extension by Red Hat page](https://marketplace.visualstudio.com/items?itemName=redhat.ansible)
-  [What is a VS Code workspace?](https://code.visualstudio.com/docs/editing/workspaces/workspaces)


