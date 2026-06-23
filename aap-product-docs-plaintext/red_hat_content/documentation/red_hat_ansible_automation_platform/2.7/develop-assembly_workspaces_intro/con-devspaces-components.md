# Access preconfigured development tools with Ansible development workspaces
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

