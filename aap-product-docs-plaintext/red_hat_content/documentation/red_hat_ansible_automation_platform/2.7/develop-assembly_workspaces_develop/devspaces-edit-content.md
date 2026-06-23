# Develop automation content in your workspace
## Edit and debug automation content in your Ansible development workspace

You can continue to work in an existing workspace. Workspaces that are inactive might be paused due to an administrator-set timeout to free up resources. However, they will automatically relaunch when you select them from the OpenShift Dev Spaces dashboard.

### About this task

The administrator in OpenShift Dev Spaces configures the duration of this inactivity timeout. Additionally, Ansible lint will identify errors within your playbooks.

### Procedure

1.  To display your previously created workspaces, select **Workspaces** in your OpenShift Dev Spaces dashboard.
2.  Select **Open** next to the workspace that you want to use.
3.  Select the **Explorer** icon in the **Activity** bar to open the file explorer, and open the file you want to edit.
4.  While you are editing, the Ansible extension provides suggestions. Select a suggestion from the dropdown list to include it in your playbook.
5.  To view documentation for a keyword or a module, hover your mouse over it.
6.  Open the terminal in VS Code: click the main menu icon in the **Activity** bar and select Terminal> (and then)New Terminal.
7.  Select the **Problems** tab in the terminal to view issues that `ansible-lint` has identified. In the following example, one error is selected in the **Problems** tab, and the corresponding line in the playbook is highlighted.


![Playbook and ansible-lint messages](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/playbook.png)

8.  When you have resolved the problems in your playbook, a message is displayed in the **Problems** tab of the terminal.

