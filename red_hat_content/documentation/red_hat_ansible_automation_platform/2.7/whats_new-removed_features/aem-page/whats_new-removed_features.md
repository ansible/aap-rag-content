+++
title = "Removed features - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-removed_features"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-overview_of_redhat_ansible_intro/", "Ansible Automation Platform release notes"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-removed_features/aem-page/whats_new-removed_features.html"
last_crumb = "Removed features"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Removed features"
oversized = "false"
page_slug = "whats_new-removed_features"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/whats_new-removed_features"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-removed_features/toc/toc.json"
type = "aem-page"
+++

# Removed features

The following release notes detail the removed features for the Ansible Automation Platform general availability released on June 3, 2026

Removed features are those that were deprecated in earlier releases. They are now removed from Ansible Automation Platform 2.7, and will no longer be supported.

- Removal of direct component API access
- Removal of RPM Installer in Ansible Automation Platform 2.7

## Removal of direct component API access

The next version of Ansible Automation Platform marks the completion of the platform unification initiative introduced in Ansible Automation Platform 2.5. With this release, the platform gateway becomes the sole entry point for all Ansible Automation Platform interactions, replacing direct API access to automation controller, automation hub, and Event-Driven Ansible. This change centralizes organization management, authentication, and access control through a single, unified interface — providing a more consistent and secure experience across all automation capabilities within the platform.

Note:

Any existing direct integrations with automation controller, automation hub, or Event-Driven Ansible APIs must be migrated to route through the platform gateway prior to upgrading to the next version of Ansible Automation Platform.

**Minimum collection versions**

Ansible Automation Platform 2.7 requires the following minimum collection versions:

- ansible.controller version 4.8.0
- ansible.hub version version1.0.6
- ansible.eda version version 2.12.0
- ansible.platform version 2.7.0
See [Update collection versions](/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-con_upgrade_api_changes_27#GUID-bc50aa1a-9717-4cde-816e-7f5bf1d78b75 "Older collection versions construct URLs and authentication flows that target component APIs directly. Only the latest collection versions route requests through platform gateway.") for more information.

## Previous compatibility support

Ansible Automation Platform 2.5 and 2.6 maintained backward compatibility with pre-unification access patterns to provide a transition period for customers migrating to the unified platform. This compatibility layer is now removed. Integrations that continued to function through an upgrade from 2.4 to 2.6 will require remediation before upgrading.

## Pre-upgrade migration assessment

Before upgrading, review your environment for the following direct-access patterns, all of which require a migration plan:

| Area                  | What to Review                                                                                                                                  |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| User & Org Management | Any organization, team, or user management interfacing directly with automation controller or automation hub APIs or collections Authentication |
| Authentication        | Legacy users authenticating with basic auth directly to automation controller                                                                   |
| Tokens & OAuth        | Legacy Personal Access Tokens (PATs) or OAuth applications connecting directly to automation controller                                         |
| Image Management      | Any container registry processes managing images directly on private automation hub                                                             |
| Access Control        | RBAC configurations managed directly on individual components rather than through platform gateway                                              |
| Job Management        | Job template or job re-execution triggers to launch jobs directly to automation controller                                                      |
| Inventory Management  | Managing Inventory using automation controller to add, edit, or remove inventory groups or nodes                                                |
| Project Management    | Managing SCM projects using automation controller to add, edit, or remove projects.                                                             |
All of the above must be migrated to use the equivalent functionality provided by the platform gateway.

## Direct access detection tooling

A CLI detection tool is available to identify direct API usage in Ansible Automation Platform 2.5 or 2.6 environments. The tool analyzes NGINX logs to detect requests that bypass platform gateway. You can run the tool directly from the GitHub repository using uvx.

Prerequisites
- Ansible Automation Platform 2.5 or 2.6 is installed.
- You have one of the following, depending on your deployment type:
  * RPM or containerized deployments: An SOSReport.
  * OpenShift Container Platform deployments: A must-gather or ocp-inspect output

Note:

The tool requires NGINX log format updates introduced in the Ansible Automation Platform 2.6 patch released March 25, 2026. If you are running an earlier 2.6.x patch and your logs do not contain the required fields, apply the provided patch script or upgrade to the latest 2.6.x release.

## Procedure

1.      Scan a containerized or RPM SOSReport:

     `$ uvx --from "git+https://github.com/ansible/aap-detect-direct-component-access" aap-detect-direct-component-access /path/to/sosreport/`

2.      Scan an OpenShift Container Platform must-gather tarball:

     `$ uvx --from "git+https://github.com/ansible/aap-detect-direct-component-access" aap-detect-direct-component-access /path/to/must-gather/`

3.      Scan an OpenShift Container Platform inspect output:

     `$ uvx --from "git+https://github.com/ansible/aap-detect-direct-component-access" aap-detect-direct-component-access /path/to/ocp-inspect/`

The tool produces a summary of direct-access requests organized by component, source IP, and request path. Internal traffic such as health checks and readiness probes is excluded automatically.

## Removal of RPM installer in Ansible Automation Platform 2.7

In Ansible Automation Platform 2.5 release, the RPM installer was deprecated. Starting with Ansible Automation Platform 2.7, we are no longer providing the installer, and customers who have Ansible Automation Platform installed using RPM must migrate to either the containerised or Openshift Ansible Automation Platform Operator. Follow the guidelines for migrating to a new topology. Customers must first migrate to the new supported topology on the version that they are currently running (that is, Ansible Automation Platform 2.6 RPM to Ansible Automation Platform 2.6 containerised) before upgrading to Ansible Automation Platform 2.7.
