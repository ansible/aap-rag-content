# Configure custom TLS certificates
## Receptor certificate considerations

To ensure successful TLS hostname validation and compatibility for Receptor nodes using custom certificates, specify the host FQDN and the required `otherName` OID in the *Subject Alternative Name* (SAN), as wildcard certificates are unsupported.

When using a custom certificate for Receptor nodes, the certificate requires the `otherName` field specified in the Subject Alternative Name (SAN) of the certificate with the value `1.3.6.1.4.1.2312.19.1`.

Receptor does not support the usage of wildcard certificates. Additionally, each Receptor certificate must have the host FQDN specified in its SAN for TLS hostname validation to be correctly performed.

**Preflight validation for custom receptor certificates**

When `receptor_tls_cert` is provided without `ca_tls_cert`, the installation program validates that `custom_ca_cert` is also set. If `custom_ca_cert` is not defined, the installation fails with the following error:

```
When receptor_tls_cert is provided without ca_tls_cert, custom_ca_cert must also be set to the CA certificate that signed the receptor certificates.
```

This validation ensures that the CA that signed the custom receptor certificates is available in `mesh-CA.crt` for receptor mesh trust. To resolve this error, set `custom_ca_cert` to the path of the CA certificate that signed your receptor certificates.

