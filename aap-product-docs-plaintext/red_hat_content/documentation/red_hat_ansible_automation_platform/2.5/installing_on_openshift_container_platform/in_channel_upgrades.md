# 6. Upgrading Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform
## 6.4. Channel upgrades
### 6.4.1. In-channel upgrades




Most upgrades occur within a channel as follows:

1. A new update becomes available in the marketplace, through the redhat-operator CatalogSource.
1. The system automatically creates a new InstallPlan for your Ansible Automation Platform subscription.


- If set to **Manual** , the InstallPlan needs manual approval in the OpenShift UI.
- If set to **Automatic** , it upgrades as soon as the new version is available.

Note
Set a manual install strategy on your Ansible Automation Platform Operator subscription during installation or upgrade. You will be prompted to approve upgrades when available in your chosen update channel. Stable channels, like stable-2.5, are available for each X.Y release.





1. A new subscription, CSV, and operator containers are created alongside the old ones. The old resources are cleaned up after a successful install.


