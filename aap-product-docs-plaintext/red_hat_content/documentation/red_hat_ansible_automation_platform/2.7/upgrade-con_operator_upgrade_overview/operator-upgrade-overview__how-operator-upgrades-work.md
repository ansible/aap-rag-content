# Overview
## How operator upgrades work

The Ansible Automation Platform Operator uses OpenShift Operator Lifecycle Manager (OLM) to manage upgrades. When a new operator version becomes available in your subscription channel, OLM creates an InstallPlan that you can review and approve before the upgrade begins.

After you approve the InstallPlan, the upgrade proceeds in the following sequence:

1. OLM replaces the current operator pod with the new version. The new operator pod starts and begins reconciling your custom resources (CRs).
2. The operator evaluates the deployed versions of automation controller, automation hub, and Event-Driven Ansible against the versions bundled with the new operator release.
3. The operator updates each component by rolling out new container images. Component pods restart one at a time in a rolling fashion to maintain availability where possible.
4. The operator updates the status fields on each CR to reflect the new versions and reconciliation state.

Each operator release bundles specific default versions of automation controller, automation hub, and Event-Driven Ansible. When the operator upgrades, it automatically upgrades all managed components to these bundled versions unless you have overridden a component version in the CR spec.

