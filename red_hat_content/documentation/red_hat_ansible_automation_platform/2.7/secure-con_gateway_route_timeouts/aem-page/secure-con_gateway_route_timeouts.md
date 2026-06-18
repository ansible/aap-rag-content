+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-con_gateway_route_timeouts"
title = "Configure platform gateway route timeouts - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_configure_authentication/", "Configure central authentication for Ansible Automation Platform"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-con_gateway_route_timeouts/aem-page/secure-con_gateway_route_timeouts.html"
last_crumb = "Configure platform gateway route timeouts"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure platform gateway route timeouts"
oversized = "false"
page_slug = "secure-con_gateway_route_timeouts"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-con_gateway_route_timeouts"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-con_gateway_route_timeouts/toc/toc.json"
type = "aem-page"
+++

# Configure platform gateway route timeouts

In Ansible Automation Platform 2.7, all API access to platform components goes through platform gateway. Gateway-level timeout settings control how long platform gateway waits for backend services to respond before closing a connection.

Important:

If you experience timeout errors when uploading container images or collections to automation hub, increase gateway route timeouts to allow more time for the upload to complete.

As all traffic now routes through platform gateway, gateway-level settings for request body size limits and connection timeouts apply to uploads that previously went directly to automation hub.

Collection uploads and container image uploads have different size characteristics and are affected by different gateway settings.

## Collection upload limits

Collections uploaded to automation hub are typically under 20 MB for public content and under 200 MB for private automation hub. These uploads are affected by the gateway request body size limit.

Platform gateway controls request body size through the `GRPC_SERVER_MAX_RECEIVE_MESSAGE_LENGTH` setting (default: 20 MiB, minimum: 4 MiB), which is enforced by the Envoy proxy. This default matches automation hub's 20 MB limit, so collection uploads work without additional configuration.

For collections larger than 20 MB, such as large private content, increase `GRPC_SERVER_MAX_RECEIVE_MESSAGE_LENGTH` by setting the environment variable to match your largest expected collection size. When increasing this value, also increase `ENVOY_PER_CONNECTION_BUFFER_LIMIT_BYTES` (default: 25 MiB) to remain at least 5 MiB above the request body size limit.

Note:

For containerized deployments, the installer variable `gateway_nginx_client_max_body_size` (default: `5m`) controls nginx body size limits. Since nginx sits in front of Envoy in containerized topologies, this limit is applied first. If collection uploads fail with HTTP 413 errors on containerized deployments, increase this value to at least `20m` to match automation hub's default.

## Container image uploads

Container images for execution environments can exceed 4 GB. These uploads use chunked transfer encoding, so they are primarily affected by gateway route timeout settings rather than body size limits.

## When to configure gateway settings

Adjust platform gateway settings when you experience upload errors or timeouts after routing traffic through platform gateway in Ansible Automation Platform 2.7.

### Symptoms requiring configuration changes

Adjust platform gateway settings if you experience:

- **HTTP 413 Request Entity Too Large errors** when uploading collections: increase `GRPC_SERVER_MAX_RECEIVE_MESSAGE_LENGTH` and `ENVOY_PER_CONNECTION_BUFFER_LIMIT_BYTES` (and `gateway_nginx_client_max_body_size` for containerized deployments).
- **Timeout errors** during container image pushes: increase route timeout values.
- **Incomplete transfers or interrupted uploads:** increase route timeout values.

### Affected operations

| Operation                                           | Primary setting                          | Size range   |
| --------------------------------------------------- | ---------------------------------------- | ------------ |
| Collection uploads to automation hub                | `GRPC_SERVER_MAX_RECEIVE_MESSAGE_LENGTH` | Up to 200 MB |
| Container image push (`podman push`, `docker push`) | Route timeout                            | 1-10+ GB     |
| Execution environment uploads                       | Route timeout                            | 1-10+ GB     |
| Bulk content synchronization                        | Route timeout                            | Varies       |

## Configure gateway routes using the ansible.platform collection

You can configure platform gateway route timeouts during installation or redeployment to support large file uploads to automation hub.

### Before you begin

- The `ansible.platform` collection is installed.
- You have administrator access to the deployment environment.
- For Red Hat OpenShift Container Platform deployments, you have cluster administrator privileges.

### Procedure

1.  Create or edit your platform gateway deployment playbook.
2.  Add the route timeout configuration for your deployment type.
      For OpenShift Container Platform deployments:

```
---
- name: Set hub container registry route timeout
  ansible.platform.route:
    name: "hub container registry"
    request_timeout_seconds: 600
    idle_timeout_seconds: 600
```
    For containerized deployments:

```
---
- name: Set hub container registry route timeout
  ansible.platform.route:
    name: "hub container registry"
    request_timeout_seconds: 600
    idle_timeout_seconds: 600
```

3.  Run the playbook to apply the configuration:
  

```
$ ansible-playbook -i inventory gateway-deploy.yml
```

### Results

Upload a large container image to automation hub:

