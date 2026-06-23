# Container growth topology
## Metrics service database

The growth topology uses a managed PostgreSQL database that includes the metrics_service database alongside other AAP component databases.

**Databases created**

- `gateway` - Platform gateway data
- `awx` - Automation controller data
- `pulp` - Automation hub data
- `eda` - Event-Driven Ansible data
- `metrics_service` - Metrics service data storage (20 GB minimum)


**Database users**

- `metrics_service` - Full access to metrics_service database
- `ms_awx_readonly` - Read-only access to awx database for metrics collection


Note:

The installer automatically creates both databases and users. No manual database provisioning is required for growth topology.
