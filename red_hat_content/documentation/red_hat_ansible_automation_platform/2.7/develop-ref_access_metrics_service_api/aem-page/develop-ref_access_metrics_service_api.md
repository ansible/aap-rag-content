+++
title = "Access metrics service API - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-ref_access_metrics_service_api"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_controller_api_tools/", "Use the REST API to browse, query, filter, and authenticate"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-ref_access_metrics_service_api/aem-page/develop-ref_access_metrics_service_api.html"
last_crumb = "Access metrics service API"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Access metrics service API"
oversized = "false"
page_slug = "develop-ref_access_metrics_service_api"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-ref_access_metrics_service_api"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-ref_access_metrics_service_api/toc/toc.json"
type = "aem-page"
+++

# Access metrics service API

Access metrics service REST API endpoints for programmatic health checks, task status queries, and feature flag inspection to automate monitoring.

## API architecture

Metrics service exposes a REST API at `/api/v1/` with endpoints for task management, health monitoring, feature flag inspection, and settings configuration. The API is accessible through Ansible Automation Platform Gateway routing and requires authentication.

**Base URL:**

- **Containerized installer**: `https://<gateway-route>/api/metrics/v1/` (via Gateway route)
- **OpenShift operator**: `https://<gateway-route>/api/v1/` (via Gateway route)


**Authentication:**

API requests require authentication using Ansible Automation Platform Gateway credentials. Include a valid authentication token in the request headers:

```
curl -H "Authorization: Bearer <token>" https://<gateway-route>/api/metrics/v1/health/
```
For local development or troubleshooting on the metrics service host, you can access the API directly (bypassing Gateway authentication):

```
# Containerized: Direct access via container
podman exec automation-metrics-web curl http://localhost:8006/api/v1/health/

# OpenShift: Direct access via pod
oc exec deployment/metrics-service-web -n <namespace> -- curl http://localhost:8080/api/v1/health/
```

## API endpoints

