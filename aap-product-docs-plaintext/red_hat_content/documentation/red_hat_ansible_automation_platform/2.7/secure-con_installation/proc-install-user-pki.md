# Installation settings to secure your platform
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

