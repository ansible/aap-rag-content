# Prerequisites and channel upgrades

To upgrade to a newer version of Ansible Automation Platform Operator, you must:

Ensure your system meets the system requirements detailed in the **Operator topologies** section of the*Tested deployment models* .

- Create **AutomationControllerBackup** and **AutomationHubBackup** objects. For help with this see **Backup and recovery for operator environments**
- Review the **Release notes** for the new Ansible Automation Platform version to which you are upgrading and any intermediate versions.
- Determine the type of upgrade you want to perform. See the **Channel Upgrades** section for more information.

## Channel upgrades

Upgrading Ansible Automation Platform involves retrieving updates from a channel. A channel refers to a location where you can access your update from the OpenShift console UI.

![Update channel](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/aap-2-6-channels.png)

### In-channel upgrades

Most upgrades occur within a channel as follows:

1. A new update becomes available in the marketplace, through the redhat-operator CatalogSource.
2. The system automatically creates a new InstallPlan for your Ansible Automation Platform subscription.   - If set to **Manual**, the InstallPlan needs manual approval in the OpenShift UI.
- If set to **Automatic**, it upgrades as soon as the new version is available.  Note:
Set a manual install strategy on your Ansible Automation Platform Operator subscription during installation or upgrade. You will be prompted to approve upgrades when available in your chosen update channel. A stable channel is available for each X.Y release, following the naming pattern `stable-*X.Y*`.

3. A new subscription, CSV, and operator containers are created alongside the old ones. The old resources are cleaned up after a successful install.

### Cross-channel upgrades

Upgrading between X.Y channels is always manual and intentional. Stable channels for major and minor versions are in the Operator Catalog. It is recommended to stay on the latest minor version channel for the latest patches.

If the subscription is set for manual upgrades, you must approve the upgrade in the UI. Then, the system upgrades the Operator to the latest version in that channel.

Note:

It is recommended to set a manual install strategy on your Ansible Automation Platform Operator subscription during installation or upgrade. You will be prompted to approve upgrades when they become available in your chosen update channel. Stable channels, such as stable-2.7, are available for each X.Y release.

The containers provided in the latest channel are updated regularly for OS upgrades and critical fixes. This allows customers to receive critical patches and CVE fixes faster. Larger changes and new features are saved for minor and major releases.

For each major or minor version channel, there is a corresponding "cluster-scoped" channel available. Cluster-scoped channels deploy operators that can manage all namespaces, while non-cluster-scoped channels can only manage resources in their own namespace.

Important:

Cluster-scoped bundles are not compatible with namespace-scoped bundles. Do not switch between namespace-scoped (`stable-*X.Y*`) channels and cluster-scoped (`stable-*X.Y*-cluster-scoped`) channels. This is not supported.
