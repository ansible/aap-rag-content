# Scaffold an Ansible project with the AI assistant
## Create the project structure
### Procedure

1.  In the Copilot chat window, enter a prompt specifying the project name and type. For example:


```
Create a new Ansible playbook project called 'webserver-deployment'.
```
This triggers the `create_ansible_projects`tool.

The extension executes `ansible-creator init playbook`and generates the content.

2.  Verify that the generated structure is consistent with the standard layout by navigating to the VS Code Explorer view and locating the new directory (`webserver-deployment`)
3.  Confirm the presence of standard artifacts like:
1.  Initial playbook files.
2.  Recommended configuration files (such as `ansible.cfg` or `inventory`).

