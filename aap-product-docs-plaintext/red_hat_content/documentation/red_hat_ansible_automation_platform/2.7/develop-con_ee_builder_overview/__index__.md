# Understand execution environment builder

Execution environment builder enables your teams to discover Ansible collections, create EE definitions, and build container images through Ansible automation portal.

## How it works

Execution environment builder connects to your Git provider and private automation hub to accomplish three tasks:

- **Content discovery** — scans Git repositories and private automation hub for Ansible collections (`galaxy.yml` files). Populates the collection catalog that users browse when building an EE definition.
- **Saving EE definition files to a repository** — creates a set of definition files and saves them to a Git repository (new repo or pull request) on the user's behalf, using OAuth to authenticate with their Git provider.
- **Automated image builds** — triggers a CI/CD pipeline (GitHub Actions or GitLab CI) to produce a container image from the saved definition files.

## Configuration file

| Platform       | Configuration file                                          | Apply changes                                      |
| -------------- | ----------------------------------------------------------- | -------------------------------------------------- |
| OpenShift      | Helm chart values file                                      | `helm upgrade`                                     |
| RHEL appliance | `/etc/portal/configs/app-config/app-config.production.yaml` | See*Apply configuration changes* in Related links. |

## Secrets

Sensitive values such as Git provider tokens, OAuth client secrets, and registry credentials are stored separately from the configuration file.

- **OpenShift deployments:** Store secrets with `oc create secret generic`. Reference the secret name in your Helm chart values.
- **RHEL appliance deployments:** Store secrets with `podman secret create` using the `portal_` prefix naming convention (for example, `portal_github_oauth_client_id`). The portal automatically injects any `portal_`-prefixed Podman secret into the container as an environment variable. Restart the portal service after creating secrets.

For automated image builds, configure organization secrets (GitHub) or group CI/CD variables (GitLab) in your Git provider. For details, see Connect to GitHub or Connect to GitLab in Related links.

Note:

If you host execution environment wizard templates in a private Git repository or deploy in an air-gapped environment, complete the steps in Host execution environment wizard templates in a private Git repository before configuring discovery sources.
