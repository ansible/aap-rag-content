+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_self_service_rhel_upgrade"
title = "Upgrade the Ansible automation portal RHEL appliance - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_self_service_rhel_upgrade/", "Upgrade the Ansible automation portal RHEL appliance"]]
category = "Upgrade"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_self_service_rhel_upgrade/aem-page/install-proc_self_service_rhel_upgrade.html"
last_crumb = "Upgrade the Ansible automation portal RHEL appliance"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Upgrade the Ansible automation portal RHEL appliance"
oversized = "false"
page_slug = "install-proc_self_service_rhel_upgrade"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-proc_self_service_rhel_upgrade"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_self_service_rhel_upgrade/toc/toc.json"
type = "aem-page"
+++

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

## Authenticate to the container registry

To pull new appliance images from `registry.redhat.io`, authenticate to the registry and save the credentials where bootc can find them.

Important:

Bootc and Podman use separate credential stores. The `--authfile /etc/ostree/auth.json` flag saves credentials to the location that `bootc upgrade` and `bootc switch` read. Running `podman login` without `--authfile` stores credentials only for Podman and does not authenticate bootc operations.

Procedure:

1. SSH into the Ansible automation portal RHEL appliance and log in to the container registry:

```terminal
$ sudo podman login --authfile /etc/ostree/auth.json registry.redhat.io
```

## Upgrade the appliance

Procedure:

1. [Back up and restore data](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-ref_self_service_portal_cli_commands "The Ansible automation portal appliance provides the ansible-portal management CLI for administration and troubleshooting.").

2. Run the upgrade:

```terminal
$ sudo bootc upgrade
```
     The upgrade is staged and does not take effect until you reboot. The current version continues running. You can schedule the reboot for a convenient maintenance window.

     `bootc upgrade` pulls the latest image for the current tag. To upgrade to a specific version, use `bootc switch` with a version tag:



```terminal
$ sudo bootc switch registry.redhat.io/ansible-automation-platform/bootc-automation-portal-rhel9:*version*
```

3. Reboot to activate the new image:

```terminal
$ sudo systemctl reboot
```

Verification:

- Verify that the new image is booted:

```terminal
$ sudo bootc status
```
     The booted digest matches the digest from the upgrade output. The previous version is retained as a rollback target.

- Check the portal service logs:

```terminal
$ sudo journalctl -u portal -f
```

- Verify that all services are running:

```terminal
$ sudo systemctl status portal postgres devtools
```
     All three services (`portal`, `postgres`, `devtools`) show `active (running)`.

## Roll back an upgrade

Bootc maintains two image slots: the booted image and one rollback image. After an upgrade, the previous version becomes the rollback target. After a rollback, the upgraded version becomes the rollback target. You can switch between the two versions as needed.

If the new version has issues, roll back to the previous image.

Procedure:

1. Roll back to the previous image:

```terminal
$ sudo bootc rollback
```

2. Reboot to activate the rollback image:

```terminal
$ sudo systemctl reboot
```

Verification:

- Confirm the rollback was applied:

```terminal
$ sudo bootc status
```
     The booted image shows the previous digest. The upgraded image is now listed as the rollback target.

- Verify that all services are running:

```terminal
$ sudo systemctl status portal postgres devtools
```
