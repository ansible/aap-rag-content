+++
title = "Delete an Ansible development workspace - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-assembly_workspaces_management"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-technology_preview/", "Technology Preview"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-assembly_workspaces_management/aem-page/whats_new-assembly_workspaces_management.html"
last_crumb = "Delete an Ansible development workspace"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Delete an Ansible development workspace"
oversized = "false"
page_slug = "whats_new-assembly_workspaces_management"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/whats_new-assembly_workspaces_management"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-assembly_workspaces_management/toc/toc.json"
type = "aem-page"
+++

# Delete an Ansible development workspace

Manage your Ansible development workspaces by understanding how to delete them from OpenShift Dev Spaces when they are no longer needed.

Deleting unused workspaces helps free up cluster resources and maintains a clean development environment within OpenShift Dev Spaces.

## Delete an Ansible development workspace

To delete the contents of an Ansible development workspace, you delete the workspace itself. This action removes all the pods, storage, and other resources associated with that specific workspace, effectively wiping its contents.

### Before you begin

- You know the name of the workspace you want to delete.

### About this task

### Procedure

1.  Stop the Ansible development workspace that you want to delete.   - To stop the workspace in the Dev Spaces dashboard, select the workspace that you want to delete and select actions> (and then)Stop Workspace.
  - To stop the workspace using OpenShift `oc` commands, follow the steps in [Stopping workspaces](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.22/html-single/user_guide/index#managing-workspaces-with-apis-stopping-workspaces) in the Red Hat OpenShift Dev Spaces *User Guide*.

2.  Delete the workspace:

  - To delete the workspace from the Dev Spaces dashboard, select the workspace that you want to delete and select actions> (and then)Delete Workspace.
  - To delete a workspace using OpenShift `oc` commands, follow the steps in [Removing workspaces](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.22/html-single/user_guide/index#managing-workspaces-with-apis-removing-workspaces) in the Red Hat OpenShift Dev Spaces *User Guide*.

## Uninstall OpenShift Dev Spaces

Uninstall OpenShift Dev Spaces completely when it is no longer required. Remember that this action removes all related Ansible dev spaces user data.

### About this task

### Procedure

 To uninstall OpenShift Dev Spaces, follow the steps in the [Uninstalling Dev Spaces](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.23/html/administration_guide/uninstalling-devspaces) chapter of the Red Hat OpenShift Dev Spaces *Administration Guide*.

Note:

Uninstalling Ansible dev spaces removes all Ansible dev spaces-related user data.
