+++
title = "Access preconfigured development tools with Ansible development workspaces - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-assembly_workspaces_intro"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-technology_preview/", "Technology Preview"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-assembly_workspaces_intro/aem-page/whats_new-assembly_workspaces_intro.html"
last_crumb = "Access preconfigured development tools with Ansible development workspaces"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Access preconfigured development tools with Ansible development workspaces"
oversized = "false"
page_slug = "whats_new-assembly_workspaces_intro"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/whats_new-assembly_workspaces_intro"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-assembly_workspaces_intro/toc/toc.json"
type = "aem-page"
+++

# Access preconfigured development tools with Ansible development workspaces

Ansible development workspaces provide a fully supported browser-based development environment that includes Ansible development tools for creating and testing Ansible playbooks, roles, and collections. The workspaces run as containers within Red Hat OpenShift Dev Spaces.

## Introduction to Ansible development workspaces

Ansible development workspaces offer centralized management and policy enforcement, giving administrators better control and governance over secure, consistent automation development environments. Developers benefit by avoiding local application installs, especially in locked-down settings.

Ansible development tools and runtimes are pre-configured in Ansible development workspaces. Developers can start creating projects for automation content quickly by logging in to Ansible development workspaces in a browser.

The development tools in Ansible development workspaces are based on Ansible recommended practices, which improves the quality and reliability of your automation content. As a component of your Red Hat Ansible Automation Platform subscription, Ansible development workspaces are fully supported.

To ensure that your automation content files persist when you quit Ansible development workspaces, you push your projects to a git repository in a source control manager (SCM) that is linked to your workspace.

## Ansible development workspaces components

Each Ansible development workspace is a project-agnostic full development environment. Dependencies are satisfied for all the tools in the environment.

The following applications are pre-installed.

- Microsoft VS Code
- Python
-  `ansible-core`
- Ansible development tools (ADT) package, which includes:
  * `ansible-creator` for scaffolding directory structure for your automation content
  * `ansible-lint` for identifying stylistic errors and anti-patterns
  * `molecule` for running functional tests on your automation content

## About the Ansible dev spaces image

Red Hat OpenShift Dev Spaces is a containerized cloud development environment (CDE) that provides pre-configured, consistent workspaces running on OpenShift Container Platform. It provisions ready-to-code workspaces on demand.

The Ansible dev spaces image is the container image for Ansible development workspaces. It replaces an existing Ansible demo within OpenShift Dev Spaces and is fully supported by Red Hat.

The following diagram illustrates the relationship between OpenShift Container Platform, OpenShift Dev Spaces, and Ansible development workspaces.


![Ansible development workspaces topology](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/devtools-workspaces-architecture.png)  

## Set up and install Red Hat OpenShift dev spaces to run your Ansible container

An administrator must install Red Hat OpenShift Dev Spaces to create a OpenShift Dev Spaces dashboard from where developers can launch Ansible development workspaces.

### Prerequisites

Review the prerequisites listed here before beginning the installation of Red Hat OpenShift Dev Spaces. Meeting these requirements helps ensure a successful setup.

- You have access to a web-browser and network connectivity.
- You have installed Red Hat OpenShift Container Platform.
- You have an active Red Hat OpenShift cluster.
- You have a valid subscription to Red Hat Ansible Automation Platform.
- You have set up a version control system such as Git.

### Install Red Hat OpenShift dev spaces

An administrator must install Red Hat OpenShift Dev Spaces to generate an OpenShift Dev Spaces dashboard. The dashboard is the entry point for developers to launch Ansible development workspaces.

#### Procedure

1.  Follow the steps in [Installing Dev Spaces on OpenShift using the web console](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.22/html/administration_guide/installing-devspaces#installing-devspaces-on-openshift-using-the-web-console) in the *Red Hat OpenShift Dev Spaces Administration guide* to install OpenShift Dev Spaces. This process includes the following steps:

  1.  Log in to your OpenShift cluster as an administrator.
  2.  Install the OpenShift Dev Spaces operator from the OperatorHub.
  3.  Create an instance of the OpenShift Dev Spaces operator.

2.  Share the URL for the OpenShift Dev Spaces dashboard with the users who need to launch Ansible development workspaces.
