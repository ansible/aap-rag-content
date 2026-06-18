# Troubleshooting RHEL appliances

Common issues and solutions for deploying and managing Ansible automation portal RHEL appliances.

## View logs and service status

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

## Portal services do not start

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

## OAuth login fails

**Symptom:** After clicking **Sign in with RHAAP**, the browser redirects back to the login page or Ansible Automation Platform returns "Invalid redirect_uri."

**Cause:** The OAuth redirect URI in Ansible Automation Platform does not match the Ansible automation portal user-accessible URL, or the `app.baseUrl`, `backend.baseUrl`, and `backend.cors.origin` values in the configuration file are not consistent with each other.

**Resolution:**

1. Check the current user-accessible URL and CORS configuration:

```terminal
$ grep -E 'baseUrl|origin' /etc/portal/configs/app-config/app-config.production.yaml
```

2. Verify that `app.baseUrl`, `backend.baseUrl`, and `backend.cors.origin` all use the same address.
3. Verify that the OAuth application redirect URI in Ansible Automation Platform matches the format `https://*portal-address*/api/auth/rhaap/handler/frame`.
4. If the values do not match, update either:
- The OAuth redirect URI in Ansible Automation Platform (if the Ansible automation portal address is correct), or
- The Ansible automation portal user-accessible URL and CORS origin in `app-config.production.yaml` (if the OAuth URI is correct).
5. Restart the Ansible automation portal service after any configuration change:

```terminal
$ sudo systemctl restart portal
```

## GitHub login appears instead of RHAAP

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

## Login fails with a 500 error

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

## Cannot SSH to the VM

**Symptom:** SSH connection refused or permission denied.

**Cause:** The appliance enforces SSH key-only authentication. Password login is disabled.

**Resolution:**

- Verify that your SSH private key matches the public key you provided in the cloud-init user-data.
- Verify that you are using the correct username from your cloud-init configuration.


If you have lost access to your SSH key, use platform-specific recovery:

- **KVM:** Access the VM console with `virsh console *vm-name*` and add a new SSH key.
- **Red Hat OpenShift Virtualization:** Access the VM console with `virtctl console *vm-name* -n *namespace*`.
- **VMware vSphere:** Use the vSphere console with `systemd.unit=rescue.target` boot parameter to add a new SSH key.

## VM is inaccessible

**Symptom:** The VM was deployed without cloud-init user-data. No SSH keys or Ansible Automation Platform credentials are configured.

**Cause:** The appliance has no default password. Without cloud-init configuration, the VM is not accessible.

**Resolution:** Redeploy the VM with a cloud-init configuration attached. See [Configure the appliance at first boot](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_self_service_initial_config_wizard "Provide initial configuration for the Ansible automation portal appliance so that portal services can start and connect to Ansible Automation Platform.").

## Red Hat OpenShift Virtualization issues

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

## VMware vSphere troubleshooting

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

## External database connection fails

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

## Database schema creation fails

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

## Built-in database ignored when external database is configured

**Symptom:** The cloud-init configuration specifies `database.type: builtin`, but the Ansible automation portal attempts to connect to an external database host instead of starting the built-in PostgreSQL.

**Cause:** In older appliance images, the `database.type` setting was ignored if `database.external.host` was also present in the cloud-init user-data. The external host value took precedence regardless of the `database.type` setting.

**Resolution:**

- Upgrade the appliance to the latest image, which resolves this issue.
- As a workaround on older images, remove the `database.external` section entirely from the cloud-init user-data when using the built-in database.

## Collect diagnostic information

If an issue persists, collect the following information before contacting support:

```terminal
$ sudo systemctl status portal postgres devtools > service-status.txt
$ sudo journalctl -u portal -n 200 > portal-logs.txt
$ sudo journalctl -u postgres -n 100 > postgres-logs.txt
$ sudo journalctl -u devtools -n 100 > devtools-logs.txt
$ sudo bootc status > bootc-status.txt
$ cat /etc/os-release > os-release.txt
```

## SSH key recovery

After initial configuration, the `admin` user account is locked and console login is disabled. If you lose SSH access, use one of the following recovery methods for your deployment environment.

Important:

Back up your SSH private key before configuring the appliance. If you lose your SSH key, you must use infrastructure-level access (hypervisor console, cloud provider tools) to recover.

## Recovery on Red Hat OpenShift Virtualization

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

## Recovery on VMware vSphere

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

## Recovery on KVM

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

## Account locking behavior

When the admin account is locked with `passwd -l`, the system adds a `!` prefix to the password hash in `/etc/shadow`. This disables all password-based authentication (console login, SSH password auth) while SSH key authentication continues to work.

To temporarily unlock the account for recovery, use `passwd -u admin`. After adding a new SSH key, lock the account again with `passwd -l admin` for security.
