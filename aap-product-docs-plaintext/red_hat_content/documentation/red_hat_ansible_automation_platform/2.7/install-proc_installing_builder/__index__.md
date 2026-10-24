# Install Ansible Builder to create or edit execution environments

Ansible Builder is included in the Ansible development tools package, but you can also install it standalone if you only need to create or manage execution environments. Builder creates custom execution environments that contain the dependencies and collections required for your automation content.

## Before you begin

- You have installed the Podman container runtime.
- You have valid subscriptions attached on the host. With a valid subscription you can access the subscription-only resources needed to install `ansible-builder`, and ensures that the necessary repository for `ansible-builder` is automatically enabled. See [Register your Red Hat Enterprise Linux hosts](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_attaching_subscriptions "You must register all nodes with Red Hat Subscription Management (RHSM) before installing Ansible Automation Platform.") for more information. Note:
To install the developer tools without consuming a managed node subscription, you can use MCT4589-Red Hat Ansible Developer, Standard (10 Managed Nodes), which is available at no cost. This subscription requires the approval of the Ansible Business Unit.

## Procedure

Run the following command to install Ansible Builder and activate your Ansible Automation Platform repo:

```
#  dnf install --enablerepo=ansible-automation-platform-*aap-version*-for-rhel-*rhel-version*-x86_64-rpms
ansible-builder
```

Replace *aap-version* with your Ansible Automation Platform version and *rhel-version* with your Red Hat Enterprise Linux major version.
