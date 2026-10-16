+++
title = "Revert to ee-supported on OpenShift Container Platform - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-proc_control_plane_ee_revert_ocp"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-technology_preview/", "Technology Preview"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-proc_control_plane_ee_revert_ocp/aem-page/whats_new-proc_control_plane_ee_revert_ocp.html"
last_crumb = "Revert to ee-supported on OpenShift Container Platform"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Revert to ee-supported on OpenShift Container Platform"
oversized = "false"
page_slug = "whats_new-proc_control_plane_ee_revert_ocp"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/whats_new-proc_control_plane_ee_revert_ocp"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-proc_control_plane_ee_revert_ocp/toc/toc.json"
type = "aem-page"
+++

# Revert to ee-supported on OpenShift Container Platform

If you encounter problems with project updates or constructed inventory source updates after opting in, revert to the default `ee-supported` control-plane execution environment.

## About this task

Note:

This procedure applies only to OpenShift Container Platform deployments.

## Procedure

1. In the OpenShift Container Platform web console, open the top-level `AnsibleAutomationPlatform` custom resource for your deployment.
2. Remove the `spec.controller.control_plane_ee_image` field.
3. Save the custom resource.

## Results

The operator reconciles the controller deployment and restores the default `ee-supported` image.

Note:

Removing this field also causes the operator to reconcile the controller deployment. Wait for the deployment rollout to complete before running project or inventory updates.

## What to do next

 **Verification**

1. Select **Automation Execution** > **Infrastructure** > **Execution Environments**. Confirm that the **Image** value for **Control Plane Execution Environment** matches the default `ee-supported` image for your release.
2. Run a project update and a constructed inventory source update, and confirm that both complete successfully.
