# 3. Using Ansible Builder
## 3.2. Installing Ansible Builder




**Prerequisites**

- You have valid subscriptions attached on the host. Doing so enables you to access the subscription-only resources needed to install ansible-builder, and ensures that the necessary repository for ansible-builder is automatically enabled. See Attaching your Red Hat Ansible Automation Platform subscription for more information.
- You have installed the Podman container runtime.
- You have valid subscriptions attached on the host. Doing so allows you to access the subscription-only resources needed to install `    ansible-builder` , and ensures that the necessary repository for `    ansible-builder` is automatically enabled. See [Attaching your Red Hat Ansible Automation Platform subscription](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication/assembly-gateway-licensing#proc-attaching-subscriptions) for more information.

Note
To install the developer tools without consuming a valid Red Hat Ansible Automation Platform managed node entitlement you can use MCT4589–Red Hat Ansible Developer, Standard (10 Managed Nodes), which is free. This subscription is for enabling users of Ansible Automation Platform. This subscription requires the approval of Ansible Business Unit.






**Procedure**

- Run the following command to install Ansible Builder and activate your Ansible Automation Platform repo:


```
#  dnf install --enablerepo=ansible-automation-platform-2.5-for-rhel-9-x86_64-rpms ansible-builder
```




