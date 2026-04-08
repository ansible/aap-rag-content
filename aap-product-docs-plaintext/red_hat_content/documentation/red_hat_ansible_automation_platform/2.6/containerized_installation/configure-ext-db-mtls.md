# 5. Advanced containerized deployment
## 5.6. Configuring an external (customer provided) PostgreSQL database
### 5.6.4. Optional: configuring mutual TLS (mTLS) authentication for an external database




mTLS authentication is disabled by default. To configure each component’s database with mTLS authentication, add the following variables to your inventory file under the `[all:vars]` group and ensure each component has a different TLS certificate and key:

**Procedure**

- Add the following variables to your inventory file under the `    [all:vars]` group:


```
# Platform gateway    gateway_pg_cert_auth=true    gateway_pg_tls_cert=/path/to/gateway.cert    gateway_pg_tls_key=/path/to/gateway.key    gateway_pg_sslmode=verify-full        # Automation controller    controller_pg_cert_auth=true    controller_pg_tls_cert=/path/to/awx.cert    controller_pg_tls_key=/path/to/awx.key    controller_pg_sslmode=verify-full        # Automation hub    hub_pg_cert_auth=true    hub_pg_tls_cert=/path/to/pulp.cert    hub_pg_tls_key=/path/to/pulp.key    hub_pg_sslmode=verify-full        # Event-Driven Ansible    eda_pg_cert_auth=true    eda_pg_tls_cert=/path/to/eda.cert    eda_pg_tls_key=/path/to/eda.key    eda_pg_sslmode=verify-full
```




