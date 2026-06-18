+++
title = "Installation settings to secure your platform - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-con_installation"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_hardening_aap/", "Harden the platform security posture"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-con_installation/aem-page/secure-con_installation.html"
last_crumb = "Installation settings to secure your platform"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Installation settings to secure your platform"
oversized = "false"
page_slug = "secure-con_installation"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-con_installation"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-con_installation/toc/toc.json"
type = "aem-page"
+++

# Installation settings to secure your platform

Installation decisions directly impact the security posture of Ansible Automation Platform. The process involves setting several variables critical to infrastructure hardening. Before installing, review the installation guidance to ensure your configuration meets security standards.

## Install from a dedicated installation host

The Ansible Automation Platform installation program can be run from one of the infrastructure servers, such as an automation controller, or from an external system that has SSH access to the Ansible Automation Platform infrastructure servers.

The Ansible Automation Platform installation program is also used not just for installation, but for subsequent day-two operations, such as backup and restore, and upgrades. Perform installation and day-two operations from a dedicated external server, hereafter referred to as the installation host. Doing so eliminates the need to log in to one of the infrastructure servers to run these functions. The installation host must only be used for management of Ansible Automation Platform and must not run any other services or software.

The installation host must be a Red Hat Enterprise Linux server that has been installed and configured in accordance with Security hardening for Red Hat Enterprise Linux and any security profile requirements relevant to your organization (CIS, STIG, and so on). Obtain the Ansible Automation Platform installer and create the installation program inventory file. This inventory file is used for upgrades, adding infrastructure components, and day-two operations by the installation program, so preserve the file after installation for future operational use.

Access to the installation host must be restricted only to those personnel who are responsible for managing the Ansible Automation Platform infrastructure. Over time, it will contain sensitive information, such as the installation inventory (which contains the initial login credentials for Ansible Automation Platform), copies of user-provided PKI keys and certificates, backup files, and so on. The installation host must also be used for logging in to the Ansible Automation Platform infrastructure servers through SSH when necessary for infrastructure management and maintenance.

## Security-relevant variables in the installation inventory

Customize the installation inventory file to define your Ansible Automation Platform architecture and change the initial configuration of its components.

The following table lists several security-relevant variables and their recommended values for an RPM-based deployment.

*Table 1. Security\-relevant inventory variables*

| **RPM deployment variable**                                                                                                  | **Recommended Value** | **Details**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------- | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br> `postgres_use_ssl`                                                                                                      | <br>true              | <br>The installation program configures the installation program-managed Postgres database to accept SSL/TLS-based connections when this variable is set.<br>The default for this variable is false which means SSL/TLS is not used for PostgreSQL connections.<br>When set to true, the platform connects to PostgreSQL by using SSL/TLS.                                                                                                                                                                                                                                                           |
| <br> `pg_sslmode` `automation_gateway_pg_sslmode` `automationhub_pg_sslmode` `automationcontroller_pg_sslmode`               | <br>verify-full       | <br>These variables control mutual TLS (mTLS) authentication to the database. By default, when each service connects to the database, it tries an encrypted connection, but it is not enforced.<br>Setting this variable to `verify-full` enforces an mTLS negotiation between the service and the database. The `postgres_use_ssl` variable must also be set to `true` for this pg\_sslmode to be effective.<br>**NOTE**: If a third-party database is used instead of the installation program-managed database, the third-party database must be set up independently to accept mTLS connections. |
| <br> `nginx_disable_hsts` `automation_gateway_disable_hsts` `automationhub_disable_hsts` `automationcontroller_disable_hsts` | <br>false             | <br>If set to `true`, these variables disable HTTPS *strict transport Security* (HSTS) connections to each of the component web services.<br>The default is `false`. If these variables are absent from the installation program inventory it is effectively equivalent to defining the variables as `false`.                                                                                                                                                                                                                                                                                        |


The following table lists several security-relevant variables and their recommended values for a container-based deployment.

*Table 2. Security\-relevant containerized inventory variables*

