+++
title = "Opt in to control-plane-ee on OpenShift Container Platform - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-proc_control_plane_ee_opt_in_ocp"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-technology_preview/", "Technology Preview"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-proc_control_plane_ee_opt_in_ocp/aem-page/whats_new-proc_control_plane_ee_opt_in_ocp.html"
last_crumb = "Opt in to control-plane-ee on OpenShift Container Platform"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Opt in to control-plane-ee on OpenShift Container Platform"
oversized = "false"
page_slug = "whats_new-proc_control_plane_ee_opt_in_ocp"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/whats_new-proc_control_plane_ee_opt_in_ocp"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-proc_control_plane_ee_opt_in_ocp/toc/toc.json"
type = "aem-page"
+++

# Opt in to control-plane-ee on OpenShift Container Platform

Set `spec.controller.control_plane_ee_image` on the `AnsibleAutomationPlatform` custom resource. You do not need to reinstall Ansible Automation Platform.

## Before you begin

- You have an Ansible Automation Platform deployment on OpenShift Container Platform.
- You have permission to edit the `AnsibleAutomationPlatform` custom resource.

Note:

This procedure applies only to OpenShift Container Platform deployments.

## About this task

The operator reconciles the change and updates the automation controller deployment when you modify `spec.controller.control_plane_ee_image`. You do not need to reinstall Ansible Automation Platform.

## Procedure

1. In the OpenShift Container Platform web console, open the top-level `AnsibleAutomationPlatform` custom resource for your deployment.
2. Edit the custom resource and set `spec.controller.control_plane_ee_image` to `registry.redhat.io/ansible-automation-platform-27/ee-control-plane-rhel9:latest`.
3. Save the custom resource.
  
  Note:
      Saving this change causes the operator to reconcile the automation controller deployment. Wait for the deployment rollout to complete before running project or inventory updates.

## Results

The operator reconciles the controller deployment and rolls out the control-plane execution environment.

Note:

Saving this change causes the operator to reconcile the controller deployment. Wait for the deployment rollout to complete before running project or inventory updates.

## What to do next

 **Verification**

1. Select **Automation Execution** > **Infrastructure** > **Execution Environments**. Confirm that the **Image** value for **Control Plane Execution Environment** matches the configured `control-plane-ee` image.
2. Run a project update and a constructed inventory source update, and confirm that both complete successfully.
