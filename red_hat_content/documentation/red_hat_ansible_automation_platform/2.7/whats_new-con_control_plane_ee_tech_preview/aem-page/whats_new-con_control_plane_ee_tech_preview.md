+++
title = "Control-plane execution environment (Technology Preview) - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-con_control_plane_ee_tech_preview"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-technology_preview/", "Technology Preview"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-con_control_plane_ee_tech_preview/aem-page/whats_new-con_control_plane_ee_tech_preview.html"
last_crumb = "Control-plane execution environment (Technology Preview)"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Control-plane execution environment (Technology Preview)"
oversized = "false"
page_slug = "whats_new-con_control_plane_ee_tech_preview"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/whats_new-con_control_plane_ee_tech_preview"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-con_control_plane_ee_tech_preview/toc/toc.json"
type = "aem-page"
+++

# Control-plane execution environment (Technology Preview)

As a Technology Preview, you can configure automation controller to use `control-plane-ee` for internal operations.

Important:

`control-plane-ee` is a Technology Preview feature. Technology Preview features are not supported with Red Hat production service level agreements (SLAs), might not be functionally complete, and are not recommended for production. These features provide early access to upcoming product features so that you can test functionality and provide feedback.

For this Technology Preview, the control-plane execution environment is used for internal automation controller operations such as:

- Project updates from Git, Subversion, remote archives, and Red Hat Insights
- Constructed inventory source updates

Regular inventory sources, such as cloud inventory sources, use the execution environment configured for the inventory source, when one is set. Otherwise, automation controller uses the execution environment resolved for the inventory update. Regular inventory sources do not automatically use `control-plane-ee`.

`ee-supported` remains the default. The control-plane execution environment does not run customer automation jobs.

Important:

`control-plane-ee` is intended only for internal automation controller operations. It is maintained for automation controller needs, not customer workloads, and its content updates do not provide customer notifications. It contains only dependencies for internal operations and does not include the collections, Python packages, and system tools that customer playbooks might require. Customer playbooks can fail. Do not select it for a job template or use it for customer workloads.
