# Upgrade Ansible automation portal
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

