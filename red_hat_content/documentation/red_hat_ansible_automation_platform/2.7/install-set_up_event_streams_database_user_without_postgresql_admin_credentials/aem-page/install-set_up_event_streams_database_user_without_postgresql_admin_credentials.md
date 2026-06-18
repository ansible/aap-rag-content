+++
title = "Set up event streams database user without PostgreSQL admin credentials - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-set_up_event_streams_database_user_without_postgresql_admin_credentials"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_aap_containerized_installation_intro/", "Install containerized Ansible Automation Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-set_up_event_streams_database_user_without_postgresql_admin_credentials/aem-page/install-set_up_event_streams_database_user_without_postgresql_admin_credentials.html"
last_crumb = "Set up event streams database user without PostgreSQL admin credentials"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Set up event streams database user without PostgreSQL admin credentials"
oversized = "false"
page_slug = "install-set_up_event_streams_database_user_without_postgresql_admin_credentials"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-set_up_event_streams_database_user_without_postgresql_admin_credentials"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-set_up_event_streams_database_user_without_postgresql_admin_credentials/toc/toc.json"
type = "aem-page"
+++

# Set up event streams database user without PostgreSQL admin credentials

If you do not have PostgreSQL admin credentials, you must manually create the eda_event_stream database user before running the installation program.

## Procedure

1.  Connect to your PostgreSQL database server with a user that has `SUPERUSER` privileges:
  

```
----
# psql -h <hostname> -U <username> -p <port_number>
----
```
  
  For example:

```
----
# psql -h db.example.com -U superuser -p 5432
----
```

2.  Create the `eda_event_stream` database user and grant access to your database:
  

```
----
CREATE USER eda_event_stream WITH PASSWORD
'<eda_event_stream_password>';
GRANT CONNECT ON DATABASE <database_name> TO eda_event_stream;
----
```

3.  Add the following variables to your inventory file under the `[all:vars]` group, replacing the password with the value used in the previous step:
  

```
----
eda_event_stream_pg_username=eda_event_stream
eda_event_stream_pg_password=<eda_event_stream_password>
----
```
