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

## Ansible automation portal version compatibility

Use the Helm chart version and `imageTagInfo` settings from the lifecycle page for your target release.

When you upgrade Ansible automation portal, use the `redhat-rhaap-portal` Helm chart version and `imageTagInfo` settings documented for your target release on the Ansible automation portal lifecycle page.

- **OCI delivery (recommended):** Set `pluginMode: oci`. Set `imageTagInfo` to the plug-in tag listed for your chart version on the lifecycle page. The chart pulls `registry.redhat.io/ansible-automation-platform/automation-portal:<plugin-version>`.
- **HTTP plug-in registry (deprecated):** Set `pluginMode: tarball`. Refresh the plug-in bundle so its major.minor matches the chart; the bundle patch must be equal to or greater than the chart patch. Prefer migrating from tarball to OCI during upgrade.

## Export and preserve your Helm values

Export your release configuration to a file, merge in upgrade settings such as `pluginMode` and `imageTagInfo`, then pass the file to every `helm upgrade` command to preserve custom settings.

### About this task

Important:

Export and edit your Helm values before you upgrade. Upgrades from the OpenShift Container Platform web console or CLI without `-f backup-values.yaml` can reset custom OAuth, RBAC, and certificate settings.

### Procedure

1.  Identify your Helm release name and namespace:


```
$ helm list -n <namespace>
```

2.  Export the values currently applied to the release:


```
$ helm get values <release_name> -n <namespace> > backup-values.yaml
```
Note:
The `helm get values` command returns only values you supplied at install or on a previous upgrade. It does not list chart defaults. If you never set `pluginMode`, the export might not include it even though the cluster is using the default `tarball` mode.

3.  Edit `backup-values.yaml` on your local machine. Keep existing keys such as OAuth, `clusterRouterBase`, database, and RBAC settings. Add or update the plug-in delivery settings using the plug-in tag from the lifecycle page for your chart version:


```
redhat-developer-hub:
global:
pluginMode: oci
imageTagInfo: "<plugin-version>"
```
Replace `<plugin-version>` with the value from the Ansible automation portal lifecycle page.

4.  Use the file when you upgrade the Helm release:


```
$ helm upgrade <release_name> openshift-helm-charts/redhat-rhaap-portal \
--version <chart_version> \
-f backup-values.yaml \
-n <namespace>
```
If you upgrade from the OpenShift Container Platform web console, export and edit `backup-values.yaml` first, then confirm the YAML view matches your file, including `pluginMode: oci` and the lifecycle-documented `imageTagInfo`, before you click Upgrade.

## Choose an upgrade path

Select the upgrade procedure that matches how your Ansible automation portal deployment currently delivers Ansible plug-ins.

The following upgrade paths are available:

- **Upgrade with OCI container delivery (recommended):** Your release already uses `pluginMode: oci`, or you will set it during this upgrade.
- **Migrate from tarball to OCI during upgrade:** You currently use the deprecated HTTP plug-in registry and want to move to OCI container delivery in one maintenance window.
- **Upgrade with HTTP plug-in registry (deprecated):** You must stay on tarball delivery temporarily. Refresh tarball files, update the plug-in registry, then upgrade the Helm release.


Note:

If you upgrade in a disconnected or air-gapped OpenShift Container Platform environment, mirror `registry.redhat.io/ansible-automation-platform/automation-portal:<plugin-version>` where `<plugin-version>` is the `imageTagInfo` value from the lifecycle page. Configure `imageRegistry` or `ociPluginImage` before you upgrade.

## Upgrade Ansible automation portal with OCI container delivery

Upgrade the Helm chart and plug-in OCI tag when `pluginMode` is `oci`. This path does not require a plug-in registry or Customer Portal tarball files.

### Before you begin

- You completed the pre-upgrade checks and exported your Helm values. Your `backup-values.yaml` includes `pluginMode: oci` and the lifecycle `imageTagInfo` value.
- The secret `<release-name>-dynamic-plugins-registry-auth` exists in the same project as the Helm release, where `<release-name>` is your Helm release name, not the chart name `redhat-rhaap-portal`. If the secret does not exist, create it as described in OCI container delivery in the install guide.

### Procedure

