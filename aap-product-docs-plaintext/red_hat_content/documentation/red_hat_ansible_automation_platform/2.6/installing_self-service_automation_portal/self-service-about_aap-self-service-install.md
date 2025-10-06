# Chapter 1. About self-service automation portal




Self-service automation portal makes enterprise automation accessible to users of varying roles and skill levels through a simplified web interface designed for business users, not automation experts.

Instead of requiring users to understand Ansible playbooks or complex automation workflows, self-service automation portal provides a streamlined "point-and-click" experience.

Self-service automation portal uses your existing Ansible Automation Platform setup: it uses the same logins, same security controls, and the same automation logic.

Job templates in Ansible Automation Platform are synced to self-service automation portal, where they appear as auto-generated self-service templates. Users can launch the auto-generated self-service templates in self-service automation portal to run the corresponding job templates in Ansible Automation Platform.

When launching a job, users follow step-by-step guided forms in self-service automation portal. These forms are identical to the forms for the equivalent job templates in Ansible Automation Platform.

You can also import custom self-service templates in self-service automation portal. These templates are pulled from a git repository, and their configuration file associates them with a job template in Ansible Automation Platform. The configuration file contains the forms for the template.

You can associate more than one custom self-service template with one Ansible Automation Platform job template. You set the RBAC for the custom self-service templates in self-service automation portal. Therefore you can set up different types of forms for users with different levels of automation experience.

For example, for a job template that configures network settings, you could associate a custom template with minimum scope for adjusting settings to a group with less automation experience, and use a more detailed custom template with deeper scope for configuration for automation experts.

Self-service automation portal connects with Red Hat Ansible Automation Platform using an OAuth application for authentication.

The following restrictions apply:

- You can only use one Ansible Automation Platform instance.
- You can only use one Ansible Automation Platform organization.


