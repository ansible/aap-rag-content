# Pre-upgrade checklist
## Gateway authentication assessment

Ansible Automation Platform 2.7 requires all external authentication and API access to go through platform gateway. Identify the following items in your environment that require migration to gateway-based authentication:

- Scripts that use direct component URLs, such as `controller.example.com`, `hub.example.com`, or `eda.example.com`.
- Configuration as Code (CaC) implementations that reference component-specific endpoints.
- Active Personal Access Tokens (PATs) that were created through individual component interfaces.
- API integrations and custom applications that connect to component-specific APIs.
- Container registry workflows, such as `podman login` or `docker login` commands that target component hostnames.
- Certified collection usage, specifically the latest versions of `ansible.controller`, `ansible.hub`, and `ansible.eda`. These collections may be replaced by `ansible.platform`.
- Third-party authentication provider configurations, including LDAP, SAML, RADIUS, and TACACS+.
- Platform gateway accounts are configured for all users who require access after the upgrade.

