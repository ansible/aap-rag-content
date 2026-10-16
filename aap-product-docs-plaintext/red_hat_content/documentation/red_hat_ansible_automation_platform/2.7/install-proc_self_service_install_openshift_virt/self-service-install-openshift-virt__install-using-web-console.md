# Install Ansible automation portal on Red Hat OpenShift Virtualization
## Install using the OpenShift web console

You can also deploy the appliance from the OpenShift web console without using the CLI.

**Prerequisites**

- Red Hat OpenShift Container Platform with the Red Hat OpenShift Virtualization operator installed and configured.
- Cluster administrator or equivalent permissions.
- The Ansible automation portal QCOW2 disk image available on your local machine.
- Ansible Automation Platform credentials (host URL, OAuth client ID and secret, and API token) and an SSH key pair. The meta-data file is not required for this platform.

**Procedure**

1. Go to **Storage** > **PersistentVolumeClaims**.
2. Create a PVC using **Data upload form**. Upload the QCOW2 image. Set the size to at least 50 Gi.
3. Go to **Workloads** > **Secrets**. Create a Key or Value secret with a key named `userdata`. Paste the following cloud-init user-data contents as the value, replacing the placeholder values with your credentials:

```yaml
#cloud-config
users:
- name: admin
sudo: ALL=(ALL) NOPASSWD:ALL
ssh_authorized_keys:
- "<your-ssh-public-key>"

aap:
host_url: "https://<aap-host>"
token: "<aap-api-token>"
check_ssl: true
oauth:
client_id: "<oauth-client-id>"
client_secret: "<oauth-client-secret>"

database:
type: builtin
```

4. Go to **Virtualization** > **VirtualMachines**. Click **Create VirtualMachine** > **From YAML**. Apply the manifest from the CLI procedure.
5. Wait for the VM status to change to **Running**.
6. Go to **Networking** > **Services**. Create a service targeting port 443 on the VM.
7. Go to **Networking** > **Routes**. Create a passthrough TLS route for the service. Note the route hostname.
8. SSH into the VM. Set `app.baseUrl`, `backend.baseUrl`, and `backend.cors.origin` to `https://<route-hostname>`.
9. Restart the portal service:

```terminal
$ sudo systemctl restart portal
```

**Verification**

- SSH into the VM and confirm that all services are running:

```terminal
$ sudo ansible-portal status
```

- Access the portal URL from your browser.

If you encounter upload, boot, or scheduling failures, see Troubleshooting RHEL appliances.
