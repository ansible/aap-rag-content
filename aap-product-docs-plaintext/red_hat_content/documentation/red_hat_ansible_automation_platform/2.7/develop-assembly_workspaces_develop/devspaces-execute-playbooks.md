# Develop automation content in your workspace
## Execute playbooks in your Ansible development workspace

Execute your playbooks using the integrated Ansible extension or `ansible-navigator` within the VS Code environment of your workspace.

### About this task

With the introduction of full container-in-container support, you can seamlessly use execution environments within Ansible development workspaces. Tools such as `ansible-navigator` and `ansible-builder` are fully supported for executing playbooks and building custom execution environments directly from your browser-based workspace.

### Procedure

1.  To execute a playbook using the Ansible extension, right-click on a playbook name in the file explorer and select Run ansible playbook via> (and then)Run ansible playbook via ansible playbook.
2.  Alternatively, to execute a playbook using `ansible-navigator` with an execution environment, open a terminal in VS Code and run:


```
ansible-navigator run *your_playbook.yml*
```

