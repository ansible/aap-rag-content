+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-configure_an_external_database_for_event_streams"
title = "Configure an external database for event streams - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_aap_containerized_installation_intro/", "Install containerized Ansible Automation Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-configure_an_external_database_for_event_streams/aem-page/install-configure_an_external_database_for_event_streams.html"
last_crumb = "Configure an external database for event streams"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Configure an external database for event streams"
oversized = "false"
page_slug = "install-configure_an_external_database_for_event_streams"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-configure_an_external_database_for_event_streams"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-configure_an_external_database_for_event_streams/toc/toc.json"
type = "aem-page"
+++

# Configure an external database for event streams

Event-Driven Ansible event streams require a dedicated PostgreSQL database user (`eda_event_stream`) for security and access control. This user must exist on the Event-Driven Ansible database and requires only `CONNECT` privileges.

If you use the Ansible Automation Platform provisioned database, the installer configures this user automatically. For external databases not managed by Ansible Automation Platform, use one of the following scenarios to set up the event streams database user:

1. An external database with PostgreSQL admin credentials: The installer creates the user automatically.
2. An external database without PostgreSQL admin credentials: You must create the user manually.
