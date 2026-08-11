+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-proc_self_service_rhel_upgrade"
title = "Upgrade the Ansible automation portal RHEL appliance - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-proc_self_service_rhel_upgrade/", "Upgrade the Ansible automation portal RHEL appliance"]]
category = "Upgrade"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-proc_self_service_rhel_upgrade/aem-page/upgrade-proc_self_service_rhel_upgrade.html"
last_crumb = "Upgrade the Ansible automation portal RHEL appliance"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Upgrade the Ansible automation portal RHEL appliance"
oversized = "false"
page_slug = "upgrade-proc_self_service_rhel_upgrade"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/upgrade-proc_self_service_rhel_upgrade"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-proc_self_service_rhel_upgrade/toc/toc.json"
type = "aem-page"
+++

# Upgrade the Ansible automation portal RHEL appliance

The Ansible automation portal RHEL appliance uses RHEL image mode (bootc) for atomic upgrades. Your configuration, data, and secrets are preserved, and you can roll back to the previous image if needed.

Important:

If you are upgrading from plug-in version 2.1 to 2.2, you must grant navigation permissions to existing roles. The **Templates** and **History** sidebar items now require explicit `ansible.templates.view` and `ansible.history.view` permission grants. Without these permissions, non-admin users cannot see the Templates and History navigation items. Administrators and superusers are unaffected.

