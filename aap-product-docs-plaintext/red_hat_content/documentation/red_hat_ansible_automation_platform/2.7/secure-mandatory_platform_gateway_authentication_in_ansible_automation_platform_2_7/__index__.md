# Mandatory platform gateway authentication in Ansible Automation Platform 2.7

In Red Hat Ansible Automation Platform 2.7, platform gateway is the only supported method for external authentication to platform components. Direct API access to automation controller, automation hub, and Event-Driven Ansible has been removed.

Platform components enforce gateway-only authentication through an immutable configuration. This enforcement activates automatically when components are deployed and cannot be bypassed or disabled.

Attempts to authenticate directly to a platform component using legacy methods result in an HTTP 401 Unauthorized error. Legacy methods include:

- Basic authentication
- Session authentication
- Component-level tokens

## Authentication changes in platform gateway

In Ansible Automation Platform 2.7, all user authentication and API access is centralized through platform gateway. Third-party provider configuration must also be performed in platform gateway.

- **Centralized flow:** All user authentication flows through platform gateway.
- **API requests:** All API requests must use platform gateway URLs and gateway-issued tokens.
- **Third-party providers:** Configuration for LDAP, SAML, and OAuth, must be performed in platform gateway.
- **Disabled methods:** Basic and session authentication are no longer available at the component level.

## Unaffected internal operations

Internal platform operations continue to function normally using internal JWT-based authentication. The following communications do not go through platform gateway.

- **Service-to-service communication:** Interactions between components, such as automation controller retrieving images from automation hub.

- **Rulebook workers:** Event-Driven Ansible worker processes communicating with automation controller through WebSockets.

- **Container registry:** The automation hub container registry supports authentication using gateway tokens by using `podman login` or `docker login`. To authenticate, use your platform gateway credentials:

```
$ podman login <platform-host> --username <gateway-username> --password
```
For large container image uploads, you might need to adjust platform gateway route timeout settings.
