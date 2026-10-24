+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-con_operator_upgrade_overview"
title = "Overview - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-assembly_operator_upgrade/", "Upgrade your Operator-based deployment of Ansible Automation Platform"]]
category = "Upgrade"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-con_operator_upgrade_overview/aem-page/upgrade-con_operator_upgrade_overview.html"
last_crumb = "Overview"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Overview"
oversized = "false"
page_slug = "upgrade-con_operator_upgrade_overview"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/upgrade-con_operator_upgrade_overview"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-con_operator_upgrade_overview/toc/toc.json"
type = "aem-page"
+++

# Overview

The Ansible Automation Platform Operator coordinates the upgrade of all platform components on OpenShift Container Platform. Review what the operator handles automatically and what requires manual action.

Important:

Upgrading from version 2.4 or 2.5 is not supported. Upgrade to Red Hat Ansible Automation Platform 2.6 before upgrading to version 2.7.

See the Upgrading Red Hat Ansible Automation Platform Operator in the version 2.6 documentation, for help updating to 2.6.

## How operator upgrades work

The Ansible Automation Platform Operator uses OpenShift Operator Lifecycle Manager (OLM) to manage upgrades. When a new operator version becomes available in your subscription channel, OLM creates an InstallPlan that you can review and approve before the upgrade begins.

After you approve the InstallPlan, the upgrade proceeds in the following sequence:

1. OLM replaces the current operator pod with the new version. The new operator pod starts and begins reconciling your custom resources (CRs).
2. The operator evaluates the deployed versions of automation controller, automation hub, and Event-Driven Ansible against the versions bundled with the new operator release.
3. The operator updates each component by rolling out new container images. Component pods restart one at a time in a rolling fashion to maintain availability where possible.
4. The operator updates the status fields on each CR to reflect the new versions and reconciliation state.

Each operator release bundles specific default versions of automation controller, automation hub, and Event-Driven Ansible. When the operator upgrades, it automatically upgrades all managed components to these bundled versions unless you have overridden a component version in the CR spec.

## Expected behavior during upgrade

During an operator upgrade, expect the following behavior:

- **Brief service interruptions** occur as component pods restart. The duration depends on the size of your deployment and the number of components being upgraded.
- **Component pods restart in sequence**, not all at once. You may see a mix of old and new pods running during the rollout.
- **Running jobs in automation controller** may be interrupted if a controller pod restarts during execution. Schedule upgrades during a maintenance window to avoid disruption to active automation.
- **Database migrations** run automatically as part of the component startup process. For large databases, this can extend the time before a component becomes fully available.
- **Custom resource status** fields update throughout the process. The upgrade is complete when all CRs report a healthy status and all pods show a `Running` or `Completed` state.

## What the operator does not handle

The operator automates the core platform upgrade, but several tasks require manual action before or after the upgrade:

- **Execution node updates.** For operator-based deployments, execution node updates at the OS level are not managed by the operator. You must update execution nodes manually after the control plane upgrade completes.
- **API endpoint and integration changes.** If the new release includes API changes, such as the migration to platform gateway in Ansible Automation Platform 2.7, you must update scripts, playbooks, and external integrations separately.
- **Authentication provider migration.** Changes to authentication configuration, such as moving third-party providers from component-level to platform gateway, require manual reconfiguration.
- **Backup and restore.** The operator does not create backups before an upgrade. You must create `AutomationControllerBackup`, `AutomationHubBackup`, and `EDABackup` resources before starting the upgrade.
- **OpenShift Container Platform version compatibility.** The operator does not verify whether your OpenShift cluster version is supported by the target Ansible Automation Platform release. You must confirm compatibility before upgrading.

## Patch updates compared with version upgrades

The operator supports two types of upgrades, each with different scope and risk profiles:

In-channel patch updates
Patch updates deliver bug fixes, security patches, and minor improvements within the same Ansible Automation Platform version (for example, 2.6.1 to 2.6.2). These updates are lower risk and typically do not include breaking changes. If your subscription is set to automatic approval, patch updates apply as soon as they are available.

Cross-channel version upgrades
Version upgrades move your deployment to a new Ansible Automation Platform release (for example, 2.6 to 2.7). These upgrades require you to change the subscription channel, are always manual, and may include infrastructure changes, API changes, or authentication changes that require additional preparation.

## Subscription channel in the OpenShift console

![Subscription tab in the OpenShift console](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/aap-operator-stable-2.7-deployment.png)
