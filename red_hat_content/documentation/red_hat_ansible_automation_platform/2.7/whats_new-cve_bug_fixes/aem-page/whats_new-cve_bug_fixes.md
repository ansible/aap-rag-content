+++
title = "CVE - Bug Fixes - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-cve_bug_fixes"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-overview_of_redhat_ansible_intro/", "Ansible Automation Platform release notes"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-cve_bug_fixes/aem-page/whats_new-cve_bug_fixes.html"
last_crumb = "CVE - Bug Fixes"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "CVE - Bug Fixes"
oversized = "false"
page_slug = "whats_new-cve_bug_fixes"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/whats_new-cve_bug_fixes"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-cve_bug_fixes/toc/toc.json"
type = "aem-page"
+++

# CVE - Bug Fixes

The following release notes detail the CVEs and bug fixes for the Ansible Automation Platform general availability release on June 3, 2026.

This release of Ansible Automation Platform delivers critical security patches addressing multiple CVEs across Automation Controller, Automation Hub, and Ansible Lightspeed, including fixes for a cryptography buffer overflow and a Dynaconf template injection vulnerability. It also includes bug fixes spanning authentication mapping, workload identity, schedule parsing, and Hub memory stability, alongside enhancements to proxy configuration support and MCP telemetry, and a new default-enabled metrics service for OpenShift deployments.

- namespace: aap-operator.v2.7.0-0.1779173639
- cluster: aap-operator.v2.7.0-0.1779173658

## CVE

- Automation controller
  * [CVE-2026-39892](https://access.redhat.com/security/cve/cve-2026-39892): `Cryptography` — buffer overflow via non-contiguous buffer in API. (AAP-75138)
  * [CVE-2026-39892](https://access.redhat.com/security/cve/cve-2026-39892): Updated cryptography package to address version affected by known vulnerability. (AAP-72126)
- Automation hub
  * [CVE-2026-39892](https://access.redhat.com/security/cve/cve-2026-39892): `Cryptography` — buffer overflow via non-contiguous buffer in API. (AAP-75149)
  * [CVE-2026-33154](https://access.redhat.com/security/cve/cve-2026-33154): `Dynaconf` — arbitrary code execution via server-side template injection; dependency updated to 3.2.13. (AAP-69471)
- Ansible Lightspeed
  * [CVE-2026-39892](https://access.redhat.com/security/cve/cve-2026-39892): aap-rag-content — cryptography buffer overflow via non-contiguous buffer in API. (AAP-75144)
  * [CVE-2026-39892](https://access.redhat.com/security/cve/cve-2026-39892): `aap-inventory-mcp-server` — cryptography buffer overflow via non-contiguous buffer in API. (AAP-75142)
- Execution environments
  * [CVE-2026-39892](https://access.redhat.com/security/cve/cve-2026-39892): Updated cryptography package to address version affected by known vulnerability. (AAP-75235)

## Bug fixes

- Ansible automation portal
  * **Survey and form rendering improvements**: Nested survey parameters, conditional form schemas, and password fields now render correctly. Survey passwords are written as secrets.


- Controller
  * Fixed an issue where OIDC workload identity tokens were not applied to cloud credentials during inventory sync, because `populate_workload_identity_tokens()` did not include the cloud credential when called from `RunInventoryUpdate`. (AAP-75205)
  * Fixed an issue where workflow node updates failed when the Job Template had labels without "Prompt on Launch" enabled, causing API or UI updates to prompt fields to return "Field is not configured to prompt on launch." The serializer now validates only the prompt fields included in the request rather than re-validating all persisted prompt state. (AAP-75202)
  * Fixed an issue where `awxkit as_user()` failed to switch the authenticated user when requests were routed through the AAP gateway, because the gateway uses `gateway_sessionid` instead of `sessionid`. A fallback now checks `gateway_sessionid` when no cookie matches `session_cookie_name`. (AAP-75199)
  * Fixed an issue where the Thycotic Secret Server (Delinea) credential plugin failed with an HTTP 500 error when resolving credentials from Delinea Platform URLs due to an older version of `python-tss-sdk`. (AAP-75198)
  * Fixed an issue where at CLI failed on clean install with ModuleNotFoundError: No module named 'packaging' because setup.py listed setuptools instead of packaging as a runtime dependency after the Python 3.12 upgrade. (AAP-74277)
  * Fixed an issue where schedules could not parse a valid RRULE with certain BYHOUR constraints. (AAP-72482)
- Django-ansible-base
  * Fixed an issue where an authenticator map of type "allow" could not recover access once it had been set to false by an earlier deny-all rule. (AAP-75209)
  * Fixed an issue where an authenticator map of type "allow" could not recover access once it had been set to false by an earlier deny-all rule. (AAP-75207)
- Hub
  * Fixed an issue where Automation Hub pods experienced sustained high memory usage under idle conditions because health probes caused progressive memory growth in pulpcore worker processes, approaching configured memory limits and triggering unnecessary HPA scaling events. (AAP-68883)
- Lightspeed
  * Fixed an issue where the containerized installer did not show the image used for Ansible Lightspeed chatbot BYOK configuration. (AAP-73534)
  * Fixed an issue where the containerized installer did not show the image used for Ansible Lightspeed chatbot BYOK configuration. (AAP-72986)
- Platform operator
  * Fixed an issue where a cluster-scoped operator could not resolve PostgreSQL database connections when components were installed in other namespaces. (AAP-75065)
