# 5. Decision environments
## 5.1. Installing ansible-builder




To build images, install `ansible-builder` Python package (along with Podman or Docker) to build the custom decision environments required for rulebooks.

The `--container-runtime` option must correspond to the Podman or Docker executable you intend to use.

When building a decision environment image, it must support the architecture that Ansible Automation Platform is deployed with.

For more information, see [Quickstart for Ansible Builder](https://ansible.readthedocs.io/projects/builder/en/latest/#quickstart-for-ansible-builder) or [Creating and using execution environments](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/creating_and_using_execution_environments) .

