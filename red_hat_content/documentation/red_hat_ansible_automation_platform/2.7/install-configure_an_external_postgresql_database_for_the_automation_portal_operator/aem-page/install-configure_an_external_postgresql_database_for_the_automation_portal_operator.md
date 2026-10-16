+++
title = "Configure an external PostgreSQL database for the automation portal operator - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-configure_an_external_postgresql_database_for_the_automation_portal_operator"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-install_automation_portal_on_openshift_container_platform/", "Install automation portal on OpenShift Container Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-configure_an_external_postgresql_database_for_the_automation_portal_operator/aem-page/install-configure_an_external_postgresql_database_for_the_automation_portal_operator.html"
last_crumb = "Configure an external PostgreSQL database for the automation portal operator"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Configure an external PostgreSQL database for the automation portal operator"
oversized = "false"
page_slug = "install-configure_an_external_postgresql_database_for_the_automation_portal_operator"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-configure_an_external_postgresql_database_for_the_automation_portal_operator"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-configure_an_external_postgresql_database_for_the_automation_portal_operator/toc/toc.json"
type = "aem-page"
+++

# Configure an external PostgreSQL database for the automation portal operator

Configure the automation portal operator to use an external PostgreSQL database instead of the local database instance managed by the Red Hat Developer Hub Operator.

## Before you begin

- The automation portal operator installed and running on your OpenShift cluster.
- The `oc` CLI installed and authenticated to your OpenShift cluster.
- An external PostgreSQL database server accessible from your OpenShift cluster, with a database user that has the `CREATEDB` privilege. The operator creates application databases during deployment and cannot proceed without this privilege. For guidance on provisioning the PostgreSQL server and creating the database user, see [Configure an external PostgreSQL database for Ansible automation portal](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_self_service_configure_external_database#self-service-configure-external-database "By default, Ansible automation portal deploys an embedded PostgreSQL instance. For production deployments, configure Ansible automation portal to use an external PostgreSQL database managed by your organization's database team.").

## About this task

Important:

The automation portal operator is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production.

By default, the automation portal operator deploys a local PostgreSQL instance managed by the Red Hat Developer Hub Operator. You can replace this with an external PostgreSQL server by creating a credentials Secret and updating the `AutomationPortal` custom resource.

## Procedure

1. Create a Secret with your external database connection details.
  

```terminal
$ oc create secret generic portal-db-credentials \
  --namespace automation-portal \
  --from-literal=POSTGRES_HOST='<db-hostname>' \
  --from-literal=POSTGRES_PORT='5432' \
  --from-literal=POSTGRES_USER='<db-username>' \
  --from-literal=POSTGRES_PASSWORD='<db-password>'
```

      Replace the placeholder values with your external database details:

  - `POSTGRES_HOST` — hostname or IP address of the PostgreSQL server.
  - `POSTGRES_PORT` — port number, typically `5432`.
  - `POSTGRES_USER` — database user with the `CREATEDB` privilege.
  - `POSTGRES_PASSWORD` — password for the database user.

2. Update the `AutomationPortal` custom resource to disable the local database and reference the credentials Secret.
  

```yaml
spec:
  database:
    enableLocalDb: false
    authSecretName: portal-db-credentials
```

3. Apply the updated custom resource.
  

```terminal
$ oc apply -f portal.yaml -n automation-portal
```

      The operator stops the local PostgreSQL instance and reconnects to the external database. Monitor the deployment status:

```terminal
$ oc get automationportal portal -n automation-portal -w
```

    Wait for `Phase: Running`. If the phase stays `Pending`, check the status conditions for database connectivity errors. See [Troubleshoot your portal operator deployment](/documentation/en-us/red_hat_ansible_automation_platform/2.7/troubleshoot-troubleshoot_your_portal_operator_deployment#troubleshoot-portal-operator "Diagnose and resolve common issues when deploying or operating the automation portal operator on OpenShift, including status condition interpretation, log collection, and cleanup procedures.").

## Results

The automation portal operator creates and manages application databases on the external PostgreSQL server. The local PostgreSQL instance is no longer deployed.
