# Develop automation content in your workspace
## Create collections and playbooks in your Ansible development workspace

Use the Ansible extension in VS Code to use Ansible development tools to scaffold directories and files for your automation content. You can use Red Hat Ansible Lightspeed with IBM watsonx Code Assistant to help you write playbooks, and `ansible-lint` to debug them.

### About this task

### Procedure

1.  In the OpenShift Dev Spaces dashboard. select the Ansible development workspace where you want to develop automation content.
2.  In the **Activity** bar of VS Code, select the Ansible icon to open Ansible development tools.
3.  Select **Connect** in the Ansible Lightspeed section to log in to Ansible Lightspeed.
4.  Select an option in the **initialize** section of **Ansible Development tools** to scaffold files and directories for a collection project or a playbook project. For more information on creating projects, see:

- Scaffold a playbook project in [Auto-generate the structure and files for your automation project](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_creating_playbook_project#creating-playbook-project "Use the Ansible Automation Platform VS Code extension to scaffold a new Ansible playbook project. This process creates the necessary directory structure and configuration files, preparing your environment for playbook development.")
- Scaffold a collection for your roles in [Package and distribute automation content with collections](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-devtools_develop_collections#devtools-develop-collections "Collections are a distribution format for Ansible content that can include playbooks, roles, modules, and plugins. Red Hat provides Ansible Content Collections on Ansible automation hub that contain both Red Hat Ansible Certified Content and Ansible validated content.")

5.  Select options in the **Add** section of Ansible development tools to add files for playbooks or roles to your project. Alternatively, you can use the options in the **Ansible Lightspeed** section to generate playbooks or roles.
6.  Save your work:
1.  Click the main menu icon in the **Activity** bar and select Terminal> (and then)New Terminal.
2.  Use `git add` and `git commit` commands to stage the changed files and commit your changes to the local repository in the workspace.
3.  Use the `git push` command to push your updates to your remote Git repository.

