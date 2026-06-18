+++
template = "docs/aem-title.html"
title = "Configure mutual TLS certificate authentication for event streams database - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-configure_mutual_tls_certificate_authentication_for_event_streams_database"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_aap_containerized_installation_intro/", "Install containerized Ansible Automation Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-configure_mutual_tls_certificate_authentication_for_event_streams_database/aem-page/install-configure_mutual_tls_certificate_authentication_for_event_streams_database.html"
last_crumb = "Configure mutual TLS certificate authentication for event streams database"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure mutual TLS certificate authentication for event streams database"
oversized = "false"
page_slug = "install-configure_mutual_tls_certificate_authentication_for_event_streams_database"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-configure_mutual_tls_certificate_authentication_for_event_streams_database"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-configure_mutual_tls_certificate_authentication_for_event_streams_database/toc/toc.json"
type = "aem-page"
+++

# Configure mutual TLS certificate authentication for event streams database

Configure mutual TLS (mTLS) authentication to secure event streams database connections with client certificates. This eliminates password management, provides stronger identity verification, and meets enterprise security and compliance requirements.

## Before you begin

- An external PostgreSQL database configured for mTLS connections
- Client certificate and key files for the eda_event_stream database user
- PostgreSQL server configured to accept certificate authentication

## Procedure

1.  Configure your PostgreSQL `pg_hba.conf` file to allow certificate authentication for the event streams user.
  
  For example:

```
----
# TYPE      DATABASE           USER                 ADDRESS      METHOD
hostssl     <database_name>    eda_event_stream     all          cert
----
```
    Replace `<database_name>` with your actual database name (for example, `eda`).

2.  Reload the PostgreSQL configuration:
  

```
----  
# systemctl reload postgresql  
----
```

3.  Add the following variables to your inventory file under the `[all:vars]` group:
  

```
----
eda_event_stream_pg_cert_auth=true
eda_event_stream_pg_tls_cert=/path/to/client-cert.pem eda_event_stream_pg_tls_key=/path/to/client-key.pem eda_event_stream_pg_sslmode=verify-full
----
```
  Note:

  - When using certificate authentication (`eda_event_stream_pg_cert_auth=true`), you do not need to provide the `eda_event_stream_pg_password`.
  - The `sslmode` value determines the level of verification. Valid options include `verify-full`, `verify-ca`, `require`, `prefer`, `allow`, and `disable`. For production environments, use `prefer`.

4.  Ensure the certificate and key files are accessible to the installation program by completing one of the following options:

  - If the files are on the Ansible control node (where you run the installer), set `eda_event_stream_pgclient_tls_files_remote=false` (default).
  - If the files are on the remote event streams server, set `eda_event_stream_pgclient_tls_files_remote=true`.
