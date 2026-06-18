+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-ref_ee_builder_helm_values"
template = "docs/aem-title.html"
title = "Complete Helm chart values reference for execution environment builder - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_configure_github_app_ee_builder/", "Configure a GitHub App for content discovery"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-ref_ee_builder_helm_values/aem-page/develop-ref_ee_builder_helm_values.html"
last_crumb = "Complete Helm chart values reference for execution environment builder"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Complete Helm chart values reference for execution environment builder"
oversized = "false"
page_slug = "develop-ref_ee_builder_helm_values"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-ref_ee_builder_helm_values"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-ref_ee_builder_helm_values/toc/toc.json"
type = "aem-page"
+++

# Complete Helm chart values reference for execution environment builder

A complete Helm chart values configuration for execution environment builder with GitHub App authentication, content discovery, and private automation hub enabled.

## Example configuration

The following example shows all execution environment builder settings in context. Adapt this to your environment.

```
upstream:
    backstage:
      appConfig:
        integrations:
          github:
            - host: github.com
              apps:
                - appId: ${GITHUB_APP_ID}
                  clientId: ${GITHUB_APP_CLIENT_ID}
                  clientSecret: ${GITHUB_APP_CLIENT_SECRET}
                  privateKey: ${GITHUB_APP_PRIVATE_KEY}

        backend:
          cors:
            origin:
              - ${BASE_URL}
              ## Add self-hosted Git provider URLs if not using github.com / gitlab.com:
              # - https://github.internal.example.com
              # - https://gitlab.internal.example.com

        auth:
          providers:
            github:
              production:
                clientId: ${GITHUB_OAUTH_CLIENT_ID}
                clientSecret: ${GITHUB_OAUTH_CLIENT_SECRET}

        catalog:
          locations:
            - type: url
              target: https://github.com/ansible/ansible-rhdh-templates/blob/v2.0.0/templates/ee-start-from-scratch.yaml
              rules:
                - allow: [Template]
            - type: url
              target: https://github.com/ansible/ansible-rhdh-templates/blob/v2.0.0/templates/ee-cloud-automation.yaml
              rules:
                - allow: [Template]
            - type: url
              target: https://github.com/ansible/ansible-rhdh-templates/blob/v2.0.0/templates/ee-network-automation.yaml
              rules:
                - allow: [Template]

          providers:
            rhaap:
              production:
                sync:
                  ansibleGitContents:
                    enabled: true
                    schedule:
                      frequency: {minutes: 120}
                      timeout: {minutes: 30}
                    providers:
                      github:
                        - name: "github-org"
                          host: github.com
                          checkSSL: true
                          orgs:
                            - name: <your_github_org>
                              branches: [main, master]
                              tags: ['v*']
                              galaxyFilePaths: []
                              crawlDepth: 0

                  pahCollections:
                    enabled: true
                    repositories:
                      - name: rh-certified
                        schedule:
                          frequency: {days: 1}
                          timeout: {minutes: 60}
                      - name: validated
                        schedule:
                          frequency: {days: 1}
                          timeout: {minutes: 60}
                      - name: published
                        schedule:
                          frequency: {days: 1}
                          timeout: {minutes: 60}

          ansible:
            skipTlsVerifyForHosts: []

        ansible:
          rhaap:
            baseUrl: https://aap.example.com
            token: ${AAP_API_TOKEN}
```


Note:

Replace placeholder values (`${...}`, `<your_github_org>`, `aap.example.com`) with your actual environment values. Secrets referenced with `${...}` are resolved from the `secrets-scm` OpenShift secret at runtime.

## RHEL appliance configuration reference

The following example shows the equivalent configuration for RHEL appliance deployments in `/etc/portal/configs/app-config/app-config.production.yaml`. RHEL configuration omits the `upstream.backstage.appConfig` nesting used by the Helm chart.

