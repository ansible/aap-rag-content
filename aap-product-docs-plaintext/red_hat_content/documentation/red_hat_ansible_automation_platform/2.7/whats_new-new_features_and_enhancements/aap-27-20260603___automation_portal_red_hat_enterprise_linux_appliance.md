# New features and enhancements
## Automation portal Red Hat Enterprise Linux appliance

Ansible automation portal is now available as a pre-built RHEL 9 virtual machine appliance. The appliance packages automation portal as a QCOW2 or VMDK disk image that you deploy on your existing virtualization infrastructure.

- Key capabilities include:
* Multi-platform deployment: Deploy on RHEL with KVM, Red Hat OpenShift Virtualization, or VMware vSphere.
* Automated first-boot configuration: Provide SSH keys and AAP OAuth credentials in a cloud-init user-data file. The appliance configures itself on first boot with no manual steps.
* Atomic upgrades and rollback: Built on RHEL 9 image mode (bootc). Upgrade the appliance atomically while preserving configuration and data, and roll back to the previous version if needed.


For more information, see the Ansible automation portal documentation.

