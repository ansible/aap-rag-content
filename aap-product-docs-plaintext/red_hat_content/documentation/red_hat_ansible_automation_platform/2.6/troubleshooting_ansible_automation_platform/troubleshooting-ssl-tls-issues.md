# 7. Networking
## 7.2. Troubleshooting SSL/TLS issues




To troubleshoot SSL/TLS issues, verify the certificate chain, use the correct certificates, and confirm that a trusted Certificate Authority (CA) signed the certificate.

**Procedure**

1. Check if the server is reachable over SSL/TLS.


1. Run the following command to confirm whether the server is reachable over SSL/TLS and to see the full certificate chain:


```
# true | openssl s_client -showcerts -connect &lt;fqdn_or_ip&gt;:&lt;port&gt;
```


1. Replace `        &lt;fqdn_or_ip&gt;` and `        &lt;port&gt;` with suitable values.

1. Verify the certificate details.


1. Run the following command to view the details of a certificate:


```
# openssl x509 -in &lt;path_to_certificate&gt; -noout -text
```



1. Replace `    &lt;path_to_certificate&gt;` with the path to the certificate file you want to inspect.

The result of the command shows information such as:


- Subject - The entity the certificate has been issued to.
- Issuer - The CA that issued the certificate.
- Validity "Not Before" - The date the certificate was issued.
- Validity "Not After" - The date the certificate expires.

1. Verify a trusted CA signed the certificate.


1. Run the following command to verify that a specific certificate is valid and was signed by a trusted CA:


```
openssl verify -CAfile &lt;path_to_ca_public_certificate&gt; &lt;path_to_server_certificate_file_to_verify&gt;
```


1. If the command returns `        OK` , it means the certificate file is valid and signed by a trusted CA.



