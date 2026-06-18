+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_self_service_rhel_configure_external_db"
template = "docs/aem-title.html"
title = "Configure an external database - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_self_service_rhel_appliances/", "Deploy Ansible automation portal RHEL appliance"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_self_service_rhel_configure_external_db/aem-page/install-proc_self_service_rhel_configure_external_db.html"
last_crumb = "Configure an external database"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure an external database"
oversized = "false"
page_slug = "install-proc_self_service_rhel_configure_external_db"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-proc_self_service_rhel_configure_external_db"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_self_service_rhel_configure_external_db/toc/toc.json"
type = "aem-page"
+++

# Configure an external database

By default, the Ansible automation portal RHEL appliance runs a built-in PostgreSQL database. For production deployments, connect to an external PostgreSQL database.

## Before you begin

- A PostgreSQL database instance accessible from the appliance.
- A database user with the `CREATEDB` privilege.
- The database password.
- SSH access to the appliance.

## About this task

You can provide external database settings in the cloud-init user-data at first boot or configure the database after deployment. For the cloud-init template fields, see [External database cloud-init template](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_self_service_rhel_prerequisites "Before you deploy an Ansible automation portal RHEL appliance, verify that your environment meets the system, network, and access requirements.").

## Procedure

1.  Edit the configuration file:
  

```terminal
$ sudo vi /etc/portal/configs/app-config/app-config.production.yaml
```

2.  Update the `backend.database` section:
  

```yaml
backend:
  database:
    connection:
      host: *database-host*
      port: 5432
      user: *database-user*
      ssl:
        require: true
    client: pg
```
    The database user requires the `CREATEDB` privilege.

3.  Store the database password as a Podman secret:
  

```terminal
$ printf '%s' "*database-password*" | sudo podman secret create portal_postgresql_password -
```

4.  Restart the Ansible automation portal service:
  

```terminal
$ sudo systemctl restart portal
```

## Results

Check the portal logs to verify the database connection:

```terminal
$ sudo journalctl -u portal --no-pager | grep -i "database"
```
The output shows a successful database connection with no errors.
