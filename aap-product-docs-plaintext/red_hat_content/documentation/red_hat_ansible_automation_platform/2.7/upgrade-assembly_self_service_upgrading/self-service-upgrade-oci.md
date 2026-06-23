# Upgrade Ansible automation portal
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

