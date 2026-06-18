+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-ref_pre_upgrade_assessment_checklist"
template = "docs/aem-title.html"
title = "Pre-upgrade migration checklist - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-ref_pre_upgrade_assessment_checklist/", "Pre-upgrade migration checklist"]]
category = "Upgrade"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-ref_pre_upgrade_assessment_checklist/aem-page/upgrade-ref_pre_upgrade_assessment_checklist.html"
last_crumb = "Pre-upgrade migration checklist"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Pre-upgrade migration checklist"
oversized = "false"
page_slug = "upgrade-ref_pre_upgrade_assessment_checklist"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/upgrade-ref_pre_upgrade_assessment_checklist"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-ref_pre_upgrade_assessment_checklist/toc/toc.json"
type = "aem-page"
+++

# Pre-upgrade migration checklist

Before upgrading to Red Hat Ansible Automation Platform 2.7, assess the environment to identify components and integrations that require migration to gateway-based authentication.

Before upgrading, identify the following items in your environment:

- Scripts using direct component URLs (for example, `controller.example.com`, `hub.example.com`, or `eda.example.com`).
- Configuration as Code (CaC) implementations.
- Active Personal Access Tokens (PATs).
- API integrations and custom applications.
- Container registry workflows, such as `podman login` or `docker login`.
- Certified collection usage, specifically the latest versions of `ansible.controller`, `ansible.hub`, and `ansible.eda` (these may be replaced by `ansible.platform`).
- Third-party authentication provider configurations, including LDAP, SAML, RADIUS, and TACACS+.

## Pre-upgrade detection tooling

A CLI detection tool is available to identify direct API usage in Ansible Automation Platform 2.5 or 2.6 environments. The tool analyzes NGINX logs to detect requests that bypass platform gateway.

You can run the tool directly from the GitHub repository using `uvx`.

**Prerequisites**

- Ansible Automation Platform 2.5 or 2.6 is installed.
- You have one of the following, depending on your deployment type:
  * Containerized deployments: An SOSReport.
  * OpenShift Container Platform deployments: A must-gather or ocp-inspect output.


Note:

The tool requires NGINX log format updates introduced in the Ansible Automation Platform 2.6 patch released March 25, 2026. If you are running an earlier 2.6.x patch and your logs do not contain the required fields, apply the provided patch script or upgrade to the latest 2.6.x release.

**Scan a containerized or RPM SOSReport:**

```
$ uvx --from "git+https://github.com/ansible/aap-detect-direct-component-access" aap-detect-direct-component-access /path/to/sosreport/
```
**Scan an OpenShift must-gather tarball:**

```
$ uvx --from "git+https://github.com/ansible/aap-detect-direct-component-access" aap-detect-direct-component-access /path/to/must-gather/
```
**Scan an OpenShift Container Platform inspect output:**

```
$ uvx --from "git+https://github.com/ansible/aap-detect-direct-component-access" aap-detect-direct-component-access /path/to/ocp-inspect/
```
