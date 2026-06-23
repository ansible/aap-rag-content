# Patch update for Operator-based Ansible Automation Platform
## Patch updating Ansible Automation Platform on OpenShift Container Platform

When you perform a patch update for an installation of Ansible Automation Platform on OpenShift Container Platform, most updates happen within a channel:

1. A new update becomes available in the marketplace (through the redhat-operator CatalogSource).
2. A new InstallPlan is automatically created for your Ansible Automation Platform subscription. If the subscription is set to Manual, the InstallPlan must be manually approved in the OpenShift UI. If the subscription is set to Automatic, it upgrades as soon as the new version is available. Note:
Set a manual install strategy on your Ansible Automation Platform Operator subscription. With a manual strategy, you are prompted to approve an upgrade when it becomes available in your selected update channel. Stable channels are available for each X.Y release (for example, stable-*X.Y*).

3. A new Subscription, CSV, and Operator containers will be created alongside the old Subscription, CSV, and containers. Then the old resources will be cleaned up if the new install was successful.
