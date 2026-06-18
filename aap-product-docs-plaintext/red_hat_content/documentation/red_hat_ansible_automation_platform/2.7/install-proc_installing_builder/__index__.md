# Install Ansible Builder to create or edit execution environments

Install Ansible Builder to create custom execution environments that contain the dependencies and collections required for your automation content. You need a valid Red Hat subscription and Podman installed on your RHEL system.

## Before you begin

- You have installed the Podman container runtime.
- You have valid subscriptions attached on the host. With a valid subscription you can access the subscription-only resources needed to install `ansible-builder`, and ensures that the necessary repository for `ansible-builder` is automatically enabled. See [Attaching your Red Hat Ansible Automation Platform subscription](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_attaching_subscriptions_1 "You must have valid subscriptions on all nodes before installing Red Hat Ansible Automation Platform.") for more information. Note:
To install the developer tools without consuming a managed node subscription, you can use MCT4589-Red Hat Ansible Developer, Standard (10 Managed Nodes), which is available at no cost. This subscription requires the approval of the Ansible Business Unit.

## Procedure

Run the following command to install Ansible Builder and activate your Ansible Automation Platform repo:

```
#  dnf install --enablerepo=ansible-automation-platform-*aap-version*-for-rhel-*rhel-version*-x86_64-rpms
ansible-builder
```
Replace *aap-version* with your Ansible Automation Platform version and *rhel-version* with your Red Hat Enterprise Linux major version.
