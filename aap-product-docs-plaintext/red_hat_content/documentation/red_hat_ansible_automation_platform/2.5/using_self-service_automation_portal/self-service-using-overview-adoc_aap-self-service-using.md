# Chapter 1. Overview




You can launch templates from self-service automation portal to execute job templates from your existing Ansible Automation Platform setup.

- Auto-generated self-service templates are automatically synced from the job templates in Ansible Automation Platform to the self-service automation portal. The forms for the auto-generated templates are identical to the forms for the job templates.
- You can import custom self-service templates from a Git repository. A configuration file links each custom template to a specific job template in Ansible Automation Platform and contains the forms that users must complete.


You can associate multiple custom self-service templates with a single Ansible Automation Platform job template. You can use role-based access control (RBAC) to assign different custom self-service templates for users with different levels of automation experience. For example, you can design a simplified template with a narrow scope for configuration for new users, and a more detailed template for automation experts.

