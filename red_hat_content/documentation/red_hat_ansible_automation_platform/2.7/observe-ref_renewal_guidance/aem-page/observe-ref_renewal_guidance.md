+++
title = "Configure options in the RENEWAL_GUIDANCE report - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/observe-ref_renewal_guidance"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/observe-assembly_metrics_utility/", "Generate consumption-based billing reports with the metrics-utility"]]
category = "Observe"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/observe-ref_renewal_guidance/aem-page/observe-ref_renewal_guidance.html"
last_crumb = "Configure options in the RENEWAL_GUIDANCE report"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure options in the RENEWAL_GUIDANCE report"
oversized = "false"
page_slug = "observe-ref_renewal_guidance"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/observe-ref_renewal_guidance"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/observe-ref_renewal_guidance/toc/toc.json"
type = "aem-page"
+++

# Configure options in the `RENEWAL_GUIDANCE` report

The `RENEWAL_GUIDANCE` report provides historical usage from the HostMetric table, applying deduplication and showing real historical usage for renewal guidance purposes.

To generate this report, set the report type to `METRICS_UTILITY_REPORT_TYPE=RENEWAL_GUIDANCE`.

Important:

This report is currently a tech preview solution. It is designed to provide more information than automation controller when built in the `awx-manage host_metric` command.

## Storage and invocation

The `RENEWAL_GUIDANCE` report supports the use of only local disk storage to store the report results. This report does not have a gather data step. It reads directly from the controller HostMetric table, so it does not store any raw data under the `METRICS_UTILITY_SHIP_PATH`.

```
# All parameters the RENEWAL_GUIDANCE report needs
export METRICS_UTILITY_SHIP_TARGET=controller_db
export METRICS_UTILITY_REPORT_TYPE=RENEWAL_GUIDANCE
export METRICS_UTILITY_SHIP_PATH=/path_to_built_report/...

# Will generate report for 12 months back with ephemeral nodes being nodes
# automated for less than 1 month.
metrics-utility build_report --since=12months --ephemeral=1month
```

## Generate reports to show ephemeral usage

The `metrics-utility` command-line tool can generate reports showing ephemeral usage of managed nodes.

The `RENEWAL_GUIDANCE` report has the capability to list additional sheets with ephemeral usage if the `-ephemeral` parameter is provided. Using the parameter `--ephemeral=1month`, you can define ephemeral nodes as any managed node that has been automated for a maximum of one month, then never automated again. Using this parameter, the total ephemeral usage of the 12-month period is computed as maximum ephemeral nodes used over all 1-month rolling date windows. This sheet is also added into the report.

```
# Will generate report for 12 months back with ephemeral nodes being nodes
# automated for less than 1 month.
metrics-utility build_report --since=12months --ephemeral=1month
```

## Select a date range for your `RENEWAL_GUIDANCE` report

The default behavior of the `RENEWAL_GUIDANCE` report is to build a report for the current date. The following examples describe how to override this default behavior to select a specific date range for your report:

The `RENEWAL_GUIDANCE` report requires a `since` parameter as the parameter is not supported due to the nature of the `HostMetric` data and is always set to `now`. To override a report date range that is already built, use parameter `-force` with the command. For more information, see the following examples:

```
# Build report for a specific date range, including the provided days
metrics-utility build_report --since=2025-03-01

# Build report for a last 12 months from a current date
metrics-utility build_report --since=12months

# Build report for a last 12 months from a current date overwriting an existing report
metrics-utility build_report --since=12months --force
```