**/api/v1/health/**

**Purpose:** Health status monitoring for integration with monitoring systems (Prometheus, Nagios, etc.)

**Method:** `GET`

**Authentication:** Not required for direct container/pod access; required for Gateway access

**Response schema:**

```
{
  "status": "good",
  "version": "1.0.0",
  "database": {
    "status": "connected",
    "migrations": "up-to-date"
  },
  "scheduler": {
    "status": "running",
    "last_heartbeat": "2026-05-20T14:35:00Z"
  }
}
```
**Status values:**

| Status      | Meaning                                             | Action                             |
| ----------- | --------------------------------------------------- | ---------------------------------- |
| `good`      | All components healthy                              | No action required                 |
| `degraded`  | Some components unhealthy but service functional    | Investigate degraded components    |
| `unhealthy` | Critical components failing, service non-functional | Immediate troubleshooting required |


**Example usage:**

```
# Containerized
curl http://localhost:8087/health/

# OpenShift
curl https://<gateway-route>/api/metrics/v1/health/ -H "Authorization: Bearer <token>"

# Monitoring integration (Prometheus)
http_probe:
  targets:
    - https://<gateway-route>/api/metrics/v1/health/
  bearer_token: <token>
```
**Response codes:**

- `200 OK`: Service is healthy (`status: "good"`)
- `503 Service Unavailable`: Service is degraded or unhealthy
- `401 Unauthorized`: Invalid or missing authentication token (Gateway access only)


**/api/v1/tasks/**

**Purpose:** Task execution status for troubleshooting collection pipeline

**Method:** `GET`

**Authentication:** Required

**Query parameters:**

| Parameter | Type    | Description                                                     | Example                        |
| --------- | ------- | --------------------------------------------------------------- | ------------------------------ |
| `name`    | string  | Filter by task name                                             | `?name=collect_hourly_metrics` |
| `status`  | string  | Filter by task status (`success`,`failure`,`running`,`pending`) | `?status=failure`              |
| `limit`   | integer | Maximum results to return (default: 50, max: 500)               | `?limit=100`                   |
| `offset`  | integer | Pagination offset                                               | `?offset=50`                   |


**Response schema:**

```
{
  "count": 150,
  "next": "/api/metrics/v1/tasks/?limit=50&offset=50",
  "previous": null,
  "results": [
    {
      "id": 1234,
      "name": "collect_hourly_metrics",
      "status": "success",
      "started": "2026-05-20T14:05:00Z",
      "finished": "2026-05-20T14:06:32Z",
      "duration_seconds": 92,
      "error_message": null
    },
    {
      "id": 1233,
      "name": "daily_metrics_rollup",
      "status": "failure",
      "started": "2026-05-20T02:00:00Z",
      "finished": "2026-05-20T02:00:15Z",
      "duration_seconds": 15,
      "error_message": "Database connection timeout"
    }
  ]
}
```
**Example usage:**

```
# Get all tasks from last 24 hours
curl https://<gateway-route>/api/metrics/v1/tasks/?limit=100 \
  -H "Authorization: Bearer <token>"

# Get failed tasks only
curl https://<gateway-route>/api/metrics/v1/tasks/?status=failure \
  -H "Authorization: Bearer <token>"

# Get specific task by name
curl https://<gateway-route>/api/metrics/v1/tasks/?name=daily_anonymize_and_prepare \
  -H "Authorization: Bearer <token>"
```
**Use cases:**

- Monitor task success rates over time
- Identify which collectors are failing
- Troubleshoot collection pipeline performance
- Alert on task failures (integrate with monitoring systems)


**/api/metrics/v1/feature_flag_state/**

**Purpose:** Troubleshooting endpoint for Red Hat Support to inspect internal feature enablement settings

**Method:** `GET`

**Authentication:** Required

Important:

This endpoint exposes internal feature enablement settings used for troubleshooting and support cases. Customers should not modify these settings directly. If you need to opt out of data collection, contact Red Hat Support for guidance.

**Use cases:**

- Red Hat Support troubleshooting: Verify internal settings during support cases
- Support-guided opt-out verification: Confirm settings after Red Hat Support applies opt-out configuration


**Example usage (support-guided only):**

```
# Get current feature flag state
curl https://<gateway-route>/api/metrics/v1/feature_flag_state/ \
  -H "Authorization: Bearer <token>"
```
**Response includes internal settings:**

- `METRICS_COLLECTION`: Controls local data collection
- `ANONYMIZED_DATA_COLLECTION`: Controls transmission to Red Hat
- `DASHBOARD_COLLECTION`: Controls dashboard-specific data


For information about these settings, contact Red Hat Support.

**/api/v1/settings/**

**Purpose:** Troubleshooting endpoint for Red Hat Support to retrieve and update internal dynamic settings

**Methods:** `GET`, `PATCH`

**Authentication:** Required (write operations require admin privileges)

Important:

This endpoint exposes internal feature enablement settings used for troubleshooting and support cases. Customers should not modify these settings directly without Red Hat Support guidance. If you need to opt out of data collection or change metrics service configuration, contact Red Hat Support.

**Use cases:**

- Red Hat Support troubleshooting: Retrieve current internal settings during support cases
- Support-guided configuration: Red Hat Support may use this endpoint to apply configuration changes
- Audit trail: Track configuration changes made by Red Hat Support


**Example usage (support-guided only):**

```
# Get all settings (read-only query for troubleshooting)
curl https://<gateway-route>/api/v1/settings/ \
  -H "Authorization: Bearer <token>"
```


Note:

Do not use `PATCH` operations to modify settings without Red Hat Support guidance. Incorrect configuration can impact service operation and supportability.

## Gateway routing and authentication

**Routing**

Ansible Automation Platform Gateway routes API requests to metrics service based on URL path prefix:

**Gateway routing rules:**

```
https://<gateway-route>/api/v1/health/        → metrics-service-web:8006/api/v1/health/
https://<gateway-route>/api/v1/tasks/         → metrics-service-web:8006/api/v1/tasks/
https://<gateway-route>/api/v1/feature_flag_state/ → metrics-service-web:8006/api/v1/feature_flag_state/
https://<gateway-route>/api/v1/settings/      → metrics-service-web:8006/api/v1/settings/
```
**Troubleshooting routing issues:**

If API requests return `404 Not Found` when accessing through Gateway:

1. Verify Gateway is running and healthy
2. Check Gateway logs for routing errors
3. Verify metrics service pods are running
4. Test direct access to metrics service (bypass Gateway) to isolate routing vs service issues


**Authentication**

**Token-based authentication:**

Metrics service API uses Ansible Automation Platform Gateway authentication. Obtain a token from Gateway:

```
# Request token from Gateway
curl -X POST https://<gateway-route>/api/gateway/v1/tokens/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "admin",
    "password": "<password>"
  }'
```
Response:

```
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "expires": "2026-05-20T18:00:00Z"
}
```
Use the token in subsequent API requests:

```
curl https://<gateway-route>/api/v1/health/ \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```
**Service accounts:**

For automation and monitoring integrations, create a dedicated service account with minimal privileges:

```
# Create service account via Gateway API
curl -X POST https://<gateway-route>/api/gateway/v1/service_accounts/ \
  -H "Authorization: Bearer <admin-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "metrics-monitoring",
    "description": "Service account for metrics service health monitoring",
    "scopes": ["metrics:read"]
  }'
```
**Troubleshooting authentication:**

| Error              | Cause                    | Solution                                                                      |
| ------------------ | ------------------------ | ----------------------------------------------------------------------------- |
| `401 Unauthorized` | Missing or invalid token | Verify token is included in`Authorization` header and has not expired         |
| `403 Forbidden`    | Insufficient permissions | Verify service account has required scopes (`metrics:read` or`metrics:write`) |
| `Token expired`    | Token TTL exceeded       | Request a new token from Gateway                                              |

## Integration examples

**Prometheus monitoring**

**prometheus.yml configuration:**

```
scrape_configs:
  - job_name: 'metrics-service-health'
    metrics_path: '/api/v1/health/'
    scheme: https
    bearer_token: '<token>'
    static_configs:
      - targets:
          - '<gateway-route>'
```
**Nagios monitoring**

```
#!/bin/bash
# check_metrics_service_health.sh

GATEWAY="https://<gateway-route>"
TOKEN="<service-account-token>"

response=$(curl -s -o /dev/null -w "%{http_code}" \
  -H "Authorization: Bearer $TOKEN" \
  "$GATEWAY/api/v1/health/")

if [ "$response" -eq 200 ]; then
  echo "OK: metrics service is healthy"
  exit 0
elif [ "$response" -eq 503 ]; then
  echo "WARNING: metrics service is degraded"
  exit 1
else
  echo "CRITICAL: metrics service is unreachable"
  exit 2
fi
```
**Ansible playbook integration**

```
---
- name: Disable anonymized data collection
  hosts: localhost
  tasks:
    - name: Update ANONYMIZED_DATA_COLLECTION setting
      uri:
        url: "https://{{ gateway_route }}/api/v1/settings/ANONYMIZED_DATA_COLLECTION/"
        method: PATCH
        headers:
          Authorization: "Bearer {{ gateway_token }}"
          Content-Type: "application/json"
        body_format: json
        body:
          value: "false"
        status_code: 200
      register: result

    - name: Verify setting was updated
      debug:
        msg: "ANONYMIZED_DATA_COLLECTION disabled successfully"
      when: result.status == 200
```
