# Configure role-based access control for Ansible automation portal
## Configure RBAC for synchronization

Synchronization uses the Ansible Automation Platform API token configured in Ansible automation portal to determine which data to synchronize from Ansible Automation Platform.

Before you begin:

- You have credentials for an Ansible Automation Platform administrator.
- Synchronization of Ansible Automation Platform organization information from Ansible Automation Platform is complete.
- Users who execute job templates through Ansible automation portal must have job template execute permissions assigned in Ansible Automation Platform.
- The **Allow external users to create OAuth2 tokens** setting is enabled in Settings> (and then)Platform gateway settings in Ansible Automation Platform.


Procedure:

1. Log in to Ansible automation portal as an administrator.

2. Navigate to Administration> (and then)RBAC.

3. Click **Create Role** and provide a name (for example, `portal-user`).

4. In the **Users and Groups** section, select the Ansible Automation Platform teams and users to assign to this role. Click **Next**. You can only select teams and users from the Ansible Automation Platform organization that you configured for synchronization with Ansible automation portal.

5. In the **Add permission policies** section, select the **Catalog** plugin from the dropdown menu and enable `catalog.entity.read`.

6. Select the **Scaffolder** plugin and enable the following permissions:
- `scaffolder.template.parameter.read`
- `scaffolder.template.step.read`
- `scaffolder.action.execute`
- `scaffolder.task.create`
- `scaffolder.task.read` — Required for users to view previous task runs on the **History** page.
- `scaffolder.task.cancel`

7. Add the base navigation permissions so users can see the **Templates** and **History** sidebar items:
- `ansible.templates.view`
- `ansible.history.view`

8. Click **Next** to review your settings, then click **Create**.

Your new role appears in the **All roles** list under Administration> (and then)RBAC.

Important:

If you are upgrading from plug-in version 2.1, you must add `ansible.templates.view` and `ansible.history.view` to existing roles. Without these permissions, non-admin users cannot see the **Templates** and **History** navigation items. For more information, see the upgrade guide for your platform.

