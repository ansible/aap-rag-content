+++
title = "Known limitations - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-ref_control_plane_ee_limitations"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-technology_preview/", "Technology Preview"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-ref_control_plane_ee_limitations/aem-page/whats_new-ref_control_plane_ee_limitations.html"
last_crumb = "Known limitations"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Known limitations"
oversized = "false"
page_slug = "whats_new-ref_control_plane_ee_limitations"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/whats_new-ref_control_plane_ee_limitations"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-ref_control_plane_ee_limitations/toc/toc.json"
type = "aem-page"
+++

# Known limitations

The control-plane execution environment Technology Preview has the following known limitations.

- `control-plane-ee` is a Technology Preview and is not enabled by default. `ee-supported` remains the default.
- `control-plane-ee` is used for project updates and constructed inventory updates. Regular inventory sources use the execution environment configured for the inventory source, when one is set, or the execution environment resolved for the inventory update.
- `control-plane-ee` has only the dependencies required for internal automation controller operations and is not intended for customer workloads.
- The OpenShift Container Platform and containerized installer procedures use different configuration methods.
