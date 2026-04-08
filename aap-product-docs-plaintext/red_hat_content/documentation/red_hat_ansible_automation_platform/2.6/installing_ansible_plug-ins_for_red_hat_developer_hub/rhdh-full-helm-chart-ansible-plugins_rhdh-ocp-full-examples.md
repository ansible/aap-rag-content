# 2. Installing the Ansible plug-ins with a Helm chart on OpenShift Container Platform
## 2.6. Full examples
### 2.6.2. Full Helm chart config example for Ansible plug-ins




This example provides a full YAML configuration for the Helm chart using OCI container delivery.

```
global:
dynamic:
includes:
- dynamic-plugins.default.yaml
plugins:
- disabled: false
package: 'oci://registry.redhat.io/ansible-automation-platform/automation-portal:2.1!ansible-plugin-backstage-rhaap'
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
package: 'oci://registry.redhat.io/ansible-automation-platform/automation-portal:2.1!ansible-plugin-scaffolder-backend-module-backstage-rhaap'
pluginConfig:
dynamicPlugins:
backend:
ansible.plugin-scaffolder-backend-module-backstage-rhaap: null

upstream:
backstage:
image:
pullSecrets:
- &lt;your-redhat-registry-pull-secret&gt;
extraAppConfig:
- configMapRef: app-config-rhdh
filename: app-config-rhdh.yaml
extraContainers:
- command:
- adt
- server
image: &gt;-
registry.redhat.io/ansible-automation-platform-26/ansible-dev-tools-rhel9:latest
imagePullPolicy: IfNotPresent
name: ansible-devtools-server
ports:
- containerPort: 8000
```

