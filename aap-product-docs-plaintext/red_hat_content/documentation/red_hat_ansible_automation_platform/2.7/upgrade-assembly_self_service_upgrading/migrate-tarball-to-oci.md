# Upgrade Ansible automation portal
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

