# Set up initial RBAC rules in Ansible automation portal
## Permissions reference for Ansible Automation Platform job template access

Permissions for Ansible Automation Platform job templates

| Permission                                | Resource type           | Policy     | Description                                                                                                 |
| ----------------------------------------- | ----------------------- | ---------- | ----------------------------------------------------------------------------------------------------------- |
| <br> `catalog.entity.read`                | <br>catalog-entity      | <br>read   | <br>Users can view synchronized Ansible Automation Platform job templates in the Ansible automation portal. |
| <br> `scaffolder.template.parameter.read` | <br>scaffolder-template | <br>read   | <br>Users can read template parameters.                                                                     |
| <br> `scaffolder.action.execute`          | <br>scaffolder-action   | <br>use    | <br>Users can execute actions through templates.                                                            |
| <br> `scaffolder.task.create`             |                         | <br>create | <br>Users can trigger the execution of Ansible Automation Platform job templates.                           |
| <br> `scaffolder.task.read`               |                         | <br>read   | <br>Users can view task execution history and logs on the **History** page.                                 |
| <br> `scaffolder.task.cancel`             |                         | <br>use    | <br>Users can cancel currently running templates.                                                           |

