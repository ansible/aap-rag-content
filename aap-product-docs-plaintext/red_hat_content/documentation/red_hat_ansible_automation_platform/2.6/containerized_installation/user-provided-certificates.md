# 5. Advanced containerized deployment
## 5.7. Configuring custom TLS certificates
### 5.7.2. User-provided certificates

To use your own TLS certificates and keys to replace some or all of the self-signed certificates generated during installation, you can set specific variables in your inventory file. A public or organizational CA must generate these certificates and keys in advance so that they are available during the installation process.

#### 5.7.2.1. Using a custom CA to generate all TLS certificates

Use this method when you want Ansible Automation Platform to generate all of the certificates, but you want them signed by a custom CA rather than the default self-signed certificates.

When you use `ca_tls_cert` and `ca_tls_key`, the installation program automatically creates TLS certificates for each Ansible Automation Platform service using your provided CA certificate. You do not need to define individual service certificate variables (such as `gateway_tls_cert`, `controller_tls_cert`, or `hub_tls_cert`) because the installation program generates these certificates for you.

**Procedure**

- To use a custom Certificate Authority (CA) to generate TLS certificates for all Ansible Automation Platform services, set the following variables in your inventory file:

ca_tls_cert=<path_to_ca_tls_certificate>
ca_tls_key=<path_to_ca_tls_key>

Where:

- `ca_tls_cert` is the path to your custom CA certificate file.

- `ca_tls_key` is the path to the key file for your custom CA certificate.

#### 5.7.2.2. Providing custom TLS certificates for each service

Use this method if your organization manages TLS certificates outside of Ansible Automation Platform and requires manual provisioning.

**Procedure**

- To manually provide TLS certificates for each individual service (for example, automation controller, automation hub, and Event-Driven Ansible), set the following variables in your inventory file:

# Platform gateway
gateway_tls_cert=<path_to_tls_certificate>
gateway_tls_key=<path_to_tls_key>
gateway_pg_tls_cert=<path_to_tls_certificate>
gateway_pg_tls_key=<path_to_tls_key>
gateway_redis_tls_cert=<path_to_tls_certificate>
gateway_redis_tls_key=<path_to_tls_key>

# Automation controller
controller_tls_cert=<path_to_tls_certificate>
controller_tls_key=<path_to_tls_key>
controller_pg_tls_cert=<path_to_tls_certificate>
controller_pg_tls_key=<path_to_tls_key>

# Automation hub
hub_tls_cert=<path_to_tls_certificate>
hub_tls_key=<path_to_tls_key>
hub_pg_tls_cert=<path_to_tls_certificate>
hub_pg_tls_key=<path_to_tls_key>

# Event-Driven Ansible
eda_tls_cert=<path_to_tls_certificate>
eda_tls_key=<path_to_tls_key>
eda_pg_tls_cert=<path_to_tls_certificate>
eda_pg_tls_key=<path_to_tls_key>
eda_redis_tls_cert=<path_to_tls_certificate>
eda_redis_tls_key=<path_to_tls_key>

# PostgreSQL
postgresql_tls_cert=<path_to_tls_certificate>
postgresql_tls_key=<path_to_tls_key>

# Receptor
receptor_tls_cert=<path_to_tls_certificate>
receptor_tls_key=<path_to_tls_key>

# Redis
redis_tls_cert=<path_to_tls_certificate>
redis_tls_key=<path_to_tls_key>

If all components share the same fully qualified domain name (FQDN), use the same certificate and key for each service:

gateway_tls_cert=/home/user/certs/myhost.example.com.crt
gateway_tls_key=/home/user/certs/myhost.example.com.key
controller_tls_cert=/home/user/certs/myhost.example.com.crt
controller_tls_key=/home/user/certs/myhost.example.com.key
hub_tls_cert=/home/user/certs/myhost.example.com.crt
hub_tls_key=/home/user/certs/myhost.example.com.key
eda_tls_cert=/home/user/certs/myhost.example.com.crt
eda_tls_key=/home/user/certs/myhost.example.com.key
postgresql_tls_cert=/home/user/certs/myhost.example.com.crt
postgresql_tls_key=/home/user/certs/myhost.example.com.key

If components are deployed on separate hosts with different FQDNs, provide a unique certificate for each service:

gateway_tls_cert=/home/user/certs/gateway.example.com.crt
gateway_tls_key=/home/user/certs/gateway.example.com.key
controller_tls_cert=/home/user/certs/controller.example.com.crt
controller_tls_key=/home/user/certs/controller.example.com.key
hub_tls_cert=/home/user/certs/hub.example.com.crt
hub_tls_key=/home/user/certs/hub.example.com.key
eda_tls_cert=/home/user/certs/eda.example.com.crt
eda_tls_key=/home/user/certs/eda.example.com.key
postgresql_tls_cert=/home/user/certs/postgresql.example.com.crt
postgresql_tls_key=/home/user/certs/postgresql.example.com.key

#### 5.7.2.3. Considerations for certificates provided per service

When providing custom TLS certificates for each individual service, consider the following:

- Each service has its own `_tls_cert` and `_tls_key` variables. You can provide unique certificates for each service, or use the same certificate across multiple services if they share a fully qualified domain name (FQDN). If you do not define a certificate for a service, the installation program generates a self-signed certificate for that service.
- For services deployed across many nodes (for example, when following the enterprise topology), the provided certificate for that service must include the FQDN of all associated nodes in its Subject Alternative Name (SAN) field.
- If an external-facing service (such as automation controller or platform gateway) is deployed behind a load balancer that performs SSL/TLS offloading, the service’s certificate must include the load balancer’s FQDN in its SAN field, in addition to the FQDNs of the individual service nodes.

**Additional resources**

- [Securing networks](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/securing_networks/index)

#### 5.7.2.4. Providing a custom CA certificate

When you manually provide TLS certificates for Ansible Automation Platform services (such as `gateway_tls_cert`, `controller_tls_cert`, or `hub_tls_cert`), those certificates might be signed by a custom CA.

Use the `custom_ca_cert` variable to add your CA certificate to the environment for proper authentication and trust of the manually provided certificates.

**Procedure**

- If any of the TLS certificates you manually provided are signed by a custom CA, specify the CA certificate by using the following variable in your inventory file:

custom_ca_cert=<path_to_custom_ca_certificate>

If you have more than one CA certificate, combine them into a single file and reference the combined certificate with the `custom_ca_cert` variable.

