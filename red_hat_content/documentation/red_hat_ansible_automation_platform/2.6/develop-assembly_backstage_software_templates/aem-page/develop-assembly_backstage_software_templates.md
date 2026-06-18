+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_backstage_software_templates"
title = "Use custom actions and UI components in Backstage Software Templates - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_self_service_login/", "Launch automation templates from Ansible automation portal"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-assembly_backstage_software_templates/aem-page/develop-assembly_backstage_software_templates.html"
last_crumb = "Use custom actions and UI components in Backstage Software Templates"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Use custom actions and UI components in Backstage Software Templates"
oversized = "false"
page_slug = "develop-assembly_backstage_software_templates"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/develop-assembly_backstage_software_templates"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-assembly_backstage_software_templates/toc/toc.json"
type = "aem-page"
+++

# Use custom actions and UI components in Backstage Software Templates

The Ansible automation portal is built on a Red Hat Developer Hub base image. It uses Backstage Software Templates, which are YAML-based workflow definitions that provide user forms to execute automation tasks in Ansible Automation Platform.

## Overview

Learn how to use the custom actions, filters, and UI components provided by the **Ansible Backstage Plugins** to create and manage custom software templates for the Ansible automation portal.

Important:

Red Hat does not support the use of the Red Hat Developer Hub image for standalone purposes outside the scope of the Ansible Automation Platform Ansible automation portal functionality. Refer to the official support policy for details.

## Ansible backstage plugins

The portal’s capabilities are delivered through **Ansible Backstage Plugins** that extend Red Hat Developer Hub functionality; the base Red Hat Developer Hub image is not customized. These plugins provide additional Backstage actions and filters that you use to create custom software templates.

| Plugin                                        | Functionality                                                                               |
| --------------------------------------------- | ------------------------------------------------------------------------------------------- |
| <br>auth-backend-module-rhaap-provider        | <br>Provides OAuth 2.0 authentication with Ansible Automation Platform.                     |
| <br>catalog-backend-module-rhaap              | <br>Synchronizes Ansible Automation Platform job templates as Backstage Software Templates. |
| <br>scaffolder-backend-module-backstage-rhaap | <br>Provides the `rhaap:launch-job-template` action.                                        |
| <br>backstage-rhaap-common                    | <br>Contains shared libraries and utilities for Ansible Automation Platform integration.    |
| <br>self-service                              | <br>Provides the user interface for all listed functionality.                               |
