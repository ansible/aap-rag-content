# Configure role-based access control for Ansible automation portal

Configure RBAC permissions in Ansible automation portal to control which users can view and execute templates, and which sidebar items are visible to non-admin users.

After you install Ansible automation portal and synchronize it with Ansible Automation Platform, only users with AAP administrator privileges can view the auto-generated templates. You must configure role-based access control (RBAC) permissions to allow non-admin users to view and execute templates.

Ansible automation portal uses two categories of permissions:

- **Catalog and scaffolder permissions** control whether users can view templates, execute actions, and manage tasks.
- **Navigation permissions** control which sidebar items and pages are visible to users. Without the required navigation permission, a sidebar item and its associated pages are hidden.


Important:

RBAC differs by template type:

- **Auto-generated templates:** Permissions are synchronized from Ansible Automation Platform. Users must have permissions on the underlying AAP job template.
- **Custom templates:** Permissions must be explicitly configured within Ansible automation portal. Users must also have permissions to run the associated job templates in Ansible Automation Platform.

