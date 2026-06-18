+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/task_enable_metrics_service_operator"
title = "Enable metrics service in operator deployments - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/task_enable_metrics_service_operator/aem-page/task_enable_metrics_service_operator.html"
last_crumb = "Enable metrics service in operator deployments"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Enable metrics service in operator deployments"
oversized = "false"
page_slug = "task_enable_metrics_service_operator"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/task_enable_metrics_service_operator"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/task_enable_metrics_service_operator/toc/toc.json"
type = "aem-page"
+++

# Enable metrics service in operator deployments

Enable metrics service using the operator to collect anonymized usage data without manual database configuration or inventory file editing.

## Before you begin

- Ansible Automation Platform operator installed on OpenShift cluster
- AnsibleAutomationPlatform custom resource (CR) created
- Cluster administrator or equivalent permissions to edit custom resources

## About this task

Use this procedure when:

- Deploying Ansible Automation Platform on OpenShift using the operator
- You need to enable anonymized usage data collection for Red Hat analytics
- You want the operator to automatically provision database access and configuration


Important:

The operator handles all configuration automatically, including database access, OAuth integration with the gateway, and traffic routing through Envoy. No manual database passwords, inventory variables, or network configuration is required.

## Procedure

1.  Edit the AnsibleAutomationPlatform custom resource
      Add or modify the `metrics` section in the CR specification:

```
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
  name: myaap
spec:
  controller:
    disabled: false
  eda:
    disabled: false
  hub:
    disabled: false
  metrics:
    disabled: false
```
    **Example using oc edit:**

```
oc edit ansibleautomationplatform myaap -n ansible-automation-platform
```

2.  Apply the custom resource
      If you edited the CR in a file:

```
oc apply -f aap.yml
```
    **Result:** The AAP gateway operator reconciles the change and creates the metrics service components.

3.  Verify that the MetricsService custom resource was created
      The gateway operator automatically creates a MetricsService CR named `<aap-name>-automationmetricsservice` in the same namespace:

```
oc get metricsservice -n <namespace>
```
    **Example output:**

```
NAME                                   AGE
myaap-automationmetricsservice         2m
```

4.  Verify that metrics service pods are running
  

```
oc get pods -l app.kubernetes.io/component=automationmetricsservice -n <namespace>
```
    **Example output:**

```
NAME                                        READY   STATUS    RESTARTS   AGE
myaap-metrics-api-6f8b9c5d7f-xk9pj          1/1     Running   0          2m
myaap-metrics-tasks-7d4c8b6f5d-j2k5h        1/1     Running   0          2m
myaap-metrics-scheduler-5c9d7f8b6d-m3n7k    1/1     Running   0          2m
```

5.  Verify the health endpoint
      Port-forward to the metrics service and check the health endpoint:

```
oc port-forward svc/<aap-name>-metrics-api 8080:80 -n <namespace>
```
    In another terminal:

```
curl http://localhost:8080/health/
```
    **Expected response when healthy:**

```
{
  "status": "good",
  "checks": {
    "database": "ok",
    "segment_send": {"status": "ok", "last_success_at": "<timestamp>"}
  }
}
```

## Results

Metrics service is enabled and collecting anonymized usage data from your OpenShift deployment. The operator automatically configured:

- Database access to automation controller (read-only)
- Dedicated metrics service database
- OAuth integration with the platform gateway
- Scheduled data collection tasks (hourly and daily)
- Secure transmission to Red Hat Data Ingress via Segment

## Disable metrics service

To disable metrics service in operator deployments, set `metrics.disabled: true` in the AnsibleAutomationPlatform CR and re-apply:

```
spec:
  metrics:
    disabled: true
```
Apply the change:

```
oc apply -f aap.yml
```
The gateway operator stops reconciling the metrics service on its next cycle. To fully remove the MetricsService CR:

```
oc delete metricsservice <aap-name>-automationmetricsservice -n <namespace>
```


Note:

Because ownerReferences are removed from the MetricsService CR in Ansible Automation Plateform 2.7, it is not automatically deleted when disabled. You must manually delete it if you want to fully remove metrics service.

## What to do next

**Verify data collection is running**

After the service has been running for at least 24 hours, check pod logs to confirm data transmission:

```
oc logs -l app.kubernetes.io/component=automationmetricsservice-tasks -n <namespace> | grep "Successfully sent metrics"
```
Look for log entries like:

```
Successfully sent metrics to Segment.com (Size: <size> bytes, Chunks: <chunks>)
```