| **Container deployment variable**                                                                                      | **Recommended Value** | **Details**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------------------------------------------------------------------------------------------------------------- | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br> `postgresql_disable_tls`                                                                                          | <br>false             | <br>If set to `true`, this variable disables TLS connections to the installation program-managed PostgreSQL database.<br>The default is `false`<br>If this variable is absent from the installation program inventory, it is effectively equivalent to defining the variable as `false`.                                                                                                                                                                                                            |
| <br> `controller_pg_sslmode` `gateway_pg_sslmode` `hub_pg_sslmode` `eda_pg_sslmode`                                    | <br>verify-full       | <br>These variables control mutual TLS (mTLS) authentication to the database.<br>By default, when each service connects to the database, it tries an encrypted connection, but it is not enforced. Setting this variable to `verify-full` enforces an mTLS negotiation between the service and the database.  Note:   <br>If a third-party database is used instead of the installation program-managed database, the third-party database must be set up independently to accept mTLS connections. |
| <br> `controller_nginx_disable_https` `gateway_nginx_disable_https` `hub_nginx_disable_https` `da_nginx_disable_https` | <br> `false`          | <br>If set to `true`, these variables disable HTTPS connections to each of the component web services.<br>The default is `false`.<br>If these variables are absent from the installation program inventory, it is effectively equivalent to defining the variables as `false`.                                                                                                                                                                                                                      |
| <br> `controller_nginx_disable_hsts` `gateway_nginx_disable_hsts` `hub_nginx_disable_hsts` `eda_nginx_disable_hsts`    | <br> `false`          | <br>If set to 'true', these variables disable HTTPS Strict Transport Security (HSTS) connections to each of the component web services.<br>The default is `false`.<br>If these variables are absent from the installation program inventory it is effectively equivalent to defining the variables as `false`.                                                                                                                                                                                      |


In an enterprise architecture where a load balancer is used in front of multiple platform gateways, SSL/TLS client connections can be terminated at the load balancer or passed through to the individual AAP servers. If SSL/TLS is being terminated at the load balancer, this section recommends that the traffic gets re-encrypted from the load balancer to the individual Ansible Automation Platform servers. This ensures that end-to-end encryption is in use. In this scenario, the `*_disable_https` variables listed are set to the default value of `false`.

## Install with user-provided PKI certificates

Replace the default self-signed certificates with custom PKI certificates for your Ansible Automation Platform components. Using your existing PKI infrastructure helps ensure trusted and secure communication across the platform.

### Procedure

1.  Copy the certificate files and their relevant key files to the installation program directory, along with the CA certificate used to verify the certificates.
2.  Use the following inventory variables to configure the infrastructure components with the new certificates. *Table 3. PKI certificate inventory variables*

    | <br> **RPM Variable**                   | <br> **Containerized Variable** | <br> **Details**                                                                                                                                                                                                                  |
    | --------------------------------------- | ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | <br> `custom_ca_cert`                   | <br> `custom_ca_cert`           | <br>The path to the custom CA certificate file.<br>If set, this will install a custom CA certificate to the system truststore.                                                                                                    |
    | <br> `web_server_ssl_cert`              | <br> `controller_tls_cert`      | <br>The file name of the automation controller PKI certificate located in the installation program directory.                                                                                                                     |
    | <br> `web_server_ssl_key`               | <br> `controller_tls_key`       | <br>The file name of the automation controller PKI key located in the installation program directory.                                                                                                                             |
    | <br> `automationhub_ssl_cert`           | <br> `hub_tls_cert`             | <br>The file name of the private automation hub PKI certificate located in the installation program directory.                                                                                                                    |
    | <br> `automationhub_ssl_key`            | <br> `hub_tls_key`              | <br>The file name of the private automation hub PKI key located in the installation program directory.                                                                                                                            |
    | <br> `postgres_ssl_cert`                | <br> `postgresql_tls_cert`      | <br>The file name of the database server PKI certificate located in the installation program directory. This variable is only needed for the installation program managed database server, not if a third-party database is used. |
    | <br> `postgres_ssl_key`                 | <br> `postgresql_tls_key`       | <br>The file name of the database server PKI key located in the installation program directory. This variable is only needed for the installation program-managed database server, not if a third-party database is used.         |
    | <br> `automationedacontroller_ssl_cert` | <br> `eda_tls_cert`             | <br>The file name of the Event-Driven Ansible controller PKI certificate located in the installation program directory.                                                                                                           |
    | <br> `automationedacontroller_ssl_key`  | <br> `eda_tls_key`              | <br>The file name of the Event-Driven Ansible controller PKI key located in the installation program directory.                                                                                                                   |
    | <br>-                                   | <br> `gateway_tls_cert`         | <br>The filename of the platform gateway PKI certificate located in the installation program directory.                                                                                                                           |
    | <br>-                                   | <br> `gateway_tls_key`          | <br>The file name of the platform gateway PKI key located in the installation program directory.                                                                                                                                  |
    When multiple platform gateways are deployed with a load balancer, `gateway_tls_cert` and `gateway_tls_key` are shared by each platform gateway. To prevent hostname mismatches, the certificate’s *Common Name* (CN) must match the DNS FQDN used by the load balancer. If your organizational policies require unique certificates for each service, each certificate requires a *Subject Alt Name* (SAN) that matches the DNS FQDN used for the load-balanced service. To install unique certificates and keys on each platform gateway, the certificate and key variables in the installation inventory file must be defined as host variables instead of in the `[all:vars]` section. For example:

