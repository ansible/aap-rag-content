# 2. System requirements
## 2.7. PostgreSQL requirements
### 2.7.4. Using custom TLS certificates




Configure the installer to use your custom TLS certificates and keys for all Ansible Automation Platform services instead of the default self-signed certificates. This is achieved by setting inventory variables ( `aap_ca_cert_file` and `aap_ca_key_file` ), and optionally specifying a custom Certificate Authority (CA) certificate using `custom_ca_cert` to ensure trust and security across the platform.

**Procedure**

- To replace these with your own custom certificate and key, set the following inventory file variables:


```
aap_ca_cert_file=&lt;path_to_ca_tls_certificate&gt;    aap_ca_key_file=&lt;path_to_ca_tls_key&gt;
```


- If any of your certificates are signed by a custom Certificate Authority (CA), then you must specify the Certificate Authority’s certificate by using the `    custom_ca_cert` inventory file variable:


```
custom_ca_cert=&lt;path_to_custom_ca_certificate&gt;
```

Note
If you have more than one custom CA certificate, combine them into a single file, then reference the combined certificate with the `    custom_ca_cert` inventory file variable.






