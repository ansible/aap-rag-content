+++
title = "Develop automation content in your workspace - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_workspaces_develop"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_workspaces_develop/", "Develop automation content in your workspace"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-assembly_workspaces_develop/aem-page/develop-assembly_workspaces_develop.html"
last_crumb = "Develop automation content in your workspace"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Develop automation content in your workspace"
oversized = "false"
page_slug = "develop-assembly_workspaces_develop"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-assembly_workspaces_develop"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-assembly_workspaces_develop/toc/toc.json"
type = "aem-page"
+++

# Develop automation content in your workspace

The Ansible development tools are installed as part of the Ansible extension in the Ansible development workspace. You can use Ansible development tools to scaffold directories for automation content in your repository.

Using the Ansible extension ensures that best practices for directory structure are met.

Red Hat recommends that you create only one collection per repository, so that each collection has a clear, specific purpose. This approach promotes reusability, as each collection is a self-contained unit of content. A one-to-one relationship between a collection and its repository also improves manageability by simplifying dependency management, maintenance, and release cycles.

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

## Edit and debug automation content in your Ansible development workspace

You can continue to work in an existing workspace. Workspaces that are inactive might be paused due to an administrator-set timeout to free up resources. However, they will automatically relaunch when you select them from the OpenShift Dev Spaces dashboard.

### About this task

The administrator in OpenShift Dev Spaces configures the duration of this inactivity timeout. Additionally, Ansible lint will identify errors within your playbooks.

### Procedure

1.  To display your previously created workspaces, select **Workspaces** in your OpenShift Dev Spaces dashboard.
2.  Select **Open** next to the workspace that you want to use.
3.  Select the **Explorer** icon in the **Activity** bar to open the file explorer, and open the file you want to edit.
4.  While you are editing, the Ansible extension provides suggestions. Select a suggestion from the dropdown list to include it in your playbook.
5.  To view documentation for a keyword or a module, hover your mouse over it.
6.  Open the terminal in VS Code: click the main menu icon in the **Activity** bar and select Terminal> (and then)New Terminal.
7.  Select the **Problems** tab in the terminal to view issues that `ansible-lint` has identified. In the following example, one error is selected in the **Problems** tab, and the corresponding line in the playbook is highlighted.


![Playbook and ansible-lint messages](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/playbook.png)  

8.  When you have resolved the problems in your playbook, a message is displayed in the **Problems** tab of the terminal.

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

## Configure ansible-navigator for execution environments

Customize `ansible-navigator` settings in your Ansible development workspace to configure execution environment options, logging, and output format.

### About this task

The `ansible-navigator` tool uses a YAML configuration file to define settings for execution environments, container engines, and output behavior. An example `ansible-navigator.yaml` file is available in the [Ansible Development Workspace Sample](https://github.com/redhat-cop/ansible-devspaces) repository.

### Procedure

1.  In your Ansible development workspace, create a file named `ansible-navigator.yaml` in the root of your project directory.
2.  Add the following minimal configuration and modify it to suit your requirements:
  

```
ansible-navigator:
  execution-environment:
    container-engine: podman
  logging:
    level: critical
  playbook-artifact:
    enable: false
```
    The Ansible dev spaces image includes a default execution environment. You only need to add additional settings such as `environment-variables`, `volume-mounts`, or `container-options` if your project requires them.

3. **Optional:** To override the default execution environment image, add the `image` setting under the `execution-environment` section:
  

```
execution-environment:
  image: registry.redhat.io/ansible-automation-platform-27/ee-supported-rhel9:latest
```

4.  Save the file. The `ansible-navigator` tool automatically loads the configuration from the current working directory or from the default locations.
      For more information about `ansible-navigator` settings, see [ansible-navigator settings](https://docs.ansible.com/projects/navigator/settings) in the ansible-navigator documentation.

## Share your work

Share your automation content and collaborate with colleagues by working together from a single shared Git repository and submitting pull requests.

### About this task

### Procedure

1.  To contribute to a colleague's project, request the URL for the Git repository that corresponds to your colleague's Ansible development workspace.
2.  Launch a workspace using the repository URL that your colleague shared.
3.  Work within a new git branch and contribute to your colleague's repository by creating a merge or pull request.
