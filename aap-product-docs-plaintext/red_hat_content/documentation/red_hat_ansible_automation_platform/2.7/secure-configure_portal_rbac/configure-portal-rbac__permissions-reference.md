# Configure role-based access control for Ansible automation portal
## Permissions reference

| Permission                            | Resource type       | Policy | Description                                                                   |
| ------------------------------------- | ------------------- | ------ | ----------------------------------------------------------------------------- |
| `catalog.entity.read`                 | catalog-entity      | read   | View synchronized AAP job templates in the Ansible automation portal catalog. |
| `scaffolder.template.parameter.read`  | scaffolder-template | read   | Read template parameters in the launch wizard.                                |
| `scaffolder.template.step.read`       | scaffolder-template | read   | Read template steps in the launch wizard.                                     |
| `scaffolder.action.execute`           | scaffolder-action   | use    | Execute actions through templates.                                            |
| `scaffolder.task.create`              | scaffolder-task     | create | Trigger the execution of job templates.                                       |
| `scaffolder.task.read`                | scaffolder-task     | read   | View task execution history and logs on the **History** page.                 |
| `scaffolder.task.cancel`              | scaffolder-task     | use    | Cancel running templates.                                                     |
| `ansible.templates.view`              | —                   | —      | Show the **Templates** sidebar item and pages. Required for all portal users. |
| `ansible.history.view`                | —                   | —      | Show the **History** sidebar item and pages. Required for all portal users.   |
| `ansible.execution-environments.view` | —                   | —      | Show the **Execution Environments** sidebar item and pages.                   |
| `ansible.collections.view`            | —                   | —      | Show the **Collections** sidebar item and pages.                              |
| `ansible.git-repositories.view`       | —                   | —      | Show the **Git Repositories** sidebar item and pages.                         |

