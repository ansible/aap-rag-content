# Grant execution environment builder access to a role

Enable navigation permissions in the Ansible automation portal RBAC configuration so that non-admin users can access execution environment builder features.

## Before you begin

- You have configured base RBAC roles per [Configure role-based access control for Ansible automation portal](/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_rhdh_configure#rhdh-configure-rbac "Red Hat Developer Hub offers Role-based Access Control (RBAC) functionality. RBAC can then be applied to the Ansible plug-ins content.").
- You have the AAP Administrator role and access to **Administration > RBAC** in automation portal.

## Procedure

1.  In automation portal, navigate to **Administration > RBAC** in the sidebar.
2.  Select an existing role to edit, or click **Create Role** to create a new role (for example, `ee-builder-users`).
3.  In the permissions section, add the execution environment builder permissions.
For the list of permissions, see [Execution environment builder permissions](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-ref_ee_builder_permissions "Execution environment builder uses navigation-level permissions that control which sidebar items and pages are visible to users in Ansible automation portal.").

4.  If creating a new role, assign the role to the appropriate users or groups.
5.  Click **Save**.

## Results

To verify the configuration:

1. Log out and log in as a user assigned to the modified role.
2. Verify that the expected sidebar items are visible based on the permissions you assigned.
3. If you granted full access, navigate to **Execution Environments > Create** and verify that templates are visible and the wizard launches.


To hide execution environment builder from specific user groups, remove these permissions from their assigned roles.
