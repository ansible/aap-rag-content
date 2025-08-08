# 7. Upgrading Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform
## 7.4. Channel upgrades
### 7.4.2. Cross-channel upgrades




Upgrading between X.Y channels is always manual and intentional. Stable channels for major and minor versions are in the Operator Catalog. Currently, only version 2.x is available, so there are few channels. It is recommended to stay on the latest minor version channel for the latest patches.

If the subscription is set for manual upgrades, you must approve the upgrade in the UI. Then, the system upgrades the Operator to the latest version in that channel.

Note
It is recommended to set a manual install strategy on your Ansible Automation Platform Operator subscription during installation or upgrade. You will be prompted to approve upgrades when they become available in your chosen update channel. Stable channels, such as stable-2.5, are available for each X.Y release.



The containers provided in the latest channel are updated regularly for OS upgrades and critical fixes. This allows customers to receive critical patches and CVE fixes faster. Larger changes and new features are saved for minor and major releases.

For each major or minor version channel, there is a corresponding "cluster-scoped" channel available. Cluster-scoped channels deploy operators that can manage all namespaces, while non-cluster-scoped channels can only manage resources in their own namespace.

Important
Cluster-scoped bundles are not compatible with namespace-scoped bundles. Do not try to switch between normal (stable-2.4 for example) channels and cluster-scoped (stable-2.4-cluster-scoped) channels, as this is not supported.



