# 3. Installing the Ansible plug-ins with the Operator on OpenShift Container Platform
## 3.5. Installing the dynamic plug-ins




To install the dynamic plugins, add them to your ConfigMap for your RHDH plugin settings (for example, `rhaap-dynamic-plugins-config` ).

If you have not already created a ConfigMap file for your RHDH plugin settings, create one by following the procedure in the [Creating and using config maps](https://docs.redhat.com/en/documentation/openshift_container_platform/4.15/html-single/nodes/index#configmaps) section of the OpenShift Container Platform _Nodes_ guide.

**Procedure**

1. Select **ConfigMaps** in the navigation pane of the OpenShift console.
1. Select the `    rhaap-dynamic-plugins-config` ConfigMap from the list.
1. Select the **YAML** tab to edit the `    rhaap-dynamic-plugins-config` ConfigMap.
1. Add the Ansible plug-ins. Choose the configuration that matches your delivery method.


- OCI container delivery method (recommended):


```
kind: ConfigMap        apiVersion: v1        metadata:          name: rhaap-dynamic-plugins-config        data:          dynamic-plugins.yaml: |            includes:              - dynamic-plugins.default.yaml            plugins:              - disabled: false                package: 'oci://registry.redhat.io/ansible-automation-platform/automation-portal:2.1!ansible-plugin-backstage-rhaap'                pluginConfig:                  dynamicPlugins:                    frontend:                      ansible.plugin-backstage-rhaap:                        appIcons:                          - importName: AnsibleLogo                            name: AnsibleLogo                        dynamicRoutes:                          - importName: AnsiblePage                            menuItem:                              icon: AnsibleLogo                              text: Ansible                            path: /ansible              - disabled: false                package: 'oci://registry.redhat.io/ansible-automation-platform/automation-portal:2.1!ansible-plugin-scaffolder-backend-module-backstage-rhaap'                pluginConfig:                  dynamicPlugins:                    backend:                      ansible.plugin-scaffolder-backend-module-backstage-rhaap: null
```

Replace `        x.y.z` with the Ansible plug-ins version.


- HTTP plug-in registry method:


```
kind: ConfigMap        apiVersion: v1        metadata:          name: rhaap-dynamic-plugins-config        data:          dynamic-plugins.yaml: |            includes:              - dynamic-plugins.default.yaml            plugins:              - disabled: false                package: 'http://plugin-registry:8080/ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz'                integrity: &lt;SHA512 value&gt;                pluginConfig:                  dynamicPlugins:                    frontend:                      ansible.plugin-backstage-rhaap:                        appIcons:                          - importName: AnsibleLogo                            name: AnsibleLogo                        dynamicRoutes:                          - importName: AnsiblePage                            menuItem:                              icon: AnsibleLogo                              text: Ansible                            path: /ansible              - disabled: false                package: &gt;-                  http://plugin-registry:8080/ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz                integrity: &lt;SHA512 value&gt;                pluginConfig:                  dynamicPlugins:                    backend:                      ansible.plugin-scaffolder-backend-module-backstage-rhaap: null
```



1. ClickSave.


**Verification**

1. In the OpenShift console, select the **Topology** view.
1. Click the **Open URL** icon on the deployment pod to open your Red Hat Developer Hub instance in a browser window.


The Ansible plug-in is present in the navigation pane. If you select **Administration** , you can see the installed plug-ins in the **Plugins** tab.

