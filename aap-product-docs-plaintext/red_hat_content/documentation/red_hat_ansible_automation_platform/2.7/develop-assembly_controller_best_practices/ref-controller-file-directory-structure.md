# Best practices for automation execution
## Ansible file and directory structure

Follow recommended directory structures for Ansible projects to organize playbooks, inventories, and variables. A consistent layout improves maintainability and scaling.

To ensure reliable and consistent automation, follow these best practices for managing your content:

- Package reusable content, such as roles, modules, and plugins into Ansible Collections.
- Reference all necessary Collections for a project in the project’s `requirements.yml` file. These dependencies are automatically installed into the execution environment (EE) at runtime, but only if they are not already present in the EE image.
- Do not import content from other projects or common file-system locations, such as `/opt`, at runtime. All content must be explicitly defined within the EE.
- Working directory: The playbook directory is used as the current working directory at runtime. However, always use the `playbook_dir` variable instead of relying on the current working directory path.


Warning:

Automation controller does not support interactive features.

- Avoid using the `vars_prompt` feature, as automation controller does not permit interactive questions. For user input, use [Surveys in job templates](/documentation/en-us/red_hat_ansible_automation_platform/2.7/get_started-assembly_gs_auto_op#controller-surveys-in-job-templates "Surveys provide a way to prompt users for input when launching a job from a job template. This input can then be used as variables in the playbook run.").
- Do not use the `pause` feature without a timeout. Automation controller does not permit canceling a pause interactively. If `pause` is necessary, you must set a timeout.

