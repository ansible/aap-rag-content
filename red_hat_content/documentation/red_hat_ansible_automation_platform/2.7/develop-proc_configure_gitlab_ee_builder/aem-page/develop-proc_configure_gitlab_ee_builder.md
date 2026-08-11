+++
title = "Configure a GitLab OAuth App for saving definitions - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_configure_gitlab_ee_builder"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-build_execution_environments_with_the_automation_portal/", "Build execution environments with automation portal"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-proc_configure_gitlab_ee_builder/aem-page/develop-proc_configure_gitlab_ee_builder.html"
last_crumb = "Configure a GitLab OAuth App for saving definitions"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Configure a GitLab OAuth App for saving definitions"
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

# Configure a GitLab OAuth App for saving definitions

Configure a GitLab OAuth App so that users can save execution environment definition files to a GitLab repository.

## Before you begin

- You have admin access to your GitLab instance or group settings.
- You have configured a GitLab PAT for content discovery.

## About this task

Automated image builds authenticate through the signed-in user's GitLab OAuth session. No additional admin-level tokens or app-config changes are needed beyond the OAuth application scopes configured below.

## Procedure

1.  Create a GitLab OAuth application in your GitLab instance under **Admin Area > Applications** (or group-level settings). Enter the following details:

  - **Name:** A descriptive name, for example `ansible-portal-ee-builder`.
  - **Redirect URI:** `https://<my_portal_domain>/api/auth/gitlab/handler/frame`
  - **Scopes:** Select `api`, `read_api`, `read_user`, `read_repository`, and `write_repository`.
    | OAuth scope        | Purpose                                                                               | When used                                                                         |
    | ------------------ | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
    | `api`              | Access the GitLab API on behalf of the authenticated user.                            | Every save and build operation.                                                   |
    | `read_api`         | Read-only API access.                                                                 | Content discovery and pipeline status checks.                                     |
    | `read_user`        | Read the authenticated user's profile information.                                    | User identification during OAuth flow.                                            |
    | `read_repository`  | Read-only access to repositories.                                                     | Content discovery (scanning for collections).                                     |
    | `write_repository` | Push EE definition files and open merge requests on behalf of the authenticated user. | Every save operation (new repository or merge request to an existing repository). |
  Note:
      If you previously configured a GitLab OAuth application for content discovery or saving definition files, verify that the existing application includes the `api`, `read_api`, `read_user`, `read_repository`, and `write_repository` scopes. Open your OAuth application in **Admin Area > Applications**, select any missing scopes, and save. No other changes are required.

2.  Note the **Application ID** and **Secret**. Save the secret value immediately — you cannot view it again.
3.  Enable the GitLab auth provider in your configuration.
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

4.  Add the OAuth client credentials to your `secrets-scm` secret.
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

## What to do next

After updating the configuration, apply your changes. See [Apply configuration changes](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_apply_configuration_changes "Apply configuration changes after modifying your Helm chart values or RHEL appliance configuration file for execution environment builder.").
