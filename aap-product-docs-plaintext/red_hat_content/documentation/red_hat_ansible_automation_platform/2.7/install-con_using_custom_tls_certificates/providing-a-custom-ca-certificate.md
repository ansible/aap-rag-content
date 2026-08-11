# Configure custom TLS certificates
## Provide a custom CA certificate

To ensure proper authentication and trust for manually provided TLS certificates signed by a custom Certificate Authority (CA), specify the path to your single or combined CA certificate using the `custom_ca_cert` variable in your inventory file.

### About this task

When you manually provide TLS certificates for Ansible Automation Platform services (such as `gateway_tls_cert`, `controller_tls_cert`, `hub_tls_cert`, or `automationmetrics_tls_cert`), those certificates might be signed by a custom CA.

Use the `custom_ca_cert` variable to add your CA certificate to the system-level truststore on all Ansible Automation Platform hosts. This allows the hosts to trust external endpoints that present certificates signed by your organization's CA, such as LDAP servers, Git repositories, and container registries.

The `custom_ca_cert` certificate is added to `mesh-CA.crt` only when `receptor_tls_cert` is also provided. In that scenario, the CA in `custom_ca_cert` must be the CA that signed the custom receptor certificates so that the receptor mesh can validate them. When `receptor_tls_cert` is not set, `custom_ca_cert` is not included in `mesh-CA.crt` and does not affect receptor mesh trust.

### Procedure

If any of the TLS certificates you manually provided are signed by a custom CA, specify the CA certificate by using the following variable in your inventory file:

`custom_ca_cert=<path_to_custom_ca_certificate>`

If you have more than one CA certificate, combine them into a single file and reference the combined certificate with the `custom_ca_cert` variable.

Important:

The receptor mesh has a practical size limit on the CA trust bundle in `mesh-CA.crt`. If you provide `receptor_tls_cert` and the `custom_ca_cert` file contains a large enterprise CA bundle with many intermediate or cross-signed certificates, receptor can fail with `crypto buffer exceeded` errors. When providing custom receptor certificates, use a `custom_ca_cert` file that contains only the CA certificate that signed the receptor certificates. Large CA bundles are safe to use with `custom_ca_cert` when `receptor_tls_cert` is not set, because in that case the bundle is used only for system trust and is not added to `mesh-CA.crt`.

