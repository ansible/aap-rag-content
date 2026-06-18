+++
title = "Known issues - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-known_issues"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-overview_of_redhat_ansible_intro/", "Ansible Automation Platform release notes"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-known_issues/aem-page/whats_new-known_issues.html"
last_crumb = "Known issues"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Known issues"
oversized = "false"
page_slug = "whats_new-known_issues"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/whats_new-known_issues"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-known_issues/toc/toc.json"
type = "aem-page"
+++

# Known issues

The following release notes detail the known issues for the Ansible Automation Platform general availability released on June 3, 2026

## Execution environment builder

- Git-backed auto-discovery of EE definitions is not implemented; definitions created in EE builder still register in the catalog. Planned for a future release.
- Automated image builds run on GitHub only; GitLab CI/CD builds are planned for a future release.


- Referenced documents are not sorted by relevance when BYOK is enabled. When you use BYOK with the intelligent assistant, document link ordering in the referenced documents list may not reflect query relevance.(AAP-72138)
- Internal file IDs visible in the intelligent assistant's responses. Depending on the LLM you have integrated, the intelligent assistant's responses may expose internal file IDs (identified by a file- prefix).(AAP-72989)
