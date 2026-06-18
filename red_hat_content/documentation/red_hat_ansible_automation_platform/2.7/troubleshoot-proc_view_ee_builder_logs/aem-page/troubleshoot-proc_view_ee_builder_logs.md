+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/troubleshoot-proc_view_ee_builder_logs"
title = "View Ansible automation portal logs for execution environment builder - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/troubleshoot-ref_troubleshoot_ee_builder/", "Troubleshoot execution environment builder"]]
category = "Troubleshoot"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/troubleshoot-proc_view_ee_builder_logs/aem-page/troubleshoot-proc_view_ee_builder_logs.html"
last_crumb = "View Ansible automation portal logs for execution environment builder"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "View Ansible automation portal logs for execution environment builder"
oversized = "false"
page_slug = "troubleshoot-proc_view_ee_builder_logs"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/troubleshoot-proc_view_ee_builder_logs"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/troubleshoot-proc_view_ee_builder_logs/toc/toc.json"
type = "aem-page"
+++

# View Ansible automation portal logs for execution environment builder

View Ansible automation portal logs to diagnose authentication failures, sync errors, catalog registration issues, and SCM connectivity problems.

## About this task

Ansible automation portal logs contain diagnostic information for troubleshooting execution environment builder issues. The procedure for accessing logs depends on your deployment type.

## Procedure

1.  Access the logs for your deployment type.
  -          For OpenShift deployments, run the following command to view backend logs:



```
$ oc logs -n *namespace* deployment/*portal-deployment-name* -c backstage-backend
```
         To filter results for relevant entries, pipe the output through `grep`:



```
$ oc logs -n *namespace* deployment/*portal-deployment-name* -c backstage-backend | grep -i "catalog\|ansible\|sync\|error"
```

  -          For RHEL appliance deployments, use `journalctl` to view recent portal logs:



```
$ sudo journalctl -u portal --since "1 hour ago"
```
         Alternatively, view container logs directly:



```
$ sudo podman logs *portal-container-name*
```

2.  Compare the log output against the common log patterns table to identify the issue.

## Results

The following table lists common log messages and their meanings to help you diagnose execution environment builder issues.

| Log message                                                      | Meaning                                                                                                                                         |
| ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `Failed to send POST request: TypeError: fetch failed`           | Portal backend cannot reach AAP due to TLS certificate rejection. Set `checkSSL` to `false` in both `ansible.rhaap` and `auth.providers.rhaap`. |
| `Failed to send fetch data: fetch failed`                        | Same TLS issue affecting catalog sync API calls. Set `checkSSL` to `false`.                                                                     |
| `Auth response is missing cookie nonce`                          | OAuth nonce cookie lost during redirect. Accept the AAP certificate in your browser first.                                                      |
| `Error retrieving organization details` or `job_templates`       | Catalog sync failed. Check `checkSSL` and verify the AAP token has read permissions.                                                            |
| `No GitHub integration configured for host`                      | Missing `integrations.github` entry in configuration.                                                                                           |
| `No credentials for GitHub host`                                 | Personal access token missing or GitHub App not installed for the organization.                                                                 |
| `catalog processing error`                                       | Invalid template YAML or unreachable `catalog.locations` URL.                                                                                   |
| `ansible content sync`                                           | Sync progress and errors for `ansibleGitContents` or `pahCollections` providers.                                                                |
| `Access-Control-Allow-Origin` or `CORS policy` (browser console) | Request blocked because the origin is not in `backend.cors.origin`. Add the missing URL.                                                        |
| `invalid redirect_uri`                                           | OAuth callback URL does not match the configured portal base URL or Git provider OAuth app settings.                                            |
| `ENOTFOUND plugin-registry`                                      | Tarball mode configured but plugin registry service not deployed.                                                                               |
