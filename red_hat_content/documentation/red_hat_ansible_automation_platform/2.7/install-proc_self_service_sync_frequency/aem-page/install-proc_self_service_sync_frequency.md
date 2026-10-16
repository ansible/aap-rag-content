+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_self_service_sync_frequency"
title = "Adjust synchronization frequency between Ansible Automation Platform and Ansible automation portal - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-install_automation_portal_on_openshift_container_platform/", "Install automation portal on OpenShift Container Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_self_service_sync_frequency/aem-page/install-proc_self_service_sync_frequency.html"
last_crumb = "Adjust synchronization frequency between Ansible Automation Platform and Ansible automation portal"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Adjust synchronization frequency between Ansible Automation Platform and Ansible automation portal"
oversized = "false"
page_slug = "install-proc_self_service_sync_frequency"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-proc_self_service_sync_frequency"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_self_service_sync_frequency/toc/toc.json"
type = "aem-page"
+++

# Adjust synchronization frequency between Ansible Automation Platform and Ansible automation portal

The Helm chart defines how frequently users,
teams and organization configuration information is synchronized from Ansible Automation Platform to Ansible automation portal.

## About this task

The frequency is set by the `catalog.providers.rhaap.schedule.frequency` key.
By default, the synchronization occurs hourly.

## Procedure

To adjust the synchronization frequency, edit the value for the `catalog.providers.rhaap.schedule.frequency` key in the Helm chart.

```
catalog:
  ...
  providers:
    rhaap:
      '{{- include "catalog.providers.env" . }}':
        schedule:
          frequency: {minutes: 60}
          timeout: {seconds: 30}
```

Note:

Increasing the synchronization frequency generates extra traffic.

Bear this in mind when deciding the frequency, particularly if you have a large number of users.
