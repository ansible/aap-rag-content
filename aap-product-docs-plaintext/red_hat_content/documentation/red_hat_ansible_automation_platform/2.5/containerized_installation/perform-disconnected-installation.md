# 8. Disconnected installation
## 8.2. Performing a disconnected installation




A disconnected installation installs containerized Ansible Automation Platform without requiring network access to external registries.

**Prerequisites**

- You have [prepared the Red Hat Enterprise Linux host](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/preparing-containerized-installation#preparing-the-rhel-host-for-containerized-installation)
- You have [obtained and configured the RPM source dependencies](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/aap-containerized-disconnected-installation#obtaining-and-configuring-rpm-dependencies) . The installation program uses your host system’s `    dnf` package manager to resolve these dependencies.
- You have [prepared the managed nodes](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/preparing-containerized-installation#preparing-the-managed-nodes-for-containerized-installation)
- You have downloaded the containerized Ansible Automation Platform setup bundle from the [Ansible Automation Platform download page](https://access.redhat.com/downloads/content/480/ver=2.5/rhel---9/2.5/x86_64/product-software) .


**Procedure**

1. Log in to the Red Hat Enterprise Linux host as your non-root user.
1. Update the inventory file by following the steps in [Configuring the inventory file](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/preparing-containerized-installation#configuring-inventory-file) .

Note
Do not include `    registry_username` or `    registry_password` in your inventory file for disconnected installations. These variables are only required for online installations. All container images are pre-packaged in the setup bundle.




1. Ensure you include the following variables in your inventory file under the `    [all:vars]` group:


```
bundle_install=true    # The bundle directory must include /bundle in the path    bundle_dir='{{ lookup("ansible.builtin.env", "PWD") }}/bundle'
```


1. Follow the steps in [Installing containerized Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/preparing-containerized-installation#installing-containerized-aap) to install containerized Ansible Automation Platform and verify your installation.


