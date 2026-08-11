+++
title = "Configure a GitHub OAuth App for saving definitions - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_configure_github_oauth_ee_builder"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-build_execution_environments_with_the_automation_portal/", "Build execution environments with automation portal"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-proc_configure_github_oauth_ee_builder/aem-page/develop-proc_configure_github_oauth_ee_builder.html"
last_crumb = "Configure a GitHub OAuth App for saving definitions"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Configure a GitHub OAuth App for saving definitions"
oversized = "false"
page_slug = "develop-proc_configure_github_oauth_ee_builder"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-proc_configure_github_oauth_ee_builder"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-proc_configure_github_oauth_ee_builder/toc/toc.json"
type = "aem-page"
+++

# Configure a GitHub OAuth App for saving definitions

Configure a GitHub OAuth App so that users can save execution environment definition files to a GitHub repository and trigger automated image builds.

## Before you begin

- You have admin access to your GitHub organization settings.
- If your GitHub organization restricts OAuth App access, you have confirmed that the `repo` and `workflow` scopes are permitted.

## About this task

When users complete the EE Builder wizard, they can save the generated definition files to a GitHub repository — either creating a new repository or opening a pull request on an existing one. The wizard creates the following files:

- `<ee-name>.yml` — the EE definition with all dependencies (collections, Python packages, system packages) declared inline. The file name matches the name the user enters in the EE Builder form.
- `<ee-name>-template.yaml` — a reusable template file (with `spec.type: execution-environment`) that captures the selected configuration. Administrators can register this template in the catalog so other users can create EE definitions from it.
- `ansible.cfg` — Galaxy server configuration (auto-generated from configured collection sources).
- `ee-build.yml` — GitHub Actions workflow for automated builds.

Users authenticate via OAuth when saving. The wizard template defines the following OAuth scopes, which are requested automatically during the OAuth flow:

| OAuth scope | Purpose                                                                                                    | When used                                                                        |
| ----------- | ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `repo`      | Create repositories, push EE definition files, and open pull requests on behalf of the authenticated user. | Every save operation (new repository or pull request to an existing repository). |
| `workflow`  | Dispatch the`ee-build.yml` GitHub Actions workflow to build and push the container image.                  | When the user selects**Build Execution Environment** during the save flow.       |

Important:

If your GitHub organization uses OAuth App access restrictions, an organization owner must approve the OAuth App and grant the `repo` and `workflow` scopes before users can save definitions.

## Procedure

1.  Create a GitHub OAuth App in your organization settings under **Developer settings > OAuth Apps**. Enter the following details:

  - **Application name:** A descriptive name, for example `ansible-portal-ee-builder`.
  - **Homepage URL:** The URL of your automation portal deployment.
  - **Authorization callback URL:** `https://<my_portal_domain>/api/auth/github/handler/frame`
  Note:
      GitHub limits the Authorization callback URL to 100 characters. If your OpenShift route URL exceeds this limit, configure a shorter route hostname for the portal before creating the OAuth App.

2.  Note the **Client ID** and generate a **Client secret**. Save the client secret value immediately — you cannot view it again.
3.  If your organization restricts OAuth App access, navigate to **Organization settings > Third-party access** and approve the OAuth App.
4.  Enable the GitHub auth provider in your configuration.
      **OpenShift:** Uncomment the `auth.providers.github` block in your Helm chart configuration.

    **RHEL appliance:** Add the following `auth.providers` block to `/etc/portal/configs/app-config/app-config.production.yaml`. If an `auth:` section already exists, add the `providers:` section inside it:

```
auth:
  providers:
    github:
      production:
        clientId: ${GITHUB_OAUTH_CLIENT_ID}
        clientSecret: ${GITHUB_OAUTH_CLIENT_SECRET}
```

5.  Add the OAuth client credentials to your `secrets-scm` secret.
      **OpenShift — CLI:**

```
$ oc patch secret secrets-scm -n <namespace> --type merge -p \
  '{"stringData":{"github-oauth-client-id":"<your_client_id>","github-oauth-client-secret":"<your_client_secret>"}}'
```

    If `secrets-scm` does not exist yet, include `--from-literal=github-oauth-client-id=<id>` and `--from-literal=github-oauth-client-secret=<secret>` in the `oc create secret generic` command from the content discovery section.

    **OpenShift — web console:**

  1. Navigate to **Workloads > Secrets**.
  2. Edit the `secrets-scm` secret and add keys `github-oauth-client-id` and `github-oauth-client-secret`.
    **RHEL appliance:**