```
[automationgateway]
gateway0.example.com gateway_tls_cert=/path/to/cert0 gateway_tls_key=/path/to/key0
gateway1.example.com gateway_tls_cert=/path/to/cert1 gateway_tls_key=/path/to/key1

    [automationcontroller]
controller0.example.com web_server_ssl_cert=/path/to/cert0 web_server_ssl_key=/path/to/key0
controller1.example.com web_server_ssl_cert=/path/to/cert1 web_server_ssl_key=/path/to/key1
controller2.example.com web_server_ssl_cert=/path/to/cert2 web_server_ssl_key=/path/to/key2

    [automationhub]
hub0.example.com automationhub_ssl_cert=/path/to/cert0 automationhub_ssl_key=/path/to/key0
hub1.example.com automationhub_ssl_cert=/path/to/cert1 automationhub_ssl_key=/path/to/key1
hub2.example.com automationhub_ssl_cert=/path/to/cert2 automationhub_ssl_key=/path/to/key2
```

## Secure sensitive variables with ansible vault

By securing sensitive values in the installation inventory file with Ansible Vault, both RPM-based and containerized Ansible Automation Platform installations benefit from improved security, password hygiene, and maintainability.

### Procedure

1.  Navigate to the install directory by using the following command:
       `cd /path/to/ansible-automation-platform-setup-bundle-2.5-<version>`

2.  Create a vault file by using the following command:
       `ansible-vault create vault.yml`

3.  When prompted, enter a vault password This password is required to access or modify the vault and is required for day-two operations such as backups and reconfigurations. Important:
      Passwords with special characters must be in double quotes.

4.  Store the vault password securely, in accordance with your organizations security policy, for example, using a password manager or vault service.
5.  Add your sensitive variables to the vault and ensure they are not also defined in the inventory file. To edit your vault file use:

     `ansible-vault edit <file>`

## Use an external vault file with an RPM-based Ansible Automation Platform deployment

When installing Ansible Automation Platform using RPM packages, you can use an external Ansible vault file to securely provide sensitive variables, such as passwords, during the installation process.

### About this task

For RPM-based installations, you can provide the Ansible vault at runtime when executing the setup script.

Add the following sensitive variables to the vault file:

```
admin_password: <secure_password>
pg_password: <secure_password>
automationgateway_admin_password: <secure_password>
automationgateway_pg_password: <secure_password>
automationhub_admin_password: <secure_password>
automationhub_pg_password: <secure_password>
automationedacontroller_admin_password: <secure_password>
automationedacontroller_pg_password: <secure_password>

*In the case of a connected installation:

registry_password: <secure_cdn_password>
```
To use the vault during installation, use the following procedure:

### Procedure

1.  Ensure the vault file, for example, `vault.yml`, contains all required sensitive variables.
2.  Run the installation using the following command:
       `./setup.sh -e @vault.yml -ask-vault-pass`

    Using this procedure ensures that the installation program reads encrypted variables from the vault and prompts for the vault password.

## Use an external vault file with a containerized installation

For containerized installations of Ansible Automation Platform, use the provided automation execution playbook with the external vault file.

### About this task

Add the following sensitive variables to the vault file:

```
postgresql_admin_password:  <secure_password>
gateway_admin_password:  <secure_password>
gateway_pg_password:  <secure_password>
controller_admin_password:  <secure_password>
controller_pg_password:  <secure_password>
hub_admin_password:  <secure_password>c
hub_pg_password:  <secure_password>
eda_admin_password:  <secure_password>
eda_pg_password: <secure_password>

*In the case of a connected installation:

registry_password: <secure_cdn_password>
```
To use the new Ansible vault with the installation program, use the following procedure:

### Procedure

1.  Ensure your vault file, for example, `vault.yml`, contains all required sensitive variables.
2.  Run the container installer using the following command:
      `ansible-playbook ansible.containerized_installer.install -e @vault.yml -ask-become-pass`.

    Ensure that the vault file is located in the working directory, or provide the full path. Do not duplicate the encrypted variables in the `plaintext` inventory file.
