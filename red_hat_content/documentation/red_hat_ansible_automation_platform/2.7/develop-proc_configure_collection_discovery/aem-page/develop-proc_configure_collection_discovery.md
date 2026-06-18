+++
title = "Configure collection discovery sources - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_configure_collection_discovery"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_configure_github_app_ee_builder/", "Configure a GitHub App for content discovery"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-proc_configure_collection_discovery/aem-page/develop-proc_configure_collection_discovery.html"
last_crumb = "Configure collection discovery sources"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure collection discovery sources"
oversized = "false"
page_slug = "develop-proc_configure_collection_discovery"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-proc_configure_collection_discovery"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-proc_configure_collection_discovery/toc/toc.json"
type = "aem-page"
+++

# Configure collection discovery sources

Configure Git content discovery and private automation hub collection discovery so that Ansible collections are available in execution environment builder and the collection catalog.

## Before you begin

- You have completed GitHub or GitLab integration setup and credentials are configured.
- You know which GitHub organizations or GitLab groups contain your Ansible collections.
- If using private automation hub, you know the base URL and which repositories to sync.

## About this task

Two discovery providers are available:

- **Git content discovery** (`ansibleGitContents`) — crawls configured GitHub or GitLab organizations for `galaxy.yml` files and registers discovered collections as catalog entities.
- **Private automation hub** (`pahCollections`) — syncs collections from your private automation hub instance, including version and dependency metadata.

## Procedure

1.  Open your configuration file for editing.
      **OpenShift — CLI:**

```
$ helm get values <release_name> -n <namespace> -o yaml > current-values.yaml
$ vi current-values.yaml
```
    **OpenShift — web console:**

    Navigate to **Helm > Installed Helm Charts**. Select your automation portal release and click **Upgrade** to open the values editor.

    **RHEL appliance:**

```
$ sudo vi /etc/portal/configs/app-config/app-config.production.yaml
```

2.  Locate the content discovery section under `catalog.providers.rhaap`.
      Both `ansibleGitContents` and `pahCollections` are included in the chart but disabled by default (`enabled: false`).

3.  To enable Git content discovery, set `ansibleGitContents.enabled` to `true` and update the provider settings to match your environment.
      You can add multiple provider entries — one for each organization or group you want to scan:

```
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
                - name: "github-public"
                  host: github.com
                  checkSSL: true
                  orgs:
                    - name: <your_github_org>
                      branches: [main, master, dev]
                      tags: ['v*']
                      galaxyFilePaths: []
                      schedule:
                        frequency: {minutes: 120}
                        timeout: {minutes: 30}
              gitlab:
                - name: "gitlab-public"
                  host: gitlab.com
                  checkSSL: true
                  orgs:
                    - name: <your_gitlab_group>
                      schedule:
                        frequency: {minutes: 120}
                        timeout: {minutes: 30}
```
  Important:
      The `name` field (for example, `github-public`) is a canonical identifier used internally by automation portal. It does not need to match your organization name. The `host` field is the actual fully qualified domain name (FQDN) of your Git provider (for example, `github.com` or `github.internal.example.com`).

    Update the following values for your environment:

  - Replace `<your_github_org>` with your GitHub organization name.
  - Replace `<your_gitlab_group>` with your GitLab group name. Nested groups are supported.
  - Set `checkSSL: false` for hosts with self-signed certificates.
  - Adjust `branches`, `tags`, and `schedule` values for your environment.
  Note:
      Content discovery consumes repository provider API quota. Large organizations with frequent sync schedules may hit rate limits (HTTP 429), causing incomplete results. Increase `schedule.frequency` or reduce the number of scanned organizations to stay within your repository provider's limits.

  Note:
      The `crawlDepth` parameter controls how many directory levels deep the provider searches for `galaxy.yml` files within each repository. The default is `1`, which discovers only collections with `galaxy.yml` at the repository root. Collections discovered at deeper levels appear in the catalog but cannot be installed by `ansible-galaxy` or used in EE builds. To adjust crawl depth, add it to the org configuration:

```
orgs:
  - name: <your_github_org>
    crawlDepth: 1
```

4.  To enable private automation hub collection discovery, set `pahCollections.enabled` to `true` and update the repository names.
  

```
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
```
  Note:
      Synchronization time depends on the number of collections and metadata in your configured repositories. Large repositories can take significantly longer. To reduce sync time, configure your private automation hub to sync only the collections your teams need.

    When `pahCollections` is configured and your private automation hub base URL is set (via `ansible.rhaap.baseUrl`), automation portal automatically generates `galaxy_servers` entries in the `ansible.cfg` file that ansible-creator produces when a user creates an EE definition.

5.  Apply the configuration changes. See [Apply configuration changes](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_apply_configuration_changes "Apply configuration changes after modifying your Helm chart values or RHEL appliance configuration file for execution environment builder.").

## What to do next

Tip:

For a complete working example of all discovery settings in context, see [Complete Helm chart values reference](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-ref_ee_builder_helm_values "A complete Helm chart values configuration for execution environment builder with GitHub App authentication, content discovery, and private automation hub enabled.").
