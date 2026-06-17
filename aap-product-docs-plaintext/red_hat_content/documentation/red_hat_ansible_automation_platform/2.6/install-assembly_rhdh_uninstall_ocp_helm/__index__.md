# Uninstall from a Helm installation on OpenShift Container Platform

To uninstall the Ansible plug-ins, you must remove any software templates that use the `ansible:content:create` action from Red Hat Developer Hub, and remove the plug-ins configuration from the Helm chart in OpenShift.

## Uninstall a Helm chart installation

To uninstall Ansible plug-ins from a Helm chart, first remove templates through the `ansible:content:create` action. Then, delete the plug-in config and `extraContainers` from the YAML, clear the ConfigMap Ansible block, restart the deployment, and remove the registry app.

### Procedure

1.  In Red Hat Developer Hub, remove any software templates that use the `ansible:content:create` action.
2.  In the OpenShift Developer UI, navigate to Helm> (and then)developer-hub> (and then)Actions> (and then)Upgrade> (and then)Yaml view.
3.  Remove the Ansible plug-ins configuration under the `plugins` section.

```
...
global:
...
plugins:
- disabled: false
integrity: <SHA512 value>
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
integrity: <SHA512 value>
package: >-
http://plugin-registry:8080/ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz
pluginConfig:
dynamicPlugins:
backend:
ansible.plugin-scaffolder-backend-module-backstage-rhaap: null
```

4.  Remove the `extraContainers` section.

```
upstream:
backstage: |
...
extraContainers:
- command:
- adt
- server
image: >-
registry.redhat.io/ansible-automation-platform-25/ansible-dev-tools-rhel8:latest
imagePullPolicy: IfNotPresent
name: ansible-devtools-server
ports:
- containerPort: 8000
image:
pullPolicy: Always
pullSecrets:
- ...
- rhdh-secret-registry
...
```

5.  Click Upgrade.
6.  Edit your custom Red Hat Developer Hub config map, for example `app-config-rhdh`.
7.  Remove the `ansible` section.

```
data:
app-config-rhdh.yaml: |
...
ansible:
analytics:
enabled: true
devSpaces:
baseUrl: '<https://MyOwnDevSpacesUrl/>'
creatorService:
baseUrl: '127.0.0.1'
port: '8000'
rhaap:
baseUrl: '<https://MyAapSubcriptionUrl>'
token: '<TopSecretAAPToken>'
checkSSL: true
automationHub:
baseUrl: '<https://MyOwnPAHUrl/>'
```

8.  Restart the Red Hat Developer Hub deployment.
9.  Remove the `plugin-registry` OpenShift application.

```
oc delete all -l app=plugin-registry
```
