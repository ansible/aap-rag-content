+++
title = "Original Certified Cloud and Service Provider (CCSP) report - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/observe-ref_ccsp"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/observe-assembly_metrics_utility/", "Generate consumption-based billing reports with the metrics-utility"]]
category = "Observe"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/observe-ref_ccsp/aem-page/observe-ref_ccsp.html"
last_crumb = "Original Certified Cloud and Service Provider (CCSP) report"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Original Certified Cloud and Service Provider (CCSP) report"
oversized = "false"
page_slug = "observe-ref_ccsp"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/observe-ref_ccsp"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/observe-ref_ccsp/toc/toc.json"
type = "aem-page"
+++

# Original Certified Cloud and Service Provider (CCSP) report

`CCSP` is the original report format. It does not include many of the customization of CCSPv2, and the intention is only to use it for the CCSP partner program.

## Optional collectors for `gather` command

You can use the following optional collectors for the `gather` command:

-  `main_jobhostsummary`
  * If present by default, this collects the `main_jobhostsummary` table from the automation controller database, and has information about jobs runs and managed nodes automated.
-  `main_host`
  * This collects daily snapshots of the `main_host` table from the automation controller database and has managed nodes/hosts present across automation controller inventories,
-  `main_jobevent`
  * This collects the `main_jobevent` table from the automation controller database and has information about which modules, roles, and ansible collections are being used.
-  `main_indirectmanagednodeaudit`
  * This collects the `main_indirectmanagednodeaudit` table from the automation controller database and has information about indirectly managed nodes,

```
# Example with all optional collectors
export METRICS_UTILITY_OPTIONAL_COLLECTORS="main_host,main_jobevent,main_indirectmanagednodeaudit"
```

## Optional sheets for `build_report` command

You can use the following optional sheets for the `build_report` command:

-  `ccsp_summary`
  * This is a landing page specifically for partners under the CCSP program. It shows managed node usage by each automation controller organization.
  * This report takes additional parameters to customize the summary page. For more information, see the following example:

```
export METRICS_UTILITY_PRICE_PER_NODE=11.55 # in USD
export METRICS_UTILITY_REPORT_SKU=MCT3752MO
export METRICS_UTILITY_REPORT_SKU_DESCRIPTION="EX: Red Hat Ansible Automation Platform, Full Support (1 Managed Node, Dedicated, Monthly)"
export METRICS_UTILITY_REPORT_H1_HEADING="CCSP Reporting <Company>: ANSIBLE Consumption"
export METRICS_UTILITY_REPORT_COMPANY_NAME="Company Name"
export METRICS_UTILITY_REPORT_EMAIL="email@email.com"
export METRICS_UTILITY_REPORT_RHN_LOGIN="test_login"
export METRICS_UTILITY_REPORT_COMPANY_BUSINESS_LEADER="BUSINESS LEADER"
export METRICS_UTILITY_REPORT_COMPANY_PROCUREMENT_LEADER="PROCUREMENT LEADER"
```

-  `managed_nodes`
  * This is a deduplicated list of managed nodes automated by automation controller.
-  `indirectly_managed_nodes`
  * This is a deduplicated list of indirect managed nodes automated by automation controller.
-  `inventory_scope`
  * This is a deduplicated list of managed nodes present across all inventories of automation controller.
-  `usage_by_collections`
  * This is a list of Ansible collections used in automation controller job runs.
-  `usage_by_roles`
  * This is a list of roles used in automation controller job runs.
-  `usage_by_modules`
  * This is a list of modules used in automation controller job runs.

```
# Example with all optional sheets
export METRICS_UTILITY_OPTIONAL_CCSP_REPORT_SHEETS='ccsp_summary,managed_nodes,indirectly_managed_nodes,inventory_scope,usage_by_collections,usage_by_roles,usage_by_modules'
```

## Select a date range for your CCSP report

By default, the CCSPv2 report generates data for the previous calendar month. You can override this behavior by specifying a different month when you run the `metrics-utility build_report` command.

The default behavior of this report is to build a report for the previous month. The following examples describe how to override this default behavior to select a specific date range for your report:

```
# Builds report for a previous month
metrics-utility build_report

# Build report for a specific month
metrics-utility build_report --month=2025-03

# Build report for a specific month overwriting an existing report
metrics-utility build_report --month=2025-03 --force
```
