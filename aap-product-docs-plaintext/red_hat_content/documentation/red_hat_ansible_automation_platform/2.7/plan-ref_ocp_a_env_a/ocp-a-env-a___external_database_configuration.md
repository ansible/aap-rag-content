# Operator growth topology
## External database configuration

When using an external database (not operator-managed), you must manually provision the metrics service databases before deployment.

**Create metrics_service database:**

```
CREATE DATABASE metrics_service
WITH ENCODING='UTF8'
LC_COLLATE='en_US.UTF-8'
LC_CTYPE='en_US.UTF-8'
TEMPLATE=template0;

CREATE USER metrics_service WITH PASSWORD '<secure_password>';
GRANT ALL PRIVILEGES ON DATABASE metrics_service TO metrics_service;
\c metrics_service
GRANT ALL ON SCHEMA public TO metrics_service;
```
**Create read-only user for controller database:**

```
CREATE USER ms_awx_readonly WITH PASSWORD '<readonly_password>';
\c awx  -- Connect to controller database
GRANT SELECT ON ALL TABLES IN SCHEMA public TO ms_awx_readonly;
ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT SELECT ON TABLES TO ms_awx_readonly;
```
**Configure external database in CR:**

```
spec:
metrics:
disabled: false
postgres_configuration_secret: <secret-name-with-db-credentials>
```

