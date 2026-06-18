# Post-upgrade requirements

After upgrading to Ansible Automation Platform 2.7, update tokens, scripts, and integrations to use platform gateway for all external authentication and API access.

After upgrading to Ansible Automation Platform 2.7, perform the following actions:

- **Regenerate tokens:** Regenerate all Personal Access Tokens through platform gateway.
- **Update CaC:** Update Configuration as Code files to use platform gateway URLs.
- **Update scripts:** Update scripts and integrations to point to platform gateway.
- **Update container registry:** Re-authenticate to the container registry.
- **Update collection connection parameters:** Update playbooks that use `ansible.controller`, `ansible.hub`, or `ansible.eda` collections to point to the platform gateway hostname instead of direct component hostnames. For example, change `controller_host` from `controller.example.com` to `gateway.example.com`. Token parameters such as `controller_oauthtoken` must use tokens created through platform gateway.
