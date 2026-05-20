# Chapter 9. Configuring an external PostgreSQL database for self-service automation portal

By default, self-service automation portal uses an embedded PostgreSQL database. For production deployments, you can configure self-service automation portal to use an external PostgreSQL database managed by your organization’s database team.

**Prerequisites**

- You have administrator access to your OpenShift Container Platform cluster.
- You have access to an external PostgreSQL database server (version 13 or later).
- You have database administrator privileges to create databases and users.
- self-service automation portal is installed or you are preparing to install it.

**Procedure**

1. Create a database and user on your external PostgreSQL server.

Connect to your PostgreSQL server as a database administrator and run the following commands:

CREATE DATABASE rhdh_production;
CREATE USER rhdh_user WITH ENCRYPTED PASSWORD 'your_secure_password';
GRANT ALL PRIVILEGES ON DATABASE rhdh_production TO rhdh_user;
ALTER DATABASE rhdh_production OWNER TO rhdh_user;

Replace `your_secure_password` with a strong password.

2. Verify that you can connect to the database from your OpenShift Container Platform cluster.

Test the connection using a temporary pod:

oc run -it --rm postgres-test --image=postgres:13 --restart=Never -- \
psql -h <database-host> -U rhdh_user -d rhdh_production

Replace `<database-host>` with your PostgreSQL server hostname or IP address.

If the connection succeeds, you can proceed. If it fails, verify network connectivity and firewall rules.

3. Create a secret in OpenShift Container Platform with your database credentials.

oc create secret generic rhdh-postgresql-secrets \
--from-literal=POSTGRES_USER=rhdh_user \
--from-literal=POSTGRES_PASSWORD=your_secure_password \
--from-literal=POSTGRES_HOST=<database-host> \
--from-literal=POSTGRES_PORT=5432 \
--from-literal=POSTGRES_DB=rhdh_production \
-n <namespace>

Replace `<namespace>` with the namespace where self-service automation portal is installed.

4. Update your self-service automation portal Helm chart values to use the external database.

Add or modify the following configuration in your `values.yaml` file:

upstream:
postgresql:
enabled: false  # Disable embedded PostgreSQL

backstage:
appConfig:
backend:
database:
client: pg
connection:
host: ${POSTGRES_HOST}
port: ${POSTGRES_PORT}
user: ${POSTGRES_USER}
password: ${POSTGRES_PASSWORD}
database: ${POSTGRES_DB}
ssl:
rejectUnauthorized: false  # Set to true if using verified SSL certificates

extraEnvVarsSecrets:
- rhdh-postgresql-secrets

5. Apply the configuration by upgrading your self-service automation portal Helm release.

helm upgrade <release-name> <chart-name> \
-f values.yaml \
-n <namespace>

Replace `<release-name>` with your Helm release name and `<chart-name>` with the self-service automation portal chart name.

6. Wait for self-service automation portal pods to restart and initialize the database schema.

Monitor the pod status:

oc get pods -n <namespace> -w

**Verification**

1. Verify that the self-service automation portal pods are running:

oc get pods -n <namespace>

All self-service automation portal pods should show a status of `Running`.

2. Check the self-service automation portal logs to confirm the database connection:

oc logs -n <namespace> <backstage-pod-name> | grep -i "database\|postgres"

You should see log entries indicating a successful database connection without errors.

3. Connect to your external PostgreSQL database and verify that self-service automation portal created the required schema:

\c rhdh_production
\dt

You should see multiple tables created by self-service automation portal.

4. Access the self-service automation portal web interface and verify that your data persists across pod restarts.

**Additional resources**

- [PostgreSQL SSL/TLS Support](https://www.postgresql.org/docs/current/ssl-tcp.html)

