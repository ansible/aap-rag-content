+++
title = "Develop automation content in your workspace - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-assembly_workspaces_develop"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-technology_preview/", "Technology Preview"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-assembly_workspaces_develop/aem-page/whats_new-assembly_workspaces_develop.html"
last_crumb = "Develop automation content in your workspace"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Develop automation content in your workspace"
oversized = "false"
page_slug = "whats_new-assembly_workspaces_develop"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/whats_new-assembly_workspaces_develop"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-assembly_workspaces_develop/toc/toc.json"
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

  - Scaffold a playbook project in [Auto-generate the structure and files for your automation project](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_creating_playbook_project#creating-playbook-project "Use the Ansible Automation Platform VS Code extension to scaffold a new Ansible playbook project. This process creates the necessary directory structure and configuration files, preparing your environment for playbook development.")
  - Scaffold a collection for your roles in [Package and distribute automation content with collections](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-devtools_develop_collections#devtools-develop-collections "Collections are a distribution format for Ansible content that can include playbooks, roles, modules, and plugins. Red Hat provides Ansible Content Collections on Ansible automation hub that contain both Red Hat Ansible Certified Content and Ansible validated content.")

5.  Select options in the **Add** section of Ansible development tools to add files for playbooks or roles to your project. Alternatively, you can use the options in the **Ansible Lightspeed** section to generate playbooks or roles.
6.  Save your work:
  1.  Click the main menu icon in the **Activity** bar and select Terminal> (and then)New Terminal.
  2.  Use `git add` and `git commit` commands to stage the changed files and commit your changes to the local repository in the workspace.
  3.  Use the `git push` command to push your updates to your repository in your source control manager.

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


![Playbook and ansible-lint messages](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/playbook.png)  

8.  When you have resolved the problems in your playbook, a message is displayed in the **Problems** tab of the terminal.

## Execute playbooks in your Ansible development workspace

Execute your playbooks efficiently using the integrated Ansible extension within the VS Code environment of your workspace.

### About this task

### Procedure

 To execute a playbook in your Ansible development workspace, right-click on a playbook name in the file explorer and select Run ansible playbook via> (and then)Run ansible playbook via ansible playbook.

 Note:

You cannot use execution environments in Ansible development workspaces. Do not use `ansible-navigator` to execute playbooks.

## Share your work

Share your automation content and collaborate with colleagues by working together from a single shared Git repository and submitting pull requests.

### About this task

### Procedure

1.  To contribute to a colleague’s project, request the URL for the Git repository that corresponds to your colleague’s Ansible development workspace.
2.  Launch a workspace using the repository URL that your colleague shared.
3.  Work within a new git branch and contribute to your colleague’s repository by creating a merge or pull request.
