+++
template = "docs/aem-title.html"
title = "Configure external database for metrics service - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/plan-configure_external_database_metrics_service_operator"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/plan-assembly_overview_tested_deployment_models/", "Choose a deployment method and topology"]]
category = "Plan"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/plan-configure_external_database_metrics_service_operator/aem-page/plan-configure_external_database_metrics_service_operator.html"
last_crumb = "Configure external database for metrics service"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure external database for metrics service"
oversized = "false"
page_slug = "plan-configure_external_database_metrics_service_operator"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/plan-configure_external_database_metrics_service_operator"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/plan-configure_external_database_metrics_service_operator/toc/toc.json"
type = "aem-page"
+++

# Configure external database for metrics service

Configure metrics service to use external PostgreSQL databases for the metrics service database and read-only access to the automation controller database.

## Before you begin

Before you configure metrics service with an external database, ensure:

- External PostgreSQL database is running (version 15, 16, or 17)
- Two databases exist:
  * `metrics_service` database with a user that has CREATEDB role
  * `automationcontroller` database (same database used by automation controller)
- Read-only user `ms_awx_readonly` exists in PostgreSQL with SELECT privileges on all tables in the `automationcontroller` database's public schema


**Create the read-only user:**

```
-- Connect to the automationcontroller database
\c automationcontroller

-- Create read-only user
CREATE USER ms_awx_readonly WITH PASSWORD '<readonly-password>';

-- Grant privileges
GRANT CONNECT ON DATABASE automationcontroller TO ms_awx_readonly;
GRANT USAGE ON SCHEMA public TO ms_awx_readonly;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO ms_awx_readonly;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO ms_awx_readonly;

ALTER DEFAULT PRIVILEGES FOR ROLE automationcontroller IN SCHEMA public GRANT
SELECT ON TABLES TO ms_awx_readonly;
ALTER DEFAULT PRIVILEGES FOR ROLE automationcontroller IN SCHEMA public GRANT SELECT ON SEQUENCES TO ms_awx_readonly;
```

## About this task

Metrics service requires two database connections: a `metrics_service` database for storing metrics data and read-only access to the `automationcontroller` database for correlating metrics with automation activity.

## Procedure

1.  Create a secret for the `metrics_service` database connection:
  

```
apiVersion: v1
kind: Secret
metadata:
  name: aap-metrics-postgres-configuration
  namespace: aap
stringData:
  host: <external-postgres-host>
  port: "5432"
  database: metrics_service
  username: <metrics-db-username>
  password: <metrics-db-password>
  type: unmanaged
type: Opaque
```
  
  Important:
  `type: unmanaged` tells the operator this is an external database. Without this field, the operator attempts to initialize the database as a managed instance and fails.

2.  Create a secret for read-only access to the `automationcontroller` database:
  

```
apiVersion: v1
kind: Secret
metadata:
  name: aap-metrics-read-token
  namespace: aap
stringData:
  host: <external-postgres-host>
  port: "5432"
  database: automationcontroller
  username: ms_awx_readonly
  password: <readonly-user-password>
type: Opaque
```

3.  Apply both secrets to your OpenShift cluster:
  

```
$ oc apply -f aap-metrics-postgres-configuration.yaml -n aap
$ oc apply -f aap-metrics-read-token.yaml -n aap
```

4.  Verify the secrets were created:
  

```
$ oc get secret -n aap | grep metrics
```
      Expected output shows both secrets:

```
aap-metrics-postgres-configuration
aap-metrics-read-token
```

5.  Reference the secrets in your AnsibleAutomationPlatform custom resource:
  

```
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
  name: aap
  namespace: aap
spec:
  metrics:
    database:
      database_secret: aap-metrics-postgres-configuration
      externally_managed: true
    ms_awx_readonly_user_secret: aap-metrics-read-token
    ms_awx_readonly_user:
      externally_managed: true
```
      Where:

  - `database.database_secret`: References the `metrics_service` database secret
  - `database.externally_managed: true`: Skips operator-managed PostgreSQL pod creation
  - `ms_awx_readonly_user_secret`: References the read-only user secret
  - `ms_awx_readonly_user.externally_managed: true`: Uses customer-provided read-only user instead of operator creating it

## Results

After applying the AnsibleAutomationPlatform custom resource, verify metrics service provisioning:

1. Check the MetricsService custom resource status:

```
$ oc get metricsservice -n aap
```

2. Verify all 3 metrics service pods are running:

```
$ oc get pods -n aap | grep metrics
```
     Expected output:



```
aap-metrics-web-xxxxx        1/1  Running
aap-metrics-tasks-xxxxx      1/1  Running
aap-metrics-scheduler-xxxxx  1/1  Running
```

3. Check database connectivity in the logs:

```
$ oc logs <instance>-metrics-web-xxxxx -n aap | grep "Database connection"
```
     This should show a successful connection to both databases.
