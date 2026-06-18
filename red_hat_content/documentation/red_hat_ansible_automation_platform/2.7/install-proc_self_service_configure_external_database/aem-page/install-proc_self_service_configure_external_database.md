+++
title = "Configure an external PostgreSQL database for Ansible automation portal - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_self_service_configure_external_database"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_self_service_about/", "Install Ansible automation portal (OpenShift Container Platform only)"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_self_service_configure_external_database/aem-page/install-proc_self_service_configure_external_database.html"
last_crumb = "Configure an external PostgreSQL database for Ansible automation portal"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure an external PostgreSQL database for Ansible automation portal"
oversized = "false"
page_slug = "install-proc_self_service_configure_external_database"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-proc_self_service_configure_external_database"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_self_service_configure_external_database/toc/toc.json"
type = "aem-page"
+++

# Configure an external PostgreSQL database for Ansible automation portal

By default, Ansible automation portal deploys an embedded PostgreSQL instance. For production deployments, configure Ansible automation portal to use an external PostgreSQL database managed by your organization's database team.

## Before you begin

- You have administrator access to your OpenShift Container Platform cluster.
- You have access to an external PostgreSQL database server.
- You have a PostgreSQL user with the `CREATEDB` privilege, or you are using the `postgres` superuser. Ansible automation portal requires `CREATEDB` because it creates multiple databases at runtime. Consult your database administrator to provision this user if needed.
- Network connectivity is available between your OpenShift Container Platform cluster and the external PostgreSQL server. Verify that firewalls and security groups allow traffic on the PostgreSQL port (default 5432).
- Ansible automation portal is installed or you are preparing to install it.

## About this task

Ansible automation portal creates multiple databases automatically at runtime. You do not need to pre-create databases. The database user must have the `CREATEDB` privilege so that the application can create and manage its own databases.

## Procedure

1.  Create a secret in OpenShift Container Platform with your database credentials.
  

```terminal
$ oc create secret generic portal-postgresql-external \
  --from-literal=POSTGRES_USER=*database-user* \
  --from-literal=POSTGRES_PASSWORD='*database-password*' \
  --from-literal=POSTGRES_HOST=*database-host* \
  --from-literal=POSTGRES_PORT=5432 \
  -n *namespace*
```
    Replace *database-user* with your PostgreSQL user name, *database-host* with your PostgreSQL server hostname or IP address, and *namespace* with the namespace where Ansible automation portal is installed.

    **Using the OpenShift Container Platform web console:**

  1. Navigate to **Workloads** > **Secrets** in the namespace where Ansible automation portal is installed.
  2. Click **Create** > **Key/value secret**.
  3. Set the **Secret name** to `portal-postgresql-external`.
  4. Add the following key/value pairs:
      | Key                 | Value                                         |
      | ------------------- | --------------------------------------------- |
      | `POSTGRES_USER`     | Your database user name                       |
      | `POSTGRES_PASSWORD` | Your database password                        |
      | `POSTGRES_HOST`     | Your PostgreSQL server hostname or IP address |
      | `POSTGRES_PORT`     | `5432`                                        |

  5. Click **Create**.

2.  Update your Ansible automation portal Helm chart values to use the external database.
      Add or modify the following configuration in your values.yaml file:

```yaml
redhat-developer-hub:
  upstream:
    postgresql:
      enabled: false
      auth:
        existingSecret: portal-postgresql-external
        secretKeys:
          adminPasswordKey: POSTGRES_PASSWORD
    backstage:
      appConfig:
        backend:
          database:
            connection:
              host: ${POSTGRES_HOST}
              port: ${POSTGRES_PORT}
              user: ${POSTGRES_USER}
              password: ${POSTGRES_PASSWORD}
      extraEnvVarsSecrets:
        - portal-postgresql-external
```
  - `postgresql.enabled: false` disables the embedded PostgreSQL instance.
  - `postgresql.auth.existingSecret` points the Helm chart's internal secret references to your external credential secret. This ensures the `POSTGRESQL_ADMIN_PASSWORD` environment variable, which the chart injects unconditionally, resolves to a valid secret.
  - `postgresql.auth.secretKeys.adminPasswordKey` tells the chart which key in your secret contains the database password, so you need only one password key in your secret.
  - `appConfig.backend.database.connection` overrides the default database connection to use your external PostgreSQL server.
  - `extraEnvVarsSecrets` injects the secret keys as environment variables into the Ansible automation portal container, which the `appConfig` block references using `${}` syntax.

