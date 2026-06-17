+++
template = "docs/aem-title.html"
title = "The MANAGE_ORGANIZATION_AUTH setting - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-con_upgrade_manage_org_setting"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-assembly_upgrade_data_movement/", "Identity and access management migration during upgrade"]]
category = "Upgrade"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/upgrade-con_upgrade_manage_org_setting/aem-page/upgrade-con_upgrade_manage_org_setting.html"
last_crumb = "The MANAGE_ORGANIZATION_AUTH setting"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "The MANAGE_ORGANIZATION_AUTH setting"
oversized = "false"
page_slug = "upgrade-con_upgrade_manage_org_setting"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/upgrade-con_upgrade_manage_org_setting"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/upgrade-con_upgrade_manage_org_setting/toc/toc.json"
type = "aem-page"
+++

# The `MANAGE_ORGANIZATION_AUTH` setting

The automation controller setting previously called **Organization Admins Can Manage Users and Teams** in the UI (or `MANAGE_ORGANIZATION_AUTH` in the API) controls whether an organization administrator can create users and teams.

This setting now exists in both platform gateway and automation controller in Ansible Automation Platform 2.6. During an upgrade the value from automation controller is imported into the platform gateway server. If you decide to change the value of this setting ensure that you change it to the same values in both the platform gateway and automation controller.

Important:

For environments with automation running directly against automation controller, maintain a consistent value for `MANAGE_ORGANIZATION_AUTH` across both automation controller and platform gateway to avoid unexpected behavior.
