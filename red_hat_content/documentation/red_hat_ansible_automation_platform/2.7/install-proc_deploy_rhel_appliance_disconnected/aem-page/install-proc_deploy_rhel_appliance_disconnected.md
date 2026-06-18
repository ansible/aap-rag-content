+++
template = "docs/aem-title.html"
title = "Deploy a RHEL appliance in a disconnected environment - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_deploy_rhel_appliance_disconnected"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_self_service_rhel_appliances/", "Deploy Ansible automation portal RHEL appliance"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_deploy_rhel_appliance_disconnected/aem-page/install-proc_deploy_rhel_appliance_disconnected.html"
last_crumb = "Deploy a RHEL appliance in a disconnected environment"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Deploy a RHEL appliance in a disconnected environment"
oversized = "false"
page_slug = "install-proc_deploy_rhel_appliance_disconnected"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-proc_deploy_rhel_appliance_disconnected"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_deploy_rhel_appliance_disconnected/toc/toc.json"
type = "aem-page"
+++

# Deploy a RHEL appliance in a disconnected environment

Deploy the Ansible automation portal RHEL appliance in a disconnected or air-gapped environment where the appliance has no access to external registries or the internet.

## Before you begin

- You have downloaded the appliance disk image (QCOW2 or VMDK) from the [Red Hat Ansible Automation Platform downloads page](https://access.redhat.com/downloads/content/480) on a connected system.
- You have a method to transfer the disk image to the disconnected environment (for example, removable media, secure file transfer, or an internal mirror registry).
- You have a virtualization platform available in the disconnected environment (Red Hat OpenShift Virtualization, VMware vSphere, or KVM).
- You have network connectivity from the appliance to your Ansible Automation Platform instance (internal network).
- You have Ansible Automation Platform credentials: host URL, API token, OAuth client ID, and OAuth client secret. See [Pre-installation configuration](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/html/installing_self-service_automation_portal/self-service-preinstall-config_aap-self-service-install) in the installation guide.
- You have an SSH key pair for appliance access.

## About this task

The appliance image includes everything needed to run without pulling content from external registries:

Pre-bundled Ansible plugins
Dynamic plugins are extracted at build time and stored at `/usr/share/portal/plugins/`. The appliance loads plugins from the local filesystem, not from a registry.

Pre-pulled container images
The Ansible automation portal and PostgreSQL container images are embedded in the appliance image. No container image pulls occur at runtime.

Self-signed SSL certificates
Generated locally at first boot. You can replace them with your own certificates after deployment.

No registry authentication required
The appliance starts and runs without registry credentials. Registry authentication is only needed for future upgrades.

## Procedure

Transfer the appliance image

1.  Transfer the disk image from a connected machine to your disconnected environment. Choose the method that fits your network topology.
      **Removable media:** Copy the disk image directly to the disconnected host using removable media (USB drive, portable storage) or a secure file transfer mechanism.

  1. On a connected machine, download the QCOW2 or VMDK disk image from the [Red Hat Ansible Automation Platform downloads page](https://access.redhat.com/downloads/content/480).
  2. Copy the disk image to removable media.
  3. Transfer the media to the disconnected environment and copy the image to the target host. For example, for a KVM deployment:

```terminal
$ rsync --progress /media/usb/portal-appliance.qcow2 /var/lib/libvirt/images/portal-appliance.qcow2
```

    **Internal mirror registry:** If your disconnected environment has an internal container registry, you can copy the bootc container image to your mirror and build disk images from it.

  1. On a connected machine, copy the bootc container image to your internal registry:

```terminal
$ skopeo copy \
  docker://registry.redhat.io/ansible-automation-platform/bootc-automation-portal-rhel9:<version> \
  docker://mirror.internal.example.com:5000/ansible-automation-platform/bootc-automation-portal-rhel9:<version>
```

  2. If your mirror registry uses a self-signed certificate, add the CA certificate to the system trust store on the machine where you will build the disk image:

```terminal
$ sudo cp ca.crt /etc/pki/ca-trust/source/anchors/
$ sudo update-ca-trust
```

  3. Build the disk image from the mirror registry in your disconnected environment. Refer to the Red Hat documentation for building bootc disk images from a custom registry source.
  4. Deploy the resulting disk image using the standard installation procedure for your platform.

Deploy the appliance

2.  Deploy the appliance on your virtualization platform following the standard deployment procedure for your environment:

  - For RHEL with KVM, see [Install Ansible automation portal on RHEL with KVM](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_self_service_install_kvm "Deploy the Ansible automation portal appliance on a RHEL 9 host with KVM using virt-install.").
  - For Red Hat OpenShift Virtualization, see [Install Ansible automation portal on Red Hat OpenShift Virtualization](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_self_service_install_openshift_virt "Deploy the Ansible automation portal appliance on Red Hat OpenShift Virtualization to run the portal as a virtual machine alongside container workloads within your Red Hat OpenShift Container Platform cluster.").
  - For VMware vSphere, see [Install Ansible automation portal on VMware vSphere](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_self_service_install_vmware "Deploy the Ansible automation portal appliance on VMware vSphere using the vSphere web client.").

Configure the appliance

3.  Provide initial configuration through cloud-init, VMware `guestinfo` properties, or a pre-seeded configuration file.
      The cloud-init configuration for a disconnected deployment is the same as a connected deployment. Use the templates from [Configure the appliance at first boot](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_self_service_initial_config_wizard "Provide initial configuration for the Ansible automation portal appliance so that portal services can start and connect to Ansible Automation Platform.").

    The following differences apply in a disconnected environment:

  - **Source control integrations require network access.** The `integrations.github` and `integrations.gitlab` cloud-init fields require network access to the source control service. If your disconnected environment has internal GitHub Enterprise or GitLab instances, configure these fields with the internal hostnames.
  - **Set `network.base_url` to match your internal DNS or IP.** Set `network.base_url` to the hostname or IP address that users will use to access the Ansible automation portal RHEL appliance on your internal network. If omitted, the appliance auto-detects the VM IP address.
    Minimal cloud-init template for disconnected deployment:

```yaml
#cloud-config

    users:
  - name: <username>
    sudo: ALL=(ALL) NOPASSWD:ALL
    ssh_authorized_keys:
      - "<your-ssh-public-key>"

    aap:
  host_url: "https://<internal-aap-host>"
  token: "<aap-api-token>"
  oauth:
    client_id: "<oauth-client-id>"
    client_secret: "<oauth-client-secret>"

    database:
  type: builtin
  builtin:
    password: "auto"
    admin_password: "auto"
```

Verify the installation

4.  SSH into the Ansible automation portal RHEL appliance:
  

```terminal
$ ssh <username>@<appliance-ip>
```

5.  Check that all three services are running:
  

```terminal
$ sudo systemctl status portal postgres devtools
```
    All three services (portal, postgres, devtools) should show `active (running)`.

    Alternatively, use the portal management CLI for detailed diagnostics:

```terminal
$ sudo ansible-portal status
```

6.  Verify that the Ansible automation portal is accessible:
  

```terminal
$ curl -fk https://<appliance-address>
```

7.  Verify that Ansible plugins loaded from the local filesystem:
  

```terminal
$ sudo podman exec portal ls /opt/app-root/src/dynamic-plugins-root/
```
    You should see plugin directories listed. These plugins were loaded from the pre-baked files at `/usr/share/portal/plugins/`, not from a registry.

Set up registry credentials for upgrades (optional)

8.  If you plan to upgrade the appliance using `bootc upgrade` from `registry.redhat.io` or a mirror registry, log in to the container registry and save the credentials:
  

```terminal
$ sudo podman login --authfile /etc/ostree/auth.json registry.redhat.io
```
    The `/etc/ostree/auth.json` file is what `bootc upgrade` and `bootc switch` use for registry authentication.

    If no registry is available for image upgrades, you can bypass the registry authentication gate:

```terminal
$ sudo touch /etc/portal/.registry-auth-override
```
    This override marker allows the appliance to start without registry credentials. It is preserved across backups, restores, and bootc upgrades.

## Results

- Verify that the portal URL is accessible from your browser.
- Verify that all services show a healthy status.

## What to do next

For appliance upgrades in disconnected environments, see [Upgrade the appliance in a disconnected environment](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_self_service_rhel_upgrade_disconnected "In disconnected environments, you can upgrade the Ansible automation portal RHEL appliance using a mirror registry. Configure the mirror registry so that bootc upgrade pulls images from your internal registry instead of registry.redhat.io.").
