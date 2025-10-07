# 3. Disconnected installation
## 3.2. Performing a disconnected installation




Use the following steps to perform a disconnected installation of containerized Ansible Automation Platform.

**Prerequisites**

You have done the following:


-  [Prepared the Red Hat Enterprise Linux host](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/aap-containerized-installation#preparing-the-rhel-host-for-containerized-installation)
-  [Obtained and configured the RPM source dependencies](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/aap-containerized-disconnected-installation#obtaining-and-configuring-rpm-dependencies) . The installation program uses your host system’s `    dnf` package manager to resolve these dependencies.
-  [Prepared the managed nodes](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/aap-containerized-installation#preparing-the-managed-nodes-for-containerized-installation)
- Downloaded the containerized Ansible Automation Platform setup bundle from the [Ansible Automation Platform download page](https://access.redhat.com/downloads/content/480/ver=2.5/rhel---9/2.5/x86_64/product-software) .


**Procedure**

1. Log in to the Red Hat Enterprise Linux host as your non-root user.
1. Update the inventory file by following the steps in [Configuring the inventory file](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/aap-containerized-installation#configuring-inventory-file) .
1. Ensure the following variables are included in your inventory file under the `    [all:vars]` group:


```
bundle_install=true    # The bundle directory must include /bundle in the path    bundle_dir='{{ lookup("ansible.builtin.env", "PWD") }}/bundle'
```


1. Follow the steps in [Installing containerized Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/aap-containerized-installation#installing-containerized-aap) to install containerized Ansible Automation Platform and verify your installation.


