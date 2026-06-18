+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-ref_case_study_f5"
template = "docs/aem-title.html"
title = "Case study with F5 example - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_aap_security_use_cases/", "Security automation use cases"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-ref_case_study_f5/aem-page/secure-ref_case_study_f5.html"
last_crumb = "Case study with F5 example"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Case study with F5 example"
oversized = "false"
page_slug = "secure-ref_case_study_f5"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-ref_case_study_f5"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-ref_case_study_f5/toc/toc.json"
type = "aem-page"
+++

# Case study with F5 example

Configure Event-Driven Ansible rulebooks to automatically mitigate threats detected by monitoring tools like Elasticsearch or Kibana. Triggering F5 security solutions immediately stops potential attacks and helps ensure secure application delivery.

This agentless automation system uses existing transport mechanisms, such as APIs and webhooks, for easier interoperability. F5 content collections for Event-Driven Ansible are developed by F5 and certified by Red Hat to ensure reliable automation and support. Together, F5 and Red Hat help organizations to reduce risk, achieve a faster mean time to resolution, and ultimately free up limited resources to focus on high-value tasks.

## Security operations use cases

The following security operations use cases benefit from automation with F5 and Event-Driven Ansible:

### Enriched security investigations

Cyberattacks are perpetual threats to organizations, and security tools generate more alerts than understaffed security teams can investigate. Organizations can generate significant savings by enabling their security teams to identify and remediate issues more efficiently through automation. A common first step for security automation is to expedite the investigation phase of potential security incidents by following pre-defined investigation playbooks. When a new security event triggers an Ansible rulebook, automated workflows gather and correlate data from multiple F5 solutions to significantly decrease the amount of time that the security analyst must spend on the investigation, which results in a faster mean time to identify and contain an incident.

### Improved threat hunting

Enterprises manage a large number of endpoint devices. This attack surface exposes an organization to multiple threat vectors. Many security teams lack the resources to invest in proactive threat hunting, but by using automation to monitor and correlate threat data and produce actionable insights, security teams can prevent security issues more effectively and quickly detect threat exposure.

### Faster response to security incidents

In the context of automated cyberattacks, immediate threat response is vital. Security teams can use automation that executes pre-built, verified workflows for instant response to contain or prevent security incidents, which reduces attacker dwell time and damage. Rules determine which workflows to trigger based on specific events. When the event is detected, automation takes effect to remediate the issue, prevent attacker access, quarantine endpoints, or update security policies to prevent future occurrences. For example, if a malicious user is detected trying to access an application, event monitoring can trigger an Ansible Rulebook that instructs F5 Advanced WAF to block the malicious user while continuing to allow application access by legitimate users.
