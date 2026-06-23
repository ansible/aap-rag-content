# Configure an external (customer provided) PostgreSQL database
## Optional: configure mutual TLS (mTLS) authentication for an external database

mTLS authentication is disabled by default. To configure each component’s database with mTLS authentication, add the following variables to your inventory file under the `[all:vars]` group and ensure each component has a different TLS certificate and key:

### Procedure

Add the following variables to your inventory file under the `[all:vars]` group:

```yaml
# Platform gateway
gateway_pg_cert_auth=true
gateway_pg_tls_cert=/path/to/gateway.cert
gateway_pg_tls_key=/path/to/gateway.key
gateway_pg_sslmode=verify-full

# Automation controller
controller_pg_cert_auth=true
controller_pg_tls_cert=/path/to/awx.cert
controller_pg_tls_key=/path/to/awx.key
controller_pg_sslmode=verify-full

# Automation hub
hub_pg_cert_auth=true
hub_pg_tls_cert=/path/to/pulp.cert
hub_pg_tls_key=/path/to/pulp.key
hub_pg_sslmode=verify-full

# Event-Driven Ansible
eda_pg_cert_auth=true
eda_pg_tls_cert=/path/to/eda.cert
eda_pg_tls_key=/path/to/eda.key
eda_pg_sslmode=verify-full

# Metrics service
automationmetrics_pg_cert_auth=true
automationmetrics_pg_tls_cert=/path/to/metrics.cert
automationmetrics_pg_tls_key=/path/to/metrics.key
automationmetrics_pg_sslmode=verify-full

# Metrics service read-only connection to controller
databaseautomationmetrics_controller_read_pg_cert_auth=true
automationmetrics_controller_read_pg_tls_cert=/path/to/metrics.cert
automationmetrics_controller_read_pg_tls_key=/path/to/metrics.key
automationmetrics_controller_read_pg_sslmode=verify-full
```
