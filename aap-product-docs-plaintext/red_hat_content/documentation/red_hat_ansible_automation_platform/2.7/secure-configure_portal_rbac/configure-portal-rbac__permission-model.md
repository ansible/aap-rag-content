# Configure role-based access control for Ansible automation portal
## Understand the permission model

Ansible automation portal and Ansible Automation Platform use separate but related permission systems.

**Ansible automation portal RBAC:**

- Controls which users can view templates in the Ansible automation portal catalog.
- Controls which users can access portal templates and submit jobs.
- Controls which navigation items are visible in the sidebar.

**Ansible Automation Platform RBAC:**

- **Controls synchronization scope:** Only Ansible Automation Platform job templates accessible by the configured API token (`ansible.rhaap.token`) are synchronized to Ansible automation portal.
- **Controls auto-generated template visibility:** Ansible Automation Platform permissions determine whether authenticated users can view and execute auto-generated templates in Ansible automation portal. Custom templates are not filtered by Ansible Automation Platform permissions.
- **Validates execution permissions:** When a user executes any template, Ansible Automation Platform checks that user's execute permissions on the underlying job template before launching the job. This applies to both auto-generated and custom templates.

If a user can see a template in the catalog but lacks Ansible Automation Platform execute permissions for the associated job template, the user cannot run the job.

