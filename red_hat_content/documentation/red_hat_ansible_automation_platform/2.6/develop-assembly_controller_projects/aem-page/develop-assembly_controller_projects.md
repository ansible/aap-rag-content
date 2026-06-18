+++
title = "Logically group playbooks with projects - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_controller_projects"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_controller_projects/", "Logically group playbooks with projects"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-assembly_controller_projects/aem-page/develop-assembly_controller_projects.html"
last_crumb = "Logically group playbooks with projects"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Logically group playbooks with projects"
oversized = "false"
page_slug = "develop-assembly_controller_projects"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/develop-assembly_controller_projects"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-assembly_controller_projects/toc/toc.json"
type = "aem-page"
+++

# Logically group playbooks with projects

A project is a logical collection of Ansible playbooks, represented in automation controller.

You can manage playbooks and playbook directories different ways:

- By placing them manually under the Project Base Path on your automation controller server.
- By placing your playbooks into a source code management (SCM) system supported by the automation controller.


These include Git, Subversion, Mercurial and Red Hat Lightspeed.

For more information on creating a Red Hat Lightspeed project, see Setting up Red Hat Lightspeed Remediations.

 Note:

The Project Base Path is `/var/lib/awx/projects`. However, this can be modified by the system administrator. It is configured in `/etc/tower/conf.d/custom.py`.

Use caution when editing this file, as incorrect settings can disable your installation.

The **Projects** page displays the list of the projects that are currently available.

A **Demo Project** is provided that you can work with initially.

For each project listed, you can get the latest SCM revision ![Refresh](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/sync.png), edit ![Edit](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/leftpencil.png) the project, or duplicate ![Copy](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/copy.png) the project attributes, using the icons next to each project.

Projects can be updated while a related job is running.

In cases where you have a large project (around 10 GB), disk space on `/tmp` may be an issue.

**Status** indicates the state of the project and may be one of the following (note that you can also filter your view by specific status types):

- **Pending** - The source control update has been created, but not queued or started yet. Any job (not just source control updates) stays in pending until it is ready to be run by the system. Possible reasons for it not being ready are:
  * It has dependencies that are currently running so it has to wait until they are done.
  * There is not enough capacity to run in the locations it is configured to.
- **Waiting** - The source control update is in the queue waiting to be executed.
- **Running** - The source control update is currently in progress.
- **Successful** - The last source control update for this project succeeded.
- **Failed** - The last source control update for this project failed.
- **Error** - The last source control update job failed to run at all.
- **Canceled** - The last source control update for the project was canceled.
- **Never updated** - The project is configured for source control, but has never been updated.
- **OK** - The project is not configured for source control, and is correctly in place.
- **Missing** - Projects are absent from the project base path of `/var/lib/awx/projects`. This is applicable for manual or source control managed projects.


 Note:

Projects of credential type `Manual` cannot update or schedule source control-based actions without being reconfigured as an SCM type credential.
