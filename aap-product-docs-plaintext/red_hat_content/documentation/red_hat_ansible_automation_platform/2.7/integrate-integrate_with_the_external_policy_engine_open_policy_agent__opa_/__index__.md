# Integrate with the external policy engine Open Policy Agent (OPA)

Integrating Ansible Automation Platform with Open Policy Agent (OPA) enforces policies at automation runtime. Use encoded rules to define, manage, and enforce how users interact with the platform. Automate policy management to improve security, compliance, and operational efficiency.

Integrating with OPA helps you to:

- **Enforce policies at runtime**: Stop automation actions that violate organizational policies and provide users with clear information about policy violations before jobs run.
- **Centralize policy management**: Offload policy decisions to your OPA server and manage automation governance rules alongside organizational policies.
- **Improve compliance and security**: Apply policy rules to automation content at the organization, inventory, or job template level to ensure consistent governance.

## How Ansible Automation Platform supports OPA integration

When you trigger policy enforcement, policies are retrieved from your OPA server. These policies are applied to automation content before jobs run. If a violation is detected, the action stops and you receive information about the specific policy violation.

Associate policies with organizations, inventories, or job templates to control where policy enforcement occurs.