Upgrade from the command line

1.  Log in to your OpenShift Container Platform cluster and select the project that contains your Helm release:


```
$ oc project <namespace>
```

2.  Update your local Helm repository index:


```
$ helm repo update openshift-helm-charts
```

3.  List available chart versions and select the version listed on the lifecycle page for your target release:


```
$ helm search repo openshift-helm-charts/redhat-rhaap-portal
```

4.  Confirm that `backup-values.yaml` includes `pluginMode: oci` and `imageTagInfo` set to the plug-in tag from the lifecycle page. Add them if they are not already set.
5.  Upgrade the Helm release. Always pass `backup-values.yaml` so custom settings are preserved:


```
$ helm upgrade <release_name> openshift-helm-charts/redhat-rhaap-portal \
--version <chart_version> \
-f backup-values.yaml \
-n <namespace>
```
Replace `<release_name>`, `<chart_version>`, and `<namespace>` with your values.

Upgrade from the OpenShift web console

6.  Log in to the OpenShift Container Platform web console.
7.  Switch to the Developer perspective.
8.  Open the project that contains your Ansible automation portal Helm release.
9.  From the navigation menu, select Helm.
10.  Select your Helm release, then select Actions> (and then)Upgrade.
11.  Select the target Chart Version.
12.  In the YAML view, confirm that `redhat-developer-hub.global.pluginMode` is `oci` and `imageTagInfo` matches the lifecycle page and your edited `backup-values.yaml`.
13.  Review the rest of the YAML to ensure custom values are preserved.
14.  Click Upgrade.

### Results

To verify the upgrade:

1. In the Topology view, confirm that Ansible automation portal pods reach **Running** state.

2. Select the deployment named `<release-name>-rhaap-portal`.

3. Open the deployment pod logs.

4. Select the Logs tab and choose the **install-dynamic-plugins** init container.

5. Confirm successful OCI pulls. The tag in the log must match your `imageTagInfo` value. Example output:

```
======= Installing dynamic plugin oci://registry.redhat.io/ansible-automation-platform/automation-portal:<plugin-version>!ansible-backstage-plugin-catalog-backend-module-rhaap
...
-> Successfully installed dynamic plugin oci://registry.redhat.io/ansible-automation-platform/automation-portal:<plugin-version>!ansible-backstage-plugin-catalog-backend-module-rhaap
```
Replace `<plugin-version>` with the value from your `imageTagInfo` setting. If you use a mirror registry, the host in the log reflects your `imageRegistry` or `ociPluginImage` configuration.

## Download the plug-in TAR files (deprecated)

Download the latest `.tar.gz` plug-in bundle for Ansible automation portal from the Red Hat Customer Portal.

### About this task

Important:

The HTTP plug-in registry method is deprecated and will be removed in a future release of Ansible Automation Platform. Red Hat recommends OCI container delivery. Use this procedure only if you cannot migrate to OCI yet and your deployment uses `pluginMode: tarball`.

### Procedure

1.  Create a directory on your local machine and set an environment variable to represent the directory path:


```
$ mkdir /path/to/<automation-portal-plugins>
$ export DYNAMIC_PLUGIN_ROOT_DIR=/path/to/<automation-portal-plugins>
```

2.  In a browser, open the Red Hat Ansible Automation Platform product software downloads page and select the Product Software tab.
3.  Download the Ansible automation portal setup bundle that matches your target chart version on the lifecycle page or the Product Software tab.
The filename format is `ansible-backstage-rhaap-bundle-<plugin-version>.tar.gz`.

4.  Extract the archive into `$DYNAMIC_PLUGIN_ROOT_DIR`:


```
$ tar --exclude='*code*' -xzf ansible-backstage-rhaap-bundle-<plugin-version>.tar.gz -C $DYNAMIC_PLUGIN_ROOT_DIR
```

### Results

Verify extracted files:

```
$ ls $DYNAMIC_PLUGIN_ROOT_DIR
```
You should see `.tgz` plug-in files and matching `.integrity` files.

## Update the plug-in registry (deprecated)

Upload refreshed plug-in tarball files to OpenShift Container Platform and start a new plug-in registry build.

### Before you begin

