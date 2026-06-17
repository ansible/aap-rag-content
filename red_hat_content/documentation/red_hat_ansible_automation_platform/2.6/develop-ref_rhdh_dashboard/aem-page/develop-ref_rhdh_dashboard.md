+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-ref_rhdh_dashboard"
title = "Dashboard navigation - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_rhdh_using/", "Streamline development by integrating Red Hat Developer Hub plug-ins"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-ref_rhdh_dashboard/aem-page/develop-ref_rhdh_dashboard.html"
last_crumb = "Dashboard navigation"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Dashboard navigation"
oversized = "false"
page_slug = "develop-ref_rhdh_dashboard"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/develop-ref_rhdh_dashboard"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-ref_rhdh_dashboard/toc/toc.json"
type = "aem-page"
+++

# Dashboard navigation

After logging into Red Hat Developer Hub (RHDH), use the Ansible navigation panel item to view the plug-in dashboard. The dashboard shows the full automation workflow, from learning to deploying jobs on Ansible Automation Platform.


![Ansible plug-in dashboard](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/rhdh-plugin-dashboard.png)  


The plug-in dashboard illustrates the steps you need to take from learning about Ansible to deploying automation jobs from Ansible Automation Platform:

- **Overview** displays the main dashboard page.
- **Learn** provides links to resources curated by Red Hat that introduce you to Ansible and provide step-by-step examples to get you started. For more information, see [Learning about Ansible](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-ref_rhdh_learning#rhdh-learning "To learn more about getting started with automation, click Learn from the Overview page of the plug-in dashboard. The Learn page provides the following options for learning:").
- **Discover existing collections** links to private automation hub, if configured in the plug-ins, or to automation hub hosted on the Red Hat Hybrid Cloud Console. Automation hub stores existing collections and execution environments that you can use in your projects. For more information, see [Discovering existing collections](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-ref_rhdh_learning#rhdh-discover-collections "From the Overview page in the Ansible plug-ins dashboard on Red Hat Developer Hub, click Discover Existing Collections.").
- **Create** creates new projects in your configured Source Control Management platforms such as GitHub. For more information, see [Creating a project](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-ref_rhdh_learning#rhdh-create "Create a new Ansible Playbook project in the Red Hat Developer Hub by logging in, navigating to the Ansible section, and selecting the project creation template. You must have the correct access (RBAC) assigned by your administrator to view the templates.").
- **Develop** links you to OpenShift Dev Spaces, if configured in the Ansible plug-ins installation. OpenShift Dev Spaces provides on-demand, web-based Integrated Development Environments (IDEs), where you can develop automation content. For more information, see [Developing projects](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-proc_rhdh_develop_projects_devspaces#rhdh-develop-projects-devspaces "OpenShift Dev Spaces provides a web-based Integrated Development Environment that includes the Ansible VS Code extension and command line tools. You can use this environment to develop and test your automation code.").
- **Operate** connects you to Ansible Automation Platform, where you can create and run automation jobs that use the projects you have developed. For more information, see [Setting up a controller project to run your playbook project](/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-proc_rhdh_develop_projects_devspaces#rhdh-set-up-controller-project "Access Ansible Automation Platform through the Red Hat Developer Hub to create a project for your playbook repository, then set up a job template that uses the playbook. You can go directly to your automation controller instance if it was not configured during the plug-in installation.").
