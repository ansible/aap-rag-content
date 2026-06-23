# Upgrade Ansible automation portal
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

