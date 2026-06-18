# Access preconfigured development tools with Ansible development workspaces

Ansible development workspaces provide a fully supported browser-based development environment that includes Ansible development tools for creating and testing Ansible playbooks, roles, and collections. The workspaces run as containers within Red Hat OpenShift Dev Spaces.

## Introduction to Ansible development workspaces

Ansible development workspaces offer centralized management and policy enforcement, giving administrators better control and governance over secure, consistent automation development environments. Developers benefit by avoiding local application installs, especially in locked-down settings.

Ansible development tools and runtimes are pre-configured in Ansible development workspaces. Developers can start creating projects for automation content quickly by logging in to Ansible development workspaces in a browser.

The development tools in Ansible development workspaces are based on Ansible recommended practices, which improves the quality and reliability of your automation content. As a component of your Red Hat Ansible Automation Platform subscription, Ansible development workspaces are fully supported.

To ensure that your automation content files persist when you quit Ansible development workspaces, you push your projects to a Git repository that is linked to your workspace.

## Ansible development workspaces components

Each Ansible development workspace is a project-agnostic full development environment. Dependencies are satisfied for all the tools in the environment.

The following applications are pre-installed.

- Microsoft VS Code with the Ansible VS Code extension
- Python
- `ansible-core`
- `podman` for container-in-container operations, including building and running execution environments
- Ansible development tools (ADT) package, which includes:
* `ansible-builder` for building Ansible execution environments
* `ansible-creator` for scaffolding directory structure for your automation content
* `ansible-lint` for identifying stylistic errors and anti-patterns
* `ansible-navigator` for developing and troubleshooting Ansible content with execution environments
* `ansible-sign` for signing and verifying Ansible content
* `molecule` for running functional tests on your automation content
* `pytest-ansible` for testing Ansible module and plugin Python code
* `tox-ansible` for multi-version testing of Ansible module and plugin code
* `ansible-dev-environment` for building and managing isolated virtual workspaces

## Ansible dev spaces container image

Red Hat OpenShift Dev Spaces is a containerized cloud development environment (CDE) that provides pre-configured, consistent workspaces running on OpenShift Container Platform. It provisions ready-to-code workspaces on demand.

The Ansible dev spaces image is the container image for Ansible development workspaces. It is fully supported by Red Hat as part of your Ansible Automation Platform subscription.

The following diagram illustrates the relationship between OpenShift Container Platform, OpenShift Dev Spaces, and Ansible development workspaces.


![Ansible development workspaces topology](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/devtools-workspaces-architecture.png)
