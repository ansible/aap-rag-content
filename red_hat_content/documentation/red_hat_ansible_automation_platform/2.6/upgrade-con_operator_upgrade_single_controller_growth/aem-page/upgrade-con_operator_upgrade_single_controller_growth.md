+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-con_operator_upgrade_single_controller_growth"
title = "2.4 single automation controller node deployment to a 2.6 growth topology - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-con_upgrade_infrastructure_operator_deployments/", "Infrastructure changes for Operator-based deployments"]]
category = "Upgrade"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/upgrade-con_operator_upgrade_single_controller_growth/aem-page/upgrade-con_operator_upgrade_single_controller_growth.html"
last_crumb = "2.4 single automation controller node deployment to a 2.6 growth topology"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "2.4 single automation controller node deployment to a 2.6 growth topology"
oversized = "false"
page_slug = "upgrade-con_operator_upgrade_single_controller_growth"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/upgrade-con_operator_upgrade_single_controller_growth"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/upgrade-con_operator_upgrade_single_controller_growth/toc/toc.json"
type = "aem-page"
+++

# 2.4 single automation controller node deployment to a 2.6 growth topology

Plan your upgrade from a 2.4 single automation controller node setup to a 2.6 growth topology. Review the required infrastructure changes and requirements for a successful upgrade.

## 2.4 infrastructure topology diagram

This diagram outlines the 2.4 infrastructure topology for this deployment model.

*Figure 1. 2.4 infrastructure topology diagram*

![2.4 single controller topology](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/ocp-a-controller-2-4.png)

## 2.6 infrastructure topology diagram

This diagram outlines the 2.6 infrastructure topology that Red Hat has tested with this deployment model.

*Figure 2. 2.6 infrastructure topology diagram*

![2.6 growth topology](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/ocp-a-controller-2-6.png)

## Requirements for upgrading a single automation controller node deployment

The following table highlights the requirements for upgrading from Ansible Automation Platform 2.4 to 2.6.

| Existing 2.4 topology                                                                                                                           | Tested 2.6 topology                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Requirements for each pod                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| <br>Non-redundant automation controller-only deployment:<br>One automation controller web podOne automation controller task podOne database pod | <br>Growth topology:<br>One automation controller web podOne automation controller task podOne automation hub web podOne automation hub API podTwo automation hub content podsTwo automation hub worker podsOne automation hub Redis podOne Event-Driven Ansible controller API podOne Event-Driven Ansible controller activation worker podOne Event-Driven Ansible controller default worker podOne Event-Driven Ansible controller event stream podOne Event-Driven Ansible controller scheduler podOne platform gateway podOne database podOne Redis pod | <br>See the **Operator growth topology** section of *Tested deployment models*. |
