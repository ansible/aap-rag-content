# Ansible development tools components and workflow

You can operate some Ansible development tools from the VS Code UI when you have installed the Ansible extension, and the remainder from the command line. VS Code is a free open-source code editor available on Linux, Mac, and Windows.

Ansible VS Code extension
This is not packaged with the Ansible Automation Platform RPM package, but it is an integral part of the automation creation workflow. From the VS Code UI, you can use the Ansible development tools for the following tasks:

- Scaffold directories for a playbook project or a collection.
- Write playbooks with the help of syntax highlighting and auto-completion.
- Debug your playbooks with a linter.
- Execute playbooks with Ansible Core using `ansible-playbook`.
- Execute playbooks in an execution environment with `ansible-navigator`.

From the VS Code extension, you can also connect to Red Hat Ansible Lightspeed with IBM watsonx Code Assistant.

Command-line Ansible development tools
You can perform the following tasks with Ansible development tools from the command line, including the terminal in VS Code:

- Create an execution environment.
- Test your playbooks, roles, modules, plugins and collections.

## Development workflow

The development workflow for automation content includes three stages: Create, Test, and Deploy. Follow these stages to successfully manage and publish your automation.

### Workflow

The workflow for developing automation content involves three key stages: Create, Test, and Deploy.

#### Create

In the create stage, you create a new playbook project locally, using VS Code. The following is a typical workflow:

1. Install and run the Ansible extension in VS Code.
2. Scaffold a playbook project from VS Code.
3. Add playbook files to your project and edit them in VS Code.

#### Test

1. Debug your playbook with the help of `ansible-lint`.
2. Select or create an automation execution environment so that your local environment replicates the environment on Ansible Automation Platform.
3. Run your playbooks from VS Code, using `ansible-playbook` or using `ansible-navigator` with an execution environment.
4. Test your playbooks by running them on an execution environment that replicates your production environment.

#### Deploy

1. Push your playbooks project to a source control repository.
2. Set up credentials on Ansible Automation Platform to pull from your source control repository and create a project for your playbook repository.
3. If you have created an execution environment, push it to private automation hub.
4. Create a job template on Ansible Automation Platform that runs a playbook from your project, and specify the execution environment that you want to use.
