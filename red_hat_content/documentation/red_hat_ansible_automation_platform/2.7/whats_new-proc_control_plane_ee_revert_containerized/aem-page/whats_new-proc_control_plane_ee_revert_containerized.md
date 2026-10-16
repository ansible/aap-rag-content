+++
template = "docs/aem-title.html"
title = "Revert to ee-supported on a containerized installation - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-proc_control_plane_ee_revert_containerized"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-technology_preview/", "Technology Preview"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-proc_control_plane_ee_revert_containerized/aem-page/whats_new-proc_control_plane_ee_revert_containerized.html"
last_crumb = "Revert to ee-supported on a containerized installation"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Revert to ee-supported on a containerized installation"
oversized = "false"
page_slug = "whats_new-proc_control_plane_ee_revert_containerized"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/whats_new-proc_control_plane_ee_revert_containerized"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-proc_control_plane_ee_revert_containerized/toc/toc.json"
type = "aem-page"
+++

# Revert to ee-supported on a containerized installation

Remove the `control_plane_execution_environment` override and rerun the containerized installer to restore the default `ee-supported` image.

## Before you begin

- You have access to the installer configuration used to configure the containerized installation.
- You have permission to run the installer on the Ansible Automation Platform host.

## Procedure

1. Remove or unset `control_plane_execution_environment` in the installer configuration.
2. Rerun the containerized Ansible Automation Platform installer.

## What to do next

 **Verification**

1. Confirm that the installer completes successfully and restores the default `ee-supported` image.
2. Select **Automation Execution** > **Infrastructure** > **Execution Environments**. Confirm that the **Image** value for **Control Plane Execution Environment** matches the default `ee-supported` image for your release.
3. Perform a project update and a constructed inventory source update, and confirm that both complete successfully.
