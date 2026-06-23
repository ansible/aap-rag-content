# Upgrade the Ansible automation portal RHEL appliance

The Ansible automation portal RHEL appliance uses RHEL image mode (bootc) for atomic upgrades. Your configuration, data, and secrets are preserved, and you can roll back to the previous image if needed.

Important:

If you are upgrading from plug-in version 2.1 to 2.2, you must grant navigation permissions to existing roles. The **Templates** and **History** sidebar items now require explicit `ansible.templates.view` and `ansible.history.view` permission grants. Without these permissions, non-admin users cannot see the Templates and History navigation items. Administrators and superusers are unaffected.

After upgrading, log in as an administrator, navigate to Administration> (and then)RBAC, and add `ansible.templates.view` and `ansible.history.view` to each role that requires access. For more information, see [Configure role-based access control for Ansible automation portal](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-configure_portal_rbac "Configure RBAC permissions in Ansible automation portal to control which users can view and execute templates, and which sidebar items are visible to non-admin users.").

When you upgrade, the entire system image is replaced atomically. If an upgrade causes issues, you can roll back to the previous image in one command.

Bootc downloads only the layers that changed between the current and new image, making incremental upgrades fast and bandwidth-efficient.

Bootc divides the filesystem into three categories that determine what happens during an upgrade:

| Path | Upgrade behavior                              | What the appliance stores here                                                                       |
| ---- | --------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| /usr | Replaced atomically with the new image        | Portal scripts, pre-baked Ansible plugins, image version stamp                                       |
| /etc | Three-way merged (your changes are preserved) | Portal configuration (app-config.production.yaml), Quadlet files, Quadlet drop-ins, SSL certificates |
| /var | Never touched by bootc                        | PostgreSQL database, backups, Podman secrets, generated configs                                      |


Your configuration files in /etc are preserved through upgrades using a three-way merge: bootc compares the original file from the old image, your modified version, and the new file from the new image. Your changes take precedence. Files in /var (database, backups) are never modified by bootc.

For more information about RHEL image mode, see [Managing RHEL bootc images](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/managing-rhel-bootc-images).

Prerequisites:

- [Back up and restore data](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-ref_self_service_portal_cli_commands "The Ansible automation portal appliance provides the ansible-portal management CLI for administration and troubleshooting.") before upgrading.
- For connected upgrades, authenticate to `registry.redhat.io` (see the Authenticate to the container registry section).
- For disconnected upgrades, [Upgrade the Ansible automation portal RHEL appliance in a disconnected environment](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_self_service_rhel_upgrade_disconnected "In disconnected environments, you can upgrade the Ansible automation portal RHEL appliance using a mirror registry. Configure the mirror registry so that bootc upgrade pulls images from your internal registry instead of registry.redhat.io.").

