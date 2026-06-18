# Create secrets in OpenShift for Ansible automation portal

Before installing the Helm chart, you must create a set of secrets in your OpenShift project. The Ansible automation portal Helm chart fetches environment variables from OpenShift secrets.

## Create Ansible Automation Platform authentication secrets

You must create a secret in OpenShift Container Platform for Ansible Automation Platform authentication.

### Before you begin

- You have logged in to your OpenShift Container Platform cluster.
- You have access to the OpenShift project where you will install Ansible automation portal.

### About this task

Create the `secrets-rhaap-portal` secret using the `oc` CLI or the OpenShift web console.

Note:

The secret must use the exact name `secrets-rhaap-portal` with the exact key names specified below.

### Procedure

Run the following command to create the secret:

```
$ oc create secret generic secrets-rhaap-portal \
--from-literal=aap-host-url="<aap_instance_url>" \
--from-literal=oauth-client-id="<oauth_client_id>" \
--from-literal=oauth-client-secret="<oauth_client_secret>" \
--from-literal=aap-token="<aap_token>" \
-n <project_name>
```
Replace the placeholder values:

- `<aap_instance_url>`: The URL of your Ansible Automation Platform instance.
- `<oauth_client_id>`: Your Ansible Automation Platform OAuth client ID.
- `<oauth_client_secret>`: Your Ansible Automation Platform OAuth client secret value.
- `<aap_token>`: A token for Ansible Automation Platform user authentication. The token must have `write` access.
- `<project_name>`: The OpenShift project where you will install Ansible automation portal.

### Results

**OpenShift web console**

You can also create the `secrets-rhaap-portal` secret in the OpenShift web console.

1. In the Administrator view, click Workloads> (and then)Secrets.
2. Click Create> (and then)Key/value secret.
3. Set the secret name to `secrets-rhaap-portal`.
4. Add the following key-value pairs:
- Key: `aap-host-url`, Value: Ansible Automation Platform instance URL
- Key: `oauth-client-id`, Value: Ansible Automation Platform OAuth client ID
- Key: `oauth-client-secret`, Value: Ansible Automation Platform OAuth client secret value
- Key: `aap-token`, Value: Token for Ansible Automation Platform user authentication (must have `write` access)
5. Click Create.

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
