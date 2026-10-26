# Understand metrics service architecture
## Architecture components

*Figure 1. Metrics service overall system architecture*
![Overall system architecture diagram for metrics service](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/metrics-service-system-architecture.png)

**Core components**

| Component                                          | Container Name                 | Purpose                                                                                                                                                                                                  |
| -------------------------------------------------- | ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Metrics service (web)**                          | `automation-metrics-web`       | Nginx reverse proxy + Gunicorn serving the Django application. Internal Gunicorn port: 8006. External via nginx: 8087 (HTTP) / 8450 (HTTPS). Health endpoint:/health/ (returns HTTP 2\*\* for healthy, 50\* for unhealthy) |
| **Metrics service (tasks)**                        | `automation-metrics-tasks`     | Dispatcherd async task worker for background job execution                                                                                                                                               |
| **Metrics service (scheduler)**                    | `automation-metrics-scheduler` | APScheduler process that triggers periodic data collection tasks                                                                                                                                         |
| **Init container**                                 | `automation-metrics-init`      | One-shot container that runs Django database migrations and system initialization via/app/scripts/init.sh. Exits on completion.                                                                          |
| **metrics\_service database**                      | PostgreSQL database            | Stores processed metrics data and configuration. Created with user`metrics_service` (ALL privileges)                                                                                                     |
| **awx/automation controller database (read-only)** | PostgreSQL database            | Source of automation controller usage data. Accessed via user`ms_awx_readonly` (SELECT-only privileges on all tables in schema)                                                                          |
| **Red Hat Data Ingress**                           | External endpoint              | Receives anonymized data from customer environments via Segment write key. Data flows through Gateway/api/metrics/ endpoint (no direct customer-facing endpoints in 2.7 GA)                              |

**Database architecture**

| Database                      | User              | Privileges                            | Purpose                                                            |
| ----------------------------- | ----------------- | ------------------------------------- | ------------------------------------------------------------------ |
| `metrics_service`             | `metrics_service` | ALL                                   | Metrics service own data storage, schema migrations, configuration |
| **awx/automation controller** | `ms_awx_readonly` | SELECT ON ALL TABLES IN SCHEMA public | Read-only access to controller data for metrics collection         |

Note:

The two-database model ensures metrics service cannot modify controller data. The `ms_awx_readonly` user has only SELECT privileges on the **awx/automation controller** database, preventing any writes to automation controller tables.

Note:

The `metrics_service` database includes additional tables from apps/dashboard_reports/migrations/ for dashboard-specific data. These tables are created automatically during database migration.

