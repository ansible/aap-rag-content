# Migrate from HTTP plug-in registry to OCI container delivery

Migrate from the deprecated HTTP plug-in registry to OCI container image delivery by switching Helm values and updating your Kubernetes secret configuration.

## Before you begin

Before you begin, ensure you have:

- Registry credentials for `registry.redhat.io` or your mirror registry. You can create a service account at the [Red Hat registry service accounts](https://access.redhat.com/terms-based-registry/) page.
- Your Helm release name and namespace
- OpenShift CLI (`oc`) and Helm CLI installed
- Existing Ansible automation portal installation with HTTP plug-in registry (tarball mode)
- For air-gapped environments: access to your mirror registry from the OpenShift cluster


For detailed prerequisites on creating and configuring registry credentials, see [OCI container delivery](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_self_service_oci_container_delivery "Use OCI container delivery to pull plug-in artifacts from registry.redhat.io/ansible-automation-platform/automation-portal. The plug-in version must match the imageTagInfo value in your Helm chart configuration. This is the recommended method for new installations.").

## About this task

The HTTP plug-in registry delivery method is deprecated and will be removed in a future release of Ansible Automation Platform. OCI container delivery is the recommended approach for new installations and production deployments.

Important:

Back up your current Helm values before you upgrade. Upgrades without `-f backup-values.yaml` can reset custom OAuth, RBAC, and certificate settings. The migration process exports your values, edits only the plug-in delivery method, and reapplies all custom configuration.

## Procedure

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

## Results

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