```
$ echo -n '<your_client_id>' | sudo podman secret create portal_github_oauth_client_id -
$ echo -n '<your_client_secret>' | sudo podman secret create portal_github_oauth_client_secret -
```

6.  If you use a self-hosted GitHub Enterprise instance (not `github.com`), add its URL to the CORS allowed origins so that OAuth redirects are accepted.
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

## What to do next

To enable automated image builds with GitHub Actions, configure organization secrets and variables. See Configure automated image builds below.

After updating the configuration, apply your changes. See [Apply configuration changes](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_apply_configuration_changes "Apply configuration changes after modifying your Helm chart values or RHEL appliance configuration file for execution environment builder.").

**Configure automated image builds (GitHub Actions)**

When a user saves an EE definition to a GitHub repository and selects **Build Execution Environment**, the generated `ee-build.yml` GitHub Actions workflow builds a container image and pushes it to a registry. Configure organization secrets and variables before users can run successful builds.

You need a GitHub organization where EE definitions are saved, destination registry credentials (for example, private automation hub), and source registry credentials for base images (for example, `registry.redhat.io`).

1. In GitHub, navigate to your organization settings.
2. Go to **Settings > Secrets and variables > Actions**.
3. Under **Secrets**, click **New organization secret** and add each required secret:
    | Secret                                              | Purpose                                                                                                                                                              | When required                                                                                  |
    | --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
    | `REGISTRY_PASSWORD`                                 | Password for the destination container registry where built EE images are pushed (for example, private automation hub).                                              | Not required if pushing to GitHub Container Registry.                                          |
    | `REDHAT_REGISTRY_PASSWORD`                          | Password for the source registry used to pull base images (for example,`registry.redhat.io`).                                                                        | Not required if the base image is publicly available.                                          |
    | `ANSIBLE_GALAXY_SERVER_<NAME>_TOKEN`                | Galaxy server tokens matching`[galaxy_server.<name>]` entries in`ansible.cfg`.`<NAME>` is the server id converted to ALL CAPS. One secret per configured repository. | Required when the EE definition includes collections from Private Automation Hub repositories. |
    | `AAP_EE_BUILDER_<PROVIDER>_<CANONICAL>_<ORG>_TOKEN` | Git collection tokens. EE Builder generates these token placeholders automatically based on the collection source. One secret per Git-sourced collection provider.   | Required when the EE definition includes collections from Git repositories.                    |

4. Under **Variables**, click **New organization variable** and add each required variable:
    | Variable                   | Purpose                                                                                | When required                                         |
    | -------------------------- | -------------------------------------------------------------------------------------- | ----------------------------------------------------- |
    | `REGISTRY_USERNAME`        | Username for the destination container registry (for example, private automation hub). | Not required if pushing to GitHub Container Registry. |
    | `REDHAT_REGISTRY_USERNAME` | Username for the source registry (for example,`registry.redhat.io`).                   | Not required if the base image is publicly available. |

Note:

When using GitHub Container Registry as the destination registry, the workflow uses the built-in `GITHUB_TOKEN` automatically. No additional `REGISTRY_USERNAME` or `REGISTRY_PASSWORD` configuration is required.

Tip:

Organization secrets and variables are the recommended configuration. New repositories created in the organization inherit organization secrets automatically, so users do not need to configure secrets each time they save an EE definition to a new repository. Repository-level secrets also work but require manual setup on each repository before the first build can succeed.

To pre-configure Git collection token secrets at the organization level before users create EE definitions, derive the secret name from your `app-config` entry: `<PROVIDER>` is the SCM provider (`GITHUB` or `GITLAB`), `<CANONICAL>` is the canonical name of the Git host (the `name` field under `catalog.providers.rhaap.*.sync.ansibleGitContents.providers.<provider>` in `app-config`), and `<ORG>` is the Git organization name. All segments are uppercased and non-alphanumeric characters are replaced with underscores. For example, a GitHub provider with canonical name `github-public` and organization `test-rhaap-portal` requires the secret `AAP_EE_BUILDER_GITHUB_GITHUB_PUBLIC_TEST_RHAAP_PORTAL_TOKEN`.

The generated `NEXT_STEPS.md` file in each EE project also lists the exact variable names required for your configuration. Use it as a checklist.

Trigger a build from Ansible automation portal or manually dispatch the `ee-build.yml` workflow from GitHub Actions. Verify that all validation steps pass and the image is pushed to the configured registry.
