+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_configure_gitlab_ee_builder"
title = "Set up GitLab integration for execution environment builder - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_configure_github_app_ee_builder/", "Configure a GitHub App for content discovery"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-proc_configure_gitlab_ee_builder/aem-page/develop-proc_configure_gitlab_ee_builder.html"
last_crumb = "Set up GitLab integration for execution environment builder"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Set up GitLab integration for execution environment builder"
oversized = "false"
page_slug = "develop-proc_configure_gitlab_ee_builder"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-proc_configure_gitlab_ee_builder"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-proc_configure_gitlab_ee_builder/toc/toc.json"
type = "aem-page"
+++

# Set up GitLab integration for execution environment builder

Configure GitLab content discovery and OAuth so that execution environment builder can scan GitLab groups for Ansible collections and save definition files.

## Before you begin

- You have a GitLab account with access to the groups automation portal needs to scan.
- You have admin access to your GitLab instance or group settings.

## About this task

Complete this section if your organization uses GitLab for content discovery or saving definition files. If you use GitHub only, skip to [Configure collection discovery sources](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_configure_collection_discovery "Configure Git content discovery and private automation hub collection discovery so that Ansible collections are available in execution environment builder and the collection catalog.").

GitLab uses a Personal Access Token for content discovery.

## Procedure

Content discovery (scanning repositories for collections)

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

Save definition files to a GitLab repository (OAuth)

4.  Create a GitLab OAuth application in your GitLab instance under **Admin Area > Applications** (or group-level settings). Enter the following details:

  - **Name:** A descriptive name, for example `ansible-portal-ee-builder`.
  - **Redirect URI:** `https://<my_portal_domain>/api/auth/gitlab/handler/frame`
  - **Scopes:** Select `write_repository`.
    The `write_repository` scope lets automation portal push EE definition files and open merge requests on behalf of the authenticated user. It is used for every save operation (new repository or merge request to an existing repository).

5.  Note the **Application ID** and **Secret**. Save the secret value immediately — you cannot view it again.
6.  Enable the GitLab auth provider in your configuration.
      **OpenShift:** Uncomment the `auth.providers.gitlab` block in your Helm chart configuration.

    **RHEL appliance:** Add the following `auth.providers` block to `/etc/portal/configs/app-config/app-config.production.yaml`. If an `auth:` section already exists, add the `providers:` section inside it:

```
auth:
  providers:
    gitlab:
      production:
        clientId: ${GITLAB_OAUTH_CLIENT_ID}
        clientSecret: ${GITLAB_OAUTH_CLIENT_SECRET}
```

7.  Add the OAuth client credentials to your `secrets-scm` secret.
      **OpenShift — CLI:**

```
$ oc patch secret secrets-scm -n <namespace> --type merge -p \
  '{"stringData":{"gitlab-oauth-client-id":"<your_client_id>","gitlab-oauth-client-secret":"<your_client_secret>"}}'
```
    **OpenShift — web console:**

  1. Navigate to **Workloads > Secrets**.
  2. Edit the `secrets-scm` secret and add keys `gitlab-oauth-client-id` and `gitlab-oauth-client-secret`.
    **RHEL appliance:**

```
$ echo -n '<your_client_id>' | sudo podman secret create portal_gitlab_oauth_client_id -
$ echo -n '<your_client_secret>' | sudo podman secret create portal_gitlab_oauth_client_secret -
```
    Append to the Quadlet drop-in file:

```
$ sudo tee -a /etc/containers/systemd/portal.container.d/ee-builder-secrets.conf << 'EOF'
Secret=portal_gitlab_oauth_client_id,type=env,target=GITLAB_OAUTH_CLIENT_ID
Secret=portal_gitlab_oauth_client_secret,type=env,target=GITLAB_OAUTH_CLIENT_SECRET
EOF
```
