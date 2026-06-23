# Operator growth topology
## Metrics service automatic provisioning

The operator handles all metrics service deployment details automatically:

**Database provisioning**

The operator automatically creates:

- `metrics_service` database with full permissions for the `metrics_service` user
- `ms_awx_readonly` user in the automation controller database with SELECT-only permissions
- All database connection secrets as Kubernetes secrets


No manual database setup required for operator deployments with managed databases.

**Secrets management**

The operator creates and manages these Kubernetes secrets:

- `<aap-name>`- `automationmetrics-pg-password` - Metrics database credentials
- `<aap-name>`- `automationmetrics-controller-read-pg-password` - Read-only controller database credentials
- `<aap-name>`- `automationmetrics-secret-key` - Django secret key
- `<aap-name>`- `automationmetrics-resource-server` - Resource server configuration


**Gateway routing**

The operator configures Envoy routing through platform gateway:

- Dashboard requests route to `/api/metrics/` endpoint
- Internal communication between gateway and metrics service web pod
- No external exposure of metrics service (access only through gateway)


**ConfigMap**

Configuration is managed via ConfigMap:

- `<aap-name>`- `metrics-env-properties` - Contains all metrics service environment variables including feature flags

