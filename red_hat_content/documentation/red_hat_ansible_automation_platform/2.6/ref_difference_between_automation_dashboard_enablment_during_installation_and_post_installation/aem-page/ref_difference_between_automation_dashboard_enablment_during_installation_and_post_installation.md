+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/ref_difference_between_automation_dashboard_enablment_during_installation_and_post_installation"
title = "Difference between automation dashboard enablement during-installation and post-installation - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/ref_difference_between_automation_dashboard_enablment_during_installation_and_post_installation/aem-page/ref_difference_between_automation_dashboard_enablment_during_installation_and_post_installation.html"
last_crumb = "Difference between automation dashboard enablement during-installation and post-installation"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Difference between automation dashboard enablement during-installation and post-installation"
oversized = "false"
page_slug = "ref_difference_between_automation_dashboard_enablment_during_installation_and_post_installation"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/ref_difference_between_automation_dashboard_enablment_during_installation_and_post_installation"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/ref_difference_between_automation_dashboard_enablment_during_installation_and_post_installation/toc/toc.json"
type = "aem-page"
+++

# Difference between automation dashboard enablement during-installation and post-installation

Use this reference when choosing between during-installation and post-installation dashboard enablement to compare historical data collection, downtime requirements, and time to availability.

## Comparison of enablement approaches

| Aspect               | During Installation                        | Post-Installation                                   |
| -------------------- | ------------------------------------------ | --------------------------------------------------- |
| When to use          | New Ansible Automation Platform deployment | Existing Ansible Automation Platform installation   |
| Historical data      | No historical data (new installation)      | Up to 90 days backfilled                            |
| Downtime             | Part of initial installation               | None (container restart only)                       |
| Time to dashboard    | Immediate after first collection (6 hours) | Available after backfill completes (hours to 1 day) |
| Configuration effort | One-time during install                    | Update inventory/CR and re-run installer            |

## Decision criteria

**Choose during-installation enablement when:**

- Deploying a new Ansible Automation Platform environment
- No historical data needed (starting fresh)
- You want dashboard available immediately after first collection cycle
- Installation downtime is already planned


**Choose post-installation enablement when:**

- Ansible Automation Platform is already in production
- You need historical data from existing automation jobs
- Zero downtime is required
- You want to evaluate dashboard with real historical trends
