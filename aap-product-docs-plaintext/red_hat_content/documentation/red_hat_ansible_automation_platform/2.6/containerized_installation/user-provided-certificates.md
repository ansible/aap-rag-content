# 5. Advanced containerized deployment
## 5.7. Configuring custom TLS certificates
### 5.7.2. User-provided certificates




To use your own TLS certificates and keys to replace some or all of the self-signed certificates generated during installation, you can set specific variables in your inventory file. A public or organizational CA must generate these certificates and keys in advance so that they are available during the installation process.

#### 5.7.2.1. Using a custom CA to generate all TLS certificates




Use this method when you want Ansible Automation Platform to generate all of the certificates, but you want them signed by a custom CA rather than the default self-signed certificates.

When you use `ca_tls_cert` and `ca_tls_key` , the installation program automatically creates TLS certificates for each Ansible Automation Platform service using your provided CA certificate. You do not need to define individual service certificate variables (such as `gateway_tls_cert` , `controller_tls_cert` , or `hub_tls_cert` ) because the installation program generates these certificates for you.

**Procedure**

- To use a custom Certificate Authority (CA) to generate TLS certificates for all Ansible Automation Platform services, set the following variables in your inventory file:


```
ca_tls_cert=&lt;path_to_ca_tls_certificate&gt;    ca_tls_key=&lt;path_to_ca_tls_key&gt;
```

Where:


-  `    ca_tls_cert` is the path to your custom CA certificate file.
-  `    ca_tls_key` is the path to the key file for your custom CA certificate.


#### 5.7.2.2. Providing custom TLS certificates for each service




Use this method if your organization manages TLS certificates outside of Ansible Automation Platform and requires manual provisioning.

**Procedure**

- To manually provide TLS certificates for each individual service (for example, automation controller, automation hub, and Event-Driven Ansible), set the following variables in your inventory file:


```
# Platform gateway    gateway_tls_cert=&lt;path_to_tls_certificate&gt;    gateway_tls_key=&lt;path_to_tls_key&gt;    gateway_pg_tls_cert=&lt;path_to_tls_certificate&gt;    gateway_pg_tls_key=&lt;path_to_tls_key&gt;    gateway_redis_tls_cert=&lt;path_to_tls_certificate&gt;    gateway_redis_tls_key=&lt;path_to_tls_key&gt;        # Automation controller    controller_tls_cert=&lt;path_to_tls_certificate&gt;    controller_tls_key=&lt;path_to_tls_key&gt;    controller_pg_tls_cert=&lt;path_to_tls_certificate&gt;    controller_pg_tls_key=&lt;path_to_tls_key&gt;        # Automation hub    hub_tls_cert=&lt;path_to_tls_certificate&gt;    hub_tls_key=&lt;path_to_tls_key&gt;    hub_pg_tls_cert=&lt;path_to_tls_certificate&gt;    hub_pg_tls_key=&lt;path_to_tls_key&gt;        # Event-Driven Ansible    eda_tls_cert=&lt;path_to_tls_certificate&gt;    eda_tls_key=&lt;path_to_tls_key&gt;    eda_pg_tls_cert=&lt;path_to_tls_certificate&gt;    eda_pg_tls_key=&lt;path_to_tls_key&gt;    eda_redis_tls_cert=&lt;path_to_tls_certificate&gt;    eda_redis_tls_key=&lt;path_to_tls_key&gt;        # PostgreSQL    postgresql_tls_cert=&lt;path_to_tls_certificate&gt;    postgresql_tls_key=&lt;path_to_tls_key&gt;        # Receptor    receptor_tls_cert=&lt;path_to_tls_certificate&gt;    receptor_tls_key=&lt;path_to_tls_key&gt;        # Redis    redis_tls_cert=&lt;path_to_tls_certificate&gt;    redis_tls_key=&lt;path_to_tls_key&gt;
```




#### 5.7.2.3. Considerations for certificates provided per service




When providing custom TLS certificates for each individual service, consider the following:

- It is possible to provide unique certificates per host. This requires defining the specific `    _tls_cert` and `    _tls_key` variables in your inventory file as shown in the earlier inventory file example.
- For services deployed across many nodes (for example, when following the enterprise topology), the provided certificate for that service must include the FQDN of all associated nodes in its Subject Alternative Name (SAN) field.
- If an external-facing service (such as automation controller or platform gateway) is deployed behind a load balancer that performs SSL/TLS offloading, the service’s certificate must include the load balancer’s FQDN in its SAN field, in addition to the FQDNs of the individual service nodes.


**Additional resources**

-  [Securing networks](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/securing_networks/index)


#### 5.7.2.4. Providing a custom CA certificate




When you manually provide TLS certificates for Ansible Automation Platform services (such as `gateway_tls_cert` , `controller_tls_cert` , or `hub_tls_cert` ), those certificates might be signed by a custom CA.

Use the `custom_ca_cert` variable to add your CA certificate to the environment for proper authentication and trust of the manually provided certificates.

**Procedure**

- If any of the TLS certificates you manually provided are signed by a custom CA, specify the CA certificate by using the following variable in your inventory file:


```
custom_ca_cert=&lt;path_to_custom_ca_certificate&gt;
```

If you have more than one CA certificate, combine them into a single file and reference the combined certificate with the `    custom_ca_cert` variable.




