# Operator enterprise topology
## Metrics service automatic provisioning

When you create an AnsibleAutomationPlatform custom resource with metrics service enabled, the operator automatically provisions:

**1. MetricsService custom resource**

- Defines the metrics service deployment (web, tasks, and scheduler pods)
- Configures database connection secrets
- Sets resource limits and replicas


**2. Database configuration**

- Reads customer-provided database secrets (external database scenario) or creates managed database credentials
- Creates Kubernetes Secrets for both database connections:
* `<instance>`-automationmetricsservice-postgres-configuration - metrics service database
* `<instance>`-automationmetricsservice-awx-postgres-configuration - automation controller read-only credentials
- Database connectivity is verified at pod start time by an init container in the web pod, which polls until `manage.py check --database default` succeeds. The AWX read-only connection is validated at application runtime, not during operator reconciliation.


**3. Service routing**

- Creates a Kubernetes Service (`<instance>`-automationmetricsservice-service) on port 8000, targeting the web pod on port 8080
- Registers the metrics service with the platform gateway (Envoy) at `/api/metrics/`, making the API accessible through the standard Ansible Automation Platform gateway URL


**4. Backup integration**

- Backup resources are not created automatically during provisioning. They are created on-demand when you trigger a backup by applying an AnsibleAutomationPlatformBackup custom resource. The operator then creates a MetricsServiceBackup CR, which provisions a PersistentVolumeClaim for backup staging and runs a `pg_dump` of the metrics database.


**Validation**

After operator reconciliation completes, verify metrics service provisioning:

```
# Check MetricsService CR status
oc get metricsservice -n <namespace>

# Verify all 3 pods are running
oc get pods -n <namespace> | grep automationmetricsservice
```
Expected output:

```
<aap-name>-automationmetricsservice-web-xxxxx         1/1  Running
<aap-name>-automationmetricsservice-tasks-xxxxx       1/1  Running
<aap-name>-automationmetricsservice-scheduler-xxxxx   1/1  Running
```

```
# Check web pod init container logs for database readiness
oc logs <aap-name>-automationmetricsservice-web-xxxxx -c wait-for-db -n <namespace>
# Should show: "Database is ready"

# Verify the service exists and is on the correct port
oc get svc -n <namespace> | grep automationmetricsservice
# Expected: <aap-name>-automationmetricsservice-service   ClusterIP   ...   8000/TCP
```

