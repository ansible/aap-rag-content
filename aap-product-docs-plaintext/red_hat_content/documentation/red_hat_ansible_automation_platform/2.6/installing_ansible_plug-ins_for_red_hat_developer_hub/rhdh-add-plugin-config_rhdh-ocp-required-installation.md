# 2. Installing the Ansible plug-ins with a Helm chart on OpenShift Container Platform
## 2.4. Required configuration
### 2.4.1. Adding the Ansible plug-ins configuration




Modify the Red Hat Developer Hub Helm chart to add the Ansible plug-ins. The configuration depends on the plug-in delivery method you chose earlier.

**Procedure**

1. In the OpenShift Developer UI, navigate toHelm→developer-hub→Actions→Upgrade→Yaml view.
1. Update the Helm chart configuration to add the dynamic plug-ins in the Red Hat Developer Hub instance. Under the `    plugins` section in the YAML file, add the dynamic plug-ins that you want to enable. Choose the configuration that matches your delivery method.


- OCI container delivery (recommended):


```
global:          dynamic:            includes:              - dynamic-plugins.default.yaml            plugins:              - disabled: false                package: 'oci://registry.redhat.io/ansible-automation-platform/automation-portal:21!ansible-plugin-backstage-rhaap'                pluginConfig:                  dynamicPlugins:                    frontend:                      ansible.plugin-backstage-rhaap:                        appIcons:                          - importName: AnsibleLogo                            name: AnsibleLogo                        dynamicRoutes:                          - importName: AnsiblePage                            menuItem:                              icon: AnsibleLogo                              text: Ansible                            path: /ansible              - disabled: false                package: 'oci://registry.redhat.io/ansible-automation-platform/automation-portal:2.1!ansible-plugin-scaffolder-backend-module-backstage-rhaap'                pluginConfig:                  dynamicPlugins:                    backend:                      ansible.plugin-scaffolder-backend-module-backstage-rhaap: null
```

Replace `        x.y.z` with the Ansible plug-ins version.

Note
OCI delivery does not require the `        integrity` hash values. The OCI registry handles integrity verification.




- HTTP plug-in registry:


```
global:          dynamic:            includes:              - dynamic-plugins.default.yaml            plugins:              - disabled: false                integrity: &lt;SHA512 value&gt;                package: 'http://plugin-registry:8080/ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz'                pluginConfig:                  dynamicPlugins:                    frontend:                      ansible.plugin-backstage-rhaap:                        appIcons:                          - importName: AnsibleLogo                            name: AnsibleLogo                        dynamicRoutes:                          - importName: AnsiblePage                            menuItem:                              icon: AnsibleLogo                              text: Ansible                            path: /ansible              - disabled: false                integrity: &lt;SHA512 value&gt;                package: &gt;-                  http://plugin-registry:8080/ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz                pluginConfig:                  dynamicPlugins:                    backend:                      ansible.plugin-scaffolder-backend-module-backstage-rhaap: null
```

Replace `        x.y.z` with the correct plug-in version numbers and update the `        integrity` values using the corresponding `        .integrity` file content.



1. ClickUpgrade.

The Red Hat Developer Hub pods restart and the plug-ins are installed.




**Verification**

To verify that the plug-ins have been installed, open the `install-dynamic-plugin` container logs:


1. Open the Developer perspective for the Red Hat Developer Hub application in the OpenShift Web console.
1. Select the **Topology** view.
1. Select the Red Hat Developer Hub deployment pod to open an information pane.
1. Select the **Resources** tab of the information pane.
1. In the **Pods** section, click **View logs** to open the **Pod details** page.
1. In the **Pod details** page, select the **Logs** tab.
1. Select `    install-dynamic-plugins` from the drop-down list of containers to view the container log.


- For OCI delivery, a successful installation displays:


```
=&gt; Successfully installed dynamic plugin oci:registry.redhat.io/ansible-automation-platform/ansible-plugin-backstage-rhaap-dynamic:x.y.z
```


- For HTTP plug-in registry, a successful installation displays:


```
=&gt; Successfully installed dynamic plugin http://plugin-registry:8080/ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz
```





