+++
template = "docs/aem-title.html"
title = "How to deduplicate host data in reports - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/observe-ref_deduplication_hosts_metrics_utility"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/observe-assembly_metrics_utility/", "Generate consumption-based billing reports with the metrics-utility"]]
category = "Observe"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/observe-ref_deduplication_hosts_metrics_utility/aem-page/observe-ref_deduplication_hosts_metrics_utility.html"
last_crumb = "How to deduplicate host data in reports"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "How to deduplicate host data in reports"
oversized = "false"
page_slug = "observe-ref_deduplication_hosts_metrics_utility"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/observe-ref_deduplication_hosts_metrics_utility"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/observe-ref_deduplication_hosts_metrics_utility/toc/toc.json"
type = "aem-page"
+++

# How to deduplicate host data in reports

Deduplication changes how `metrics-utility` merges individual host records into countable managed nodes when building reports. Deduplication identifies identical hosts to ensure an accurate count of unique hosts.

`metrics-utility` tracks individual hosts based on their hostnames. It tracks any entries that use the same hostname as the host. Additional deduplication strategies are also available using the following environment variable: `METRICS_UTILITY_DEDUPLICATOR=`.

## Deduplication in the `RENEWAL_GUIDANCE` report

The `RENEWAL_GUIDANCE` report uses deduplication to merge several entries for the same managed node into a single entry. This is important to provide accurate counts of managed nodes for subscription renewal.

The default value for `METRICS_UTILITY_DEDUPLICATOR=renewal`. This is the original method, which analyzes `host_name`, `ansible_host`, `ansible_product_serial`, and `ansible_machine_id` separately, and merges entries any duplicated items.

`METRICS_UTILITY_DEDUPLICATOR=renewal` applies deduplication in multiple iterations. It is limited by the `REPORT_RENEWAL_GUIDANCE_DEDUP_ITERATIONS` environment variable, which defaults to `3`.

You can also run `METRICS_UTILITY_DEDUPLICATOR` with the following environment variables:

- `METRICS_UTILITY_DEDUPLICATOR=renewal-hostname`. This is similar to `ccsp`, again preferring `ansible_host` over `host_name` when present. No other fields are considered.
- `METRICS_UTILITY_DEDUPLICATOR=renewal-experimental`. This is similar to `ccsp-experimental`, which first applies the hostname-based deduplication, then deduplicates again, merging when both of the serials match.

## Deduplication in the CCSP or CCSPv2 reports

When generating the CCSP or CCSPv2 reports, you can set deduplication options to avoid counting the same managed node multiple times.

The default value for `METRICS_UTILITY_DEDUPLICATOR=ccsp`. This limits deduplication to hostnames only.

The `ansible_host` variable, from `main_host.variables`, is preferred over `host_name`, from `main_jobhostsummary`, when present.

You can also set `METRICS_UTILITY_DEDUPLICATOR=ccsp-experimental`. This setting merges entries when both their `ansible_product_serial` and `ansible_machine_id` facts are present and duplicated.
