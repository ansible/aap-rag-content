+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_self_service_install_vmware"
title = "Install Ansible automation portal on VMware vSphere - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_self_service_rhel_appliances/", "Deploy Ansible automation portal RHEL appliance"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_self_service_install_vmware/aem-page/install-proc_self_service_install_vmware.html"
last_crumb = "Install Ansible automation portal on VMware vSphere"
modified = "2026-06-05T07:48:10.594Z"
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

Deploy the Ansible automation portal appliance on VMware vSphere using the vSphere web client.

## Prerequisites

- VMware vSphere/vCenter with permissions to create VMs and upload files to a datastore.
- The Ansible automation portal disk image in VMDK format, available from the Red Hat Ansible Automation Platform downloads page.
- Your cloud-init user-data file prepared with Ansible Automation Platform credentials and SSH keys.
- An SSH key pair for appliance access.
- `genisoimage` installed on your local machine (for creating the cloud-init ISO).

## Install using the vSphere web client

1. Upload the VMDK disk image to a datastore:
  1. Open the vCenter web client.
  2. Navigate to **Storage** > **Datastores** and select your datastore.
  3. Click **Upload Files** and upload the Ansible automation portal VMDK file.

2. Save your cloud-init user-data file as `cloud-init-user-data.yaml`. Use the cloud-init template from the first boot configuration topic.

3. Create a cloud-init ISO from your user-data file. VMware delivers cloud-init configuration to the VM as a small ISO disk image labeled `cidata`. Cloud-init expects two files on the ISO: `user-data` (your configuration) and `meta-data` (instance identity):



```terminal
$ cp cloud-init-user-data.yaml user-data
$ echo "instance-id: automation-portal" > meta-data
$ genisoimage -output cloud-init.iso -volid cidata -joliet -rock user-data meta-data
```

4. Upload the cloud-init ISO to the same datastore.

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
  1. Copy the uploaded VMDK and cloud-init ISO to the VM folder on the datastore.
  2. Edit the VM settings.
  3. Click **Add New Device** > **Existing Hard Disk** and browse to the copied VMDK.
  4. Click **Add New Device** > **CD/DVD Drive**. Select **Datastore ISO File** and browse to the copied cloud-init ISO.
  5. Select **Connect At Power On** for the CD/DVD drive.
  6. Save the VM settings.

7. Power on the VM. First-boot configuration takes 2-3 minutes.

**Verification**

- Open the VM console in vSphere or SSH into the VM and confirm that all services are running:

```terminal
$ sudo systemctl status portal postgres devtools
```

- Access the portal URL from your browser.
