# 4. Scaffolding an Ansible project with the AI assistant
## 4.3. Create the project structure with the AI assistant




Enter a prompt in natural language to trigger the project creation tool. When prompted, `ansible-creator` works in the background to generate the directory structure.

**Procedure**

1. In the Copilot chat window, enter a prompt specifying the project name and type. For example:


-  _Create a new Ansible playbook project called `webserver-deployment.`_

This triggers the `        create_ansible_projects` tool. The extension then executes `        ansible-creator init playbook` to generate the content.





**Verification**

After the assistant confirms that the task is complete, verify that the project structure is consistent with the standard layout.


1. Navigate to the VS Code Explorer view.
1. Locate the new directory (per the example above, `    webserver-deployment/` ).
1. Confirm the presence of standard artifacts such as:


1. Initial playbook files.
1. Recommended configuration files (such as `        ansible.cfg` , `        inventory` ).



