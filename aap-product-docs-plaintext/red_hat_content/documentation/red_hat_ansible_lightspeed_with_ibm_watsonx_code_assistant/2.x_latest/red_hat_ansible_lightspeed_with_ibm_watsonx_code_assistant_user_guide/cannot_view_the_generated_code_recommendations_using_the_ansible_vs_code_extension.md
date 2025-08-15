# 7. Troubleshooting
## 7.2. Troubleshooting Ansible Visual Studio Code extension errors
### 7.2.1. Cannot view the generated code recommendations using the Ansible VS Code extension




The following scenarios are possible:

- You receive a `    403 error` message.

To resolve this error, ensure that:


- Your organization administrator has configured Red Hat Ansible Lightspeed for your organization.
- You meet **one** of the following requirements:


- Your organization has a trial or paid subscription to both the Red Hat Ansible Automation Platform and IBM watsonx Code Assistant.
- Your organization has a trial or paid subscription to the Red Hat Ansible Automation Platform, and you have a Red Hat Ansible Lightspeed trial account.


- You have not configured the required Ansible VS code extension settings.


- To resolve this error, ensure that you have enabled the **Lightspeed:Enabled** andLightspeed→Suggestions:Enabledsettings. For more information, see [Configure the Ansible VS Code extension](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#configure-vscode-extension_developing-ansible-content) .

- You receive a `    Failure on completion requests` error when you make inference requests in VS Code.

If you are part of an organization that has a trial or paid subscription to both Ansible Automation Platform and IBM watsonx Code Assistant, but your organization administrator has not configured an IBM watsonx Code Assistant model for your organization, you will encounter a `    Failure on completion requests` error when you make inference requests in VS Code.


- You receive an `    Ansible Lightspeed encountered an error. Try again after some time.` error message when you make single-task or multitask requests.

This error occurs when you use a remote SSH extension with VS Code to request single or multitask recommendations in playbooks. However, the task recommendations are generated when using a role. This error occurs in workspaces that contain a large number of roles.


- Your VS Code Workspace settings override user settings.

If your Workspace settings are configured, they can override our user settings even if you have configured the Ansible VS Code extension correctly. The Workspace settings can disable your VS Code extension settings, and therefore you cannot access the Ansible Lightspeed service.

To resolve this error, ensure that there are no Workspace settings configured in VS Code. For more information, see [Workspace settings](https://code.visualstudio.com/docs/getstarted/settings#_workspace-settings) in the VS Code documentation.


- You entered a multitask prompt, but code recommendations were not generated.

To resolve this error, log out of VS Code and log in again using your Red Hat account.


- You clicked a different location or switched to a different window; therefore, the populated code recommendations disappeared.

The Red Hat Ansible Lightspeed service could take multiple seconds per task to populate the code recommendations. If you are using a multitask prompt, the Red Hat Ansible Lightspeed service takes a bit longer to populate the results. Do not move your cursor or press any key while the code recommendation is being generated. If you change the cursor location or press any key, the Ansible VS Code extension cancels the request and the Red Hat Ansible Lightspeed service does not process your request. In this scenario, you must get the cursor back to its original position and repopulate the results.




