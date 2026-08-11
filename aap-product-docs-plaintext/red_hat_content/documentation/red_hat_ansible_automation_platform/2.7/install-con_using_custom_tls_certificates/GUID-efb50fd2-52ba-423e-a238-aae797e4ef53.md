# Configure custom TLS certificates
## Understand the receptor mesh CA trust bundle

The receptor mesh uses a CA trust bundle stored in `mesh-CA.crt` to validate TLS connections between mesh nodes. The contents of `mesh-CA.crt` depend on which certificate variables you set in your inventory file.

The following table describes the three scenarios that determine the contents of `mesh-CA.crt`.

| **Variables set**                     | **mesh-CA.crt contains**   | **Approach** |
| ------------------------------------- | -------------------------- | ------------ |
| None (default)                        | Installer self-signed CA   | Default      |
| `ca_tls_cert` +`ca_tls_key`           | Your enterprise CA         | Recommended  |
| `receptor_tls_cert` +`custom_ca_cert` | Your custom CA certificate | Advanced     |

**Default: No custom certificates**

When you do not set `ca_tls_cert`, `ca_tls_key`, `receptor_tls_cert`, or `custom_ca_cert`, the installation program generates its own self-signed CA and uses it to sign receptor node certificates. The self-signed CA is placed in `mesh-CA.crt`.

**Provide an enterprise CA and key**

When you set `ca_tls_cert` and `ca_tls_key`, the installer uses your CA and key to sign receptor node certificates instead of generating its own. Your CA certificate is placed in `mesh-CA.crt` and becomes the mesh CA for receptor communication.

If you also set `custom_ca_cert`, that certificate is used only for system-level trust (`update-ca-trust`) and is not added to `mesh-CA.crt`.

This is the recommended approach for organizations that want to use their own CA for receptor mesh certificates. Create an Ansible Automation Platform-specific child or intermediate CA and key from your organization's root CA. This lets the installer generate properly formatted receptor node certificates with the required receptor OID while keeping the mesh CA small and purpose-built.

**Provide pre-signed receptor certificates**

When you set `receptor_tls_cert` and `receptor_tls_key` without `ca_tls_cert`, you provide your own receptor certificates that were signed externally. You must also set `custom_ca_cert` to the CA certificate that signed the receptor certificates. The installation program imports the receptor certificates directly and does not generate or sign them.

In this scenario, the CA certificate from `custom_ca_cert` is placed in `mesh-CA.crt` so that receptor nodes can validate each other's certificates.

This approach gives you full control over certificate issuance. You must generate receptor node certificates that include the required receptor OID (`1.3.6.1.4.1.2312.19.1`) in the Subject Alternative Name (SAN) `otherName` field and the host FQDN in the SAN. Wildcard certificates are not supported for receptor.

**Recommended approaches for custom receptor certificates**

If your organization requires custom certificates for receptor mesh communication, there are two approaches. Choose the approach that matches your certificate management requirements.

**Use ca_tls_cert and ca_tls_key**

Create an Ansible Automation Platform-specific child or intermediate CA and key from your organization's root CA. Set `ca_tls_cert` and `ca_tls_key` in your inventory file to point to this CA and key.

The installation program uses your CA to generate properly formatted receptor node certificates with the required receptor OID. This approach keeps the mesh CA small and purpose-built and does not require you to manage individual receptor node certificates.

`ca_tls_cert=/home/user/certs/aap-intermediate-ca.crt`

`ca_tls_key=/home/user/certs/aap-intermediate-ca.key`

If your Ansible Automation Platform hosts also need to trust external endpoints signed by a different CA, set `custom_ca_cert` separately. That certificate is used only for system trust and does not affect `mesh-CA.crt`.

**Use receptor_tls_cert and receptor_tls_key**

Generate your own receptor node certificates and provide them with `receptor_tls_cert` and `receptor_tls_key`. You must also set `custom_ca_cert` to the CA certificate that signed the receptor certificates.

`receptor_tls_cert=/home/user/certs/receptor.example.com.crt`

`receptor_tls_key=/home/user/certs/receptor.example.com.key`

`custom_ca_cert=/home/user/certs/signing-ca.crt`

This approach requires you to manage certificate issuance for each receptor node, including the following requirements:

- Each certificate must include the `otherName` field in the *Subject Alternative Name* (SAN) with the value `1.3.6.1.4.1.2312.19.1`.
- Each certificate must include the host FQDN in the SAN
- Wildcard certificates are not supported.
- The `custom_ca_cert` file should contain only the CA certificate that signed the receptor certificates. Avoid using large enterprise CA bundles, which can cause `crypto buffer exceeded` errors when the `mesh-CA.crt` bundle exceeds the QUIC 16 KB buffer limit.

