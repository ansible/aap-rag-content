+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-configure_automated_image_builds__gitlab_ci_"
title = "Configure automated image builds (GitLab CI) - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-build_execution_environments_with_the_automation_portal/", "Build execution environments with automation portal"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-configure_automated_image_builds__gitlab_ci_/aem-page/develop-configure_automated_image_builds__gitlab_ci_.html"
last_crumb = "Configure automated image builds (GitLab CI)"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Configure automated image builds (GitLab CI)"
oversized = "false"
page_slug = "develop-configure_automated_image_builds__gitlab_ci_"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-configure_automated_image_builds__gitlab_ci_"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-configure_automated_image_builds__gitlab_ci_/toc/toc.json"
type = "aem-page"
+++

# Configure automated image builds (GitLab CI)

Configure GitLab CI/CD variables so that execution environment builder can build container images and push them to a registry when users save EE definitions to a GitLab repository.

## Before you begin

- You have configured a GitLab OAuth App for saving definitions.
- You have a GitLab group or subgroup where EE definitions are saved.
- You have destination registry credentials (for example, private automation hub) and source registry credentials for base images (for example, `registry.redhat.io`).

## About this task

When a user saves an EE definition to a GitLab repository and triggers **Build Execution Environment**, the generated `.gitlab-ci.yml` pipeline builds a container image and pushes it to a registry. Configure group-level CI/CD variables before users can run successful builds.

## Procedure

1.  In GitLab, navigate to your group or subgroup and go to **Settings > CI/CD > Variables**.
2.  Click **Add variable** and add each required CI/CD variable. For each variable:

  - Set **Role** to **Developer** so that developers who push to this group can run pipelines with these variables.
  - **Unselect** the **Protected variable** checkbox. Protected variables are enabled by default. EE build pipelines run on non-protected branches (for example, feature branches created by the portal). If protected is selected, the pipeline cannot access the variable on those branches.
  - Select **Mask variable** for sensitive values (passwords, tokens) to prevent them from appearing in job logs.

3.  Add the following registry and token variables:
    | Variable                                                   | Purpose                                                                                                                                                           | When required                                                                                  |
    | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
    | `REGISTRY_USERNAME`                                        | Username for the destination container registry where built EE images are pushed (for example, private automation hub).                                           | Not required if pushing to GitLab Container Registry.                                          |
    | `REGISTRY_PASSWORD` (mask)                                 | Password for the destination container registry.                                                                                                                  | Not required if pushing to GitLab Container Registry.                                          |
    | `REDHAT_REGISTRY_USERNAME`                                 | Username for the source registry used to pull base images (for example,`registry.redhat.io`).                                                                     | Not required if the base image is publicly available.                                          |
    | `REDHAT_REGISTRY_PASSWORD` (mask)                          | Password for the source registry.                                                                                                                                 | Not required if the base image is publicly available.                                          |
    | `ANSIBLE_GALAXY_SERVER_<ID>_TOKEN` (mask)                  | Galaxy server token matching a`[galaxy_server.<id>]` entry in`ansible.cfg`.`<ID>` is the server id converted to ALL CAPS. One variable per configured repository. | Required when the EE definition includes collections from Private Automation Hub repositories. |
    | `AAP_EE_BUILDER_<PROVIDER>_<CANONICAL>_<ORG>_TOKEN` (mask) | Git collection token. EE Builder generates these variable names automatically based on the collection source. One variable per Git-sourced collection provider.   | Required when the EE definition includes collections from Git repositories.                    |

## What to do next

Note:

When pushing to GitLab Container Registry, the pipeline uses the built-in `CI_REGISTRY_USER` and `CI_REGISTRY_PASSWORD` automatically, provided the EE registry is set to `registry.gitlab.com` and no `REGISTRY_USERNAME` or `REGISTRY_PASSWORD` variables are present in the CI/CD variables on the GitLab group. If those variables exist at the group level, override them at the project level by setting them to `$CI_REGISTRY_USER` and `$CI_REGISTRY_PASSWORD` respectively.

Tip:

Configure variables at the GitLab group level rather than project level. New projects created in the group inherit group-level variables automatically, so users do not need to configure variables each time they save an EE definition to a new project.

To pre-configure Git collection token variables at the group level before users create EE definitions, derive the variable name from your `app-config` entry: `<PROVIDER>` is the SCM provider (`GITHUB` or `GITLAB`), `<CANONICAL>` is the canonical name of the Git host (the `name` field under `catalog.providers.rhaap.*.sync.ansibleGitContents.providers.<provider>` in `app-config`), and `<ORG>` is the Git organization or group name. All segments are uppercased and non-alphanumeric characters are replaced with underscores. For example, a GitHub provider with canonical name `github-public` and organization `test-rhaap-portal` requires the variable `AAP_EE_BUILDER_GITHUB_GITHUB_PUBLIC_TEST_RHAAP_PORTAL_TOKEN`.

The generated `NEXT_STEPS.md` file in each EE project also lists the exact variable names required for your configuration. Use it as a checklist.

Trigger a build from Ansible automation portal. Verify that all pipeline stages pass and the image is pushed to the configured registry.
