# Mandatory platform gateway authentication in Ansible Automation Platform 2.7

In Red Hat Ansible Automation Platform 2.7, platform gateway is the only supported method for external authentication to platform components. Direct API access to automation controller, automation hub, and Event-Driven Ansible has been removed.

Platform components enforce gateway-only authentication through an immutable configuration. This enforcement activates automatically when components are deployed and cannot be bypassed or disabled.

Attempts to authenticate directly to a platform component using legacy methods result in an HTTP 401 Unauthorized error. Legacy methods include:

- Basic authentication
- Session authentication
- Component-level tokens

