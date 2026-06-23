# Upgrade Ansible automation portal

Upgrade the Helm chart and plug-in artifacts for your target release.

Important:

If you are upgrading from plug-in version 2.1 to 2.2, you must grant navigation permissions to existing roles. The Templates and History sidebar items now require explicit `ansible.templates.view` and `ansible.history.view` permission grants. Without these permissions, non-admin users cannot see the Templates and History navigation items. Administrators and superusers are unaffected.

After upgrading, log in as an administrator, navigate to Administration> (and then)RBAC, and add `ansible.templates.view` and `ansible.history.view` to each role that requires access. For more information, see *Configuring role-based access control for Ansible automation portal*.

To upgrade Ansible automation portal:

1. Prepare versions and values. See *Before you upgrade*.
2. Choose your upgrade path. See *Choose an upgrade path*.
3. Complete the procedure for that path:
- **OCI container delivery (recommended):** Use `pluginMode: oci` and pull plug-ins from `registry.redhat.io` (or your mirror). See *Upgrade Ansible automation portal with OCI container delivery*.
- **HTTP plug-in registry (deprecated):** Refresh tarball files in-cluster. Plan to *migrate from tarball to OCI during upgrade*.


## Before you upgrade

- **Versions:** Consult the Ansible automation portal lifecycle page for Helm chart version, `imageTagInfo`, and Ansible Automation Platform compatibility. Run `helm search repo openshift-helm-charts/redhat-rhaap-portal` and select the chart version that matches the lifecycle page.
- **Values:** Export and preserve your Helm values. Use `-f backup-values.yaml` on every upgrade (OpenShift console or CLI). Upgrades without this file can reset custom OAuth, RBAC, and certificate settings.
- **OCI delivery:** Set `pluginMode: oci` in `backup-values.yaml`. The chart default is `tarball`; without `oci`, upgrades keep deprecated tarball mode.

