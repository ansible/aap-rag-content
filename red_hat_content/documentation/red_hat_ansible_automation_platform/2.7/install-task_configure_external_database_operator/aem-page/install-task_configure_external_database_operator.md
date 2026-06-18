+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-task_configure_external_database_operator"
title = "Configure external PostgreSQL database for metrics service with OpenShift operator - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_understand_metrics_service_architecture/", "Understand metrics service architecture"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-task_configure_external_database_operator/aem-page/install-task_configure_external_database_operator.html"
last_crumb = "Configure external PostgreSQL database for metrics service with OpenShift operator"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure external PostgreSQL database for metrics service with OpenShift operator"
oversized = "false"
page_slug = "install-task_configure_external_database_operator"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-task_configure_external_database_operator"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-task_configure_external_database_operator/toc/toc.json"
type = "aem-page"
+++

# Configure external PostgreSQL database for metrics service with OpenShift operator

Configure metrics service to use external PostgreSQL databases instead of operator-provisioned databases to leverage enterprise infrastructure.

## Before you begin

- External PostgreSQL 15 or later database server accessible from metrics service
- Database administrator credentials with CREATE DATABASE and CREATE USER privileges
- Network connectivity to database server (port 5432 default)
- Firewall rules configured to allow connections from metrics service pods
- Ansible Automation Platform operator installed on OpenShift Container Platform
- oc CLI access with cluster-admin or sufficient role-based access control (RBAC) permissions
- Kubernetes secret creation permissions in target namespace
- Understanding of OpenShift networking (pod network CIDR, network policies)

## About this task

This procedure configures metrics service to use an external PostgreSQL database instead of operator-provisioned databases when deploying with the Ansible Automation Platform operator on OpenShift Container Platform. By using enterprise database infrastructure, you eliminate operator-managed PostgreSQL pods (saving approximately 2 GB memory and 2 vCPU per database instance), reduce database provisioning time by approximately 50% (5 minutes versus 10 minutes), enable centralized database management with unified backup, restore, and high availability for all Ansible Automation Platform components, and prevent pod scheduling failures caused by the operator attempting to provision databases when external databases are configured.

Important:

The operator supports externally managed databases for both the metrics service database (`metrics_service`) and the read-only connection to the automation controller database (`ms_awx_readonly_user`). Without proper configuration, the operator attempts to provision PostgreSQL pods using KubeVirt (Kubernetes virtualization), causing scheduling failures.

## Procedure

1.  Create external databases and users
      On the external PostgreSQL server, create the `metrics_service` database and required users:

    **Create the metrics_service database:**

```
psql -h <EXTERNAL_DB_HOST> -U postgres

    CREATE DATABASE metrics_service
  WITH ENCODING='UTF8'
       LC_COLLATE='en_US.UTF-8'
       LC_CTYPE='en_US.UTF-8'
       TEMPLATE=template0;
```
    **Create database users:**

```
-- metrics service user (ALL privileges)
CREATE USER metrics_service WITH PASSWORD '<SECURE_PASSWORD>';
GRANT ALL PRIVILEGES ON DATABASE metrics_service TO metrics_service;
\c metrics_service
GRANT ALL ON SCHEMA public TO metrics_service;

    -- Read-only user for controller database
\c postgres
CREATE USER ms_awx_readonly WITH PASSWORD '<READONLY_PASSWORD>';
\c awx
GRANT SELECT ON ALL TABLES IN SCHEMA public TO ms_awx_readonly;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO ms_awx_readonly;
```
  Important:
      Change `awx` to match your actual database name for automation controller. Common alternative names: `automationcontroller`, `tower`, `awx_production`.

    **Network access requirement:** Ensure OpenShift pods can reach the external PostgreSQL server. Verify network policies, firewall rules, and routes allow connectivity from the metrics service namespace to the database host on port 5432.

    **Example pg_hba.conf for OpenShift:**

```
# Allow connections from OpenShift pod network CIDR
host    metrics_service    metrics_service    10.128.0.0/14    scram-sha-256
host    awx               ms_awx_readonly    10.128.0.0/14    scram-sha-256
```
  Note:
      Replace `10.128.0.0/14` with your OpenShift cluster's pod network CIDR. Find it with: `oc get network.config cluster -o jsonpath='{.status.clusterNetwork[0].cidr}'`

    **After configuring pg_hba.conf:**

```
# Reload PostgreSQL configuration
sudo systemctl reload postgresql

    # Or for containerized PostgreSQL:
podman exec postgres-container pg_ctl reload
```

2.  Create Kubernetes secrets for database credentials
      Create two secrets in the same namespace where you deploy the `metricsService` CR. These secrets store database connection parameters that the operator uses to configure metrics service.

    **Secret 1: Metrics service database credentials**

```
apiVersion: v1
kind: Secret
metadata:
  name: automation-platform-metrics-postgres-configuration
  namespace: <your-namespace>
type: Opaque
stringData:
  host: external-db.example.com
  port: "5432"
  database: metrics_service
  username: metrics_service
  password: <SECURE_PASSWORD>
  sslmode: prefer
  type: unmanaged
```
    **Secret 2: Automation controller database read-only credentials**

