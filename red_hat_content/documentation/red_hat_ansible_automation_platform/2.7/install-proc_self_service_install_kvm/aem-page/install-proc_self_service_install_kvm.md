+++
title = "Install Ansible automation portal on RHEL with KVM - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_self_service_install_kvm"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_self_service_rhel_appliances/", "Deploy Ansible automation portal RHEL appliance"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_self_service_install_kvm/aem-page/install-proc_self_service_install_kvm.html"
last_crumb = "Install Ansible automation portal on RHEL with KVM"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Install Ansible automation portal on RHEL with KVM"
oversized = "false"
page_slug = "install-proc_self_service_install_kvm"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-proc_self_service_install_kvm"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_self_service_install_kvm/toc/toc.json"
type = "aem-page"
+++

# Install Ansible automation portal on RHEL with KVM

Deploy the Ansible automation portal appliance on a RHEL 9 host with KVM using `virt-install`.

## Before you begin

- A RHEL 9 host with KVM support (Intel VT-x or AMD-V enabled).
- An SSH key pair on the host.
- The Ansible automation portal QCOW2 disk image.
- Minimum 24 GB available memory on the host.
- A completed cloud-init user-data file. See [Prerequisites for deploying Ansible automation portal on RHEL](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_self_service_rhel_prerequisites "Before you deploy an Ansible automation portal RHEL appliance, verify that your environment meets the system, network, and access requirements.").

## About this task

The following procedure provides example commands that you can adapt to your environment.

## Procedure

1.  Install the required packages and enable `libvirtd`.
  

```terminal
$ sudo dnf install -y qemu-kvm libvirt virt-install genisoimage
$ sudo systemctl enable --now libvirtd
```

2.  Verify that KVM is available.
  

```terminal
$ lsmod | grep kvm
```

3.  Ensure you have an SSH key pair to use in the cloud-init configuration.
      If you do not have one, generate a key pair:

```terminal
$ ssh-keygen -t ed25519 -N ""
```

4.  Set environment variables for your deployment.
      Replace the placeholder values. The examples in this procedure use `automation-portal` as the VM and project name. You can choose any name that suits your environment.

```terminal
$ export QCOW2_PATH="/path/to/portal-appliance.qcow2"
$ export VM_NAME="automation-portal"
$ export VM_MEMORY=24576
$ export VM_CPUS=6
$ export WORK_DIR="$HOME/portal-deploy"
$ export IMAGE_DIR="/var/lib/libvirt/images"
$ mkdir -p "$WORK_DIR"
```

5.  Save your cloud-init user-data file as $WORK_DIR/cloud-init-user-data.yaml.
6.  Create a cloud-init ISO from your user-data file.
      KVM delivers cloud-init configuration to the VM as a small ISO disk image labeled `cidata`. Cloud-init expects two files on the ISO: `user-data` (your configuration) and `meta-data` (instance identity).

```terminal
$ cd "$WORK_DIR"
$ cp cloud-init-user-data.yaml user-data
$ echo "instance-id: ${VM_NAME}" > meta-data
$ genisoimage -output cloud-init.iso -volid cidata -joliet -rock user-data meta-data
```

7.  Copy the disk image and create the VM.
  

```terminal
$ sudo cp "$QCOW2_PATH" "$IMAGE_DIR/${VM_NAME}.qcow2"
$ sudo virt-install \
  --name "$VM_NAME" \
  --memory "$VM_MEMORY" \
  --vcpus "$VM_CPUS" \
  --disk "$IMAGE_DIR/${VM_NAME}.qcow2" \
  --disk "$WORK_DIR/cloud-init.iso,device=cdrom" \
  --osinfo rhel9-unknown \
  --network default \
  --noautoconsole \
  --import
```

8.  Wait 1-3 minutes for first-boot configuration to complete, then retrieve the VM IP address.
  

```terminal
$ sudo virsh domifaddr "$VM_NAME"
```

## Results

SSH into the Ansible automation portal RHEL appliance and confirm that all services are running:

```terminal
$ ssh -i <private-key> <username>@<vm-ip>
$ sudo systemctl status portal postgres devtools
```
Example output for a healthy Ansible automation portal RHEL appliance:

```terminal
portal.service - Automation portal
     Active: active (running) since ...
postgres.service - PostgreSQL database
     Active: active (running) since ...
devtools.service - Ansible development tools
     Active: active (running) since ...
```
All three services should show `active (running)`.

## What to do next

Continue to [Connect and verify Ansible automation portal](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_self_service_connect_verify "After deploying the Ansible automation portal appliance, update the OAuth redirect URI, verify service health, and sign in to the portal.") to complete the post-installation steps.

## Remove the VM

Delete the VM and its storage after an evaluation.

### About this task

To delete the VM and its storage after an evaluation, run the following commands.

### Procedure

 Destroy the VM, remove its definition and storage, and clean up the working directory.

```terminal
$ sudo virsh destroy "$VM_NAME"
$ sudo virsh undefine "$VM_NAME" --remove-all-storage
$ rm -rf "$WORK_DIR"
```
