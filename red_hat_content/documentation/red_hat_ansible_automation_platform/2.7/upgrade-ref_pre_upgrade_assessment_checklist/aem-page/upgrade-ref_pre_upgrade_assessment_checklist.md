+++
title = "Pre-upgrade checklist - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-ref_pre_upgrade_assessment_checklist"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-ref_pre_upgrade_assessment_checklist/", "Pre-upgrade checklist"]]
category = "Upgrade"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-ref_pre_upgrade_assessment_checklist/aem-page/upgrade-ref_pre_upgrade_assessment_checklist.html"
last_crumb = "Pre-upgrade checklist"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Pre-upgrade checklist"
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

# Pre-upgrade checklist

Before upgrading to Red Hat Ansible Automation Platform 2.7, verify that your environment meets all requirements and identify components that require updates.

## Platform and version requirements

Verify the following platform requirements before you begin the upgrade:

- Your deployment is running the latest Ansible Automation Platform 2.6 release.
- Your deployment uses a containerized or OpenShift Container Platform installation method. RPM-based deployments cannot upgrade directly to 2.7.
- For containerized deployments: Red Hat Enterprise Linux 9 or Red Hat Enterprise Linux 10.
- For Operator-based deployments: OpenShift Container Platform 4.18 through 4.23 with `cluster-admin` access.
- You have a valid Red Hat Ansible Automation Platform subscription.
- PostgreSQL version compatibility: PostgreSQL 15 for platform-managed databases, or PostgreSQL 15, 16, or 17 with International Components for Unicode (ICU) support for customer-provided databases.

## Backup and data protection

Complete the following backup tasks before you upgrade:

- Back up your Ansible Automation Platform deployment. For more information, see *Back up your Ansible Automation Platform instance*.
- Back up the `metrics_service` database if you use the metrics service.
- Record your current inventory file settings and instance group configurations.
- Document your current `SECRET_KEY` value and any custom encryption artifacts used by your deployment.

## Gateway authentication assessment

Ansible Automation Platform 2.7 requires all external authentication and API access to go through platform gateway. Identify the following items in your environment that require migration to gateway-based authentication:

- Scripts that use direct component URLs, such as `controller.example.com`, `hub.example.com`, or `eda.example.com`.
- Configuration as Code (CaC) implementations that reference component-specific endpoints.
- Active Personal Access Tokens (PATs) that were created through individual component interfaces.
- API integrations and custom applications that connect to component-specific APIs.
- Container registry workflows, such as `podman login` or `docker login` commands that target component hostnames.
- Certified collection usage, specifically the latest versions of `ansible.controller`, `ansible.hub`, and `ansible.eda`. These collections may be replaced by `ansible.platform`.
- Third-party authentication provider configurations, including LDAP, SAML, RADIUS, and TACACS+.
- Platform gateway accounts are configured for all users who require access after the upgrade.

## Run the pre-upgrade detection tool

Use the pre-upgrade detection tool to identify direct API usage in your Ansible Automation Platform 2.6 environment. The tool analyzes NGINX logs to detect requests that bypass platform gateway.

- For containerized deployments, collect an SOSReport from your deployment.
- For OpenShift Container Platform deployments, collect a must-gather or `ocp-inspect` output.

Note:

The tool requires NGINX log format updates introduced in the Ansible Automation Platform 2.6 patch released March 25, 2026. If your logs do not contain the required fields, apply the provided patch script or upgrade to the latest 2.6.x release before running the detection tool.

For more information, see *Pre-upgrade detection tooling*.

## Infrastructure and environment checks

Verify the following infrastructure and environment settings before you upgrade:

- TLS certificates include Subject Alternative Name (SAN) entries for the platform gateway hostname in addition to existing component hostnames.
- For deployments that use proxy servers, verify that `no_proxy` entries use the correct case. The `no_proxy` environment variable is case-sensitive on Red Hat Enterprise Linux.
- For containerized deployments on Red Hat Enterprise Linux with custom mount points, verify that SELinux contexts are set correctly on all non-default paths used by Ansible Automation Platform.
- For deployments that use NFS-backed storage, verify that NFS mount permissions allow read and write access for the Ansible Automation Platform service accounts.
- For Operator-based deployments, verify that PersistentVolumeClaim (PVC) sizes are sufficient for post-upgrade data growth. Review the sizing guidelines in *Automation Orchestrator system requirements*.
- The `oc` CLI is installed and authenticated to your OpenShift cluster (Operator-based deployments only).

## Integration and automation readiness

Verify the following integration and automation items before you upgrade:

- You have access to your project `requirements.yml` files and execution environment definition files.
- You have verified that your custom execution environments use a Python version compatible with Ansible Automation Platform 2.7.
- You have permissions to rebuild execution environments in your deployment.
- You have downloaded the latest version of the Ansible Automation Platform containerized installer or verified access to the updated Operator catalog.
- You have updated your Ansible Automation Platform collections to the latest versions compatible with 2.7, including `ansible.controller`, `ansible.hub`, `ansible.eda`, or `ansible.platform`.

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
