# Basic authentication removal

Basic authentication has been removed in Ansible Automation Platform 2.7. Direct authentication to automation controller, automation hub, and Event-Driven Ansible controller is no longer available. Use OAuth 2 token authentication through platform gateway instead.

If you have existing scripts or integrations that use basic authentication with direct component URLs, for example, `curl -u user:password https://<controller-host>/api/v2/...`, you must update them to use OAuth 2 token authentication through platform gateway. Replace basic authentication headers with a Bearer token and update the base URL to the platform gateway host. For example:

```
$ curl -H "Authorization: Bearer <oauth2-token-value>" https://<platform-host>/api/controller/v2/...
```
