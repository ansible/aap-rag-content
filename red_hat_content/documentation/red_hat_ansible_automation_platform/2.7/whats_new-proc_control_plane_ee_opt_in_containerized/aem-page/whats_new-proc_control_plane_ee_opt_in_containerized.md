+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-proc_control_plane_ee_opt_in_containerized"
title = "Opt in to control-plane-ee on a containerized installation - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-technology_preview/", "Technology Preview"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-proc_control_plane_ee_opt_in_containerized/aem-page/whats_new-proc_control_plane_ee_opt_in_containerized.html"
last_crumb = "Opt in to control-plane-ee on a containerized installation"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Opt in to control-plane-ee on a containerized installation"
oversized = "false"
page_slug = "whats_new-proc_control_plane_ee_opt_in_containerized"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/whats_new-proc_control_plane_ee_opt_in_containerized"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-proc_control_plane_ee_opt_in_containerized/toc/toc.json"
type = "aem-page"
+++

# Opt in to control-plane-ee on a containerized installation

For an existing containerized installation, set `control_plane_execution_environment` to `registry.redhat.io/ansible-automation-platform-27/ee-control-plane-rhel9:latest` in the installer configuration and rerun the Ansible Automation Platform installer.

## Before you begin

- You have an Ansible Automation Platform 2.7 containerized installer that supports the `control_plane_execution_environment` variable.
- You have the approved `control-plane-ee` image reference and access to its registry.
- You have permission to run the installer on the Ansible Automation Platform host.

## Procedure

1. Set `control_plane_execution_environment` to `registry.redhat.io/ansible-automation-platform-27/ee-control-plane-rhel9:latest` in the installer configuration:
  

```
control_plane_execution_environment: "registry.redhat.io/ansible-automation-platform-27/ee-control-plane-rhel9:latest"
```

2. Rerun the containerized Ansible Automation Platform installer.

## What to do next

 **Verification**

1. Confirm that the installer completes successfully and pulls the configured `control-plane-ee` image to the target host.
2. Select **Automation Execution** > **Infrastructure** > **Execution Environments**. Confirm that the **Image** value for **Control Plane Execution Environment** matches the configured `control-plane-ee` image.
3. Perform a project update and a constructed inventory source update, and confirm that both complete successfully.
