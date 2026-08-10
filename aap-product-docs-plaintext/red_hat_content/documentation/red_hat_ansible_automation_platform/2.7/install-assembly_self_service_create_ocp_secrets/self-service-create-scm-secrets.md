# Create secrets in OpenShift for Ansible automation portal
## Create GitHub and GitLab secrets

Create an OpenShift secret to hold Personal Access Tokens for your external Source Control Management systems, such as GitHub or GitLab. This helps securely manage access credentials.

### Before you begin

- You have logged in to your OpenShift Container Platform cluster.
- You have access to the OpenShift project where you will install Ansible automation portal.

### About this task

This procedure establishes the required `secrets-scm` Key/Value secret within your OpenShift Container Platform project to securely store the GitHub and/or GitLab Personal Access Tokens (PATs).

Create the `secrets-scm` secret using the `oc` CLI or the OpenShift web console. If you use only one SCM provider, include only that provider's token.

Note:

The secret must use the exact name `secrets-scm` with the exact key names specified below.

If you plan to use the execution environment builder to save definitions to a Git repository, this secret also holds OAuth App or GitHub App credentials. You add those credentials later when setting up the EE Builder. See [Configure a GitHub OAuth App for saving definitions](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_configure_github_oauth_ee_builder "Configure a GitHub OAuth App so that users can save execution environment definition files to a GitHub repository and trigger automated image builds.") or [Configure a GitHub App for content discovery](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_configure_github_app_ee_builder "Create and install a GitHub App so that execution environment builder can scan your organization's repositories for Ansible collections.").

### Procedure

Run the appropriate command to create the secret.

To create the secret with both GitHub and GitLab tokens:

```
$ oc create secret generic secrets-scm \
--from-literal=github-token="<github_pat>" \
--from-literal=gitlab-token="<gitlab_pat>" \
-n <project_name>
```

To create the secret with only a GitHub token:

```
$ oc create secret generic secrets-scm \
--from-literal=github-token="<github_pat>" \
-n <project_name>
```

To create the secret with only a GitLab token:

```
$ oc create secret generic secrets-scm \
--from-literal=gitlab-token="<gitlab_pat>" \
-n <project_name>
```

### Results

**OpenShift web console**

You can also create the `secrets-scm` secret in the OpenShift web console.

1. In the Administrator view, click Workloads> (and then)Secrets.
2. Click Create> (and then)Key/value secret.
3. Set the secret name to `secrets-scm`.
4. Add key-value pairs for your SCM providers:
- Key: `github-token`, Value: GitHub Personal Access Token (PAT)
- Key: `gitlab-token`, Value: GitLab Personal Access Token (PAT)
5. Click Create.