```
apiVersion: v1
kind: Secret
metadata:
  name: automation-controller-read-postgres-configuration
  namespace: <your-namespace>
type: Opaque
stringData:
  host: controller-db.example.com
  port: "5432"
  database: awx
  username: ms_awx_readonly
  password: <READONLY_PASSWORD>
  sslmode: prefer
  type: unmanaged
```
    **Apply the secrets:**

```
oc create -f automation-platform-metrics-postgres-configuration.yaml
oc create -f automation-controller-read-postgres-configuration.yaml

    # Verify secrets created
oc get secret -n <your-namespace> | grep postgres-configuration
```
    **Secret field reference:**

    | Field      | Required | Description                                                                         |
    | ---------- | -------- | ----------------------------------------------------------------------------------- |
    | `host`     | Yes      | Database server hostname or IP address                                              |
    | `port`     | Yes      | Database port (5432 default)                                                        |
    | `database` | Yes      | Database name                                                                       |
    | `username` | Yes      | Database user                                                                       |
    | `password` | Yes      | Database password                                                                   |
    | `sslmode`  | No       | SSL mode: disable, allow, prefer, require, verify-ca, verify-full (default: prefer) |
    | `type`     | Yes      | Must be`managed` for operator-managed configuration                                 |
  Note:
      Replace `<your-namespace>` with the namespace where you deploy metrics service (for example, `aap-27-metrics`).

3.  Create metricsService custom resource with external database configuration
      Create a `metricsService` CR that references the external database secrets. This configuration directs the operator to use external databases instead of provisioning PostgreSQL pods.

```
apiVersion: automationmetricsservice.ansible.com/v1alpha1
kind: MetricsService
metadata:
  name: metrics-service
  namespace: <your-namespace>
spec:
  database:
    database_secret: automation-platform-metrics-postgres-configuration
    externally_managed: true
    ms_awx_readonly_user_secret: automation-controller-read-postgres-configuration
  ms_awx_readonly_user:
    externally_managed: true
  image_pull_secrets:
    - redhat-operators-pull-secret
  ingress_type: None
```
    **Key configuration fields:**

    | Field                                             | Value                                                | Description                                                          |
    | ------------------------------------------------- | ---------------------------------------------------- | -------------------------------------------------------------------- |
    | `metrics.database.database_secret`                | `automation-platform-metrics-postgres-configuration` | Name of secret containing metrics service database credentials       |
    | `metrics.database.externally_managed`             | `true`                                               | Tells operator NOT to provision a PostgreSQL pod for metrics service |
    | `metrics.ms_awx_readonly_user.externally_managed` | `true`                                               | Tells operator NOT to create`ms_awx_readonly` user automatically     |
    | `metrics.ms_awx_readonly_user_secret`             | `automation-controller-read-postgres-configuration`  | Name of secret containing read-only controller database credentials  |
  Important:
      Both `metrics.database.externally_managed: true` AND `metrics.ms_awx_readonly_user.externally_managed: true` must be set. If only one is set, the operator attempts to provision database resources, causing pod scheduling failures with errors like `Insufficient devices.kubevirt.io/kvm` or `Insufficient memory`.

    **Why both fields are required:**

  - `metrics.database.externally_managed: true` — Prevents operator from creating PostgreSQL pod for metrics service database
  - `metrics.ms_awx_readonly_user.externally_managed: true` — Prevents operator from attempting to create `ms_awx_readonly` user (assumes you created it manually)
  - Missing either field triggers operator's default behavior: provision database using KubeVirt virtual machines (VMs)
    **Apply the CR:**

```
oc create -f metricsservice-external-db.yaml

    # Monitor CR status
oc get metricsservice metrics-service -n <your-namespace> -w
```

4.  Verify deployment
  

```
# Check metricsService CR status
oc get metricsservice metrics-service -n <your-namespace>

    # Expected output shows Ready condition
NAME              AGE
metrics-service   5m

    # Check pod status (should show metrics pods, NO postgres pods)
oc get pods -n <your-namespace>

    # Expected output:
# metrics-service-web-xxx     1/1  Running
# metrics-service-tasks-xxx   1/1  Running
# metrics-service-scheduler-xxx   1/1  Running
# NO virt-launcher-postgres-* pods should exist

    # Verify NO virt-launcher pods (confirms external DB config worked)
oc get pods -n <your-namespace> | grep virt-launcher && echo "ERROR: Database pods found" || echo "SUCCESS: No database pods"

    # Check pod logs for database connectivity
oc logs deployment/metrics-service-web -n <your-namespace> | tail -20

    # Verify database connectivity from pod
oc exec deployment/metrics-service-web -n <your-namespace> -- \
  psql -h external-db.example.com -U metrics_service -d metrics_service -c "SELECT 1;"
# Expected output:
#  ?column?
# ----------
#         1

    # Verify read-only access to controller database
oc exec deployment/metrics-service-tasks -n <your-namespace> -- \
  psql -h controller-db.example.com -U ms_awx_readonly -d awx -c "SELECT COUNT(*) FROM main_job LIMIT 1;"
# Expected output: count (non-zero if jobs exist)

    # Check for scheduling errors (should return no events)
oc get events -n <your-namespace> | grep FailedScheduling
```

