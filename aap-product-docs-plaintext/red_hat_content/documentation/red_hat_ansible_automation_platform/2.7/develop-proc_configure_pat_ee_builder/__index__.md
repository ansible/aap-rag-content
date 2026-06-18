# Configure a Personal Access Token for GitHub content discovery

Create and store a GitHub Personal Access Token (PAT) so that execution environment builder can scan repositories for Ansible collections.

## Before you begin

- You have a GitHub account with access to the repositories automation portal needs to scan.

## About this task

PATs provide a simpler setup with user-scoped access. If you are already using PATs for automation portal, you can continue using them. Choose this option or a GitHub App for content discovery. GitHub App and PAT are mutually exclusive.

## Procedure

1.  Create a GitHub PAT with the following scopes:

- `repo`
- `read:org`
- `workflow` (required for the CI activity tab to display workflow run status)

2.  Store the PAT.
**OpenShift — CLI:**

```
$ oc create secret generic secrets-scm \
--from-literal=github-token=<your_github_pat> \
-n <namespace>
```
**OpenShift — web console:**

1. Navigate to **Workloads > Secrets > Create > Key/value secret**.
2. Set the name to `secrets-scm`.
3. Add key `github-token` with your PAT value.
**RHEL appliance:**

```
$ echo -n '<your_github_pat>' | sudo podman secret create portal_github_token -
```
Note:
If you configured a GitHub personal access token during RHEL appliance installation (via cloud-init), the `portal_github_token` secret already exists and is active for content discovery. Running the command above updates the existing secret with a new value.

## Results

Note:

If you already have PAT-based GitHub integration configured from a previous AAP release, those instructions remain valid. This guide documents both authentication methods.
