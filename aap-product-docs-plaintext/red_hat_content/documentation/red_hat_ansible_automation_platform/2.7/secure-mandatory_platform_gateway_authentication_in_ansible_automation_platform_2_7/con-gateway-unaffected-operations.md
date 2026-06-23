# Mandatory platform gateway authentication in Ansible Automation Platform 2.7
## Unaffected internal operations

Internal platform operations continue to function normally using internal JWT-based authentication. The following communications do not go through platform gateway.

- **Service-to-service communication:** Interactions between components, such as automation controller retrieving images from automation hub.

- **Rulebook workers:** Event-Driven Ansible worker processes communicating with automation controller through WebSockets.

- **Container registry:** The automation hub container registry supports authentication using gateway tokens by using `podman login` or `docker login`. To authenticate, use your platform gateway credentials:

```
$ podman login <platform-host> --username <gateway-username> --password
```
For large container image uploads, you might need to adjust platform gateway route timeout settings.