```
integrations:
    github:
      - host: github.com
        apps:
          - appId: ${GITHUB_APP_ID}
            clientId: ${GITHUB_APP_CLIENT_ID}
            clientSecret: ${GITHUB_APP_CLIENT_SECRET}
            privateKey: ${GITHUB_APP_PRIVATE_KEY}

  backend:
    cors:
      origin:
        - "https://portal.example.com"
        ## Add self-hosted Git provider URLs if not using github.com / gitlab.com:
        # - "https://github.internal.example.com"
        # - "https://gitlab.internal.example.com"

  auth:
    providers:
      github:
        production:
          clientId: ${GITHUB_OAUTH_CLIENT_ID}
          clientSecret: ${GITHUB_OAUTH_CLIENT_SECRET}

  catalog:
    providers:
      rhaap:
        production:
          sync:
            ansibleGitContents:
              enabled: true
              schedule:
                frequency: {minutes: 120}
                timeout: {minutes: 30}
              providers:
                github:
                  - name: "github-org"
                    host: github.com
                    checkSSL: true
                    orgs:
                      - name: <your_github_org>
                        branches: [main, master]
                        tags: ['v*']
                        galaxyFilePaths: []

            pahCollections:
              enabled: true
              repositories:
                - name: rh-certified
                  schedule:
                    frequency: {days: 1}
                    timeout: {minutes: 60}
                - name: validated
                  schedule:
                    frequency: {days: 1}
                    timeout: {minutes: 60}

    ansible:
      skipTlsVerifyForHosts: []

  ansible:
    rhaap:
      baseUrl: https://aap.example.com
      token: ${AAP_API_TOKEN}
```


Note:

The `${...}` references are resolved from Podman secrets through the Quadlet drop-in file (`ee-builder-secrets.conf`). PAT-based secrets (`portal_github_token`, `portal_gitlab_token`) are managed by the base portal infrastructure and do not require a drop-in entry.

## Key configuration sections

`integrations.github`
Git provider authentication. Configure either a PAT (`token`) or a GitHub App (`apps`), not both. See [Configure a GitHub App for content discovery](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_configure_github_app_ee_builder "Create and install a GitHub App so that execution environment builder can scan your organization's repositories for Ansible collections.") or [Configure a Personal Access Token for GitHub](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_configure_pat_ee_builder "Create and store a GitHub Personal Access Token (PAT) so that execution environment builder can scan repositories for Ansible collections.").

`backend.cors.origin`
CORS allowed origins. Add self-hosted Git provider URLs if not using `github.com` or `gitlab.com`.

`auth.providers.github`
OAuth App credentials for saving definition files and automated builds. See [Configure a GitHub OAuth App for saving definitions](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_configure_github_oauth_ee_builder "Configure a GitHub OAuth App so that users can save execution environment definition files to a GitHub repository and trigger automated image builds.").

`catalog.locations`
EE Builder wizard templates. Replace with private repository URLs for air-gapped environments. See [Host EE wizard templates in a private Git repository](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_host_templates_private_repo "Copy the EE Builder wizard templates from the public Ansible GitHub repository to a private repository for use in private or air-gapped environments.").

`catalog.providers.rhaap.production.sync.ansibleGitContents`
Git content discovery configuration. See [Configure collection discovery sources](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_configure_collection_discovery "Configure Git content discovery and private automation hub collection discovery so that Ansible collections are available in execution environment builder and the collection catalog.").

`catalog.providers.rhaap.production.sync.pahCollections`
Private automation hub collection discovery. See [Configure collection discovery sources](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_configure_collection_discovery "Configure Git content discovery and private automation hub collection discovery so that Ansible collections are available in execution environment builder and the collection catalog.").

`ansible.rhaap`
Ansible Automation Platform connection settings including base URL and API token.

`catalog.ansible.skipTlsVerifyForHosts`
Hosts where TLS verification is skipped for catalog interactions. See [Host EE wizard templates in a private Git repository](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_host_templates_private_repo "Copy the EE Builder wizard templates from the public Ansible GitHub repository to a private repository for use in private or air-gapped environments.").
