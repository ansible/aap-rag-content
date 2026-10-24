# Permissions reference for Ansible Automation Platform job template access

Permissions for Ansible Automation Platform job templates

| Permission                           | Resource type       | Policy | Description                                                                                             |
| ------------------------------------ | ------------------- | ------ | ------------------------------------------------------------------------------------------------------- |
| `catalog.entity.read`                | catalog-entity      | read   | Users can view synchronized Ansible Automation Platform job templates in the Ansible automation portal. |
| `scaffolder.template.parameter.read` | scaffolder-template | read   | Users can read template parameters.                                                                     |
| `scaffolder.action.execute`          | scaffolder-action   | use    | Users can execute actions through templates.                                                            |
| `scaffolder.task.create`             |                     | create | Users can trigger the execution of Ansible Automation Platform job templates.                           |
| `scaffolder.task.read`               |                     | read   | Users can view task execution history and logs on the **History** page.                                 |
| `scaffolder.task.cancel`             |                     | use    | Users can cancel currently running templates.                                                           |
