# Understand the permission model

Ansible automation portal and Ansible Automation Platform use separate but related permission systems. Ansible Automation Platform RBAC is the source of truth for synchronization scope and execution permissions.

**Ansible automation portal RBAC:**

- Controls which users can view templates in the Ansible automation portal catalog and submit jobs.
- Controls navigation permissions that determine which sidebar items and feature pages (such as the execution environment builder or administration menus) are visible to users.
- Maps portal roles to synchronized Ansible Automation Platform teams and users.

**Ansible Automation Platform RBAC:**

- **Controls synchronization scope:** Only Ansible Automation Platform job templates accessible by the configured API token are synchronized to Ansible automation portal.
- **Controls auto-generated template visibility:** Ansible Automation Platform permissions determine whether authenticated users can view and execute auto-generated templates in Ansible automation portal. Custom templates are not filtered by Ansible Automation Platform permissions.
- **Validates execution permissions:** When an Ansible automation portal user executes a template, Ansible Automation Platform checks that user’s execute permissions before launching the job.

Note:

If a user can see an Ansible automation portal template in the catalog but lacks Ansible Automation Platform execution permissions for the associated job template in Ansible Automation Platform, the user cannot run the job.
