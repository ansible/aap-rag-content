# Container enterprise topology
## Metrics service database architecture

The enterprise topology uses an externally managed PostgreSQL database service. Metrics service requires provisioning of two database configurations:

**Database 1: `metrics_service` (read/write)**

Purpose: Store metrics data, dashboard calculations, anonymized payloads

Database configuration:

```
CREATE DATABASE metrics_service
WITH ENCODING='UTF8'
LC_COLLATE='en_US.UTF-8'
LC_CTYPE='en_US.UTF-8'
TEMPLATE=template0;

CREATE USER metrics_service WITH PASSWORD '<secure_password>';
GRANT ALL PRIVILEGES ON DATABASE metrics_service TO metrics_service;
```
Storage requirements:

- Minimum: 20 GB
- Recommended: 40 GB
- High-volume (>20,000 jobs/day): 60-80 GB


**Database 2: awx (read-only access)**

Purpose: Collect automation job data for metrics calculation

User configuration:

```
CREATE USER ms_awx_readonly WITH PASSWORD '<readonly_password>';
\c awx  -- Connect to automation controller database
GRANT SELECT ON ALL TABLES IN SCHEMA public TO ms_awx_readonly;
ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT SELECT ON TABLES TO ms_awx_readonly;
```
Security model:

- `ms_awx_readonly` user has SELECT-only privileges
- Prevents metrics service from modifying automation controller operations
- Read-only access ensures separation of concerns


**External database storage allocation**

Update your external PostgreSQL database storage to accommodate metrics service:

*Table 5. External database storage allocation*

| Database          | Purpose               | Storage allocation |
| ----------------- | --------------------- | ------------------ |
| `gateway`         | Platform gateway      | 20 GB              |
| `awx`             | Automation controller | 80 GB              |
| `metrics_service` | Metrics service       | 40 GB              |
| `pulp`            | Automation hub        | 60 GB              |
| `eda`             | Event-Driven Ansible  | 20 GB              |
| Total             | All components        | 220 GB             |


Note:

Database storage consumption varies based on job frequency, playbook complexity, and retention policies. Monitor actual usage after deployment and adjust accordingly.
