# Configure role-based access control for Ansible automation portal
## Grant navigation permissions to a role

Before you begin:

- You have configured base RBAC roles as described in the [Configure RBAC for synchronization](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-configure_portal_rbac#configure-portal-rbac__configure-rbac-for-synchronization) section.
- You have the AAP Administrator role and access to Administration> (and then)RBAC in Ansible automation portal.


Procedure:

1. In Ansible automation portal, navigate to Administration> (and then)RBAC in the sidebar.
2. Select an existing role to edit, or click **Create Role** to create a new role (for example, `ee-builder-users`).
3. In the permissions section, add the navigation permissions your users require:
- For all portal users: `ansible.templates.view` and `ansible.history.view`.
- For execution environment builder users: `ansible.execution-environments.view`, `ansible.collections.view`, and `ansible.git-repositories.view`.
4. If creating a new role, assign the role to the appropriate users or groups.
5. Click **Save**.


To hide specific sidebar items from a user group, remove the corresponding permissions from their assigned roles.

Note:

Importing and deleting EE templates are AAP administrator-only actions. Users with the AAP Administrator role can perform these actions without additional permission grants.

Verification:

- Log out and log in as a user assigned to the modified role.
- Verify that the expected sidebar items are visible based on the permissions you assigned.
- If you granted execution environment builder access, navigate to Execution Environments> (and then)Create and verify that templates are visible and the wizard launches.

