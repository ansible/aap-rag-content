# Authentication changes in Ansible Automation Platform 2.7

In Ansible Automation Platform 2.7, all authentication has been consolidated through platform gateway. Direct API access to individual platform components has been removed.

Important:

Only upgrades from Ansible Automation Platform 2.6 to 2.7 are supported. If you are running version 2.4 or 2.5, you must first upgrade to version 2.6 before upgrading to 2.7.

## Architectural changes in Ansible Automation Platform 2.7

Ansible Automation Platform 2.7 removes direct API access and component-level authentication. All external access to platform components must go through platform gateway.

The following features and access methods are removed in this release:

- Direct API access to automation controller, automation hub, and Event-Driven Ansible controller.
- Basic authentication at the component level.
- Component-level Personal Access Tokens (PATs) and legacy OAuth applications.
- Third-party authentication provider configuration (LDAP, SAML, RADIUS, TACACS+) within automation controller.
- Direct external routes or ingress to automation controller and automation hub.


Important:

If you use Red Hat Ansible Lightspeed and have automation or scripts that change the `max_stream_duration` or `stream_idle_timeout` global proxy settings, you must update your scripts. These global settings have been removed, and you should now use the per-route service timeouts that are configurable on any route.

## How direct access is prevented in Ansible Automation Platform 2.7

In Ansible Automation Platform 2.7, platform components are configured to accept only platform gateway JWT authentication, ensuring that all external access goes through platform gateway.

When deployed as part of Ansible Automation Platform, this enforcement is immutable and cannot be changed through configuration files or environment variables, ensuring no bypass is possible.
