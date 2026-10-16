+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_backstage_software_templates"
title = "Use custom actions and UI components in Backstage Software Templates - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_self_service_login/", "Launch automation templates from Ansible automation portal"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-assembly_backstage_software_templates/aem-page/develop-assembly_backstage_software_templates.html"
last_crumb = "Use custom actions and UI components in Backstage Software Templates"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Use custom actions and UI components in Backstage Software Templates"
oversized = "false"
page_slug = "develop-assembly_backstage_software_templates"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-assembly_backstage_software_templates"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-assembly_backstage_software_templates/toc/toc.json"
type = "aem-page"
+++

# Use custom actions and UI components in Backstage Software Templates

The Ansible automation portal is built on a Red Hat Developer Hub base image.
It uses Backstage Software Templates, which are YAML-based workflow definitions that provide user forms to execute automation tasks in Ansible Automation Platform.

## Overview

Learn how Backstage Software Templates relate to the Ansible automation portal and how custom templates execute automation jobs in Ansible Automation Platform.

### Understanding software templates in the automation portal

The Ansible automation portal uses Backstage Software Templates as the foundation for its self-service catalog. A software template is a YAML document stored in a Git repository (GitHub or GitLab) that defines an interactive web form and an automated workflow.

When an automation creator registers a custom software template in the portal, end users can launch it to execute jobs in Ansible Automation Platform without needing direct access to automation controller or familiarity with Ansible playbooks.

### Anatomy of a portal software template

A custom software template consists of four main sections:

- **Metadata:** Identifies the template in the portal catalog, including its display name, title, description, and source taxonomy.
- **Spec:** Declares the template type (`spec.type: automation-template`) and ownership.
- **Parameters:** Defines the input form that users complete in the portal UI before execution, such as target hosts, environment choices, or application versions.
- **Steps:** Defines the sequence of actions executed when the user submits the form, including calling custom `rhaap:*` actions to launch jobs or create resources.

### Upstream Backstage documentation versus portal differences

The Ansible automation portal is built on a Red Hat Developer Hub base image. While upstream Backstage template syntax provides the foundation, specific conventions apply to the portal:

| Template area         | Upstream Backstage convention                                       | Ansible automation portal convention                                                                                                                                   |
| --------------------- | ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Entity type**       | `spec.type: service` or`website`                                    | **Must** use`spec.type: automation-template`.                                                                                                                          |
| **Source annotation** | Not used or generic SCM annotations                                 | Include`ansible.com/template-source: scm` so custom templates appear correctly in the portal source filter.                                                            |
| **Authentication**    | Parameters prompt for tokens or use generic secrets                 | The portal automatically injects the user's OAuth token on submit. Steps**must** reference`token: ${{ secrets.aapToken }}`. Do not define a token field in parameters. |
| **Custom actions**    | Upstream scaffolder actions (e.g.`fetch:template`,`publish:github`) | Portal includes native`rhaap:*` actions (such as`rhaap:launch-job-template`) to interact directly with Ansible Automation Platform.                                    |

Important:

Red Hat does not support the use of the Red Hat Developer Hub image for standalone purposes outside the scope of the Ansible Automation Platform self-service automation portal functionality.

## Ansible backstage plugins

The portal’s capabilities are delivered through **Ansible Backstage Plugins** that extend Red Hat Developer Hub functionality; the base Red Hat Developer Hub image is not customized.
These plugins provide additional Backstage actions and filters that you use to create custom software templates.

| Plugin                                    | Functionality                                                                           |
| ----------------------------------------- | --------------------------------------------------------------------------------------- |
| auth-backend-module-rhaap-provider        | Provides OAuth 2.0 authentication with Ansible Automation Platform.                     |
| catalog-backend-module-rhaap              | Synchronizes Ansible Automation Platform job templates as Backstage Software Templates. |
| scaffolder-backend-module-backstage-rhaap | Provides the `rhaap:launch-job-template` action.                                        |
| backstage-rhaap-common                    | Contains shared libraries and utilities for Ansible Automation Platform integration.    |
| self-service                              | Provides the user interface for all listed functionality.                               |
