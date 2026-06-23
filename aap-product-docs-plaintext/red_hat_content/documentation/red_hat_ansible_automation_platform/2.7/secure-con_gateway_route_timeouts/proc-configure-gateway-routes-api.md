# Configure platform gateway route timeouts
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

