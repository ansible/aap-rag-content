+++
title = "Post-upgrade requirements - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-ref_post_upgrade_requirements"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-ref_post_upgrade_requirements/", "Post-upgrade requirements"]]
category = "Upgrade"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-ref_post_upgrade_requirements/aem-page/upgrade-ref_post_upgrade_requirements.html"
last_crumb = "Post-upgrade requirements"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Post-upgrade requirements"
oversized = "false"
page_slug = "upgrade-ref_post_upgrade_requirements"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/upgrade-ref_post_upgrade_requirements"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-ref_post_upgrade_requirements/toc/toc.json"
type = "aem-page"
+++

# Post-upgrade requirements

After upgrading to Ansible Automation Platform 2.7, update tokens, scripts, and integrations to use platform gateway for all external authentication and API access.

After upgrading to Ansible Automation Platform 2.7, perform the following actions:

- **Regenerate tokens:** Regenerate all Personal Access Tokens through platform gateway.
- **Update CaC:** Update Configuration as Code files to use platform gateway URLs.
- **Update scripts:** Update scripts and integrations to point to platform gateway.
- **Update container registry:** Re-authenticate to the container registry.
- **Update collection connection parameters:** Update playbooks that use `ansible.controller`, `ansible.hub`, or `ansible.eda` collections to point to the platform gateway hostname instead of direct component hostnames. For example, change `controller_host` from `controller.example.com` to `gateway.example.com`. Token parameters such as `controller_oauthtoken` must use tokens created through platform gateway.
