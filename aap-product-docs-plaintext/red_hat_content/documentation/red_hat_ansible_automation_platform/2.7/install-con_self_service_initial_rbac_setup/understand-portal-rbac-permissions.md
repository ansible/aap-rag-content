# Set up initial RBAC rules in Ansible automation portal
## Understand the permission model

Ansible automation portal and Ansible Automation Platform use separate but related permission systems. Ansible Automation Platform RBAC is the source of truth for synchronization scope and execution permissions.

**Ansible automation portal RBAC:**

- Controls which users can view templates in the Ansible automation portal catalog.
- Controls which users can access portal templates and submit jobs.


**Ansible Automation Platform RBAC:**

- **Controls synchronization scope:** Only Ansible Automation Platform job templates accessible by the configured Ansible Automation Platform token (ansible.rhaap.token) are synchronized to Ansible automation portal.
- **Controls Ansible Automation Platform job template visibility and execution:** Ansible Automation Platform permissions determine whether authenticated users can view and execute Ansible Automation Platform job templates in Ansible automation portal.
- **Validates execution permissions:** When a Ansible automation portal user executes a template, Ansible Automation Platform checks that user’s execute permissions before launching the job.


Note:

If a user can see a Ansible automation portal template in the catalog but lacks Ansible Automation Platform execution permissions for the associated Ansible Automation Platform job template in Ansible Automation Platform, the user cannot run the Ansible Automation Platform Job.

