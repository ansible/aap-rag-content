# 2. System requirements
## 2.7. PostgreSQL requirements
### 2.7.3. Enabling mutual TLS (mTLS) authentication




Enable mutual TLS authentication to secure PostgreSQL database connections with certificate-based verification. This protects against unauthorized access and man-in-the-middle attacks while meeting enterprise security and compliance requirements.

**Procedure**

- To configure each component’s database with mTLS authentication, add the following variables to your inventory file under the `    [all:vars]` group and ensure each component has a different TLS certificate and key:


```
# Automation controller    pgclient_sslcert=/path/to/awx.cert    pgclient_sslkey=/path/to/awx.key    pg_sslmode=verify-full or verify-ca        # Platform gateway    automationgateway_pgclient_sslcert=/path/to/gateway.cert    automationgateway_pgclient_sslkey=/path/to/gateway.key    automationgateway_pg_sslmode=verify-full or verify-ca        # Automation hub    automationhub_pgclient_sslcert=/path/to/pulp.cert    automationhub_pgclient_sslkey=/path/to/pulp.key    automationhub_pg_sslmode=verify-full or verify-ca        # Event-Driven Ansible    automationedacontroller_pgclient_sslcert=/path/to/eda.cert    automationedacontroller_pgclient_sslkey=/path/to/eda.key    automationedacontroller_pg_sslmode=verify-full or verify-ca
```




