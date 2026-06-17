# 6. Uninstalling the Ansible plug-ins from a Helm installation on OpenShift Container Platform
## 6.1. Uninstalling a Helm chart installation

To uninstall the Ansible plug-ins from a Helm chart installation, you remove templates using the ansible:content:create action first. Then, you delete the plug-in configuration from the Helm chart YAML, remove the extraContainers section, and delete the Ansible block from the custom ConfigMap. Finally, you restart the deployment.

**Procedure**

1. In Red Hat Developer Hub, remove any software templates that use the `ansible:content:create` action.

2. In the OpenShift Developer UI, navigate to Helm → developer-hub → Actions → Upgrade → Yaml view.

3. Remove the Ansible plug-ins configuration under the `plugins` section.

global:
dynamic:
plugins:
- disabled: false
package: 'oci://registry.redhat.io/ansible-automation-platform/automation-portal:2.1!ansible-plugin-backstage-rhaap'
pluginConfig:
...
- disabled: false
package: 'oci://registry.redhat.io/ansible-automation-platform/automation-portal:2.1!ansible-plugin-scaffolder-backend-module-backstage-rhaap'
pluginConfig:
...

For HTTP plug-in registry, remove the `<http://plugin-registry:8080/>...` entries instead.

4. Remove the `extraContainers` section.

upstream:
backstage:
...
extraContainers:
- command:
- adt
- server
image: >-
registry.redhat.io/ansible-automation-platform-26/ansible-dev-tools-rhel9:latest
imagePullPolicy: IfNotPresent
name: ansible-devtools-server
ports:
- containerPort: 8000

5. Click Upgrade.

6. Edit your custom Red Hat Developer Hub config map, for example `app-config-rhdh`.

7. Remove the `ansible` section.

8. Restart the Red Hat Developer Hub deployment.

9. If you used OCI delivery, delete the registry auth secret:

oc delete secret <deployment-name>-dynamic-plugins-registry-auth

10. If you used the HTTP plug-in registry method, remove the plug-in registry application:

oc delete all -l app=plugin-registry

