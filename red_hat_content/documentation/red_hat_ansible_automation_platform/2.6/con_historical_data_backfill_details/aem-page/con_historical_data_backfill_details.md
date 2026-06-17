+++
template = "docs/aem-title.html"
title = "Historical data backfill details - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/con_historical_data_backfill_details"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/con_historical_data_backfill_details/aem-page/con_historical_data_backfill_details.html"
last_crumb = "Historical data backfill details"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Historical data backfill details"
oversized = "false"
page_slug = "con_historical_data_backfill_details"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/con_historical_data_backfill_details"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/con_historical_data_backfill_details/toc/toc.json"
type = "aem-page"
+++

# Historical data backfill details

Understand how automation dashboard backfills historical data after post-installation enablement by learning the backfill scope, behavior, performance impact, and duration estimates for dashboard data collection.

## Backfill scope and behavior

**How backfill works:**

When you enable dashboard post-installation, metrics service initiates a historical data backfill using the following logic:

- **Starting point:** 90 days before current time (`since = now - 90 days`)
- **End point:** Current time (`until = now`)
- **Data query:** Requests all jobs in Controller (AWX) database between `since` and `until`
- **Collection:** Collects whatever data exists in that timeframe


Important:

90 days is the starting point, not a minimum or maximum requirement. Metrics service collects all available data within the 90-day window.

**Examples:**

| Controller Data Available                | Data Collected | Result                                               |
| ---------------------------------------- | -------------- | ---------------------------------------------------- |
| 90+ days of job history                  | 90 days        | Backfill collects maximum (90 days from since point) |
| 30 days of job history                   | 30 days        | Backfill collects all available data (no error)      |
| 0 days of job history (new installation) | 0 jobs         | Backfill completes successfully with`job_count: 0`   |


**Key points:**

- Less than 90 days of data is not an error - backfill collects what exists
- Backfill does not fail if Controller has less than 90 days of data
- New installations with no historical jobs complete backfill immediately (within minutes)

## Backfill process control

The backfill process runs to completion automatically and cannot be paused or resumed. Once initiated, it continues until all available data within the 90-day window is collected. If metrics service is restarted during backfill, the process resumes from the last successful checkpoint.

## Performance impact and duration

| Aspect             | Details                                                                                |
| ------------------ | -------------------------------------------------------------------------------------- |
| Data Source        | Controller (awx) database by using`ms_readonly` user (read-only access)                |
| Performance Impact | Minimal - backfill uses same read-only queries as regular collection, spread over time |
| Duration           | Varies based on data volume; typically completes within 24 hours for large datasets    |
| Automatic          | Yes - no manual intervention required after enablement                                 |


**Estimated completion times:**

| Data Volume (Controller Jobs) | Estimated Backfill Duration |
| ----------------------------- | --------------------------- |
| < 10,000 jobs                 | Under 5 minutes             |
| 10,000 - 50,000 jobs          | 5–20 minutes                |
| 50,000 - 100,000 jobs         | 20–45 minutes               |
| > 100,000 jobs                | 45 minutes–2 hours          |


Note:

These duration figures are estimates. Actual duration depends on job complexity, number of hosts per job, database performance, and system load.
