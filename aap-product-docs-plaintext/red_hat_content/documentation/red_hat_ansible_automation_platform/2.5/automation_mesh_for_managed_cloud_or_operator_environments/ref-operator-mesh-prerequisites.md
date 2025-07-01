# 2. Automation mesh for operator-based Red Hat Ansible Automation Platform
## 2.1. Prerequisites




The automation mesh is dependent on hop and execution nodes running on _Red Hat Enterprise Linux_ (RHEL). Your Red Hat Ansible Automation Platform subscription grants you ten Red Hat Enterprise Linux licenses that can be used for running components of Ansible Automation Platform.

For more information about Red Hat Enterprise Linux subscriptions, see [Registering the system and managing subscriptions](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_basic_system_settings/assembly_registering-the-system-and-managing-subscriptions_configuring-basic-system-settings) in the Red Hat Enterprise Linux documentation.

The following steps prepare the RHEL instances for deployment of the automation mesh.

1. You require a Red Hat Enterprise Linux operating system. Each node in the mesh requires a static IP address, or a resolvable DNS hostname that Ansible Automation Platform can access.
1. Ensure that you have the minimum requirements for the RHEL virtual machine before proceeding. For more information, see the [System requirements](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/planning_your_installation/platform-system-requirements) .
1. Deploy the RHEL instances within the remote networks where communication is required. For information about creating virtual machines, see [Creating Virtual Machines](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_and_managing_virtualization/assembly_creating-virtual-machines_configuring-and-managing-virtualization) in the _Red Hat Enterprise Linux_ documentation. Remember to scale the capacity of your virtual machines sufficiently so that your proposed tasks can run on them.


- RHEL ISOs can be obtained from access.redhat.com.
- RHEL cloud images can be built using Image Builder from console.redhat.com.