- You have downloaded the plug-in TAR files for Ansible automation portal.
- You have set an environment variable `$DYNAMIC_PLUGIN_ROOT_DIR` to the directory that contains the TAR files.

### About this task

Important:

Use this procedure only with `pluginMode: tarball`. OCI upgrades do not require a plug-in registry update.

### Procedure

1.  Log in to your OpenShift Container Platform cluster.
2.  Select your automation portal project:


```
$ oc project <namespace>
```

3.  List build configurations and identify your plug-in registry build configuration, for example `plugin-registry` or a legacy name such as `aap-self-service-plugins`:


```
$ oc get buildconfig
```

4.  Start a new build from your local directory:


```
$ oc start-build <build_config_name> --from-dir=$DYNAMIC_PLUGIN_ROOT_DIR --wait
```
Replace `<build_config_name>` with the build configuration name you identified in the previous step.

### Results

Verify the registry update:

1. In the **Topology** view, open the **plugin-registry** details pane.
2. In the **Pods** section, select **View logs** for the new build pod.
3. In the build pod terminal, run `ls` and confirm the new `.tgz` files are present.


After you verify the registry, upgrade the Helm release.

## Upgrade the Helm release

Upgrade the `redhat-rhaap-portal` Helm release after you complete the steps for your plug-in delivery method.

### Before you begin

- You have completed the before-you-upgrade checklist and exported your Helm values.
- For tarball mode: you have updated the plug-in registry and confirmed `pluginMode: tarball` in `backup-values.yaml`.
- For OCI mode: the `<release-name>-dynamic-plugins-registry-auth` secret exists and `backup-values.yaml` includes `pluginMode: oci` and the lifecycle-documented `imageTagInfo`.

### About this task

- **OCI delivery:** Update `imageTagInfo` and the chart version in your values file, then upgrade. You do not refresh a plug-in registry.
- **Tarball delivery (deprecated):** Refresh the plug-in registry first, then upgrade with `pluginMode: tarball` in your values file.


You can upgrade from the command line or from the OpenShift web console.

Note:

For upgrades in air-gapped or disconnected environments, the standard procedure cannot be used directly. You must first mirror the necessary container images to your local registry and prepare the Helm chart for offline use.

