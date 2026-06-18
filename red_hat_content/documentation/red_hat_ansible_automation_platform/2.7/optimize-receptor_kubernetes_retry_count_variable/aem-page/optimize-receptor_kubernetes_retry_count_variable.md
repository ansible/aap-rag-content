+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/optimize-receptor_kubernetes_retry_count_variable"
title = "Fine-tune Receptor worker backoff strategies for API reliability - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/optimize-assembly_pod_spec_modifications/", "Performance tuning for operator environments"]]
category = "Optimize"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/optimize-receptor_kubernetes_retry_count_variable/aem-page/optimize-receptor_kubernetes_retry_count_variable.html"
last_crumb = "Fine-tune Receptor worker backoff strategies for API reliability"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Fine-tune Receptor worker backoff strategies for API reliability"
oversized = "false"
page_slug = "optimize-receptor_kubernetes_retry_count_variable"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/optimize-receptor_kubernetes_retry_count_variable"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/optimize-receptor_kubernetes_retry_count_variable/toc/toc.json"
type = "aem-page"
+++

# Fine-tune Receptor worker backoff strategies for API reliability

Configure the Receptor worker within the Ansible Automation Platform Operator through the`RECEPTOR_KUBE_RETRY_COUNT` environment variable. This variable controls how the worker handles Kubernetes API connection failures.

Note:

The retry mechanism uses an exponential backoff strategy which is capped at 5 minutes to prevent excessive wait times during job execution errors.

*Table 1. RECEPTOR_KUBE_RETRY_COUNT details*

| Variable                    | Description                                                                                                                                                                         | Default value | Valid range |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ----------- |
| `RECEPTOR_KUBE_RETRY_COUNT` | Sets the maximum number of retry attempts for Kubernetes API operations within the Receptor worker. Retry delays increase using exponential backoff with a Fibonacci-like sequence. | 5             | 1-100       |
