# Upgrade Ansible automation portal
## Choose an upgrade path

Select the upgrade procedure that matches how your Ansible automation portal deployment currently delivers Ansible plug-ins.

The following upgrade paths are available:

- **Upgrade with OCI container delivery (recommended):** Your release already uses `pluginMode: oci`, or you will set it during this upgrade.
- **Migrate from tarball to OCI during upgrade:** You currently use the deprecated HTTP plug-in registry and want to move to OCI container delivery in one maintenance window.
- **Upgrade with HTTP plug-in registry (deprecated):** You must stay on tarball delivery temporarily. Refresh tarball files, update the plug-in registry, then upgrade the Helm release.


Note:

If you upgrade in a disconnected or air-gapped OpenShift Container Platform environment, mirror `registry.redhat.io/ansible-automation-platform/automation-portal:<plugin-version>` where `<plugin-version>` is the `imageTagInfo` value from the lifecycle page. Configure `imageRegistry` or `ociPluginImage` before you upgrade.

