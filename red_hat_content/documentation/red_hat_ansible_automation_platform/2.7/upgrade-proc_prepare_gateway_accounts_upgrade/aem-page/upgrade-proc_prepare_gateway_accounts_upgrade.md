+++
title = "Prepare platform gateway accounts for the 2.7 upgrade - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-proc_prepare_gateway_accounts_upgrade"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-proc_prepare_gateway_accounts_upgrade/", "Prepare platform gateway accounts for the 2.7 upgrade"]]
category = "Upgrade"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-proc_prepare_gateway_accounts_upgrade/aem-page/upgrade-proc_prepare_gateway_accounts_upgrade.html"
last_crumb = "Prepare platform gateway accounts for the 2.7 upgrade"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Prepare platform gateway accounts for the 2.7 upgrade"
oversized = "false"
page_slug = "upgrade-proc_prepare_gateway_accounts_upgrade"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/upgrade-proc_prepare_gateway_accounts_upgrade"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-proc_prepare_gateway_accounts_upgrade/toc/toc.json"
type = "aem-page"
+++

# Prepare platform gateway accounts for the 2.7 upgrade

In Red Hat Ansible Automation Platform 2.6, users without a platform gateway account can authenticate using an automation controller password. In Ansible Automation Platform 2.7, this fallback authentication mechanism is removed.

## About this task

Important:

You must configure platform gateway accounts for all users before upgrading. Users cannot authenticate after the upgrade if they rely on the automation controller password fallback.

## Procedure

1.  Identify users who authenticate through the automation controller password fallback.
2.  Create platform gateway accounts for these users or instruct users to set platform gateway passwords.
  
  Note:
      If you miss this step before upgrading, automation controller accounts are automatically created in platform gateway during the upgrade, but passwords are not set. Users with automatically-created accounts must reset their passwords before they can log in.

## Results

Confirm that all active users can log in to their platform gateway accounts.
