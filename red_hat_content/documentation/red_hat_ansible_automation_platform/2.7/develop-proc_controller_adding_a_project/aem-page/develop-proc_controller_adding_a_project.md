+++
title = "Add a new project - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_controller_adding_a_project"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_controller_projects/", "Logically group playbooks with projects"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-proc_controller_adding_a_project/aem-page/develop-proc_controller_adding_a_project.html"
last_crumb = "Add a new project"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Add a new project"
oversized = "false"
page_slug = "develop-proc_controller_adding_a_project"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-proc_controller_adding_a_project"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-proc_controller_adding_a_project/toc/toc.json"
type = "aem-page"
+++

# Add a new project

You can create a logical collection of playbooks, called projects in automation controller.

## Procedure

1.  From the navigation panel, select Automation Execution> (and then)Projects.
2.  On the **Projects** page, click Create project to launch the **Create Project** window.
3.  Enter the appropriate details into the following required fields:

  - **Name** (required)
  - Optional: **Description**
  - **Organization** (required): A project must have at least one organization. Select one organization now to create the project. When the project is created you can add additional organizations.
  - Optional: **Execution environment**: Enter the name of the execution environment or search from a list of existing ones to run this project. For more information, see [Define, create, and build execution environments](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-define__create__and_build_execution_environments "Run automation consistently across nodes with execution environments, which are container images that contain everything you need to run your automation.").
  - **Source control type** (required): Select an SCM type associated with this project from the menu. Options in the following sections become available depending on the type chosen. For more information, see [Managing playbooks manually](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-ref_projects_collections_support#proc-projects-manage-playbooks-manually "Manage Ansible playbooks and directories directly on the automation controller filesystem. This approach helps ensure proper file ownership and permissions when you cannot use source control.") or [Managing playbooks using source control](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-ref_projects_manage_playbooks_with_source_control#ref-projects-manage-playbooks-with-source-control "Choose one of the following options when managing playbooks by using source control:").
  - Optional: **Content signature validation credential**: Use this field to enable content verification. Specify the GPG key to use for validating content signature during project synchronization. If the content has been tampered with, the job will not run. For more information, see [Project signing and verification](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_controller_project_signing#assembly-controller-project-signing "Use project signing and verification in your project directory to sign files. You can then verify whether or not that content has changed in any way, or files have been added to, or removed from the project unexpectedly.").

4.  Click Create project.