```
$ podman push <large-image> <gateway-host>/automation-hub/<repository>/<image>:<tag>
```
Confirm that the upload completes without timeout errors.

## Configure gateway routes using the API

You can adjust route timeouts on existing deployments to support large file uploads to automation hub.

### Before you begin

- You have platform gateway administrator access.
- You have an OAuth2 token with administrative privileges.
- Platform gateway is deployed and operational.

### Procedure

1.  Obtain an administrative OAuth2 token:
  

```
$ curl -k -X POST \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"<admin-password>"}' \
  https://<gateway-host>/api/gateway/v1/tokens/
```

2.  Update the route timeout settings.
      For OpenShift Container Platform deployments:

```
$ curl -k -X PATCH \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "request_timeout_seconds": 3600,
    "idle_timeout_seconds": 3600,
    "route_annotations": {
      "haproxy.router.openshift.io/timeout": "3600s"
    }
  }' \
  https://<gateway_host>/api/gateway/v1/routes/$ROUTE_ID/
```
    For containerized deployments:

```
$ curl -k -X PATCH \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "request_timeout_seconds": 3600,
    "idle_timeout_seconds": 3600
  }' \
  https://<gateway_host>/api/gateway/v1/routes/$ROUTE_ID/
```

### Results

Verify the new timeout settings are active:

```
$ curl -k -X GET \
  -H "Authorization: Bearer <token>" \
  https://<gateway_host>/api/gateway/v1/routes/
```
Upload a large container image to automation hub and verify completion without errors.

## Configure Ansible Lightspeed route timeouts

If you use Red Hat Ansible Lightspeed and need to adjust streaming timeouts, configure the `request_timeout_seconds` and `idle_timeout_seconds` fields on the Lightspeed route.

### Before you begin

- You have platform gateway administrator access.
- The `ansible.platform` collection is installed.

### About this task

These fields replace the `max_stream_duration` and `stream_idle_timeout` global proxy settings that were available in Ansible Automation Platform 2.6.

| Removed setting (2.6) | Replacement field (2.7)   | Default |
| --------------------- | ------------------------- | ------- |
| `max_stream_duration` | `request_timeout_seconds` | 3600    |
| `stream_idle_timeout` | `idle_timeout_seconds`    | 60      |

### Procedure

1.  Create or edit a playbook to configure the Ansible Lightspeed route timeouts:
  

```
---
- name: Configure Ansible Lightspeed route timeouts
  hosts: localhost
  tasks:
    - name: Set Ansible Lightspeed streaming timeouts
      ansible.platform.route:
        name: 'lightspeed api'
        request_timeout_seconds: 3600
        idle_timeout_seconds: 60
```
  - `request_timeout_seconds` - Maximum total duration in seconds for streaming requests. Replaces the former `max_stream_duration` setting.
  - `idle_timeout_seconds` - Idle timeout in seconds. The connection closes if no data is transmitted within this period. Replaces the former `stream_idle_timeout` setting.

2.  Run the playbook:
  

```
$ ansible-playbook configure-lightspeed-timeouts.yml
```

### Results

Verify the updated timeout settings by querying the route through the API:

```
$ curl -s -k \
  -H "Authorization: Bearer <token>" \
  https://<gateway-host>/api/gateway/v1/routes/ \
  | python3 -m json.tool
```
Locate the Lightspeed route and confirm that `effective_timeout_seconds` and `effective_idle_timeout_seconds` reflect the expected values.

## Gateway timeout recommendations

Platform gateway route timeout values determine how long the gateway waits for requests to complete before terminating the connection.

### Recommended timeout values by upload size

| Expected upload size | Recommended timeout       | Use case                          |
| -------------------- | ------------------------- | --------------------------------- |
| Up to 1 GB           | 600 seconds (10 minutes)  | Small execution environments      |
| 1-4 GB               | 1800 seconds (30 minutes) | Medium execution environments     |
| 4-10 GB              | 3600 seconds (1 hour)     | Large execution environments      |
| Over 10 GB           | 7200 seconds (2 hours)    | Enterprise execution environments |

### Calculating timeout values

If your environment requires specific settings, use the following formula to calculate a timeout value:

1. Measure your upload bandwidth by timing a test file upload.
2. Calculate the base timeout: `timeout_seconds = (file_size_in_GB x 1024) / (bandwidth_in_MB_per_second)`
3. Add a 25% buffer to the result: `recommended_timeout = timeout_seconds x 1.25`
4. Round the result up to the nearest multiple of 300 seconds (5 minutes).

### Performance considerations

Increasing timeout values might lead to the following issues:

- **Increased memory usage:** The gateway maintains connection state for all active uploads.
- **Connection pool exhaustion:** Many concurrent long-running uploads can consume all available connections.
- **Delayed error detection:** Network issues might take longer to surface.

### Best practices

- Set timeouts based on the largest file size you expect to upload.
- Monitor gateway resource usage during large uploads to automation hub.
- Schedule large uploads during off-peak hours.
- Use multiple smaller images instead of a single large image when possible.
