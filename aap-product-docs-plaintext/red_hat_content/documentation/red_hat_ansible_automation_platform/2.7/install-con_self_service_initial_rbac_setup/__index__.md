# Set up initial RBAC rules in Ansible automation portal

After you install Ansible automation portal and synchronize it with Ansible Automation Platform, only users with Ansible Automation Platform administrator privileges can view the auto-generated templates.

You must configure initial Role-Based Access Control (RBAC) permissions to allow non-admin users to view and execute synchronized Ansible Automation Platform job templates.

For the complete RBAC configuration procedure, including navigation permissions required for non-admin users to access portal pages, see [Configure role-based access control for Ansible automation portal](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-configure_portal_rbac "Configure RBAC permissions in Ansible automation portal to control which users can view and execute templates, and which sidebar items are visible to non-admin users.").

Important:

Role-Based Access Control (RBAC) differs by template type:

-   * **Auto-generated templates:** Permissions are synchronized from Ansible Automation Platform. Users must have permissions on the underlying Ansible Automation Platform job template.
* **Custom templates:** Permissions must be explicitly configured within the Ansible Automation Portal. Users must also have permissions to run the associated job templates in Ansible Automation Platform.

