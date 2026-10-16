# Operator-managed NetworkPolicies
## Unrestricted egress for user-configured destinations

Several Ansible Automation Platform components connect to external services whose destinations and ports are entirely user-configured and cannot be predicted at policy creation time. For these components, the NetworkPolicy permits unrestricted egress in addition to any specific per-component allow rules. Components with unrestricted egress are noted in the following tables.

Examples of user-configured external destinations include:

- Platform gateway: Red Hat Subscription Management (RHSM), Lightweight Directory Access Protocol (LDAP) and LDAP over TLS (LDAPS) directories, Security Assertion Markup Language (SAML) and OAuth identity providers, webhooks
- Automation controller: source control management (SCM) hosts, receptor mesh peers, execution environments
- Automation hub: external collection registries, signing services
- Event-Driven Ansible: External Secret Management System, user-defined event sources

