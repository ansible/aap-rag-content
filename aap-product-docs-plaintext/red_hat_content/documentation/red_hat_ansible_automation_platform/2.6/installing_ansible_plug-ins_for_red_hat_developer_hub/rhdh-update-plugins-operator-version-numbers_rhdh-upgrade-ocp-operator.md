# 5. Upgrading the Ansible plug-ins on an Operator installation on OpenShift Container Platform
## 5.4. Updating the Ansible plug-ins version numbers for an Operator installation




To upgrade the Ansible plug-ins, you must edit the `rhaap-dynamic-plugins-config` ConfigMap to reference the new OCI image tag.

**Procedure**

1. Log in to your OpenShift Container Platform instance.
1. Navigate to ConfigMaps and select the `    rhaap-dynamic-plugins-config` map.
1. Select the YAML tab to edit the file.
1. In the `    plugins` list, update the version tag at the end of the `    package` URL for both the frontend and backend plugins.


+

```
kind: ConfigMap
apiVersion: v1
metadata:
name: rhaap-dynamic-plugins-config
data:
dynamic-plugins.yaml: |
includes:
- dynamic-plugins.default.yaml
plugins:
# FRONTEND PLUGIN
- disabled: false
# UPDATE the version tag at the end of the URL (e.g., :2.1)
package: 'oci:registry.redhat.io/ansible-automation-platform/automation-portal:2.1'
pluginConfig:
dynamicPlugins:
frontend:
ansible.plugin-backstage-rhaap:
appIcons:
- importName: AnsibleLogo
name: AnsibleLogo
dynamicRoutes:
- importName: AnsiblePage
menuItem:
icon: AnsibleLogo
text: Ansible
path: /ansible

# BACKEND PLUGIN
- disabled: false
# UPDATE the version tag at the end of the URL (e.g., :2.1)
package: 'oci:registry.redhat.io/ansible-automation-platform/automation-portal:2.1'
pluginConfig:
dynamicPlugins:
backend:
ansible.plugin-scaffolder-backend-module-backstage-rhaap: null
```

1. ClickSave.

The Red Hat Developer Hub detects the configuration change and reload the plug-ins automatically.




**Verification**

1. In the OpenShift UI, click **Topology** .
1. Make sure that the Red Hat Developer Hub instance is available.


