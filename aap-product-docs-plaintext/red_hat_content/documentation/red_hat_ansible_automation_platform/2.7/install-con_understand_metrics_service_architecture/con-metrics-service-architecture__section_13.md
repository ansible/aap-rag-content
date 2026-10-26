# Understand metrics service architecture
## Operator-based deployment details

Metrics service is deployed through the `automation-metrics-operator` running on OpenShift. The AAP gateway operator manages the metrics operator lifecycle:

- **Container runtime:** Kubernetes pods managed by operator deployments
- **Service management:** Three Kubernetes deployments: `metrics-api`, `metrics-tasks`, `metrics-scheduler`
- **Data persistence:** Kubernetes persistent volumes managed by operator
- **Secrets management:** Kubernetes secrets automatically created and managed by operator (database credentials, OAuth tokens, Segment write key)
- **Network integration:** Kubernetes services and Envoy routing through platform gateway
- **Database provisioning:** Operator automatically creates and configures both `metrics_service` database and read-only controller database user

**Configuration simplicity:**

- Single CR field: `spec.metrics.disabled: false` in AnsibleAutomationPlatform CR
- Zero manual database configuration required
- Zero manual network configuration required
- Automatic OAuth integration with platform gateway
- Operator handles all credential rotation and secret management

**Operator-managed resources:**

- **MetricsService CR:** Created as `<aap-name>-metrics` in same namespace as AnsibleAutomationPlatform CR
- **Database:** PostgreSQL database for metrics service, automatically provisioned with credentials stored in Kubernetes secrets
- **Read-only user:** Automatically created in controller database with SELECT privileges
- **Services:** Kubernetes Service resources for metrics API, tasks, and scheduler pods
- **Routes/Ingress:** Traffic routing through platform gateway Envoy proxy (no direct external endpoints)

Important:

In AAP 2.7, the operator removes ownerReferences from the MetricsService CR. This means the CR is not automatically deleted when you set `metrics.disabled: true`. You must manually delete the CR if you want to fully remove metrics service from your cluster.

Note:

In standard operator deployments, database provisioning is fully automatic. The operator creates all required databases and users. This includes the metrics service database and the read-only user for the controller database.

**Externally managed databases:** If you use a fully externally managed database such as RDS or Cloud SQL, you must manually provision databases and configure credentials before deploying metrics service. See the related information for external database configuration procedures.

