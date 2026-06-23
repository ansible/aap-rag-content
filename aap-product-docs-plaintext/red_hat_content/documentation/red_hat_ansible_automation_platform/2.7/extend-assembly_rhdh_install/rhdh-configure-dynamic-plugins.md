# Install the Ansible plug-ins
## Configure the dynamic plug-ins

After creating the registry authentication secret, add the Ansible plug-ins to your dynamic plug-ins configuration.

### Procedure

1.  Edit your dynamic plug-ins configuration and add the Ansible plug-ins using OCI references.
**Operator installation**

In the `data.dynamic-plugins.yaml.plugins` block, add the Ansible plug-ins:

```yaml
kind: ConfigMap
apiVersion: v1
metadata:
name: dynamic-plugins-rhdh
data:
dynamic-plugins.yaml: |
includes:
- dynamic-plugins.default.yaml
plugins:
- disabled: false
package: >-
oci://registry.redhat.io/ansible-automation-platform/automation-portal:<tag>!ansible-plugin-backstage-rhaap
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
oci://registry.redhat.io/ansible-automation-platform/automation-portal:<tag>!ansible-plugin-backstage-self-service
pluginConfig:
dynamicPlugins:
frontend:
ansible.plugin-backstage-self-service:
scaffolderFieldExtensions:
- importName: AAPTokenFieldExtension
- importName: AAPResourcePickerExtension
- disabled: false
package: >-
oci://registry.redhat.io/ansible-automation-platform/automation-portal:<tag>!ansible-backstage-plugin-catalog-backend-module-rhaap
pluginConfig: {}
- disabled: false
package: >-
oci://registry.redhat.io/ansible-automation-platform/automation-portal:<tag>!ansible-plugin-scaffolder-backend-module-backstage-rhaap
pluginConfig:
dynamicPlugins:
backend:
ansible.plugin-scaffolder-backend-module-backstage-rhaap:
```
**Helm chart installation**

Update the Helm chart configuration under the `plugins` section:

```yaml
global:
# ...
dynamic:
# ...
plugins:
- disabled: false
package: >-
oci://registry.redhat.io/ansible-automation-platform/automation-portal:<tag>!ansible-plugin-backstage-rhaap
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
oci://registry.redhat.io/ansible-automation-platform/automation-portal:<tag>!ansible-plugin-backstage-self-service
pluginConfig:
dynamicPlugins:
frontend:
ansible.plugin-backstage-self-service:
scaffolderFieldExtensions:
- importName: AAPTokenFieldExtension
- importName: AAPResourcePickerExtension
- disabled: false
package: >-
oci://registry.redhat.io/ansible-automation-platform/automation-portal:<tag>!ansible-backstage-plugin-catalog-backend-module-rhaap
pluginConfig: {}
- disabled: false
package: >-
oci://registry.redhat.io/ansible-automation-platform/automation-portal:<tag>!ansible-plugin-scaffolder-backend-module-backstage-rhaap
pluginConfig:
dynamicPlugins:
backend:
ansible.plugin-scaffolder-backend-module-backstage-rhaap:
```

2.  Replace `<tag>` with the Ansible plug-ins image tag for your release (for example, `2.2`).
3.  Apply the changes. For Operator deployments, click **Save**. For Helm deployments, click **Upgrade**.

