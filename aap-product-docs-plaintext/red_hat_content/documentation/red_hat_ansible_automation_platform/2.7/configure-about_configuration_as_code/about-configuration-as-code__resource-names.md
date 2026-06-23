# Configuration as Code with the ansible.platform collection
## Resource names instead of IDs

When you reference resources such as organizations, teams, or users in your playbooks, use human-readable names instead of numeric IDs. Names are portable across environments, which means you can apply the same playbook to development, staging, and production without modification. Using names also simplifies disaster recovery because you can rebuild your configuration without looking up IDs from a previous environment.

