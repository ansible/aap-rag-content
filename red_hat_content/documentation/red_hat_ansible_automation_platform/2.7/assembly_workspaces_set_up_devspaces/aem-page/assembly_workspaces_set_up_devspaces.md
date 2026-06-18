+++
template = "docs/aem-title.html"
title = "Set up and install Red Hat OpenShift dev spaces to run your Ansible container - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/assembly_workspaces_set_up_devspaces"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/assembly_workspaces_set_up_devspaces/aem-page/assembly_workspaces_set_up_devspaces.html"
last_crumb = "Set up and install Red Hat OpenShift dev spaces to run your Ansible container"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Set up and install Red Hat OpenShift dev spaces to run your Ansible container"
oversized = "false"
page_slug = "assembly_workspaces_set_up_devspaces"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/assembly_workspaces_set_up_devspaces"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/assembly_workspaces_set_up_devspaces/toc/toc.json"
type = "aem-page"
+++

# Set up and install Red Hat OpenShift dev spaces to run your Ansible container

An administrator must install Red Hat OpenShift Dev Spaces to create a OpenShift Dev Spaces dashboard from where developers can launch Ansible development workspaces.

## Prerequisites

Review the prerequisites listed here before setting up Ansible development workspaces. Meeting these requirements helps ensure a successful setup.

- You have access to a web browser and network connectivity.
- You have installed Red Hat OpenShift Container Platform version 4.20.15 or later.
- You have an active subscription that includes Red Hat OpenShift Dev Spaces.
- You have installed Red Hat OpenShift Dev Spaces on your OpenShift Container Platform cluster.
- You have a valid subscription to Red Hat Ansible Automation Platform.
- You have access to a Git version control system.

## Install Red Hat OpenShift dev spaces

An administrator must install Red Hat OpenShift Dev Spaces to generate an OpenShift Dev Spaces dashboard. The dashboard is the entry point for developers to launch Ansible development workspaces.

### Procedure

1.  Follow the steps in [Installing Dev Spaces on OpenShift using the web console](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/latest/html/administration_guide/installing-devspaces#installing-devspaces-on-openshift-using-the-web-console) in the *Red Hat OpenShift Dev Spaces Administration guide* to install OpenShift Dev Spaces. This process includes the following steps:

  1.  Log in to your OpenShift cluster as an administrator.
  2.  Install the OpenShift Dev Spaces operator from the OperatorHub.
  3.  Create an instance of the OpenShift Dev Spaces operator.

2.  Share the URL for the OpenShift Dev Spaces dashboard with the users who need to launch Ansible development workspaces.
