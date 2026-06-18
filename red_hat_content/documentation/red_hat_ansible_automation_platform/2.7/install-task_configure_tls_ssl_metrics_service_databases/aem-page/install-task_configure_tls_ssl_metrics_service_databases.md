+++
title = "Configure TLS/SSL for metrics service databases - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-task_configure_tls_ssl_metrics_service_databases"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_understand_metrics_service_architecture/", "Understand metrics service architecture"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-task_configure_tls_ssl_metrics_service_databases/aem-page/install-task_configure_tls_ssl_metrics_service_databases.html"
last_crumb = "Configure TLS/SSL for metrics service databases"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure TLS/SSL for metrics service databases"
oversized = "false"
page_slug = "install-task_configure_tls_ssl_metrics_service_databases"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-task_configure_tls_ssl_metrics_service_databases"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-task_configure_tls_ssl_metrics_service_databases/toc/toc.json"
type = "aem-page"
+++

# Configure TLS/SSL for metrics service databases

Enable TLS/SSL encryption for metrics service database connections to protect metrics data in transit and meet security policies.

## About this task

Use this procedure when securing database connections for compliance requirements.

## Procedure

1.  Configure PostgreSQL for TLS
      Edit postgresql.conf:

```
ssl = on
ssl_cert_file = '/path/to/server.crt'
ssl_key_file = '/path/to/server.key'
ssl_ca_file = '/path/to/ca.crt'
```

2.  Configure metrics service for TLS
      Edit your inventory file:

```
[all:vars]
automationmetrics_pg_sslmode=require
automationmetrics_pg_cert_auth=true
ca_trust_bundle=/path/to/ca-bundle.crt
```
  Note:
      When `automationmetrics_pg_cert_auth` is set to `true`, the installer automatically generates TLS certificates for database connections. For custom certificates, use the tasks/tls_postgresql.yml task.

## Results

**TLS/SSL modes**

| Mode          | Encryption                              | Certificate Verification |
| ------------- | --------------------------------------- | ------------------------ |
| `disable`     | No                                      | No                       |
| `allow`       | Attempts encrypted, accepts unencrypted | No                       |
| `prefer`      | Prefers encrypted, accepts unencrypted  | No                       |
| `require`     | Yes                                     | No                       |
| `verify-ca`   | Yes                                     | CA verification          |
| `verify-full` | Yes                                     | CA + hostname            |
