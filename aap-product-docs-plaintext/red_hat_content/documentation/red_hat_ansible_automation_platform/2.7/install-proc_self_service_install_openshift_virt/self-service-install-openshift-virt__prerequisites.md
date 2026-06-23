# Install Ansible automation portal on Red Hat OpenShift Virtualization
## Prerequisites

- Red Hat OpenShift Container Platform cluster (4.x) with Red Hat OpenShift Virtualization operator installed and configured.
- Cluster administrator or equivalent permissions to create VirtualMachine resources.
- A storage class configured that supports ReadWriteOnce (RWO) access mode for virtual machine disks.
- The Ansible automation portal disk image in QCOW2 format.
- The `virtctl` CLI tool installed. You can download it from the OpenShift web console under **Virtualization** > **Overview** > **Download virtctl**.
- Access to the OpenShift web console or `oc` CLI tool.
- Your cloud-init user-data file prepared with Ansible Automation Platform credentials and SSH keys.
- Sufficient cluster resources: minimum 16 GiB allocatable memory for the virtual machine.

