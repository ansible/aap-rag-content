+++
title = "Access learning paths, labs, and collections - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-ref_rhdh_learning"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_rhdh_using/", "Streamline development by integrating Red Hat Developer Hub plug-ins"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-ref_rhdh_learning/aem-page/develop-ref_rhdh_learning.html"
last_crumb = "Access learning paths, labs, and collections"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Access learning paths, labs, and collections"
oversized = "false"
page_slug = "develop-ref_rhdh_learning"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-ref_rhdh_learning"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-ref_rhdh_learning/toc/toc.json"
type = "aem-page"
+++

# Access learning paths, labs, and collections

To learn more about getting started with automation, click **Learn** from the **Overview** page of the plug-in dashboard. The **Learn** page provides the following options for learning:

- **Learning Paths** lists a curated selection of learning tools hosted on developers.redhat.com that guide you through the foundations of working with Ansible, the Ansible VS Code extension, and using YAML. You can select other Ansible learning paths from the **Useful links** section.

- **Labs** are self-led labs that are designed to give you hands-on experience in writing Ansible content and using Ansible development tools.

## Discover existing collections

From the **Overview** page in the Ansible plug-ins dashboard on Red Hat Developer Hub, click **Discover Existing Collections**.

The links in this pane provide access to the source of reusable automation content collections that you configured during plug-in installation.

If you configured private automation hub when installing the plug-in, you can click **Go to Automation Hub** to view the collections and execution environments that your enterprise has curated.

If you did not configure a private automation hub URL when installing the plug-in, the **Discover existing collection** pane provides a link to Red Hat automation hub on console.redhat.com. You can explore certified and validated Ansible content collections on this site.

## Create a project in the Red Hat Developer Hub UI

Create a new Ansible Playbook project in the Red Hat Developer Hub by logging in, navigating to the Ansible section, and selecting the project creation template. You must have the correct access (RBAC) assigned by your administrator to view the templates.

### Before you begin

- You have the correct access (RBAC) to view the templates in Red Hat Developer Hub. Ask your administrator to assign access to you if necessary.

### Procedure

1.  Log in to your Red Hat Developer Hub UI.
2.  Click the Ansible `A` icon in the Red Hat Developer Hub navigation panel.
3.  Navigate to the **Overview** page.
4.  Click **Create**.
5.  Click **Create Ansible Git Project**. The **Available Templates** page opens.
6.  Click **Create Ansible Playbook project**.
7.  In the **Create Ansible Playbook Project** page, enter information for your new project in the form. You can see sample values for this form in the Example project.

    | Field                                                    | Description                                                                                                                |
    | -------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
    | <br>Source code repository organization name or username | <br>The name of your source code repository username or organization name                                                  |
    | <br>Playbook repository name                             | <br>The name of your new Git repository                                                                                    |
    | <br>Playbook description (Optional)                      | <br>A description of the new playbook project                                                                              |
    | <br>Playbook project’s collection namespace              | <br>The new playbook Git project creates an example collection folder for you. Enter a value for the collection namespace. |
    | <br>Playbook project’s collection name                   | <br>The name of the collection                                                                                             |
    | <br>Catalog Owner Name                                   | <br>The name of the Developer Hub catalog item owner. This is a Red Hat Developer Hub field.                               |
    | <br>Source code repository organization name or username | <br>The name of your source code repository username or organization name                                                  |
    | <br>Playbook repository name                             | <br>The name of your new Git repository                                                                                    |
    | <br>Playbook description (Optional)                      | <br>A description of the new playbook project                                                                              |
    | <br>System (Optional)                                    | <br>This is a Red Hat Developer Hub field                                                                                  |
  Note:
      Collection namespaces must follow Python module naming conventions. Collections must have short, all lowercase names. You can use underscores in the collection name if it improves readability.

8.  Click **Review**.
