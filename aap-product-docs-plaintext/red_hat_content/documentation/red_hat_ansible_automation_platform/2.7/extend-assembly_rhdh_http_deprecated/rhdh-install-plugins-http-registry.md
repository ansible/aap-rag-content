# Install Ansible plug-ins using an HTTP plug-in registry (deprecated)
## Install the plug-ins from the HTTP registry

Add the Ansible plug-ins from the HTTP registry to your Red Hat Developer Hub dynamic plug-in configuration.

### About this task

For each plug-in, you need the HTTP URL to the `.tgz` file in the registry and the SHA-512 integrity hash from the corresponding `.integrity` file.

### Procedure

1.  Add the plug-ins to your dynamic plug-ins configuration. Replace `<x.y.z>` with the correct plug-in version. Use the SHA-512 hash from the corresponding `.integrity` file for each `integrity` value.
**Operator installation**

Add the plug-ins to your dynamic plug-ins ConfigMap (for example, `rhaap-dynamic-plugins-config`).

```yaml
kind: ConfigMap
apiVersion: v1
metadata:
name: rhaap-dynamic-plugins-config
data:
dynamic-plugins.yaml: |
# ...
plugins:
- disabled: false
package: 'http://plugin-registry:8080/ansible-plugin-backstage-rhaap-dynamic-<x.y.z>.tgz'
integrity: <SHA512_value>
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
- disabled: false
package: >-
http://plugin-registry:8080/ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-<x.y.z>.tgz
integrity: <SHA512_value>
pluginConfig:
dynamicPlugins:
backend:
ansible.plugin-scaffolder-backend-module-backstage-rhaap: null
```
Reference this ConfigMap in your `Backstage` CR under `spec.application.dynamicPluginsConfigMapName`.

**Helm chart installation**

In the OpenShift Container Platform Developer UI, navigate to **Helm** > **developer-hub** > **Actions** > **Upgrade** > **Yaml view**. Add the plug-ins under the `global.dynamic.plugins` section.

```yaml
global:
# ...
plugins:
- disabled: false
integrity: <SHA512_value>
package: 'http://plugin-registry:8080/ansible-plugin-backstage-rhaap-dynamic-<x.y.z>.tgz'
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
- disabled: false
integrity: <SHA512_value>
package: >-
http://plugin-registry:8080/ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-<x.y.z>.tgz
pluginConfig:
dynamicPlugins:
backend:
ansible.plugin-scaffolder-backend-module-backstage-rhaap: null
```

2.  Apply the changes. For Helm deployments, click **Upgrade**. The Developer Hub pods restart and the plug-ins are installed.

### Results

1. In the OpenShift Container Platform web console, open the pod details for the Red Hat Developer Hub deployment.
2. Select the **Logs** tab and choose the `install-dynamic-plugins` container from the drop-down list.
3. Search the log for the Ansible plug-ins. A successful installation produces log entries similar to:

```terminal
=> Successfully installed dynamic plugin http://plugin-registry:8080/ansible-plugin-backstage-rhaap-dynamic-<x.y.z>.tgz
```

After installing the plug-ins from the HTTP registry, continue with the configuration steps.
