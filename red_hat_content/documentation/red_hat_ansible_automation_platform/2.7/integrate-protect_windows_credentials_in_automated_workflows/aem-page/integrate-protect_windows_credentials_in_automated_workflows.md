+++
template = "docs/aem-title.html"
title = "Protect Windows credentials in automated workflows - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/integrate-protect_windows_credentials_in_automated_workflows"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/integrate-automate_microsoft_windows_with_ansible_automation_platform/", "Integrate with Microsoft Windows"]]
category = "Integrate"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/integrate-protect_windows_credentials_in_automated_workflows/aem-page/integrate-protect_windows_credentials_in_automated_workflows.html"
last_crumb = "Protect Windows credentials in automated workflows"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Protect Windows credentials in automated workflows"
oversized = "false"
page_slug = "integrate-protect_windows_credentials_in_automated_workflows"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/integrate-protect_windows_credentials_in_automated_workflows"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/integrate-protect_windows_credentials_in_automated_workflows/toc/toc.json"
type = "aem-page"
+++

# Protect Windows credentials in automated workflows

When executing automated workflows at runtime, retrieving secrets from a centralized vault safeguards sensitive credentials and enforces corporate compliance.

```
[Ansible Automation Platform]
      |
      +---(Runtime Lookup Request)---> [ CyberArk / HashiCorp Vault ]
      |                                       |
      |                                (Retrieves Secret)
      |                                       v
      +<--(Injects transient variable)--------+
      |
[Target Windows Host]
```

- **CyberArk and HashiCorp Vault**: Automation controller uses native credential lookups to fetch `ansible_password` values from centralized vaults at runtime. Credentials exist only as transient variables in memory during task execution.
- **Azure Key Vault**: For workloads hosted in public cloud infrastructure, use the azure.azcollection to pull administrative passwords dynamically from cloud key management stores.
