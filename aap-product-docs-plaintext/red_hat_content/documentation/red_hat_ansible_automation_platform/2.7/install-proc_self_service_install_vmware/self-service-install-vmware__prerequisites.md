# Install Ansible automation portal on VMware vSphere
## Prerequisites

- VMware vSphere/vCenter with permissions to create VMs and upload files to a datastore.
- The Ansible automation portal disk image in VMDK format, available from the Red Hat Ansible Automation Platform downloads page.
- Your cloud-init user-data file prepared with Ansible Automation Platform credentials and SSH keys.
- An SSH key pair for appliance access.
- `genisoimage` installed on your local machine (for creating the cloud-init ISO).

