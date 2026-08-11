+++
title = "Install Ansible automation portal on VMware vSphere - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_self_service_install_vmware"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_self_service_rhel_appliances/", "Deploy Ansible automation portal RHEL appliance"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_self_service_install_vmware/aem-page/install-proc_self_service_install_vmware.html"
last_crumb = "Install Ansible automation portal on VMware vSphere"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Install Ansible automation portal on VMware vSphere"
oversized = "false"
page_slug = "install-proc_self_service_install_vmware"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-proc_self_service_install_vmware"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_self_service_install_vmware/toc/toc.json"
type = "aem-page"
+++

# Install Ansible automation portal on VMware vSphere

Deploy the Ansible automation portal appliance on VMware vSphere.

## Prerequisites

- VMware vSphere/vCenter with permissions to create VMs and upload files to a datastore.
- The Ansible automation portal disk image in VMDK format, available from the Red Hat Ansible Automation Platform downloads page.
- Your `cloud-init` user-data and meta-data files prepared with Ansible Automation Platform credentials and SSH keys. See Prerequisites for deploying Ansible automation portal on RHEL in the related links below.
- An SSH key pair for appliance access.
- `genisoimage` installed on your local machine (for creating the cloud-init ISO).
- The `govc` CLI tool installed and configured with your vSphere credentials.

## Installing the appliance

1. Upload the VMDK disk image to a datastore using the `govc` CLI:

```terminal
$ govc import.vmdk disk.vmdk *<folder_name>*
```

  Note:
  The Ansible automation portal VMDK uses stream-optimized format and requires format conversion during upload. Do not upload VMDK disk images by using the vSphere web client or `govc datastore.upload` — these methods copy the file without converting it, producing an unusable 0 MB disk. The `govc import.vmdk` command converts the image automatically. This restriction applies to VMDK disk images only, not to ISO files.

2. Save your `cloud-init` user-data file as `cloud-init-user-data.yaml`. Use the template from Prerequisites for deploying Ansible automation portal on RHEL in the related links below.

3. Create a cloud-init ISO from your user-data file. VMware delivers cloud-init configuration to the VM as a small ISO disk image labeled `cidata`. Cloud-init expects two files on the ISO: `user-data` (your configuration) and `meta-data` (instance identity):

```terminal
$ cp cloud-init-user-data.yaml user-data
$ echo "instance-id: automation-portal" > meta-data
$ genisoimage -output cloud-init.iso -volid cidata -joliet -rock user-data meta-data
```

  Note:
  Cloud-init runs only once per instance ID. If you need to re-apply cloud-init configuration to an existing VM, change the `instance-id` value in the `meta-data` file to a new unique value (for example, `automation-portal-2`), regenerate the ISO, and reattach it before rebooting.

4. Upload the cloud-init ISO to the same datastore:

```terminal
$ govc datastore.upload cloud-init.iso *<folder_name>*/cloud-init.iso
```

5. Create a virtual machine:
  1. Right-click the cluster or host and select **New Virtual Machine** > **Create a new virtual machine**.
  2. Set the following example values. Replace the name, CPU, and memory to match your environment:
      | Field         | Example value                       |
      | ------------- | ----------------------------------- |
      | **Name**      | `automation-portal`                 |
      | **Guest OS**  | Red Hat Enterprise Linux 9 (64-bit) |
      | **CPU**       | 6 cores                             |
      | **Memory**    | 24 GB                               |
      | **Hard disk** | Remove the default disk             |
      | **Network**   | Select your VM network              |

  3. Click **Next** and then **Finish**.

6. Attach the VMDK disk and cloud-init ISO to the VM:
  1. Edit the VM settings.
  2. Click **Add New Device** > **Existing Hard Disk** and browse to the imported VMDK in the *<folder_name>* folder on the datastore.
  3. Click **Add New Device** > **CD/DVD Drive**. Select **Datastore ISO File** and browse to the cloud-init ISO.
  4. Select **Connect At Power On** for the CD/DVD drive.
  5. Save the VM settings.

7. Power on the VM. First-boot configuration takes 2-3 minutes.

**Verification**

- Open the VM console in vSphere or SSH into the VM and confirm that all services are running:

```terminal
$ sudo ansible-portal status
```

- Access the portal URL from your browser.

## Using VMware guestinfo properties

Use this method for VMware vSphere deployments as an alternative to the ISO method.

1. Base64-encode your cloud-init user-data file:

```terminal
$ base64 -w 0 user-data > user-data.b64
```

2. Create a metadata file with an instance ID and Base64-encode it:

```terminal
$ echo '{"instance-id": "automation-portal"}' > meta-data
$ base64 -w 0 meta-data > meta-data.b64
```

3. Set the following guestinfo properties on the virtual machine in vSphere:

```none
guestinfo.userdata = "*<contents-of-user-data.b64>*"
guestinfo.userdata.encoding = "base64"
guestinfo.metadata = "*<contents-of-meta-data.b64>*"
guestinfo.metadata.encoding = "base64"
```

     Set these properties using the vSphere web client (**Edit Settings** > **VM Options** > **Advanced** > **Configuration Parameters**).

4. Power on the virtual machine. Cloud-init reads the guestinfo properties and applies the configuration on first boot.

Note:

Cloud-init runs only once per instance ID. If you need to re-apply cloud-init configuration to an existing VM, change the `instance-id` value in the metadata, re-encode it, and update the `guestinfo.metadata` property before rebooting.

For additional native cloud-init configuration options, such as network configuration, see the cloud-init VMware datasource documentation in the related links below.
