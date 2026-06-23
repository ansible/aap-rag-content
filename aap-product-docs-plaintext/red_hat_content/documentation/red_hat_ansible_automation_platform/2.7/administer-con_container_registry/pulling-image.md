# Manage containers in your private automation hub
## Pull an image

Use the user interface to pull an execution environment from your private automation hub remote registry to make a copy to your local machine.

### Before you begin

- You must have permission to view and pull from a private container repository.
- If you are pulling automation execution environments from a password or token-protected registry, [create a credential](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-manage_execution_environments_in_private_automation_hub#GUID-c616972e-1012-4d50-a64b-dc38f0d5105b "When you set up your container repository, you can add a description, include a README, add teams that can access the repository, and tag automation execution environments.") first.

### Procedure

1.  From the navigation panel, select Automation Content> (and then)Execution Environments.
2.  Select your execution environment.
3.  In the **Pull this image** entry, click Copy to clipboard.
4.  Paste and run the command in your terminal.

### Results

- Run `podman images` to view images on your local machine.

