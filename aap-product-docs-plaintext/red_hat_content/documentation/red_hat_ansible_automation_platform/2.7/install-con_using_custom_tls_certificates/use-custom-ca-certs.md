# Configure custom TLS certificates
## Use a custom CA to generate all TLS certificates

Use this method when you want Ansible Automation Platform to generate all of the certificates, but you want them signed by a custom CA rather than the default self-signed certificates.

### About this task

When you use `ca_tls_cert` and `ca_tls_key`, the installation program automatically creates TLS certificates for each Ansible Automation Platform service using your provided CA certificate. You do not need to define individual service certificate variables (such as `gateway_tls_cert`, `controller_tls_cert`, `hub_tls_cert`, or `automationmetrics_tls_cert`) because the installation program generates these certificates for you.

### Procedure

To use a custom Certificate Authority (CA) to generate TLS certificates for all Ansible Automation Platform services, set the following variables in your inventory file:

```
ca_tls_cert=<path_to_ca_tls_certificate>
ca_tls_key=<path_to_ca_tls_key>
```
Where:

`ca_tls_cert`
is the path to your custom CA certificate file.

`ca_tls_key`
is the path to the key file for your custom CA certificate.

