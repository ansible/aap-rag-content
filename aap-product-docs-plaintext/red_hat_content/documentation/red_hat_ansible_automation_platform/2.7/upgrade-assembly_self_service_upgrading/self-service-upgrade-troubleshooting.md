# Upgrade Ansible automation portal
## Troubleshoot Ansible automation portal upgrades

You might encounter issues during Ansible automation portal upgrades. The following sections describe common problems and their solutions.

### Plug-in not found or install tries HTTP plug-in registry

**Symptom:** The `install-dynamic-plugins` init container logs reference `http://plugin-registry:8080/...` or report that a plug-in was not found in the in-cluster registry.

**Cause:** `pluginMode` is still set to `tarball` (the chart default) or you did not set `pluginMode: oci` in the values file used for the upgrade.

**Solution:**

1. Check effective values:

```
helm get values <release_name> -n <namespace>
```
To include defaults, add the `--all` flag.

2. Edit backup-values.yaml: set `pluginMode: oci` and set `imageTagInfo` to the plug-in tag from the [Ansible automation portal lifecycle](https://access.redhat.com/page/ansible-automation-platform-self-service-automation-portal-lifecycle) page.

3. Upgrade again:

```
helm upgrade <release_name> openshift-helm-charts/redhat-rhaap-portal \
--version <plugin-version> \
-f backup-values.yaml \
-n <namespace>
```

4. Confirm that the init container logs show `oci://...automation-portal:...` URLs. For more information, see the procedure in the upgrade guide for migrating from tarball to OCI during an upgrade.

### Plug-in or OCI pull errors

**Symptom:** The init container fails during OCI pull or install.

**Cause:** The `imageTagInfo` value is wrong for the chart version, registry authentication is missing, or `pluginMode` is not set to `oci`.

**Solution:**

1. Confirm that backup-values.yaml sets `imageTagInfo` to the plug-in tag from the [Ansible automation portal lifecycle](https://access.redhat.com/page/ansible-automation-platform-self-service-automation-portal-lifecycle) page for your chart version, and sets `pluginMode: oci`.

2. Verify that the registry auth secret exists and matches your Helm release name:

```
oc get secret <release_name>-dynamic-plugins-registry-auth -n <namespace>
```
A secret named `redhat-rhaap-portal-dynamic-plugins-registry-auth` is incorrect if your release name is not `redhat-rhaap-portal`. Recreate the secret by following the OCI container delivery procedure in the upgrade guide.

3. Inspect init container logs on the `<release_name>-rhaap-portal` pod:

```
oc logs <pod_name> -c install-dynamic-plugins -n <namespace>
```

4. Re-upgrade with `-f backup-values.yaml`.

### Plug-in version mismatch (HTTP plug-in registry, deprecated)

**Symptom:** Plug-in load errors occur when `pluginMode` is set to `tarball`.

**Cause:** The plug-in bundle version does not match the Helm chart version.

**Solution:** Refresh the bundle and update the plug-in registry, or migrate to OCI plug-in delivery. For more information, see the procedures in the upgrade guide for updating the plug-in registry and migrating from tarball to OCI during an upgrade.

### Pods stuck in CrashLoopBackOff after upgrade

**Symptom:** Pods restart with a status of `CrashLoopBackOff`.

**Solution:**

1. Check the `install-dynamic-plugins` init container logs and main pod logs:

```
oc logs -n <namespace> <pod_name> --previous
```

2. If logs show database errors, verify database connectivity and secrets.
3. Re-upgrade with `-f backup-values.yaml` after you fix the values or secrets.

### Helm upgrade fails with a release not found error

**Symptom:** Running `helm upgrade` returns an error stating that the release cannot be found.

**Solution:**

1. List all Helm releases in your cluster:

```
helm list --all-namespaces
```

2. Identify the correct release name and namespace for your Ansible automation portal deployment.
3. Run the upgrade command with the correct parameters:

```
helm upgrade <release_name> openshift-helm-charts/redhat-rhaap-portal \
--version <plugin-version> \
-f backup-values.yaml \
-n <namespace>
```

### Custom values lost after upgrade

**Symptom:** OAuth, RBAC, or certificate settings reverted after the upgrade.

**Cause:** The upgrade ran without your values file. This commonly occurs when you upgrade from the console without exporting values first.

**Solution:**

1. If you created backup-values.yaml before the upgrade, re-run the upgrade with the values file:

```
helm upgrade <release_name> openshift-helm-charts/redhat-rhaap-portal \
--version <plugin-version> \
-f backup-values.yaml \
-n <namespace>
```

2. If you did not export values before the upgrade, export what remains and restore missing settings manually:

```
helm get values <release_name> -n <namespace> > recovered-values.yaml
```
Review recovered-values.yaml, restore any missing settings, and upgrade again with `-f recovered-values.yaml`.

