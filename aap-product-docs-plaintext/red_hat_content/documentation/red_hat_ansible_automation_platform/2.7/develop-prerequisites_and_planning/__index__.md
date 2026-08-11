# Prerequisites and planning

Before configuring execution environment builder, decide which Git provider your organization uses and understand the authentication method and security requirements for each capability.

## GitHub

| Capability                              | Authentication method                   | What it does                                                                     |
| --------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------- |
| Content discovery                       | GitHub App or PAT                       | Scans repositories for`galaxy.yml` files to populate the collection catalog      |
| Saving definition files to a repository | GitHub OAuth App                        | Creates EE definition files and saves them to a new repo or opens a pull request |
| Automated image builds                  | GitHub OAuth App + organization secrets | Builds a container image using GitHub Actions and pushes to a registry           |

## GitLab

| Capability                              | Authentication method                                | What it does                                                                      |
| --------------------------------------- | ---------------------------------------------------- | --------------------------------------------------------------------------------- |
| Content discovery                       | PAT                                                  | Scans groups for`galaxy.yml` files to populate the collection catalog             |
| Saving definition files to a repository | GitLab OAuth App                                     | Creates EE definition files and saves them to a new repo or opens a merge request |
| Automated image builds                  | GitLab OAuth App + group or subgroup CI/CD variables | Builds a container image using GitLab CI and pushes to a registry                 |

Important:

If a credential is created exclusively for content discovery, grant only read-only access, following the principle of least privilege. Content discovery requires only read permissions. Any write operation (saving definition files, creating repositories) goes through the OAuth flow.

## Security considerations

- **OpenShift deployments:** Store tokens and OAuth credentials in OpenShift secrets (`oc create secret generic`), never in plain text or version control.
- **RHEL appliance deployments:** Store tokens using Podman secrets (`podman secret create`).
- Use minimum required token permissions for your use case.
- Rotate PATs regularly according to your organization's security policy.
