+++
title = "Apply configuration changes - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_apply_configuration_changes"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_configure_github_app_ee_builder/", "Configure a GitHub App for content discovery"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-proc_apply_configuration_changes/aem-page/develop-proc_apply_configuration_changes.html"
last_crumb = "Apply configuration changes"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Apply configuration changes"
oversized = "false"
page_slug = "develop-proc_apply_configuration_changes"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-proc_apply_configuration_changes"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-proc_apply_configuration_changes/toc/toc.json"
type = "aem-page"
+++

# Apply configuration changes

Apply configuration changes after modifying your Helm chart values or RHEL appliance configuration file for execution environment builder.

## About this task

You can apply changes at any point — you do not need to complete all configuration sections before applying.

## Procedure

1.  Apply the updated configuration.
      **OpenShift — CLI:**

```
$ helm upgrade <release_name> <chart_name> -f <values_file> -n <namespace>
```
    **OpenShift — web console:**

  1. Navigate to **Helm > Installed Helm Charts**.
  2. Select your release and click **Upgrade**.
  3. Edit the values and click **Upgrade**.
    **RHEL appliance:**

```
$ sudo systemctl daemon-reload
$ sudo systemctl stop portal.service
$ sudo podman rm -f portal
$ sudo systemctl start portal.service
```
  Note:
      The `daemon-reload` and `stop/rm/start` sequence is required when Quadlet drop-in files have been added or changed (for example, after adding EE Builder secrets). If you only changed `app-config.production.yaml` without modifying drop-in files, `sudo systemctl restart portal` is sufficient.

2.  Verify that the service is running.
      **OpenShift — CLI:**

```
$ oc rollout status deployment -n <namespace>
$ oc get pods -n <namespace>
```
    **OpenShift — web console:**

    Navigate to **Workloads > Pods**. Filter by your namespace and verify that all pods show Running status with no restarts.

    **RHEL appliance:**

```
$ sudo systemctl status portal
```

## Results

Log in to automation portal and verify the changes you applied:

- If you configured Git provider integration: check that no `No GitHub integration configured for host` errors appear in the logs.
- If you configured content discovery sources: navigate to **Collections** and verify sources are listed.
- If you configured wizard templates: navigate to **Execution Environments > Create** and verify templates appear.
