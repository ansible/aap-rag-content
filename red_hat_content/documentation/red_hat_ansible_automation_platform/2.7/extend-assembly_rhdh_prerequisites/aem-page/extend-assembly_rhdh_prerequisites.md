+++
title = "Prerequisites - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_rhdh_prerequisites"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_rhdh_intro/", "Ansible plug-ins for Red Hat Developer Hub"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-assembly_rhdh_prerequisites/aem-page/extend-assembly_rhdh_prerequisites.html"
last_crumb = "Prerequisites"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Prerequisites"
oversized = "false"
page_slug = "extend-assembly_rhdh_prerequisites"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/extend-assembly_rhdh_prerequisites"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-assembly_rhdh_prerequisites/toc/toc.json"
type = "aem-page"
+++

# Prerequisites

Complete these prerequisites before installing the Ansible plug-ins for Red Hat Developer Hub.

## Prerequisites

To proceed, you must have Red Hat Developer Hub installed on Red Hat OpenShift Container Platform (RHOCP) and a valid subscription to Red Hat Ansible Automation Platform.

- Red Hat Developer Hub installed on Red Hat OpenShift Container Platform.   * For Helm installation, follow the steps in the Installing Red Hat Developer Hub on OpenShift Container Platform with the Helm chart section of *Installing Red Hat Developer Hub on OpenShift Container Platform*.
  * For Operator installation, follow the steps in the Installing Red Hat Developer Hub on OpenShift Container Platform with the Operator section of *Installing Red Hat Developer Hub on OpenShift Container Platform*.
- A valid subscription to Red Hat Ansible Automation Platform.
- An OpenShift Container Platform instance with the appropriate permissions within your project to create an application.
- The Red Hat Developer Hub instance can query the automation controller API.
- Optional: To use the integrated learning paths, you must have outbound access to developers.redhat.com.

## Recommended RHDH preconfiguration

Red Hat recommends performing the following initial configuration tasks in Red Hat Developer Hub (RHDH). However, you can install the Ansible plug-ins for Red Hat Developer Hub before completing these tasks.

- Authentication in Red Hat Developer Hub
- Authorization in Red Hat Developer Hub


Note:

Red Hat provides a repository of software templates for RHDH that uses the `publish:github` action. To use these software templates, you must install the required GitHub dynamic plugins.
