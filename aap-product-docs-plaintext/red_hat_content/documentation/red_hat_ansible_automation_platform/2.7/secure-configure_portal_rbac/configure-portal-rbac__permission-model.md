# Configure role-based access control for Ansible automation portal
## Understand the permission model

Ansible automation portal and Ansible Automation Platform use separate but related permission systems. Ansible Automation Platform RBAC is the source of truth for synchronization scope and execution permissions.

**Ansible automation portal RBAC:**

- Controls which users can view templates in the Ansible automation portal catalog.
- Controls which users can access portal templates and submit jobs.
- Controls which navigation items are visible in the sidebar.


**Ansible Automation Platform RBAC:**

- **Controls synchronization scope:** Only Ansible Automation Platform job templates accessible by the configured API token (`ansible.rhaap.token`) are synchronized to Ansible automation portal.
- **Controls job template visibility and execution:** Ansible Automation Platform permissions determine whether authenticated users can view and execute job templates in Ansible automation portal.
- **Validates execution permissions:** When a user executes a template, Ansible Automation Platform checks that user's execute permissions before launching the job.


If a user can see a template in the catalog but lacks Ansible Automation Platform execute permissions for the associated job template, the user cannot run the job.

