+++
title = "Monitor device resources - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-ref_edge_manager_monitor_device"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-technology_preview/", "Technology Preview"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-ref_edge_manager_monitor_device/aem-page/whats_new-ref_edge_manager_monitor_device.html"
last_crumb = "Monitor device resources"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Monitor device resources"
oversized = "false"
page_slug = "whats_new-ref_edge_manager_monitor_device"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/whats_new-ref_edge_manager_monitor_device"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-ref_edge_manager_monitor_device/toc/toc.json"
type = "aem-page"
+++

# Monitor device resources

You can set up monitors for device resources and define alerts when the use of these resources crosses a defined threshold. When the agent alerts the Red Hat Edge Manager service, the service sets the device status to "degraded" or "error" (depending on the severity level).

Resource monitors take the following parameters:

| Parameter            | Description                                                                                                                                                                    |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <br>MonitorType      | <br>The resource to monitor. Currently supported resources are "CPU", "Memory", and "Disk".                                                                                    |
| <br>SamplingInterval | <br>The interval in which the monitor samples use, specified as positive integer followed by a time unit ("s" for seconds, "m" for minutes, "h" for hours).                    |
| <br>AlertRules       | <br>A list of alert rules.                                                                                                                                                     |
| <br>Path             | <br>(Disk monitor only) The absolute path to the directory to monitor. Utilization reflects the filesystem containing the path, similar to df, even if it’s not a mount point. |


Alert rules take the following parameters:

| Parameter       | Description                                                                                                                                                                                                                             |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>Severity    | <br>The alert rule’s severity level out of "Info", "Warning", or "Critical". Only one alert rule is allowed per severity level and monitor.                                                                                             |
| <br>Duration    | <br>The duration that resource use is measured and averaged over when sampling, specified as positive integer followed by a time unit ("s" for seconds, "m" for minutes, "h" for hours). It must be smaller than the sampling interval. |
| <br>Percentage  | <br>The use threshold that triggers the alert, as percentage value (range 0 to 100 without the "%" sign).                                                                                                                               |
| <br>Description | <br>A human-readable description of the alert. This is useful for adding details about the alert that might help with debugging. By default it populates the alert as : load is above >% for more than.                                 |

## Monitor device resources on the CLI

Monitor the resource use of your Red Hat Edge Manager devices on the CLI by configuring detailed monitors and threshold-based alert rules. This enables automatic status reporting, helping you keep stability and troubleshoot performance issues.

### About this task

### Procedure

 Add resource monitors in the `resources:` section of the device’s specification.

For example, add the following monitor for your disk:

```yaml
apiVersion: flightctl.io/v1alpha1
kind: Device
metadata:
  name: <device_name>
spec:
[...]
  resources:
  - monitorType: Disk
    samplingInterval: 5s
    path: /application_data
    alertRules:
    - severity: Warning
      duration: 30m
      percentage: 75
      description: Disk space for application data is >75% full for over 30m.
    - severity: Critical
      duration: 10m
      percentage: 90
      description: Disk space for application data is >90% full over 10m.
[...]
```


samplingInterval
Samples usage every 5 seconds.

path
Checks disk usage on the file system that is associated with the `/applications_data` path.

alertRules[severity: Warning]
Initiates a warning if the average usage exceeds 75% for more than 30 minutes.

alertRules[severity: Critical]
Initiates a critical alert if the average usage exceeds 90% for over 10 minutes.
