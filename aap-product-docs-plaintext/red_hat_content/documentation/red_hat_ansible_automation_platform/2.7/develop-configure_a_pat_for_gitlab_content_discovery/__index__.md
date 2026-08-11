# Configure a Personal Access Token for GitLab content discovery

Create and store a GitLab Personal Access Token (PAT) so that execution environment builder can scan groups for Ansible collections.

## Before you begin

- You have a GitLab account with access to the groups automation portal needs to scan.

## About this task

Complete this section if your organization uses GitLab for content discovery or saving definition files. If you use GitHub only, skip to [Configure collection discovery sources](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_configure_collection_discovery "Configure Git content discovery and private automation hub collection discovery so that Ansible collections are available in execution environment builder and the collection catalog.").

GitLab uses a Personal Access Token for content discovery.

## Procedure

1.  Create a GitLab PAT with the following scopes:

- `read_repository`
- `api`

2.  Store the PAT.
**OpenShift — CLI:**

```
$ oc create secret generic secrets-scm \
--from-literal=gitlab-token=<your_gitlab_pat> \
-n <namespace>
```

If you already have a `secrets-scm` secret (for example, with GitHub credentials), patch it instead:

```
$ oc patch secret secrets-scm -n <namespace> --type merge -p \
'{"stringData":{"gitlab-token":"<your_gitlab_pat>"}}'
```

**OpenShift — web console:**

1. Navigate to **Workloads > Secrets**.
2. Edit or create the `secrets-scm` secret and add key `gitlab-token`.
**RHEL appliance:**

```
$ echo -n '<your_gitlab_pat>' | sudo podman secret create portal_gitlab_token -
```

Note:
If you configured a GitLab personal access token during RHEL appliance installation (via cloud-init), the `portal_gitlab_token` secret already exists and is active for content discovery. Running the command above updates the existing secret with a new value.

3.  If you use a self-hosted GitLab instance (not `gitlab.com`), add its URL to the CORS allowed origins.
**OpenShift:**

```
upstream:
backstage:
appConfig:
backend:
cors:
origin:
- ${BASE_URL}
- https://gitlab.internal.example.com
```

**RHEL appliance** — add to the existing `backend:` block in `app-config.production.yaml`:

```
backend:
cors:
origin:
- "https://portal.example.com"
- "https://gitlab.internal.example.com"
```

Important:
On RHEL appliances, `app.baseUrl`, `backend.baseUrl`, and `backend.cors.origin` must all use the same portal URL. If any of these values are inconsistent, OAuth callbacks and API requests fail. Do not create a duplicate `backend:` block — add `cors` to the existing one.

Note:
If you only use `gitlab.com`, no CORS changes are needed.

## What to do next

After updating the configuration, apply your changes. See [Apply configuration changes](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_apply_configuration_changes "Apply configuration changes after modifying your Helm chart values or RHEL appliance configuration file for execution environment builder.").
