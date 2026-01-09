# 2. Installing the Ansible plug-ins with a Helm chart on OpenShift Container Platform
## 2.7. Full examples
### 2.7.2. Full Helm chart config example for Ansible plug-ins




This example provides a full YAML configuration for the Helm chart, illustrating the precise structure needed to integrate the Ansible plug-ins into the Red Hat Developer Hub installation.

```
global:
...
dynamic:
...
plugins:
- disabled: false
integrity: &lt;SHA512 Integrity key for ansible-plugin-backstage-rhaap plugin&gt;
package: 'http://plugin-registry:8080/ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz'
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
integrity: &lt;SHA512 Integrity key for ansible-plugin-scaffolder-backend-module-backstage-rhaap plugin&gt;
package: &gt;-
http://plugin-registry:8080/ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz
pluginConfig:
dynamicPlugins:
backend:
ansible.plugin-scaffolder-backend-module-backstage-rhaap: null
...
upstream:
backstage:
...
extraAppConfig:
- configMapRef: app-config-rhdh
filename: app-config-rhdh.yaml
extraContainers:
- command:
- adt
- server
image: &gt;-
registry.redhat.io/ansible-automation-platform-25/ansible-dev-tools-rhel8:latest
imagePullPolicy: IfNotPresent
name: ansible-devtools-server
ports:
- containerPort: 8000
...
```