3. **Optional:** Configure TLS for the database connection.
      If your external PostgreSQL server requires TLS, create a certificate secret containing the CA certificate and optionally the client certificate and private key.

```terminal
$ cat <<EOF | oc -n *namespace* create -f -
apiVersion: v1
kind: Secret
metadata:
  name: portal-postgresql-certs
type: Opaque
stringData:
  postgres-ca.pem: |-
    -----BEGIN CERTIFICATE-----
    *ca-certificate-content*
    -----END CERTIFICATE-----
EOF
```
    If your PostgreSQL server uses client certificate authentication (mTLS), add `postgres-key.key` and `postgres-crt.pem` entries to the secret. For server-only TLS verification, only `postgres-ca.pem` is required.

    Add `PGSSLMODE` and `NODE_EXTRA_CA_CERTS` to your credential secret:

```terminal
$ oc -n *namespace* patch secret portal-postgresql-external --type merge -p \
  '{"stringData":{"PGSSLMODE":"verify-full","NODE_EXTRA_CA_CERTS":"/opt/app-root/src/postgres-ca.pem"}}'
```
    Then add the TLS configuration and volume mount to your Helm chart values. Merge these settings with the configuration from the previous step:

```yaml
redhat-developer-hub:
  upstream:
    backstage:
      appConfig:
        backend:
          database:
            connection:
              host: ${POSTGRES_HOST}
              port: ${POSTGRES_PORT}
              user: ${POSTGRES_USER}
              password: ${POSTGRES_PASSWORD}
              ssl:
                rejectUnauthorized: true
                ca:
                  $file: /opt/app-root/src/postgres-ca.pem
      extraEnvVarsSecrets:
        - portal-postgresql-external
      extraVolumes:
        - name: postgres-ca
          secret:
            secretName: portal-postgresql-certs
            items:
              - key: postgres-ca.pem
                path: postgres-ca.pem
      extraVolumeMounts:
        - name: postgres-ca
          mountPath: /opt/app-root/src/postgres-ca.pem
          subPath: postgres-ca.pem
```
    If your PostgreSQL server requires client certificate authentication (mTLS), add the following to the `ssl` block and mount the additional certificate files:

```yaml
ssl:
  rejectUnauthorized: true
  ca:
    $file: /opt/app-root/src/postgres-ca.pem
  key:
    $file: /opt/app-root/src/postgres-key.key
  cert:
    $file: /opt/app-root/src/postgres-crt.pem
```
    Add the corresponding volumes and mounts for the client key and certificate alongside the `postgres-ca` entries.

4.  Apply the configuration by upgrading your Ansible automation portal Helm release.
  

```terminal
$ helm upgrade *release-name* *chart-name* \
  -f values.yaml \
  -n *namespace*
```
    Replace *release-name* with your Helm release name and *chart-name* with the Ansible automation portal chart reference.

    **Using the OpenShift Container Platform web console:**

  1. Navigate to **Operators** > **Installed Operators** and select the Ansible automation portal operator in your namespace.
  2. Click the **Helm Releases** tab, then click your Ansible automation portal release.
  3. Click **Actions** > **Upgrade**.
  4. Switch to the **YAML view** and merge the external database configuration into the existing values.
  5. Click **Upgrade** to apply the changes.

5.  Wait for Ansible automation portal pods to restart and initialize the database schema.
  

```terminal
$ oc get pods -n *namespace* -w
```
    In the OpenShift Container Platform web console, navigate to **Workloads** > **Pods** in your namespace. Wait until all Ansible automation portal pods show a status of **Running**.

## Results

1. Verify that the Ansible automation portal pods are running:

```terminal
$ oc get pods -n *namespace*
```
     All Ansible automation portal pods should show a status of `Running`.

2. Check the Ansible automation portal logs to confirm the database connection:

```terminal
$ oc logs -n *namespace* deploy/*release-name*-rhaap-portal | grep -i "database\|postgres"
```
     You should see log entries indicating a successful database connection without errors.

3. Connect to your external PostgreSQL database and verify that Ansible automation portal created the required databases. You should see multiple databases created by Ansible automation portal, one per plugin.

4. Access the Ansible automation portal web interface and verify that the application loads correctly.
