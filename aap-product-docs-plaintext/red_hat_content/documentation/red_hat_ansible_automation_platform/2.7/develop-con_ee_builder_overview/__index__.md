# Understand execution environment builder

Execution environment builder enables your teams to discover Ansible collections, create EE definitions, and build container images through Ansible automation portal.

## How it works

Execution environment builder connects to your Git provider and private automation hub to accomplish three tasks:

- **Content discovery** — scans Git repositories and private automation hub for Ansible collections (`galaxy.yml` files). Populates the collection catalog that users browse when building an EE definition.
- **Saving EE definition files to a repository** — creates a set of definition files and saves them to a Git repository (new repo or pull request) on behalf of users via OAuth.
- **Automated image builds** — triggers a CI/CD pipeline (GitHub Actions) to produce a container image from the saved definition files.

## Configuration file

| Platform       | Configuration file                                          | Apply changes                                       |
| -------------- | ----------------------------------------------------------- | --------------------------------------------------- |
| OpenShift      | Helm chart values file                                      | `helm upgrade`                                      |
| RHEL appliance | `/etc/portal/configs/app-config/app-config.production.yaml` | See *Apply configuration changes* in Related links. |

## Secrets

Sensitive values such as Git provider tokens, OAuth client secrets, and registry credentials are stored separately from the configuration file.

- **OpenShift deployments:** Store secrets with `oc create secret generic`. Reference the secret name in your Helm chart values.
- **RHEL appliance deployments:** Store secrets with `podman secret create` using the `portal_` prefix naming convention (for example, `portal_github_oauth_client_id`). Create a Quadlet drop-in file to map each secret to a container environment variable. For more information on referencing secrets in your service configuration, see the Configuring the automation portal RHEL appliance guide.


Important:

The `portal-backup` utility does not currently capture EE Builder secrets or custom Quadlet drop-in files. After configuring EE Builder secrets, store the secret values and the contents of `ee-builder-secrets.conf` in a secure external location (for example, a vault or password manager). After a `portal-restore`, you must recreate the Podman secrets and the drop-in file manually.

Note:

If you host execution environment wizard templates in a private Git repository or deploy in an air-gapped environment, complete the steps in Host execution environment wizard templates in a private Git repository before configuring discovery sources.

## Prerequisites

Before configuring execution environment builder, decide which Git provider your organization uses and understand the authentication method for each capability.

## GitHub

| Capability                              | Authentication method                                 | What it does                                                                     |
| --------------------------------------- | ----------------------------------------------------- | -------------------------------------------------------------------------------- |
| Content discovery                       | GitHub App or PAT                                     | Scans repositories for`galaxy.yml` files to populate the collection catalog      |
| Saving definition files to a repository | GitHub OAuth App                                      | Creates EE definition files and saves them to a new repo or opens a pull request |
| Automated image builds                  | GitHub OAuth App + repository or organization secrets | Builds a container image using GitHub Actions and pushes to a registry           |

## GitLab

| Capability                              | Authentication method | What it does                                                                      |
| --------------------------------------- | --------------------- | --------------------------------------------------------------------------------- |
| Content discovery                       | PAT                   | Scans groups for`galaxy.yml` files to populate the collection catalog             |
| Saving definition files to a repository | GitLab OAuth App      | Creates EE definition files and saves them to a new repo or opens a merge request |


Important:

Content discovery credentials (GitHub App or PAT) provide read-only access only. Any write operation (saving definition files, creating repositories) goes through the OAuth flow.

## Security considerations

- **OpenShift deployments:** Store tokens and OAuth credentials in OpenShift secrets (`oc create secret generic`), never in plain text or version control.
- **RHEL appliance deployments:** Store tokens using Podman secrets (`podman secret create`).
- Use minimum required token permissions for your use case.
- Rotate PATs regularly according to your organization's security policy.
