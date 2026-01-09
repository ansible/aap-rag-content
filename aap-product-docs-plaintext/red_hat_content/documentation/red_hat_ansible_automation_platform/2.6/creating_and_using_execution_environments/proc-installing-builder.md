# 2. Using Ansible Builder
## 2.2. Installing Ansible Builder




Install Ansible Builder to create custom execution environments that contain the dependencies and collections required for your automation content. You need a valid Red Hat subscription and Podman installed on your RHEL system.

**Prerequisites**

- You have valid subscriptions attached on the host. With a valid subscription you can access the subscription-only resources needed to install ansible-builder, and ensures that the necessary repository for ansible-builder is automatically enabled. See Attaching your Red Hat Ansible Automation Platform subscription for more information.
- You have installed the Podman container runtime.
- You have valid subscriptions attached on the host. With a subscription so you can access the subscription-only resources needed to install `    ansible-builder` , and ensures that the necessary repository for `    ansible-builder` is automatically enabled. See [Attaching your Red Hat Ansible Automation Platform subscription](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/assembly-gateway-licensing#proc-attaching-subscriptions) for more information.

Note
To install the developer tools without consuming a valid Red Hat Ansible Automation Platform managed node subscription you can use MCT4589-Red Hat Ansible Developer, Standard (10 Managed Nodes), which is free. This subscription is for enabling users of Ansible Automation Platform. This subscription requires the approval of Ansible Business Unit.






**Procedure**

- Run the following command to install Ansible Builder and activate your Ansible Automation Platform repo:

Note
If you are running on RHEL 10, modify the command to reflect RHEL 10.




```
#  dnf install --enablerepo=ansible-automation-platform-2.6-for-rhel-9-x86_64-rpms ansible-builder
```




