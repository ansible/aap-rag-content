# Create and launch an Ansible development workspace
## Launch an Ansible dev spaces workspace

Launch your Ansible development workspace by providing the URL for your prepared Git repository in the OpenShift Dev Spaces dashboard. This opens your VS Code environment in a browser.

### Before you begin

- Your administrator has provided a URL for a OpenShift Dev Spaces dashboard.
- You have prepared a git repository that contains the `devfile.yaml` and `.code-workspace` files that define the Ansible development workspace configuration.

### About this task

### Procedure

1.  In a browser, navigate to the OpenShift Dev Spaces dashboard and log in.
2.  Select **Create Workspace** in the navigation pane.
3.  In the **Import from Git** field of the **Create Workspace** form, enter the URL for the Git repository that contains your `devfile.yaml` and `.code-workspace` files.
4.  Click **Create & Open**.
5.  OpenShift Dev Spaces displays the progress for the provisioning process of your Ansible development workspace.
![Workspace provisioning progress](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/devtools-workspaces-provisioning.png)
After the Ansible development workspace launches, a VS Code environment opens in your browser.

6.  To open a terminal for executing commands and viewing `ansible-lint` suggestions in VS Code, click the main menu icon in the **Activity** bar and select Terminal> (and then)New Terminal.
For more information about working in a VS Code terminal, see [Getting started with the terminal](https://code.visualstudio.com/docs/terminal/getting-started) in the VS Code documentation.
