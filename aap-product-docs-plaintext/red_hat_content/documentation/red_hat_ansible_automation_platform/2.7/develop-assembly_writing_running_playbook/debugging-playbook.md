# Write your first automation task using the VS Code extension
## Debug your playbook

Learn how to use VS Code to identify and understand error messages in playbooks.

### Procedure

1.  The following playbook contains multiple errors. Copy and paste it into a new file in VS Code.

```
- name:
hosts: localhost
tasks:
- name:
ansible.builtin.ping:
```
The errors are indicated with a wavy underline in VS Code.

2.  Hover your mouse over an error to view the details:
![Popup message explaining a playbook error](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ansible-lint-errors.png)
3.  Playbook files that contain errors are indicated with a number in the **Explorer** pane.
4.  Select the **Problems** tab of the VS Code terminal to view a list of the errors.
![Playbook errors shown in Problems tab and explorer list](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ansible-lint-errors-explorer.png)
`$[0].tasks[0].name None is not of type 'string'` indicates that the playbook does not have a label.
