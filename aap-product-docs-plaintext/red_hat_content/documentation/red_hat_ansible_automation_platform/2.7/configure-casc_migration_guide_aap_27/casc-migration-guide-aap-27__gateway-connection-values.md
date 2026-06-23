# Configuration as Code migration guide for Ansible Automation Platform 2.7
## Gateway-managed connection values

All `host`, `username`, `password`, and `token` values used by existing playbooks and automation content must be created and managed in platform gateway.

Do not continue using the following patterns:

- Component-specific hostnames, such as `controller.example.com` or `hub.example.com`, as API targets in playbooks.
- Legacy Personal Access Tokens (PATs) or API tokens issued directly from automation controller, automation hub, or Event-Driven Ansible controller.
- Username and password pairs scoped only to a single component.


Instead, do the following:

- Create credentials, OAuth2 applications, and API tokens in platform gateway.
- Update existing playbooks, inventory variables, and Configuration as Code content to use the platform gateway URL for `aap_hostname` or equivalent module parameters.
- Use platform gateway-issued tokens for `aap_token` or equivalent authentication parameters.


For detailed setup instructions and before/after examples, see [Set up your automation environment for Configuration as Code](/documentation/en-us/red_hat_ansible_automation_platform/2.7/configure-set_up_automation_environment_for_casc "Configuration as Code is a way of working where you define and manage the configuration of Ansible Automation Platform using version-controlled configuration files, such as YAML, instead of clicking through the web UI.").

