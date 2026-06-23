# Set up initial RBAC rules in Ansible automation portal

After you install Ansible automation portal and synchronize it with Ansible Automation Platform, only users with Ansible Automation Platform administrator privileges can view the auto-generated templates.

You must configure initial Role-Based Access Control (RBAC) permissions to allow non-admin users to view and execute synchronized Ansible Automation Platform job templates.

Important:

Role-Based Access Control (RBAC) differs by template type:

-   * **Auto-generated templates:** Permissions are synchronized from Ansible Automation Platform. Users must have permissions on the underlying Ansible Automation Platform job template.
* **Custom templates:** Permissions must be explicitly configured within the Ansible Automation Portal. Users must also have permissions to run the associated job templates in Ansible Automation Platform.

