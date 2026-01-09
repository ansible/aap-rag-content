# 4. Upgrading the Ansible plug-ins on a Helm installation on OpenShift Container Platform
## 4.3. Updating the Ansible plug-ins version numbers for a Helm installation




You must navigate to the Helm chart’s YAML view in the OpenShift Developer UI and replace the old version numbers and integrity hash values for both Ansible plug-ins, which triggers a restart of the Developer Hub pods to finalize the upgrade.

**Procedure**

1. Log in to your OpenShift Container Platform instance.
1. In the OpenShift Developer UI, navigate toHelm→developer-hub→Actions→Upgrade→Yaml view.
1. Update the Ansible plug-ins version numbers and associated `    .integrity` file values.


```
...    global:    ...        plugins:          - disabled: false            integrity: &lt;SHA512 value&gt;            package: 'http://plugin-registry:8080/ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz'            pluginConfig:              dynamicPlugins:                frontend:                  ansible.plugin-backstage-rhaap:                    appIcons:                      - importName: AnsibleLogo                        name: AnsibleLogo                    dynamicRoutes:                      - importName: AnsiblePage                        menuItem:                          icon: AnsibleLogo                          text: Ansible                        path: /ansible          - disabled: false            integrity: &lt;SHA512 value&gt;            package: &gt;-              http://plugin-registry:8080/ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz            pluginConfig:              dynamicPlugins:                backend:                  ansible.plugin-scaffolder-backend-module-backstage-rhaap: null
```


1. ClickUpgrade.

The developer hub pods restart and the plug-ins are installed.




**Verification**

1. In the OpenShift UI, click **Topology** .
1. Make sure that the Red Hat Developer Hub instance is available.


