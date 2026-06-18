+++
title = "Set up event streams database user with PostgreSQL admin credentials - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-set_up_event_streams_database_user_with_postgresql_admin_credentials"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_aap_containerized_installation_intro/", "Install containerized Ansible Automation Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-set_up_event_streams_database_user_with_postgresql_admin_credentials/aem-page/install-set_up_event_streams_database_user_with_postgresql_admin_credentials.html"
last_crumb = "Set up event streams database user with PostgreSQL admin credentials"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Set up event streams database user with PostgreSQL admin credentials"
oversized = "false"
page_slug = "install-set_up_event_streams_database_user_with_postgresql_admin_credentials"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-set_up_event_streams_database_user_with_postgresql_admin_credentials"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-set_up_event_streams_database_user_with_postgresql_admin_credentials/toc/toc.json"
type = "aem-page"
+++

# Set up event streams database user with PostgreSQL admin credentials

If you have PostgreSQL admin credentials configured in your inventory file, the installation program automatically creates the eda_event_stream database user and grants the necessary permissions.

## Procedure

 Ensure the following variables are set in your inventory file under the `[all:vars]` group:

```
postgresql_admin_username=<set your own>
postgresql_admin_password=<set your own>
```
If these variables are already set, the installation program automatically creates the event streams database user using these admin credentials.