After upgrading, log in as an administrator, navigate to Administration> (and then)RBAC, and add `ansible.templates.view` and `ansible.history.view` to each role that requires access. For more information, see [Configure role-based access control for Ansible automation portal](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-configure_portal_rbac "Configure RBAC permissions in Ansible automation portal to control which users can view and execute templates, and which sidebar items are visible to non-admin users.").

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
- For disconnected upgrades, configure a mirror registry or prepare an OCI archive (see [Upgrade the Ansible automation portal RHEL appliance in a disconnected environment](/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-proc_self_service_rhel_upgrade#proc-self-service-rhel-upgrade-disconnected "In disconnected environments, you can upgrade the Ansible automation portal RHEL appliance using a mirror registry or by transferring OCI archives directly. Configure the mirror registry so that bootc upgrade pulls images from your internal registry instead of registry.redhat.io.")).

## Authenticate to the container registry

To pull new appliance images from `registry.redhat.io`, authenticate to the registry and save the credentials where bootc can find them.

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

The rollback reverts the system image atomically. Your configuration and data in the `/etc` and `/var` directories are preserved. After reboot, the post-upgrade reconciliation runs again and regenerates plugin configurations from the previous image version.

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

## What survives an upgrade

The following table describes what happens to each type of content during a bootc upgrade of the Ansible automation portal RHEL appliance.

| Content                    | Location                                    | Survives upgrade | Notes                                        |
| -------------------------- | ------------------------------------------- | ---------------- | -------------------------------------------- |
| Portal configuration       | /etc/portal/configs/                        | Yes              | Three-way merge preserves your modifications |
| SSL certificates           | /etc/portal/ssl/                            | Yes              | Three-way merge                              |
| Quadlet drop-ins           | /etc/containers/systemd/portal.container.d/ | Yes              | Three-way merge                              |
| Quadlet port customization | /etc/containers/systemd/                    | Yes              | Three-way merge                              |
| PostgreSQL data            | /var/lib/portal/postgres-data/              | Yes              | Never touched by bootc                       |
| Backups                    | /var/lib/portal/backups/                    | Yes              | Never touched by bootc                       |
| Podman secrets             | /var/lib/containers/                        | Yes              | Never touched by bootc                       |
| Ansible plugins            | /usr/share/portal/plugins/                  | Updated          | New plugins from the new image               |
| Portal scripts             | /usr/share/portal/scripts/                  | Updated          | New scripts from the new image               |
| Dynamic plugin configs     | /var/lib/portal/dynamic-plugins-root/       | Cleared          | Regenerated from new plugins on first start  |

### Post-upgrade reconciliation

After reboot, the appliance automatically reconciles Ansible plugins and configuration with the new image version:

1. Clears the dynamic plugins directory so that plugins are regenerated from the new image.
2. Clears generated configuration files (regenerated on portal start).
3. Creates any new directories required by the new image version.
4. Fixes file ownership for portal and PostgreSQL directories.

## Upgrade the Ansible automation portal RHEL appliance in a disconnected environment

In disconnected environments, you can upgrade the Ansible automation portal RHEL appliance using a mirror registry or by transferring OCI archives directly. Configure the mirror registry so that `bootc upgrade` pulls images from your internal registry instead of `registry.redhat.io`.

### Before you begin

- A mirror registry is accessible from the Ansible automation portal RHEL appliance on the internal network.
- The new appliance image is copied to the mirror registry.
- You have SSH access to the appliance.

### About this task

Once the mirror registry is configured, `bootc upgrade` checks the mirror automatically.

### Procedure

1.  On a connected machine, copy the new appliance image to your internal registry:
  

```terminal
$ skopeo copy \
  docker://registry.redhat.io/ansible-automation-platform/bootc-automation-portal-rhel9:*version* \
  docker://mirror.internal.example.com:5000/ansible-automation-platform/bootc-automation-portal-rhel9:*version*
```

2.  On the Ansible automation portal RHEL appliance, create a registry mirror configuration:
  

```terminal
$ sudo tee /etc/containers/registries.conf.d/50-mirror.conf > /dev/null << 'EOF'
[[registry]]
prefix = "registry.redhat.io"
location = "registry.redhat.io"

    [[registry.mirror]]
location = "mirror.internal.example.com:5000"
insecure = false
EOF
```

    Replace `mirror.internal.example.com:5000` with your mirror registry address.

3.  If your mirror registry uses a self-signed certificate, add the CA certificate to the system trust store:
  

```terminal
$ sudo cp ca.crt /etc/pki/ca-trust/source/anchors/
$ sudo update-ca-trust
```

    Alternatively, set `insecure = true` in the mirror block. This is not recommended for production environments.

4.  Authenticate to the mirror registry:
  

```terminal
$ sudo podman login --authfile /etc/ostree/auth.json mirror.internal.example.com:5000
```

5.  Verify the mirror configuration:
  

```terminal
$ sudo podman info | grep -A5 registries
```

6.  Run the upgrade:
  

```terminal
$ sudo bootc upgrade
```

    If your mirror does not carry Red Hat GPG signatures, add `--no-signature-verification` to the `bootc switch` command when switching image sources. This flag is not needed for `bootc upgrade` when the image source is already configured.

7.  Reboot to activate the new image:
  

```terminal
$ sudo systemctl reboot
```

### Results

Note:

The mirror configuration in `/etc/containers/registries.conf.d/` survives bootc upgrades because bootc preserves `/etc` using a three-way merge. You do not need to reconfigure the mirror after each upgrade.

Verify that the new image is booted:

```terminal
$ sudo bootc status
```

Verify that all services are running:

```terminal
$ sudo systemctl status portal postgres devtools
```

### What to do next

**Sync new versions to the mirror**

When a new appliance version is available, copy it to the mirror from a connected machine:

1. Copy the new image version to the mirror registry:

```terminal
$ skopeo copy \
  docker://registry.redhat.io/ansible-automation-platform/bootc-automation-portal-rhel9:*new-version* \
  docker://mirror.internal.example.com:5000/ansible-automation-platform/bootc-automation-portal-rhel9:*new-version*
```

2. On the appliance, run the upgrade and reboot:

```terminal
$ sudo bootc upgrade
$ sudo systemctl reboot
```

## Update the Ansible Automation Platform connection

Change the Ansible Automation Platform host URL, OAuth client ID, API token, or OAuth client secret after deploying the Ansible automation portal RHEL appliance.

### About this task

To change the Ansible Automation Platform host URL or OAuth client ID after deployment, edit the configuration file directly. To update secrets (API token, OAuth client secret), use Podman secrets.

### Procedure

1.  To update the Ansible Automation Platform host URL or OAuth client ID, edit the configuration file:
  

```terminal
$ sudo vi /etc/portal/configs/app-config/app-config.production.yaml
```

    Update `ansible.rhaap.baseUrl` and `auth.providers.rhaap.production.clientId` to the new values. Save the file.

2.  To rotate the Ansible Automation Platform API token:
  

```terminal
$ temp_file=$(mktemp -p /dev/shm)
$ printf '%s' '<new-aap-token>' > "$temp_file"
$ sudo podman secret create --replace portal_aap_token "$temp_file"
$ rm -f "$temp_file"
```

3.  To rotate the OAuth client secret:
  

```terminal
$ temp_file=$(mktemp -p /dev/shm)
$ printf '%s' '<new-oauth-client-secret>' > "$temp_file"
$ sudo podman secret create --replace portal_aap_oauth_client_secret "$temp_file"
$ rm -f "$temp_file"
```

4.  Restart the Ansible automation portal service:
  

```terminal
$ sudo systemctl restart portal
```

### Results

The Ansible automation portal reconnects to the Ansible Automation Platform instance using the updated credentials. Verify the connection by signing in to the portal and confirming that job templates are synchronized.

## Troubleshooting RHEL appliances

Common issues and solutions for deploying and managing Ansible automation portal RHEL appliances.

### View logs and service status

Start troubleshooting by checking the status of all services and reviewing recent logs.

Check the status of all services:

```terminal
$ sudo systemctl status portal postgres devtools
```

A service that failed to start shows `active (failed)` or `inactive (dead)`.

View recent portal logs:

```terminal
$ sudo journalctl -u portal -n 200 --no-pager
```

Check the bootc image status:

```terminal
$ sudo bootc status
```

Check that the portal web service is responding:

```terminal
$ curl -sk https://localhost/healthcheck
```

A healthy portal returns `{"status":"ok"}`.

### Portal services do not start

**Symptom:** The Ansible automation portal service is not running after boot.

**Cause:** The Ansible automation portal RHEL appliance requires Ansible Automation Platform credentials in the cloud-init user-data to complete setup. If you provided SSH keys but no `aap:` section, you can SSH in but Ansible automation portal services do not start.

**Resolution:**

1. Check the portal service logs for errors:

```terminal
$ sudo journalctl -u portal -b --no-pager
```

2. Verify that your cloud-init user-data includes the required `aap:` section with `host_url`, `token`, `client_id`, and `client_secret`.

3. If the configuration is missing or incorrect, edit the configuration file directly:

```terminal
$ sudo vi /etc/portal/configs/app-config/app-config.production.yaml
```

     Update `ansible.rhaap.baseUrl`, `auth.providers.rhaap.production.clientId`, and other required values.

4. If Ansible Automation Platform credentials need to be updated, use Podman secrets:

```terminal
$ temp_file=$(mktemp -p /dev/shm) && chmod 600 "$temp_file"
$ printf '%s' "*aap-token*" > "$temp_file"
$ sudo podman secret create --replace portal_aap_token "$temp_file"
$ rm -f "$temp_file"
```

```terminal
$ temp_file=$(mktemp -p /dev/shm) && chmod 600 "$temp_file"
$ printf '%s' "*oauth-client-secret*" > "$temp_file"
$ sudo podman secret create --replace portal_aap_oauth_client_secret "$temp_file"
$ rm -f "$temp_file"
```

5. Restart the Ansible automation portal service:

```terminal
$ sudo systemctl restart portal
```

### OAuth login fails

**Symptom:** After clicking **Sign in with RHAAP**, the browser redirects back to the login page or Ansible Automation Platform returns "Invalid redirect_uri."

**Cause:** The OAuth redirect URI in Ansible Automation Platform does not match the Ansible automation portal user-accessible URL, or the `app.baseUrl`, `backend.baseUrl`, and `backend.cors.origin` values in the configuration file are not consistent with each other.

**Resolution:**

1. Check the current user-accessible URL and CORS configuration:

```terminal
$ grep -E 'baseUrl|origin' /etc/portal/configs/app-config/app-config.production.yaml
```

2. Verify that `app.baseUrl`, `backend.baseUrl`, and `backend.cors.origin` all use the same address.
3. In Ansible Automation Platform, navigate to **Access Management** > **OAuth Applications** and verify that the redirect URI matches the format `https://*portal-address*/api/auth/rhaap/handler/frame`.
4. If the values do not match, update either:
  - The OAuth redirect URI in Ansible Automation Platform (if the Ansible automation portal address is correct), or
  - The Ansible automation portal user-accessible URL and CORS origin in `app-config.production.yaml` (if the OAuth URI is correct).
5. Restart the Ansible automation portal service after any configuration change:

```terminal
$ sudo systemctl restart portal
```

### GitHub login appears instead of RHAAP

**Symptom:** The login page shows a "Sign in with GitHub" option instead of "Sign in with RHAAP," or both options appear.

**Cause:** The `app.baseUrl`, `backend.baseUrl`, and `backend.cors.origin` values in the configuration file do not match the URL used to access the Ansible automation portal RHEL appliance. This commonly happens when accessing the VM by IP address but the configuration uses a domain name, or vice versa. The CORS mismatch can cause the RHAAP provider to fail silently, falling back to a GitHub provider if one is configured.

**Resolution:**

1. Check the configured authentication providers:

```terminal
$ grep -A 5 'auth:' /etc/portal/configs/app-config/app-config.production.yaml
```

2. Verify that the `auth.providers` section contains `rhaap` and does not contain `github`. If a `github` provider is present, remove it.
3. Verify that `app.baseUrl`, `backend.baseUrl`, and `backend.cors.origin` all match the URL you use to access the Ansible automation portal RHEL appliance in your browser:

```terminal
$ grep -E 'baseUrl|origin' /etc/portal/configs/app-config/app-config.production.yaml
```

4. Restart the Ansible automation portal service after any configuration change:

```terminal
$ sudo systemctl restart portal
```

### Login fails with a 500 error

**Symptom:** After clicking **Sign in with RHAAP**, the browser shows a 500 Internal Server Error or redirects to an error page instead of completing the login.

**Cause:** A 500 error during login typically indicates that the Ansible Automation Platform API token or OAuth client secret is invalid, expired, or missing. The Ansible automation portal cannot authenticate with the Ansible Automation Platform instance.

**Resolution:**

1. Check the portal logs for authentication errors:

```terminal
$ sudo journalctl -u portal -n 100 --no-pager | grep -i -E 'auth|oauth|401|403|500|error'
```

2. Verify that the required Podman secrets exist:

```terminal
$ sudo podman secret ls | grep -E 'aap_token|oauth'
```

     You should see both `portal_aap_token` and `portal_aap_oauth_client_secret` listed. If either is missing or the values need to be updated, recreate them:

```terminal
$ temp_file=$(mktemp -p /dev/shm) && chmod 600 "$temp_file"
$ printf '%s' "*new-aap-token*" > "$temp_file"
$ sudo podman secret create --replace portal_aap_token "$temp_file"
$ rm -f "$temp_file"
```

3. Verify that the Ansible Automation Platform instance is reachable from the appliance:

```terminal
$ curl -sk https://*aap-host*/api/v2/ping/
```

4. Verify that the OAuth client ID in the configuration matches the OAuth application in Ansible Automation Platform:

```terminal
$ grep clientId /etc/portal/configs/app-config/app-config.production.yaml
```

5. Restart the Ansible automation portal service after any changes:

```terminal
$ sudo systemctl restart portal
```

### Cannot SSH to the VM

**Symptom:** SSH connection refused or permission denied.

**Cause:** The appliance enforces SSH key-only authentication. Password login is disabled.

**Resolution:**

- Verify that your SSH private key matches the public key you provided in the cloud-init user-data.
- Verify that you are using the correct username from your cloud-init configuration.

If you have lost access to your SSH key, use platform-specific recovery:

- **KVM:** Access the VM console with `virsh console *vm-name*` and add a new SSH key.
- **Red Hat OpenShift Virtualization:** Access the VM console with `virtctl console *vm-name* -n *namespace*`.
- **VMware vSphere:** Use the vSphere console with `systemd.unit=rescue.target` boot parameter to add a new SSH key.

### VM is inaccessible

**Symptom:** The VM was deployed without cloud-init user-data. No SSH keys or Ansible Automation Platform credentials are configured.

**Cause:** The appliance has no default password. Without cloud-init configuration, the VM is not accessible.

**Resolution:** Redeploy the VM with a cloud-init configuration attached. See [Prerequisites for deploying Ansible automation portal on RHEL](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_self_service_rhel_prerequisites "Before you deploy an Ansible automation portal RHEL appliance, verify that your environment meets the system, network, and access requirements.") to prepare cloud-init files, then follow the install guide for your platform.

### Red Hat OpenShift Virtualization issues

**Symptom:** Upload, boot, or scheduling failures when deploying on Red Hat OpenShift Virtualization.

**Resolution:**

Upload fails with "effective image size is larger than available storage"
Increase `--size` (for example, from 40 Gi to 50 Gi). Check the virtual size with `qemu-img info disk.qcow2`.

Upload hangs at "Waiting for PVC upload pod to be ready"
The storage class uses `WaitForFirstConsumer` binding. Add `--force-bind` to the `virtctl` command.

VM shows "Boot failed: not a bootable disk"
The disk image was not properly converted during upload. Verify the upload completed with "Processing completed successfully." If processing was interrupted, delete the DataVolume and PVC and re-upload.

VM stuck in Scheduling with "Insufficient memory"
Reduce the VM memory request or add cluster resources.

### VMware vSphere troubleshooting

Disk conversion fails with vmkfstools
- Verify that you have SSH access to the ESXi host.
- Verify that the `disk.vmdk` file was uploaded successfully to the datastore.
- Check that you have sufficient permissions to run `vmkfstools` on the ESXi host.
- Verify that there is sufficient free space on the datastore for the converted disk.

Virtual machine fails to boot after attaching the disk
- Verify that you selected the correct disk file.
- Verify that the disk is attached to the correct SCSI controller and bus.
- Check the virtual machine boot order settings and ensure the hard disk is the first boot device.

Cannot upload disk image to datastore
- Verify that your user account has permissions to upload files to the datastore.
- Check that there is sufficient free space on the datastore.
- Verify that the vSphere web client is properly connected.

### External database connection fails

**Symptom:** After configuring an external database and restarting the Ansible automation portal service, the portal fails to start or logs show database connection errors.

**Cause:** The external database is unreachable due to incorrect connection parameters, firewall rules blocking port 5432, or an SSL/TLS configuration mismatch.

**Resolution:**

1. Verify that the external database is reachable from the appliance:

```terminal
$ curl -v telnet://*database-host*:5432
```

     A successful connection confirms network connectivity. If the connection times out or is refused, check firewall rules and security groups.

2. Verify that the Podman secret for the database password exists:

```terminal
$ sudo podman secret ls | grep portal_postgresql_password
```

     If the secret is missing, create it. For the procedure, see [Configure an external database](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_self_service_rhel_configure_external_db "By default, the Ansible automation portal RHEL appliance runs a built-in PostgreSQL database. For production deployments, connect to an external PostgreSQL database.").

3. Check the database connection parameters in the configuration file:

```terminal
$ grep -A 6 'database:' /etc/portal/configs/app-config/app-config.production.yaml
```

     Verify that `host`, `port`, and `user` match your external database server settings.

4. If SSL is enabled, verify that the `ssl.require` setting matches your database server's TLS configuration. Set `ssl.require: false` temporarily to isolate SSL issues from connectivity issues.

5. Restart the Ansible automation portal service after any changes:

```terminal
$ sudo systemctl restart portal
```

### Database schema creation fails

**Symptom:** The Ansible automation portal service starts but logs show errors about missing tables, permission denied, or `CREATE DATABASE` failures.

**Cause:** The database user does not have the `CREATEDB` privilege. Ansible automation portal creates multiple databases at runtime and requires this privilege.

**Resolution:**

1. Check the portal logs for specific database errors:

```terminal
$ sudo journalctl -u portal -n 200 --no-pager | grep -i "permission\|CREATE\|database"
```

2. Connect to your external PostgreSQL server as a database administrator and verify the user privileges:

```terminal
$ psql -h *database-host* -U postgres -c "\du *database-user*"
```

     The output should show `Create DB` in the attributes column.

3. If the privilege is missing, grant it:

```sql
ALTER USER *database-user* CREATEDB;
```

4. Restart the Ansible automation portal service:

```terminal
$ sudo systemctl restart portal
```

### Built-in database ignored when external database is configured

**Symptom:** The cloud-init configuration specifies `database.type: builtin`, but the Ansible automation portal attempts to connect to an external database host instead of starting the built-in PostgreSQL.

**Cause:** In older appliance images, the `database.type` setting was ignored if `database.external.host` was also present in the cloud-init user-data. The external host value took precedence regardless of the `database.type` setting.

**Resolution:**

- Upgrade the appliance to the latest image, which resolves this issue.
- As a workaround on older images, remove the `database.external` section entirely from the cloud-init user-data when using the built-in database.

### Collect diagnostic information

If an issue persists, collect the following information before contacting support:

```terminal
$ sudo systemctl status portal postgres devtools > service-status.txt
$ sudo journalctl -u portal -n 200 > portal-logs.txt
$ sudo journalctl -u postgres -n 100 > postgres-logs.txt
$ sudo journalctl -u devtools -n 100 > devtools-logs.txt
$ sudo bootc status > bootc-status.txt
$ cat /etc/os-release > os-release.txt
```

### SSH key recovery

After initial configuration, the `admin` user account is locked and console login is disabled. If you lose SSH access, use one of the following recovery methods for your deployment environment.

Important:

Back up your SSH private key before configuring the appliance. If you lose your SSH key, you must use infrastructure-level access (hypervisor console, cloud provider tools) to recover.

### Recovery on Red Hat OpenShift Virtualization

1. Access the virtual machine console through the Red Hat OpenShift Container Platform web console.
2. Reboot the virtual machine.
3. At the GRUB boot menu, press **e** to edit boot parameters.
4. Add `init=/bin/bash` to the end of the kernel line.
5. Press **Ctrl+X** to boot into an emergency shell.
6. Remount the filesystem and add a new SSH key:

```terminal
mount -o remount,rw /
passwd -u admin
mkdir -p /home/admin/.ssh
echo "*your_ssh_public_key*" >> /home/admin/.ssh/authorized_keys
chown -R admin:admin /home/admin/.ssh
chmod 600 /home/admin/.ssh/authorized_keys
restorecon -R /home/admin/.ssh
passwd -l admin
exec /sbin/init
```

### Recovery on VMware vSphere

1. Open the virtual machine console in vCenter.
2. Reboot the virtual machine.
3. At the GRUB boot menu, press **e** to edit boot parameters.
4. Add `init=/bin/bash` to the end of the kernel line.
5. Press **Ctrl+X** to boot into an emergency shell.
6. Remount the filesystem and add a new SSH key:

```terminal
mount -o remount,rw /
passwd -u admin
mkdir -p /home/admin/.ssh
echo "*your_ssh_public_key*" >> /home/admin/.ssh/authorized_keys
chown -R admin:admin /home/admin/.ssh
chmod 600 /home/admin/.ssh/authorized_keys
restorecon -R /home/admin/.ssh
passwd -l admin
exec /sbin/init
```

### Recovery on KVM

Shut down the virtual machine and mount the QCOW2 image directly to add a new SSH key:

```terminal
$ sudo modprobe nbd max_part=8
$ sudo qemu-nbd --connect=/dev/nbd0 disk.qcow2
$ sudo fdisk -l /dev/nbd0
$ sudo mount /dev/nbd0p*N* /mnt
$ sudo mkdir -p /mnt/home/admin/.ssh
$ echo "*your_ssh_public_key*" | sudo tee -a /mnt/home/admin/.ssh/authorized_keys
$ sudo chown 1000:1000 /mnt/home/admin/.ssh/authorized_keys
$ sudo chmod 600 /mnt/home/admin/.ssh/authorized_keys
$ sudo umount /mnt
$ sudo qemu-nbd --disconnect /dev/nbd0
```

Where:

- `fdisk -l /dev/nbd0` lists partitions to identify the root filesystem. The root partition is typically the largest partition.
- Replace *N* in `/dev/nbd0p*N*` with the correct root partition number from the `fdisk` output.

### Account locking behavior

When the admin account is locked with `passwd -l`, the system adds a `!` prefix to the password hash in `/etc/shadow`. This disables all password-based authentication (console login, SSH password auth) while SSH key authentication continues to work.

To temporarily unlock the account for recovery, use `passwd -u admin`. After adding a new SSH key, lock the account again with `passwd -l admin` for security.

## Back up and restore data

Use the built-in backup tool to create and restore backups of the database, configuration, and SSL certificates for the Ansible automation portal RHEL appliance.

### About this task

Important:

Backups contain credentials in plain text. Restrict file permissions on backup archives. Encrypt archives before transferring to remote storage:

```terminal
$ gpg --symmetric --cipher-algo AES256 /var/lib/portal/backups/*backup-file*.tar.gz
```

### Procedure

Create a backup

1.  Run the backup tool:
  

```terminal
$ sudo ansible-portal backup
```

2.  Select a backup type from the menu. Select option 1 to create a backup with recommended defaults.
  

```
Portal Backup Tool
==================
1) Full backup (config + database + secrets) [recommended]
2) Config only (config + secrets, no database)
3) Database only

    Select backup type [1]: 1

    Creating backup...
  Backing up configuration... done
  Backing up secrets... done
  Backing up database... done

    Backup created: /var/lib/portal/backups/portal-backup-2026-05-07-143022.tar.gz
```

      Backups are stored in /var/lib/portal/backups/ as .tar.gz files.

Preview a backup

3.  Preview the contents of the most recent backup without restoring:
  

```terminal
$ sudo ansible-portal restore --latest --dry-run
```

Restore from backup

4.  Restore the most recent backup:
  

```terminal
$ sudo ansible-portal restore --latest
```

  

```
Portal Restore Tool
===================
Restoring from: /var/lib/portal/backups/portal-backup-2026-05-07-143022.tar.gz

    Stopping services...
  Restoring configuration... done
  Restoring secrets... done
  Restoring database... done
Starting services...

    Restore complete.
```

      Services stop during restore and restart automatically.
