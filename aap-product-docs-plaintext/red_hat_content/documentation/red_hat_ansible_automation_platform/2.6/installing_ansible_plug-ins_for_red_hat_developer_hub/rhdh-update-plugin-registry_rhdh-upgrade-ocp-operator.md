# 5. Upgrading the Ansible plug-ins on an Operator installation on OpenShift Container Platform
## 5.3. Update the plug-in registry




Rebuild your plug-in registry application in your OpenShift cluster with the latest Ansible plug-ins files.

**Prerequisites**

- You have downloaded the Ansible plug-ins files.
- You have set an environment variable, for example `    $DYNAMIC_PLUGIN_ROOT_DIR` , to represent the path to the local directory where you have stored the `    .tar` files.


**Procedure**

1. Log in to your OpenShift Container Platform instance with credentials to create a new application.
1. Open your Red Hat Developer Hub OpenShift project.


```
$ oc project &lt;YOUR_DEVELOPER_HUB_PROJECT&gt;
```


1. Run the following commands to update your plug-in registry build in the OpenShift cluster. The commands assume that `    $DYNAMIC_PLUGIN_ROOT_DIR` represents the directory for your `    .tar` files. Replace this in the command if you have chosen a different environment variable name.


```
$ oc start-build plugin-registry --from-dir=$DYNAMIC_PLUGIN_ROOT_DIR --wait
```


1. When the registry has started, the output displays the following message:


```
Uploading directory "/path/to/dynamic_plugin_root" as binary input for the build …    Uploading finished    build.build.openshift.io/plugin-registry-1 started
```




**Verification**

Verify that the `plugin-registry` has been updated.


1. In the OpenShift UI, click **Topology** .
1. Click the **redhat-developer-hub** icon to view the pods for the plug-in registry.
1. Click **View logs** for the plug-in registry pod.
1. Open the **Terminal** tab and run `    ls` to view the `    .tar` files in the `    plug-in registry` .
1. Verify that the new `    .tar` file has been uploaded.


