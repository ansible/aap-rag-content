+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_portal_aap_sync_overview"
title = "Understanding Ansible Automation Platform synchronization - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-install_automation_portal_on_openshift_container_platform/", "Install automation portal on OpenShift Container Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-con_portal_aap_sync_overview/aem-page/install-con_portal_aap_sync_overview.html"
last_crumb = "Understanding Ansible Automation Platform synchronization"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Understanding Ansible Automation Platform synchronization"
oversized = "false"
page_slug = "install-con_portal_aap_sync_overview"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-con_portal_aap_sync_overview"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-con_portal_aap_sync_overview/toc/toc.json"
type = "aem-page"
+++

# Understanding Ansible Automation Platform synchronization

The synchronization feature imports your Organization, Users, Teams, and Job Templates from Ansible Automation Platform into Ansible automation portal, making these entities securely discoverable and accessible to portal users.

## Overview

Ansible automation portal synchronizes two types of data from Ansible Automation Platform:

- Organization, Users, and Teams: Identity and organizational structure data
- Job Templates: Executable automation templates

Both synchronizations run on a scheduled basis and can be manually triggered by Ansible Automation Platform Administrators in the portal UI.

## How it works

1. Ansible automation portal connects to your Ansible Automation Platform instance using configured credentials.
2. Ansible automation portal fetches data based on the configured Ansible Automation Platform Organization and filter criteria.
3. Ansible automation portal converts Ansible Automation Platform entities into portal entities and displays them in the UI.
4. Synchronization runs on a configurable schedule (for example, every 60 minutes).
5. Users access and launch resources based on their existing Ansible Automation Platform permissions.
