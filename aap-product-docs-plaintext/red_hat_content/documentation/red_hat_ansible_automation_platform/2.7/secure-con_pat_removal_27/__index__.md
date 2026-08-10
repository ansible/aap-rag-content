# Personal Access Token removal in Ansible Automation Platform 2.7

In Ansible Automation Platform 2.7, component-level Personal Access Tokens (PATs) have been removed. Tokens created directly in automation controller, automation hub, or Event-Driven Ansible controller in Ansible Automation Platform 2.6 or earlier no longer work in Ansible Automation Platform 2.7.

All tokens must now be created and managed through platform gateway.

## Token migration timeline

- **Ansible Automation Platform 2.5:** Platform gateway introduced; component-level PATs deprecated.
- **Ansible Automation Platform 2.6:** PAT migration from components to platform gateway supported; component-level PATs still functional.
- **Ansible Automation Platform 2.7:** Component-level PATs removed; only platform gateway tokens supported.

Important:

The Automation Hub API token is intended only for authenticating with the `ansible-galaxy` CLI for collection operations (sync, install, publish). It is not supported for container registry operations such as `podman login` or `podman pull` of Execution Environment images. For execution environment image operations, use your username and password.