For detailed instructions on this process, see [Installing the Ansible automation portal in an air-gapped environment](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_self_service_disconnected_install#self-service-disconnected-install "You can install Ansible automation portal in a disconnected OpenShift Container Platform environment. For new installations, use OCI container delivery and mirror required container images and plug-in artifacts to your internal registry.").

### Procedure

-  **Upgrade from the command line:**
1.  Log in to OpenShift Container Platform and select your project.
2.  Update the Helm repository:


```
$ helm repo update openshift-helm-charts
```

3.  Find the target chart version:


```
$ helm search repo openshift-helm-charts/redhat-rhaap-portal
```

4.  Upgrade with your values file:


```
$ helm upgrade <release_name> openshift-helm-charts/redhat-rhaap-portal \
--version <chart_version> \
-f backup-values.yaml \
-n <namespace>
```
Replace `<release_name>` with the name of your Helm release and `<chart_version>` with the target Helm chart version.

-  **Upgrade from the OpenShift web console:**
1.  Log in to the OpenShift web console and switch to the **Developer** perspective.
2.  Open the project for your Helm release.
3.  Select **Helm**, then select your release.
4.  Select Actions> (and then)Upgrade.
5.  Select the target chart version.
6.  In the **YAML** view, confirm `pluginMode`, `imageTagInfo`, and other custom values match `backup-values.yaml`.
7.  Click Upgrade.

### Results

1. In the **Topology** view, confirm automation portal pods are in a **Running** state.
2. For OCI delivery, verify the `install-dynamic-plugins` init container logs to confirm plug-ins loaded successfully.

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

## Migrate from HTTP plug-in registry to OCI container delivery

Migrate from the deprecated HTTP plug-in registry to OCI container image delivery by switching Helm values and updating your Kubernetes secret configuration.

### Before you begin

Before you begin, ensure you have:

- Registry credentials for `registry.redhat.io` or your mirror registry. You can create a service account at the [Red Hat registry service accounts](https://access.redhat.com/terms-based-registry/) page.
- Your Helm release name and namespace
- OpenShift CLI (`oc`) and Helm CLI installed
- Existing Ansible automation portal installation with HTTP plug-in registry (tarball mode)
- For air-gapped environments: access to your mirror registry from the OpenShift cluster


For detailed prerequisites on creating and configuring registry credentials, see [OCI container delivery](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_self_service_oci_container_delivery "Use OCI container delivery to pull plug-in artifacts from registry.redhat.io/ansible-automation-platform/automation-portal. The plug-in version must match the imageTagInfo value in your Helm chart configuration. This is the recommended method for new installations.").

### About this task

The HTTP plug-in registry delivery method is deprecated and will be removed in a future release of Ansible Automation Platform. OCI container delivery is the recommended approach for new installations and production deployments.

Important:

Back up your current Helm values before you upgrade. Upgrades without `-f backup-values.yaml` can reset custom OAuth, RBAC, and certificate settings. The migration process exports your values, edits only the plug-in delivery method, and reapplies all custom configuration.

### Procedure

1.  Export your current Helm release values:


```
$ helm get values <release-name> -n <namespace> > backup-values.yaml
```
Replace `<release-name>` with your Helm release name (for example, `redhat-rhaap-portal`) and `<namespace>` with your OpenShift namespace (for example, `default`).

2.  Create the `auth.json` file and the OCI registry authentication secret.
The `install-dynamic-plugins` init container uses the authentication secret directly and does not use cluster pull secrets or `imagePullSecrets`. Follow these steps:

1. Create the base64-encoded credentials. Use the `-w0` flag to produce single-line output (required):

```
$ AUTHB64=$(printf '%s' '<username>:<password>' | base64 -w0)
```
Use your Red Hat service account username and password for `registry.redhat.io`, or your mirror registry credentials for air-gapped deployments.

2. Create the `auth.json` file:

```
$ cat > auth.json <<EOF
{
"auths": {
"registry.redhat.io": {
"auth": "${AUTHB64}"
}
}
}
EOF
```
For mirror registries, replace `registry.redhat.io` with your mirror registry host (for example, `yb-artifactory` or `mirror.example.com:5000`).

3. Create the Kubernetes secret. The secret name must include your Helm release name:

```
$ oc create secret generic <release-name>-dynamic-plugins-registry-auth \
--from-file=auth.json=./auth.json -n <namespace>
```
For example, if your release is `redhat-rhaap-portal`, the secret name is `redhat-rhaap-portal-dynamic-plugins-registry-auth`.

4. Verify the secret was created correctly:

```
$ oc get secret <release-name>-dynamic-plugins-registry-auth \
-o jsonpath='{.data.auth\.json}' -n <namespace> | base64 -d
```
The output should display valid JSON with your credentials intact.

3.  Edit `backup-values.yaml` to enable OCI delivery.
Keep all existing custom configuration (OAuth, RBAC, certificate settings, etc.). Add or modify only the plug-in delivery settings:

```yaml
redhat-developer-hub:
global:
pluginMode: oci
imageTagInfo: "<plugin-version>"
```
Replace `<plugin-version>` with the version from your current Helm release (for example, `2.2`). To find the current version, run:

```
$ helm get values <release-name> -n <namespace> | grep imageTagInfo
```

4.  Upgrade the Helm release:


```
$ helm upgrade <release-name> openshift-helm-charts/redhat-rhaap-portal \
-n <namespace> -f backup-values.yaml
```
If you also need to specify a chart version, add `--version <chart-version>`.

5.  Verify the OCI plug-in installation by checking the init container logs.
After the Helm upgrade completes, the pod will restart. Check the `install-dynamic-plugins` init container logs to confirm successful OCI pulls:

```
$ oc logs <pod-name> -c install-dynamic-plugins -n <namespace>
```
Successful output includes messages like:

```
======= Installing dynamic plugin oci://registry.redhat.io/ansible-automation-platform/automation-portal:<plugin-version>!ansible-backstage-plugin-catalog-backend-module-rhaap
...
-> Successfully installed dynamic plugin oci://registry.redhat.io/ansible-automation-platform/automation-portal:<plugin-version>!ansible-backstage-plugin-catalog-backend-module-rhaap
```
The version in the log must match your `imageTagInfo` value. If you see authentication errors or "No such image" messages, see [Troubleshooting the migration](/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-assembly_self_service_upgrading#migrate-tarball-to-oci-troubleshoot "Diagnose and resolve common errors during the migration from HTTP plug-in registry to OCI container delivery.").

6. **Optional:** After you confirm the upgrade is successful, remove the deprecated plug-in registry resources:


```
$ oc delete deployment,service,buildconfig,imagestream plugin-registry -n <namespace>
```
This cleans up the in-cluster HTTP service that hosted the tarball files. Deletion is safe once OCI pulls are confirmed in the pod logs.

### Results

You have successfully migrated from HTTP plug-in registry to OCI container delivery. Ansible automation portal now pulls plug-ins from the OCI registry instead of the deprecated tarball service.

## Migrating in air-gapped and disconnected environments

For air-gapped or disconnected clusters, mirror the OCI images to your internal registry and configure the Helm chart to use your mirror.

For air-gapped or partially disconnected clusters, you must mirror the OCI images to your internal registry and configure the Helm chart to use your mirror instead of `registry.redhat.io`.

### Mirroring Ansible plug-in images

The Ansible plug-in OCI artifacts must be mirrored to your internal registry. Mirror the images from a host with access to `registry.redhat.io`:

```
$ podman pull registry.redhat.io/ansible-automation-platform/automation-portal:<plugin-version>
$ podman tag registry.redhat.io/ansible-automation-platform/automation-portal:<plugin-version> \
<your-mirror-registry>/ansible-automation-platform/automation-portal:<plugin-version>
$ podman push <your-mirror-registry>/ansible-automation-platform/automation-portal:<plugin-version>
```
When mirroring, you must preserve the original repository path. For example, mirror `registry.redhat.io/ansible-automation-platform/automation-portal:2.2` to `<your-mirror-registry>/ansible-automation-platform/automation-portal:2.2`.

### Configuring Helm values for mirror registry

Edit your `backup-values.yaml` to point to your mirror registry:

```yaml
redhat-developer-hub:
global:
pluginMode: oci
imageTagInfo: "<plugin-version>"
imageRegistry: "<your-mirror-registry-host>"
catalogIndex:
image:
registry: "<your-mirror-registry-host>"
upstream:
backstage:
image:
repository: rhdh/rhdh-hub-rhel9
tag: "<platform-version>"
postgresql:
image:
repository: rhel9/postgresql-15
tag: "latest"
```
Key points:

- `imageRegistry` must be the registry **host only** (for example, `yb-artifactory` or `mirror.example.com:5000`). Do not include a repository path.
- `catalogIndex.image.registry` must be set separately — it is not auto-derived from `imageRegistry`. This is required for RHDH 1.9+.
- If your mirror uses a non-standard repository path for the Ansible plug-in image, use `ociPluginImage` instead to specify the full path:

```yaml
redhat-developer-hub:
global:
imageRegistry: "<your-mirror-registry-host>"
ociPluginImage: "<your-mirror-registry-host>/custom-path/automation-portal"
```

### Using custom CA certificates for private registries

If your mirror registry uses a self-signed or internal CA certificate, the `install-dynamic-plugins` init container will fail with an `x509: certificate signed by unknown authority` error. You must mount your CA certificate into the init container.

The recommended approach is to create a ConfigMap and mount it at the per-registry trust path. For complete instructions, see the RHDH documentation on installing plug-ins from OCI registries by using custom certificates.

## Troubleshooting the migration

Diagnose and resolve common errors during the migration from HTTP plug-in registry to OCI container delivery.

### Authentication failures

**Symptom:** Init container logs show `authentication required` or `unauthorized: access denied`.

**Cause:** The `<release-name>-dynamic-plugins-registry-auth` secret is missing, malformed, or has incorrect credentials.

**Resolution:**

1. Verify the secret exists:

```
$ oc get secret <release-name>-dynamic-plugins-registry-auth -n <namespace>
```

2. Check the secret contents:

```
$ oc get secret <release-name>-dynamic-plugins-registry-auth \
-o jsonpath='{.data.auth\.json}' -n <namespace> | base64 -d
```
The output should be valid JSON with your credentials.

3. Ensure the secret name matches your Helm release name exactly. For example, if your release is `redhat-rhaap-portal`, the secret must be `redhat-rhaap-portal-dynamic-plugins-registry-auth`.

4. Recreate the secret with correct credentials if needed:

```
$ oc delete secret <release-name>-dynamic-plugins-registry-auth -n <namespace>
$ oc create secret generic <release-name>-dynamic-plugins-registry-auth \
--from-file=auth.json=./auth.json -n <namespace>
```

### Duplicate registry path in OCI URLs

**Symptom:** Init container logs or Helm values show duplicate paths, for example: `oci://yb-artifactory/ansible-automation-platform/ansible-automation-platform/automation-portal:2.2`.

**Cause:** The `imageRegistry` value includes a repository path instead of being the registry host only.

**Resolution:** Edit your `backup-values.yaml` and set `imageRegistry` to the registry host only, without the repository path:

```yaml
# Incorrect (includes repository path):
imageRegistry: "yb-artifactory/ansible-automation-platform"

# Correct (host only):
imageRegistry: "yb-artifactory"
```
Then re-run `helm upgrade` with the corrected values file.

### x509 certificate errors for private registries

**Symptom:** Init container logs show `x509: certificate signed by unknown authority` or `x509: certificate has expired`.

**Cause:** Your mirror registry uses a self-signed or internal CA certificate that the `skopeo` utility cannot verify.

**Resolution:** Mount your CA certificate into the init container at the per-registry trust path. Obtain your CA certificate bundle (including the full chain), create a ConfigMap, and update your Helm values to mount it. For detailed instructions, see the RHDH documentation: [Install plugins from OCI registries by using custom certificates](https://redhat-developer.github.io/red-hat-developers-documentation-rhdh/main/plugins-rhdh-install/#rinstall-plugins-from-oci-registries-by-using-custom-certificates).

### No such image error

**Symptom:** Init container logs show `Error: no such image` or `manifest not found`.

**Cause:** The OCI image does not exist in the specified registry, or the `imageTagInfo` version does not match what is available.

**Resolution:**

1. Verify the `imageTagInfo` value in your Helm release matches an available version. Check the [Ansible automation portal lifecycle](https://access.redhat.com/page/ansible-automation-platform-self-service-automation-portal-lifecycle) page.
2. If using a mirror registry, ensure the image was mirrored to the correct path. Run:

```
$ podman search <your-mirror-registry>/ansible-automation-platform/automation-portal
```

3. Confirm that `imageRegistry` is set correctly and does not include a duplicate repository path (see the Duplicate registry path section above).

### Integrity check errors

**Symptom:** Init container logs show `integrity check failed` or `digest mismatch`.

**Cause:** The OCI image in your registry does not match the expected digest, or the image was corrupted during mirroring.

**Resolution:**

1. Re-mirror the image from `registry.redhat.io` using `skopeo copy` instead of `podman tag/push`. The `skopeo copy` command preserves the original manifest digest:

```
$ skopeo copy \
docker://registry.redhat.io/ansible-automation-platform/automation-portal:<plugin-version> \
docker://<your-mirror-registry>/ansible-automation-platform/automation-portal:<plugin-version>
```

2. If the error persists, verify the image in your mirror registry:

```
$ skopeo inspect docker://<your-mirror-registry>/ansible-automation-platform/automation-portal:<plugin-version>
```

3. Ensure you are not using a stale local image cache. Delete and re-pull if needed.

### Accessing init container logs

To view the logs of the `install-dynamic-plugins` init container:

```
$ oc get pods -n <namespace> -l app.kubernetes.io/component=backstage
$ oc logs <pod-name> -c install-dynamic-plugins -n <namespace>
```
If the pod has already completed (e.g., if the init container succeeded), you can view the previous logs:

```
$ oc logs <pod-name> -c install-dynamic-plugins --previous -n <namespace>
```
If the pod is still running, stream logs in real time:

```
$ oc logs -f <pod-name> -c install-dynamic-plugins -n <namespace>
```
