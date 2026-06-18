+++
title = "Recover metrics service after reinstallation - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/troubleshoot-task_recover_after_reinstallation"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/troubleshoot-ref_troubleshoot_metrics_service/", "Troubleshoot metrics service"]]
category = "Troubleshoot"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/troubleshoot-task_recover_after_reinstallation/aem-page/troubleshoot-task_recover_after_reinstallation.html"
last_crumb = "Recover metrics service after reinstallation"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Recover metrics service after reinstallation"
oversized = "false"
page_slug = "troubleshoot-task_recover_after_reinstallation"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/troubleshoot-task_recover_after_reinstallation"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/troubleshoot-task_recover_after_reinstallation/toc/toc.json"
type = "aem-page"
+++

# Recover metrics service after reinstallation

Restore metrics service operation when pods do not start after reinstalling Ansible Automation Platform by recreating the missing database credential secret.

## Before you begin

- oc CLI access with sufficient RBAC permissions to create and patch secrets and CRs in the metrics service namespace
- The name of your `AnsibleAutomationPlatform` CR (`<aap-name>`)
- The name of your `MetricsService` CR (`<metrics-cr-name>`)
- Access to the automation controller PostgreSQL database host and database name

## About this task

This procedure restores metrics service operation when pods do not start after reinstalling or restoring Ansible Automation Platform because the `<aap-name>-metrics-read-token` Kubernetes secret was deleted during cleanup and not automatically recreated. Use this procedure when the metrics service operator logs contain the error "Gateway-managed AWX read user secret '-metrics-read-token' not found in namespace ''" and the health endpoint does not respond.

**What causes this issue**

During reinstallation, the `<aap-name>-metrics-read-token` Kubernetes secret is deleted as part of the cleanup. Under certain conditions the Ansible Automation Platform operator does not automatically recreate this secret on the next reconcile, leaving the metrics service operator unable to configure the read-only database connection to the automation controller.

Note:

A permanent fix for this issue is available in the next async update. After applying the update, the Ansible Automation Platform operator automatically recreates the read token secret when it is missing, and the metrics service operator recovers gracefully without manual intervention.

Choose one of the following options.

## Procedure

1.  Option 1: Manually recreate the missing secret
      Use this option to restore normal operation without changing your metrics service configuration.

  1. Confirm the secret is missing. The secret name follows the pattern `<aap-name>-metrics-read-token`:

```
oc get secret <aap-name>-metrics-read-token -n <namespace>
```
         If the command returns `Error from server (NotFound)`, proceed to the next step.

  2. Retrieve the automation controller database host from the existing postgres configuration secret:

```
oc get secret <aap-name>-controller-postgres-configuration \
  -n <namespace> \
  -o jsonpath='{.data.host}' | base64 -d
```

  3. Retrieve the automation controller database name:

```
oc get secret <aap-name>-controller-postgres-configuration \
  -n <namespace> \
  -o jsonpath='{.data.database}' | base64 -d
```

  4. Create the missing secret using the values from the previous steps:

```
oc create secret generic <aap-name>-metrics-read-token \
  --from-literal=username=ms_awx_readonly \
  --from-literal=password=<password> \
  --from-literal=database=<controller-database-name> \
  --from-literal=host=<controller-db-host> \
  --from-literal=port=5432 \
  -n <namespace>
```
         Replace `<password>` with a secure password for the `ms_awx_readonly` database user. If you are restoring the same database, use the original password to avoid a credential mismatch. If you are reinstalling with a fresh database, any secure password is acceptable.

  5. Trigger a reconcile by annotating the `AnsibleAutomationPlatform` CR:

```
oc annotate ansibleautomationplatform <aap-name> \
  ansible.com/force-reconcile="$(date +%s)" \
  --overwrite -n <namespace>
```

  6. Verify that metrics service pods start successfully:

```
oc get pods -n <namespace> | grep metrics
```

2.  Option 2: Configure metrics service to manage its own read-only credentials
      Use this option if you cannot recreate the secret manually, or if you want to prevent the issue from recurring on future reinstallations. This directs the metrics service operator to create and manage the `ms_awx_readonly` database user independently.

  1. Patch the `MetricsService` CR to use operator-managed credentials:

```
oc patch metricsservice <metrics-cr-name> \
  --type merge \
  -p '{"spec":{"ms_awx_readonly_user":{"externally_managed":false}}}' \
  -n <namespace>
```

  2. Remove the `database.ms_awx_readonly_user_secret` reference so the operator does not attempt to locate the missing gateway-managed secret:

```
oc patch metricsservice <metrics-cr-name> \
  --type json \
  -p '[{"op":"remove","path":"/spec/database/ms_awx_readonly_user_secret"}]' \
  -n <namespace>
```

  3. Verify that the operator reconciles successfully and pods start:

```
oc get pods -n <namespace> | grep metrics
```

## Results

Metrics service has recovered successfully when:

- All metrics service pods show `Running` status:

```
oc get pods -n <namespace> | grep metrics
```

- The health endpoint returns a successful response:

```
oc exec deployment/<metrics-cr-name>-web -n <namespace> -- \
  curl -s http://localhost:8080/health/
```

- No secret-related errors appear in the metrics service operator logs:

```
oc logs -l name=automation-metrics-operator -n <namespace> --tail=50
```
