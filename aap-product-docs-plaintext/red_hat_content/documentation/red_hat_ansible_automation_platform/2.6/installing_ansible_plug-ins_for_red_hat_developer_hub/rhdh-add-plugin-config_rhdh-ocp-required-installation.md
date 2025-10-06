# 2. Installing the Ansible plug-ins with a Helm chart on OpenShift Container Platform
## 2.5. Required configuration
### 2.5.1. Adding the Ansible plug-ins configuration




1. In the OpenShift Developer UI, navigate toHelm→developer-hub→Actions→Upgrade→Yaml view.
1. Update the Helm chart configuration to add the dynamic plug-ins in the Red Hat Developer Hub instance. Under the `    plugins` section in the YAML file, add the dynamic plug-ins that you want to enable.


```
global:      ...        plugins:          - disabled: false            integrity: &lt;SHA512 Integrity key for ansible-plugin-backstage-rhaap-dynamic plugin&gt;            package: 'http://plugin-registry:8080/ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz'            pluginConfig:              dynamicPlugins:                frontend:                  ansible.plugin-backstage-rhaap:                    appIcons:                      - importName: AnsibleLogo                        name: AnsibleLogo                    dynamicRoutes:                      - importName: AnsiblePage                        menuItem:                          icon: AnsibleLogo                          text: Ansible                        path: /ansible          - disabled: false            integrity: &lt;SHA512 Integrity key for ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic plugin&gt;            package: &gt;-              http://plugin-registry:8080/ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz            pluginConfig:              dynamicPlugins:                backend:                  ansible.plugin-scaffolder-backend-module-backstage-rhaap: null
```


1. In the `    package` sections, replace `    x.y.z` in the plug-in filenames with the correct version numbers for the Ansible plug-ins.
1. For each Ansible plug-in, update the integrity values using the corresponding `    .integrity` file content.
1. ClickUpgrade.

The developer hub pods restart and the plug-ins are installed.




**Verification**

To verify that the plug-ins have been installed, open the `install-dynamic-plugin` container logs and check that the Ansible plug-ins are visible in Red Hat Developer Hub:


1. Open the Developer perspective for the Red Hat Developer Hub application in the OpenShift Web console.
1. Select the **Topology** view.
1. Select the Red Hat Developer Hub deployment pod to open an information pane.
1. Select the **Resources** tab of the information pane.
1. In the **Pods** section, click **View logs** to open the **Pod details** page.
1. In the **Pod details** page, select the **Logs** tab.
1. Select `    install-dynamic-plugins` from the drop-down list of containers to view the container log.
1. In the `    install-dynamic-plugin` container logs, search for the Ansible plug-ins.

The following example from the log indicates a successful installation for one of the plug-ins:


```
=&gt; Successfully installed dynamic plugin http://plugin-registry-1:8080/ansible-plugin-backstage-rhaap-dynamic-1.1.0.tgz
```

The following image shows the container log in the **Pod details** page. The version numbers and file names can differ.

![container logs for install-dynamic-plugin](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Installing_Ansible_plug-ins_for_Red_Hat_Developer_Hub-en-US/images/70103d03251d3babcbbacc093de282f4/rhdh-check-plugin-config.png)





