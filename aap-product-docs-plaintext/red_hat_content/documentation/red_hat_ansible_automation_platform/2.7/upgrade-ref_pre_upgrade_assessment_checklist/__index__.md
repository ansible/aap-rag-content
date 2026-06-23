# Pre-upgrade migration checklist

Before upgrading to Red Hat Ansible Automation Platform 2.7, assess the environment to identify components and integrations that require migration to gateway-based authentication.

Before upgrading, identify the following items in your environment:

- Scripts using direct component URLs (for example, `controller.example.com`, `hub.example.com`, or `eda.example.com`).
- Configuration as Code (CaC) implementations.
- Active Personal Access Tokens (PATs).
- API integrations and custom applications.
- Container registry workflows, such as `podman login` or `docker login`.
- Certified collection usage, specifically the latest versions of `ansible.controller`, `ansible.hub`, and `ansible.eda` (these may be replaced by `ansible.platform`).
- Third-party authentication provider configurations, including LDAP, SAML, RADIUS, and TACACS+.

