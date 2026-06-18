+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-ref_auditing_incident_detection"
title = "Apply the NIST Cybersecurity Framework - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_hardening_aap/", "Harden the platform security posture"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-ref_auditing_incident_detection/aem-page/secure-ref_auditing_incident_detection.html"
last_crumb = "Apply the NIST Cybersecurity Framework"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Apply the NIST Cybersecurity Framework"
oversized = "false"
page_slug = "secure-ref_auditing_incident_detection"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-ref_auditing_incident_detection"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-ref_auditing_incident_detection/toc/toc.json"
type = "aem-page"
+++

# Apply the NIST Cybersecurity Framework

Ansible Automation Platform should be used to fulfill security policy requirements by applying the NIST Cybersecurity Framework for common use cases, such as:

- Requiring HTTPS for web servers on Red Hat Enterprise Linux.
- Requiring TLS encryption for internal communication between web servers and database servers on Red Hat Enterprise Linux.
- Generating reports showing that the policy is properly deployed.
- Monitoring for drift that violates the policy.
- Automating correction of any policy violation.


This can be done through 5 steps of the cybersecurity framework:

IDENTIFY
Define the requirements to be implemented according to the security policy.

PROTECT
Implement and apply the requirements as an Ansible Playbook.

DETECT
Monitor for drift and generate an audit report.

RESPOND
Explore actions that could be taken when an incident is detected.

RECOVER
Use Ansible to restore the systems to the known good configuration.
