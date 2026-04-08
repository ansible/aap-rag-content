# 5. Advanced containerized deployment
## 5.7. Configuring custom TLS certificates
### 5.7.3. Receptor certificate considerations




When using a custom certificate for Receptor nodes, the certificate requires the `otherName` field specified in the Subject Alternative Name (SAN) of the certificate with the value `1.3.6.1.4.1.2312.19.1` . For more information, see [Above the mesh TLS](https://ansible.readthedocs.io/projects/receptor/en/latest/user_guide/tls.html#above-the-mesh-tls) .

Receptor does not support the usage of wildcard certificates. Additionally, each Receptor certificate must have the host FQDN specified in its SAN for TLS hostname validation to be correctly performed.

