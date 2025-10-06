# 3. Installing the Ansible plug-ins with the Operator on OpenShift Container Platform
## 3.6. Installing the dynamic plug-ins




To install the dynamic plugins, add them to your ConfigMap for your RHDH plugin settings (for example, `rhaap-dynamic-plugins-config` ).

If you have not already created a ConfigMap file for your RHDH plugin settings, create one by following the procedure in the [Creating and using config maps](https://docs.redhat.com/en/documentation/openshift_container_platform/4.15/html-single/nodes/index#configmaps) section of the OpenShift Container Platform _Nodes_ guide.

The example ConfigMap used in the following procedure is called `rhaap-dynamic-plugins-config` .

**Procedure**

1. Select **ConfigMaps** in the navigation pane of the OpenShift console.
1. Select the `    rhaap-dynamic-plugins-config` ConfigMap from the list.
1. Select the **YAML** tab to edit the `    rhaap-dynamic-plugins-config` ConfigMap.
1. In the `    data.dynamic-plugins.yaml.plugins` block, add the three dynamic plug-ins from the plug-in registry.


- For the `        integrity` hash values, use the `        .integrity` files in your `        $DYNAMIC_PLUGIN_ROOT_DIR` directory that correspond to each plug-in, for example use `        ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz.integrity` for the `        ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz` plug-in.
- Replace `        x.y.z` with the correct version of the plug-ins.


```
kind: ConfigMap        apiVersion: v1        metadata:         name: rhaap-dynamic-plugins-config        data:         dynamic-plugins.yaml: |           ...           plugins:             - disabled: false               package: 'http://plugin-registry:8080/ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz'               integrity: &lt;SHA512 value&gt; # Use hash in ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz.integrity               pluginConfig:                 dynamicPlugins:                   frontend:                     ansible.plugin-backstage-rhaap:                       appIcons:                         - importName: AnsibleLogo                           name: AnsibleLogo                       dynamicRoutes:                         - importName: AnsiblePage                           menuItem:                             icon: AnsibleLogo                             text: Ansible                           path: /ansible             - disabled: false               package: &gt;-                 http://plugin-registry:8080/ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz               integrity: &lt;SHA512 value&gt; # Use hash in ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz.integrity               pluginConfig:                 dynamicPlugins:                   backend:                     ansible.plugin-scaffolder-backend-module-backstage-rhaap: null             - ...&lt;REDACTED&gt;
```



1. ClickSave.
1. To view the progress of the rolling restart:


1. In the **Topology** view, select the deployment pod and click **View logs** .
1. Select `        install-dynamic-plugins` from the list of containers.



**Verification**

1. In the OpenShift console, select the **Topology** view.
1. Click the **Open URL** icon on the deployment pod to open your Red Hat Developer Hub instance in a browser window.


The Ansible plug-in is present in the navigation pane, and if you select **Administration** , the installed plug-ins are listed in the **Plugins** tab.

