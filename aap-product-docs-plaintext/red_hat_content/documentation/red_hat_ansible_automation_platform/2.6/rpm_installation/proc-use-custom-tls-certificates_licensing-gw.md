# 2. System requirements
## 2.6. PostgreSQL requirements
### 2.6.4. Using custom TLS certificates




By default, the installation program generates self-signed TLS certificates and keys for all Ansible Automation Platform services. However, you can optionally use custom TLS certificates.

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






