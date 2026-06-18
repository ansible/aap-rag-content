+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-task_configure_external_database_containerized"
title = "Configure external PostgreSQL database for metrics service with containerized installer - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_understand_metrics_service_architecture/", "Understand metrics service architecture"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-task_configure_external_database_containerized/aem-page/install-task_configure_external_database_containerized.html"
last_crumb = "Configure external PostgreSQL database for metrics service with containerized installer"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure external PostgreSQL database for metrics service with containerized installer"
oversized = "false"
page_slug = "install-task_configure_external_database_containerized"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-task_configure_external_database_containerized"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-task_configure_external_database_containerized/toc/toc.json"
type = "aem-page"
+++

# Configure external PostgreSQL database for metrics service with containerized installer

Configure metrics service to use an external PostgreSQL database to leverage enterprise database management, backup, and high availability infrastructure.

## Before you begin

- External PostgreSQL 15 or later database server accessible from metrics service
- Database administrator credentials with CREATE DATABASE and CREATE USER privileges
- Network connectivity to database server (port 5432 default)
- Firewall rules configured to allow connections from metrics service hosts
- Ansible Automation Platform 2.7 containerized installer downloaded and extracted
- Inventory file access with permission to modify `[automationmetrics]` group and variables
- Root or sudo access to metrics service host

## About this task

This procedure configures metrics service to use an external PostgreSQL database instead of installer-managed databases when deploying with the Ansible Automation Platform 2.7 containerized installer. By using enterprise database infrastructure, you eliminate installer-managed PostgreSQL processes (saving approximately 2 GB memory and 2 vCPU per database instance), reduce database provisioning time by approximately 50% (5 minutes versus 10 minutes), and enable centralized database management with unified backup, restore, and high availability for all Ansible Automation Platform components.

## Procedure

1.  Create metrics_service database
      Create the `metrics_service` database with UTF-8 encoding to support internationalization and ensure compatibility with Django migrations.

```
psql -h <EXTERNAL_DB_HOST> -U postgres

    CREATE DATABASE metrics_service
  WITH ENCODING='UTF8'
       LC_COLLATE='en_US.UTF-8'
       LC_CTYPE='en_US.UTF-8'
       TEMPLATE=template0;
```
  Note:
      **Why UTF-8 encoding:** Django ORM requires UTF-8 encoding for proper handling of internationalized strings and special characters in metric data.

2.  Create database users
      Create two database users. The `metrics_service` user has full database privileges for schema management. The `ms_awx_readonly` user has SELECT-only privileges for secure data collection from automation controller.

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

    | User              | Database                    | Privileges                            | Purpose                                                    |
    | ----------------- | --------------------------- | ------------------------------------- | ---------------------------------------------------------- |
    | `metrics_service` | `metrics_service`           | ALL                                   | Django migrations, schema management, metrics data storage |
    | `ms_awx_readonly` | `awx` (controller database) | SELECT ON ALL TABLES IN SCHEMA public | Read-only metrics collection from controller               |
  Note:
      **Security note:** The `ms_awx_readonly` user has only SELECT privileges, preventing any writes to automation controller data. This ensures metrics service cannot modify controller operations.

3.  Configure pg_hba.conf
      Add authentication rules to allow metrics service host to connect to both databases using secure `scram-sha-256` authentication.

```
host    metrics_service    metrics_service    <METRICS_HOST_IP>/32    scram-sha-256
host    awx               ms_awx_readonly    <METRICS_HOST_IP>/32    scram-sha-256
```
    **Replace placeholders:**

  - `<METRICS_HOST_IP>`: IP address of the host running metrics service (from `[automationmetrics]` inventory group)
    **After editing pg_hba.conf:**

```
# Reload PostgreSQL configuration
sudo systemctl reload postgresql
```

4.  Configure installer inventory
      Edit the containerized installer inventory file to specify external database connection parameters:

```
[automationmetrics]
metrics.example.com

    [all:vars]
automationmetrics_pg_host=external-db.example.com
automationmetrics_pg_port=5432
automationmetrics_pg_database=metrics_service
automationmetrics_pg_username=metrics_service
automationmetrics_pg_password='<SECURE_PASSWORD>'

    # Read-only access to controller database
automationmetrics_controller_db=awx
automationmetrics_controller_pg_username=ms_awx_readonly
automationmetrics_controller_read_pg_password='<READONLY_PASSWORD>'
automationmetrics_controller_read_pg_host=controller-db.example.com
```

5.  Run the containerized installer
  

```
cd /path/to/aap-containerized-installer
ansible-playbook -i inventory install.yml
```
    The installer performs these actions:

  1. Skips PostgreSQL process creation for metrics service (uses external database)
  2. Creates Podman secrets for external database credentials
  3. Runs database migrations on external `metrics_service` database
  4. Deploys metrics service containers configured to connect to external databases

6.  Verify external database configuration
  

```
# Test database connectivity from metrics service host
podman exec automation-metrics-web \
  psql -h external-db.example.com -U metrics_service -d metrics_service -c "SELECT 1;"

    # Test read-only access to controller database
podman exec automation-metrics-tasks \
  psql -h controller-db.example.com -U ms_awx_readonly -d awx -c "SELECT COUNT(*) FROM main_job;"

    # Verify health endpoint
curl http://localhost:8087/health/
```

## Results

External database is successfully configured when:

- No installer-managed PostgreSQL processes run on metrics service host
- Metrics service can connect to external `metrics_service` database
- Metrics service can query controller database using `ms_awx_readonly` user
- Health endpoint returns `{"status": "good", ...}` response
