# Upgrade Ansible automation portal
## Ansible automation portal version compatibility

Use the Helm chart version and `imageTagInfo` settings from the lifecycle page for your target release.

When you upgrade Ansible automation portal, use the `redhat-rhaap-portal` Helm chart version and `imageTagInfo` settings documented for your target release on the Ansible automation portal lifecycle page.

- **OCI delivery (recommended):** Set `pluginMode: oci`. Set `imageTagInfo` to the plug-in tag listed for your chart version on the lifecycle page. The chart pulls `registry.redhat.io/ansible-automation-platform/automation-portal:<plugin-version>`.
- **HTTP plug-in registry (deprecated):** Set `pluginMode: tarball`. Refresh the plug-in bundle so its major.minor matches the chart; the bundle patch must be equal to or greater than the chart patch. Prefer migrating from tarball to OCI during upgrade.