## Results

External database is successfully configured when:

- `metricsService` CR shows `Ready` status in `oc get metricsservice` output
- metrics service pods are running (check with `oc get pods`)
- **No operator-provisioned PostgreSQL pods exist** (no `virt-launcher-postgres-*` pods)
- Pods can connect to external `metrics_service` database
- Pods can query automation controller database by using the `ms_awx_readonly` user
- No `FailedScheduling` events related to database pods or kubevirt devices
- Health endpoint returns 200 status: `oc exec deployment/metrics-service-web -- curl -s http://localhost:8087/health/`


**Common verification failures:**

| Symptom                                               | Likely Cause                                                                                                         |
| ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `virt-launcher-postgres-*` pods appear                | `externally_managed: true` not set correctly for one or both database configurations                                 |
| FailedScheduling: Insufficient devices.kubevirt.io/\* | Operator attempting to provision VM-based PostgreSQL despite external config (check BOTH`externally_managed` fields) |
| FailedScheduling: Insufficient memory or CPU          | Operator attempting to provision PostgreSQL pod despite external config                                              |
| Pod CrashLoopBackOff                                  | Database connection failure (check secrets, network connectivity, firewall rules)                                    |

## Troubleshooting

**Pod fails to schedule with insufficient resources**

**Symptom:** Pod scheduling fails with errors like `Insufficient memory`, `Insufficient cpu`, or `Insufficient devices.kubevirt.io/kvm`, `devices.kubevirt.io/tun`, or `devices.kubevirt.io/vhost-net`.

**Cause:** The operator is attempting to provision a PostgreSQL VM or pod despite the `externally_managed: true` configuration. This typically occurs when one or both of the required `externally_managed` fields are missing or incorrect.

**Solution:**

1. Verify `metrics.database.externally_managed: true` is set in the metricsService CR:

```
oc get metricsservice metrics-service -o yaml | grep externally_managed
```

2. Verify `metrics.ms_awx_readonly_user.externally_managed: true` is also set. BOTH fields are required:

```
oc get metricsservice metrics-service -o yaml | grep -A 2 ms_awx_readonly_user
```

3. Check that database secret names match exactly in the CR:

```
oc get metricsservice metrics-service -o yaml | grep -E 'database_secret|ms_awx_readonly_user_secret'
```

4. Verify both secrets exist in the same namespace as the CR:

```
oc get secret -n <namespace> | grep postgres-configuration
```

5. If you corrected the configuration, delete and recreate the metricsService CR:

```
oc delete metricsservice metrics-service
oc create -f metricsservice-external-db.yaml
```

**Database connection errors in pod logs**

**Symptom:** Pod logs show connection errors such as "connection refused", "timeout", or "could not connect to server".

**Cause:** Network connectivity issues between OpenShift pods and the external database server, or incorrect database credentials in the secret.

**Solution:**

1. Verify network policies allow pod-to-database connectivity:

```
oc get networkpolicy -n <namespace>
```

2. Test database connectivity from a debug pod:

```
oc run -it --rm debug --image=registry.redhat.io/rhel9/postgresql-15 -- \
  psql -h external-db.example.com -U metrics_service -d metrics_service
```

3. Verify secret values are correct (note: password is base64 encoded):

```
oc get secret automation-platform-metrics-postgres-configuration -o yaml | \
  grep -E 'host|port|database|username'
```

4. Check that firewall rules on the database host allow connections from the OpenShift pod network CIDR.
5. Verify the database server is listening on the correct network interface:

```
# Run on database server
ss -tulpn | grep 5432
```

**Permission denied errors for ms_awx_readonly user**

**Symptom:** Pod logs show "permission denied for table main_job" or similar permission errors when querying the automation controller database.

**Cause:** The `ms_awx_readonly` user lacks SELECT privileges on the automation controller database tables.

**Solution:**

1. Connect to the automation controller database:

```
psql -h controller-db.example.com -U postgres -d awx
```

2. Grant SELECT privileges on all existing tables:

```
GRANT SELECT ON ALL TABLES IN SCHEMA public TO ms_awx_readonly;
```

3. Set default privileges for future tables:

```
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO ms_awx_readonly;
```

4. Verify privileges were granted:

```
SELECT grantee, privilege_type
FROM information_schema.role_table_grants
WHERE grantee='ms_awx_readonly';
```

**Database security best practices**

- **Use strong, unique passwords** for `metrics_service` and `ms_awx_readonly` users (minimum 16 characters, alphanumeric and special characters)
- **Enable TLS/SSL** for database connections
- **Restrict database network access** to only metrics service pods
- **Use Kubernetes secrets** for credential storage (never hard-code credentials in CR specs or ConfigMaps)
- **Apply RBAC** to restrict secret access to necessary service accounts only
- **Regularly rotate database credentials** (update secrets quarterly or per security policy)
