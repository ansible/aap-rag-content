+++
title = "Optimize request timeouts - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/optimize-optimize_request_timeouts"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/optimize-optimize_request_timeouts/", "Optimize request timeouts"]]
category = "Optimize"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/optimize-optimize_request_timeouts/aem-page/optimize-optimize_request_timeouts.html"
last_crumb = "Optimize request timeouts"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Optimize request timeouts"
oversized = "false"
page_slug = "optimize-optimize_request_timeouts"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/optimize-optimize_request_timeouts"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/optimize-optimize_request_timeouts/toc/toc.json"
type = "aem-page"
+++

# Optimize request timeouts

Ansible Automation Platform on OpenShift Container Platform manages request timeouts through a synchronized, cascading architecture. This structure ensures that if a high-level service (the Gateway) reaches a timeout limit, all dependent internal processes terminate.

placeholder

## Cascading client timeouts

Cascading timeouts ensure that if an outer layer times out, inner processes also terminate to prevent resource exhaustion. Set the primary timeout at the Gateway level to synchronize timeouts across applications.

### Timeout mathematical relationships

Ansible Automation Platform maintains a downward mathematical cascade to ensure correct behavior and assist with debugging. Ansible Automation Platform applies the following logic to internal layers:

- The `client_request_timeout` serves as the primary value from which others are derived.
- The sum of the Envoy `request_timeout` and the gRPC authentication timeout (`gateway_grpc_auth_service_timeout`) is less than the `client_request_timeout`.
- The Nginx read timeout (`nginx_read_timeout`) is less than or equal to the Envoy `request_timeout`.
- The Python web server timeout (`python_webserver_timeout`) is less than or equal to the `nginx_read_timeout`.

### Timeout grace periods

At the uWSGI layer, the `uwsgi_timeout_grace_period` allows the application to attempt a graceful shutdown. During this period, the application displays a traceback of the current stack position at the time of the timeout. If the process does not exit within the grace period, Ansible Automation Platform maintains forcefully terminates it.

## Increase the OpenShift Route timeout

High-volume API operations can exceed the default 30-second OpenShift Route timeout. To resolve HTTP 504 or 503 errors, you must increase `client_request_timeout` in the `AnsibleAutomationPlatform` custom resource..

### Before you begin

- Access to the Red Hat OpenShift Container Platform (RHOCP) web console.
- Update the Ansible Automation Platform 2.6 operator to the latest version to ensure configuration changes propagate correctly to the OpenShift Route.

### Procedure

1.  Log in to the OpenShift web console.
2.  Navigate to **Installed Operators → Ansible Automation Platform → All Instances**.
3.  Click your `AnsibleAutomationPlatform` instance.
4.  Select the **YAML** tab. Under the spec: section, add the `route_annotations` to extend the timeout:
  

```
spec:
  route_annotations: |
    haproxy.router.openshift.io/timeout: 180s

```

5.  Save the changes.

### Results

Confirm that the `haproxy.router.openshift.io/timeout` annotation in the **Route** reflects the new value.

- Navigate to **Networking → Routes** in the OpenShift console. Select the route for your **Ansible Automation Platform** instance.

- Verify the **Annotations** section contains the updated timeout value.
