+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-con_upgrade_to_aap_2_7"
title = "Upgrade to Ansible Automation Platform 2.7 - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-con_upgrade_to_aap_2_7/", "Upgrade to Ansible Automation Platform 2.7"]]
category = "Upgrade"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-con_upgrade_to_aap_2_7/aem-page/upgrade-con_upgrade_to_aap_2_7.html"
last_crumb = "Upgrade to Ansible Automation Platform 2.7"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Upgrade to Ansible Automation Platform 2.7"
oversized = "false"
page_slug = "upgrade-con_upgrade_to_aap_2_7"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/upgrade-con_upgrade_to_aap_2_7"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-con_upgrade_to_aap_2_7/toc/toc.json"
type = "aem-page"
+++

# Upgrade to Ansible Automation Platform 2.7

Start here to upgrade your Ansible Automation Platform deployment to version 2.7. Review supported source versions and changes that affect your upgrade path, then follow the upgrade procedure for your deployment type.

## Supported source versions

You can upgrade to Ansible Automation Platform 2.7 from the following versions:

- **Ansible Automation Platform 2.6** (containerized on Red Hat Enterprise Linux (RHEL), or Operator-based on OpenShift Container Platform)
- **Ansible Automation Platform 2.5** (containerized on RHEL, or Operator-based on OpenShift Container Platform)

If you are running an RPM-based deployment or a version earlier than 2.5, you must first migrate to a supported 2.6 containerized or Operator-based deployment before upgrading to 2.7.

## Before you upgrade

Review the following changes that affect your upgrade path and any actions you must take before and after the upgrade:

- **Determine your upgrade path**: Find the supported upgrade paths and RHEL version compatibility for your deployment type.
- **Infrastructure changes by deployment type**: Understand topology and architecture changes that apply to your deployment.
- **Identity and access management changes**: Review authentication provider migration and post-upgrade requirements.
- **API changes in 2.7**: Check for deprecated or removed API endpoints that affect your integrations.

## Upgrade your deployment

After you have reviewed the planning information, follow the upgrade procedure for your deployment type:

- **Upgrade your containerized deployment**: For Ansible Automation Platform deployed with the containerized installer on Red Hat Enterprise Linux.
- **Upgrade your Operator-based deployment**: For Ansible Automation Platform deployed with the Ansible Automation Platform Operator on OpenShift Container Platform.
