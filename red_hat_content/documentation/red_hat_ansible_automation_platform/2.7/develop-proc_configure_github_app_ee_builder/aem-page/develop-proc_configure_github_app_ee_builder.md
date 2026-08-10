+++
template = "docs/aem-title.html"
title = "Configure a GitHub App for content discovery - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_configure_github_app_ee_builder"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-build_execution_environments_with_the_automation_portal/", "Build execution environments with automation portal"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-proc_configure_github_app_ee_builder/aem-page/develop-proc_configure_github_app_ee_builder.html"
last_crumb = "Configure a GitHub App for content discovery"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Configure a GitHub App for content discovery"
oversized = "false"
page_slug = "develop-proc_configure_github_app_ee_builder"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-proc_configure_github_app_ee_builder"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-proc_configure_github_app_ee_builder/toc/toc.json"
type = "aem-page"
+++

# Configure a GitHub App for content discovery

Create and install a GitHub App so that execution environment builder can scan your organization's repositories for Ansible collections.

## Before you begin

- You have owner or admin permissions in your GitHub organization.

## About this task

GitHub Apps provide organization-scoped permissions that do not depend on individual user accounts. A GitHub App is the recommended option for content discovery. You can also use a Personal Access Token (PAT). You do not need both.

## Procedure

1.  In a browser, log in to GitHub.
2.  Navigate to your organization settings.
3.  Select **Developer settings > GitHub Apps**.
4.  Click **New GitHub App**.
5.  Enter the following details:

  - **GitHub App name:** A descriptive name, for example `ansible-portal-content-discovery`.
  - **Homepage URL:** The URL of your automation portal deployment.
  - **Webhook:** Clear the **Active** checkbox if you do not require webhook events.
  - **Authorization callback URL:** `https://<my_portal_domain>/api/auth/github/handler/frame`
  Note:
      GitHub limits the Authorization callback URL to 100 characters. If your OpenShift route URL exceeds this limit, configure a shorter route hostname for the portal before creating the OAuth App.

6.  In the **Permissions** section, set the following repository permissions:

  - **Contents:** Read-only
  - **Actions:** Read-only

7.  In the **Where can this GitHub App be installed?** section, select **Any account**.
8.  Click **Create GitHub App**.
9.  Note the **App ID** from the GitHub App settings page.
10.  In the **Private keys** section, click **Generate a private key**. Store the downloaded `.pem` file securely.
11.  In the **Client secrets** section, click **Generate a new client secret**. Save the client secret value immediately — you cannot view it again.
12.  Install the GitHub App in your organization:
  1.  On the GitHub App settings page, click **Install App**.
  2.  Select your organization.
  3.  Select **All repositories** or specific repositories that automation portal requires access to.
  4.  Click **Install**.

## Results

On the GitHub App settings page, the **Install App** section shows your organization with an **Installed** status.

## What to do next

After creating the GitHub App, add the credentials and update your configuration. See Create the secrets below.

**Create the secrets**

**OpenShift — CLI:**

```
$ oc create secret generic secrets-scm \
  --from-literal=github-app-id=<app_id> \
  --from-literal=github-app-client-id=<client_id> \
  --from-literal=github-app-client-secret=<client_secret> \
  --from-literal=github-app-private-key="$(cat <path_to_private_key>.pem)" \
  -n <namespace>
```

**OpenShift — web console:**

1. Navigate to **Workloads > Secrets > Create > Key/value secret**.
2. Set the name to `secrets-scm`.
3. Add keys: `github-app-id`, `github-app-client-id`, `github-app-client-secret`, `github-app-private-key` (paste the `.pem` file contents as the value).

**RHEL appliance:**

```
$ echo -n '<app_id>' | sudo podman secret create portal_github_app_id -
$ echo -n '<client_id>' | sudo podman secret create portal_github_app_client_id -
$ echo -n '<client_secret>' | sudo podman secret create portal_github_app_client_secret -
$ sudo podman secret create portal_github_app_private_key <path_to_private_key>.pem
```

**Update the Helm chart configuration**

In your Helm chart configuration, update the `integrations.github` section. Configure either a PAT or GitHub App:

```
upstream:
  backstage:
    appConfig:
      integrations:
        github:
          ## Option A: PAT-based integration (default)
          - host: github.com
            token: ${GITHUB_TOKEN}

          ## Option B: GitHub App integration (recommended)
          ## To use GitHub App, comment out the token line above
          ## and uncomment the following block:
          # - host: github.com
          #   apps:
          #     - appId: ${GITHUB_APP_ID}
          #       clientId: ${GITHUB_APP_CLIENT_ID}
          #       clientSecret: ${GITHUB_APP_CLIENT_SECRET}
          #       privateKey: ${GITHUB_APP_PRIVATE_KEY}
```

The configuration shows two options. Option A uses a Personal Access Token (see [Configure a Personal Access Token for GitHub content discovery](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_configure_pat_ee_builder "Create and store a GitHub Personal Access Token (PAT) so that execution environment builder can scan repositories for Ansible collections.")). Option B uses a GitHub App (recommended).

Important:

A GitHub App is the recommended option. If using a GitHub App, comment out the `token` line and uncomment the `apps` block.

**RHEL appliance:** Add the equivalent `integrations.github` block to `/etc/portal/configs/app-config/app-config.production.yaml` (without the `upstream.backstage.appConfig` nesting):

```
integrations:
  github:
    - host: github.com
      apps:
        - appId: ${GITHUB_APP_ID}
          clientId: ${GITHUB_APP_CLIENT_ID}
          clientSecret: ${GITHUB_APP_CLIENT_SECRET}
          privateKey: ${GITHUB_APP_PRIVATE_KEY}
```

The `${...}` references are resolved from the Podman secrets you created above. The portal automatically injects `portal_`-prefixed secrets as environment variables.

Important:

Adding an `integrations:` section to `app-config.production.yaml` replaces the auto-generated PAT-based integration from cloud-init. If you are switching from a PAT to a GitHub App, the PAT is no longer used for content discovery. Having both a PAT and a GitHub App in the same `integrations:` block does not break the install, but the PAT is unnecessary when a GitHub App is configured.

**Configure CORS for self-hosted GitHub Enterprise**

If the `host` is a self-hosted GitHub Enterprise instance (not `github.com`), add its URL to the CORS allowed origins so that OAuth redirects are accepted.

**OpenShift:**

```
upstream:
  backstage:
    appConfig:
      backend:
        cors:
          origin:
            - ${BASE_URL}
            - https://github.internal.example.com
```

**RHEL appliance** — add to the existing `backend:` block in `app-config.production.yaml`:

```
backend:
  cors:
    origin:
      - "https://portal.example.com"
      - "https://github.internal.example.com"
```

Important:

On RHEL appliances, `app.baseUrl`, `backend.baseUrl`, and `backend.cors.origin` must all use the same portal URL. If any of these values are inconsistent, OAuth callbacks and API requests fail. Do not create a duplicate `backend:` block — add `cors` to the existing one.

Note:

If you only use `github.com`, no CORS changes are needed.

For a complete working example of all settings in context, see [Complete Helm chart values reference](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-ref_ee_builder_helm_values "A complete Helm chart values configuration for execution environment builder with GitHub App authentication, content discovery, and private automation hub enabled.").

After updating the configuration, apply your changes. See [Apply configuration changes](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_apply_configuration_changes "Apply configuration changes after modifying your Helm chart values or RHEL appliance configuration file for execution environment builder.").
