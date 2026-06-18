+++
title = "Container-based installations - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-con_change_tls_container_based_install"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_changing_ssl_certs_keys/", "Renew and change SSL/TLS certificates"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-con_change_tls_container_based_install/aem-page/secure-con_change_tls_container_based_install.html"
last_crumb = "Container-based installations"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Container-based installations"
oversized = "false"
page_slug = "secure-con_change_tls_container_based_install"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-con_change_tls_container_based_install"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-con_change_tls_container_based_install/toc/toc.json"
type = "aem-page"
+++

# Container-based installations

You can change the TLS certificates and keys for your container-based Ansible Automation Platform installation. This process involves a preparation step, either providing new custom certificates or deleting or moving the old certificates, followed by running the installation program.

## Change TLS certificates and keys using the installation program

The following procedure describes how to update the TLS certificates and keys by using the installation program.

### Procedure

1.  To prepare the certificates and keys, choose one of the following methods:

  - To provide custom certificates - For each service that requires updated TLS certificates, copy the new certificates and keys to a path relative to the Ansible Automation Platform installer. Then update the inventory file variables with the absolute paths to the new files.

```yaml
# Platform gateway
gateway_tls_cert=<path_to_tls_certificate>
gateway_tls_key=<path_to_tls_key>
gateway_pg_tls_cert=<path_to_tls_certificate>
gateway_pg_tls_key=<path_to_tls_key>
gateway_redis_tls_cert=<path_to_tls_certificate>
gateway_redis_tls_key=<path_to_tls_key>

        # Automation controller
controller_tls_cert=<path_to_tls_certificate>
controller_tls_key=<path_to_tls_key>
controller_pg_tls_cert=<path_to_tls_certificate>
controller_pg_tls_key=<path_to_tls_key>

        # Automation hub
hub_tls_cert=<path_to_tls_certificate>
hub_tls_key=<path_to_tls_key>
hub_pg_tls_cert=<path_to_tls_certificate>
hub_pg_tls_key=<path_to_tls_key>

        # Event-Driven Ansible
eda_tls_cert=<path_to_tls_certificate>
eda_tls_key=<path_to_tls_key>
eda_pg_tls_cert=<path_to_tls_certificate>
eda_pg_tls_key=<path_to_tls_key>

        # PostgreSQL
postgresql_tls_cert=<path_to_tls_certificate>
postgresql_tls_key=<path_to_tls_key>

        # Receptor
receptor_tls_cert=<path_to_tls_certificate>
receptor_tls_key=<path_to_tls_key>
```

  - To generate new certificates - If you want the installation program to generate a new certificate for a service, delete or move the existing certificates and keys. *Table 1. Certificate and key file paths per service*

      | Service                   | Certificate file path                 | Key file path                         |
      | ------------------------- | ------------------------------------- | ------------------------------------- |
      | <br>Automation controller | <br>`~/aap/controller/etc/tower.cert` | <br>`~/aap/controller/etc/tower.key`  |
      | <br>Event-Driven Ansible  | <br>`~/aap/eda/etc/eda.cert`          | <br>`~/aap/eda/etc/eda.key`           |
      | <br>Platform gateway      | <br>`~/aap/gateway/etc/gateway.cert`  | <br>`~/aap/gateway/etc/gateway.key`   |
      | <br>Automation hub        | <br>`~/aap/hub/etc/pulp.cert`         | <br>`~/aap/hub/etc/pulp.key`          |
      | <br>PostgreSQL            | <br>`~/aap/postgresql/server.crt`     | <br>`~/aap/postgresql/server.key`     |
      | <br>Receptor              | <br>`~/aap/receptor/etc/receptor.crt` | <br>`~/aap/receptor/etc/receptor.key` |
      | <br>Redis                 | <br>`~/aap/redis/server.crt`          | <br>`~/aap/redis/server.key`          |

2.  After preparing your certificates, run the `install` playbook from your installation directory:
  

```
ansible-playbook -i <inventory_file_name> ansible.containerized_installer.install
```

### Results

Verify that the new TLS certificates are in use by checking that the services are running and accessible. To do this, check a specific endpoint by using `curl`:

```
$ curl -vk https://<hostname_or_ip>:<port_number>/api/v2/
```
The output of this command gives details about the TLS handshake. Look for the following output to confirm the correct certificate is being used:

```
*  SSL certificate verify OK
```
