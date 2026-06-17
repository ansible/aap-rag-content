# 7. Uninstalling an Operator installation on OpenShift Container Platform
## 7.1. Removing the Ansible plug-ins from the ConfigMap

To remove the Ansible plug-ins from an Operator installation, you must edit the custom ConfigMap that references the plug-ins. You can either delete the entire plug-in entry block or simply disable the plug-ins by setting the disabled attribute to `true`.

**Procedure**

1. Open the custom ConfigMap where you referenced the Ansible plug-ins.

For this example, the ConfigMap name is `rhaap-dynamic-plugins-config`.

2. Locate the dynamic plug-ins in the `plugins:` block.


- For OCI delivery, the entries to remove or disable:

plugins:
- disabled: false
package: 'oci://registry.redhat.io/ansible-automation-platform/automation-portal:2.1!ansible-plugin-backstage-rhaap'
pluginConfig:
...
- disabled: false
package: 'oci://registry.redhat.io/ansible-automation-platform/automation-portal:2.1!ansible-plugin-scaffolder-backend-module-backstage-rhaap'
pluginConfig:
...

- For HTTP plug-in registry, the entries use `<http://plugin-registry:8080/>...` URLs instead.

3. Click Save.

