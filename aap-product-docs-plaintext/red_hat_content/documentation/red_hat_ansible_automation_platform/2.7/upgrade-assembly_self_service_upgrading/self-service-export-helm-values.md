# Upgrade Ansible automation portal
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

