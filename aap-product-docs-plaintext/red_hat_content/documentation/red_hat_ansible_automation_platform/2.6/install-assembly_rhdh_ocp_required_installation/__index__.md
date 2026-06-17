# Complete required configurations

Complete these required configuration steps to add the Ansible plug-ins to your Helm chart and link the Red Hat Developer Hub instance to the necessary Ansible Automation Platform components.

## Add the Ansible plug-ins configuration

Modify the Red Hat Developer Hub Helm chart to add the Ansible plug-ins. The configuration depends on the plug-in delivery method you chose earlier.

### Procedure

1.  In the OpenShift Developer UI, navigate to Helm> (and then)developer-hub> (and then)Actions> (and then)Upgrade> (and then)Yaml view.
2.  Update the Helm chart configuration to add the dynamic plug-ins in the Red Hat Developer Hub instance. Under the `plugins` section in the YAML file, add the dynamic plug-ins that you want to enable. Choose the configuration that matches your delivery method.
-          **OCI container delivery (recommended)**:



```yaml
global:
dynamic:
includes:
- dynamic-plugins.default.yaml
plugins:
- disabled: false
package: 'oci://registry.redhat.io/ansible-automation-platform/automation-portal:21!ansible-plugin-backstage-rhaap'
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
```
Replace `x.y.z` with the Ansible plug-ins version.

Note:
OCI delivery does not require the `integrity` hash values. The OCI registry handles integrity verification.

-          **HTTP plug-in registry (deprecated)**:



```yaml
global:
dynamic:
includes:
- dynamic-plugins.default.yaml
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
Replace `x.y.z` with the correct plug-in version numbers and update the `integrity` values using the corresponding .integrity file content.

3.  Click Upgrade.
The Red Hat Developer Hub pods restart and the plug-ins are installed.

### Results

To verify that the plug-ins have been installed, open the `install-dynamic-plugin` container logs:

1. Open the Developer perspective for the Red Hat Developer Hub application in the OpenShift Web console.
2. Select the Topology view.
3. Select the Red Hat Developer Hub deployment pod to open an information pane.
4. Select the Resources tab of the information pane.
5. In the Pods section, click View logs to open the Pod details page.
6. In the Pod details page, select the Logs tab.
7. Select `install-dynamic-plugins` from the drop-down list of containers to view the container log.   - **For OCI delivery**, a successful installation displays:

```
=> Successfully installed dynamic plugin oci:registry.redhat.io/ansible-automation-platform/ansible-plugin-backstage-rhaap-dynamic:x.y.z
```

- **For HTTP plug-in registry (deprecated)**, a successful installation displays:

```
=> Successfully installed dynamic plugin http://plugin-registry:8080/ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz
```

## Add a pull secret to the Red Hat Developer Hub Helm configuration

You must add a pull secret to the Red Hat Developer Hub Helm configuration to enable the dynamic plug-ins to pull container images from authenticated registries.

### Before you begin

- You have a Red Hat Customer Portal account and Red Hat Service Registry account.

### About this task

### Procedure

1.  Create a new [Red Hat Registry Service account](https://access.redhat.com/terms-based-registry/), if required.
2.  Click the token name under the **Account name** column.
3.  Select the **OpenShift Secret** tab and follow the instructions to add the pull secret to your Red Hat Developer Hub OpenShift project.
4.  Add the new secret to the Red Hat Developer Hub Helm configuration, replacing `<your-redhat-registry-pull-secret>` with the name of the secret you generated on the Red Hat Registry Service Account website:


```
upstream:
backstage:
...
image:
...
pullSecrets:
- <your-redhat-registry-pull-secret>
...
```

## Add the Ansible Developer Tools container

You must update the Helm chart configuration to add an extra container.

### Procedure

1.  Log in to the OpenShift UI.
2.  Navigate to Helm> (and then)developer-hub> (and then)Actions> (and then)upgrade> (and then)Yaml view to open the Helm chart.
3.  Update the `extraContainers` section in the YAML file. Add the following code:

```
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
...
```
Note:
The image pull policy is `imagePullPolicy: IfNotPresent`. The image is pulled only if it does not already exist on the node. Update it to `imagePullPolicy: Always` if you always want to use the latest image.

4.  Click Upgrade.

### Results

To verify that the container is running, check the container log:


![View container log](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/rhdh-check-devtools-container.png)

## Add a custom ConfigMap

Create a custom Red Hat Developer Hub ConfigMap, typically named `app-config-rhdh`, to store custom application settings.

### Procedure

Create a Red Hat Developer Hub ConfigMap following the procedure in the [Creating and using config maps](https://docs.redhat.com/en/documentation/openshift_container_platform/4.15/html-single/nodes/index#configmaps) section of the OpenShift Container Platform *Nodes* guide. The following examples use a custom ConfigMap named `app-config-rhdh`.

To edit your custom ConfigMap, log in to the OpenShift UI and navigate to Select Project ( developerHubProj )> (and then)ConfigMaps> (and then){developer-hub}-app-config> (and then)EditConfigMaps> (and then)app-config-rhdh.

## Configure the Ansible development tools Server

The `creatorService` URL is required for the Ansible plug-ins to provision new projects using the provided software templates.

### Procedure

1.  Edit your custom Red Hat Developer Hub config map, `app-config-rhdh`, that you created in [Adding a custom ConfigMap](/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-configure_the_plug_ins#rhdh-add-custom-configmap "Create a custom Red Hat Developer Hub ConfigMap, typically named app-config-rhdh, to store custom application settings.").
2.  Add the following code to your Red Hat Developer Hub `app-config-rhdh.yaml` file.

```
kind: ConfigMap
apiVersion: v1
metadata:
name: app-config-rhdh
...
data:
app-config-rhdh.yaml: |-
ansible:
creatorService:
baseUrl: 127.0.0.1
port: '8000'
...
```

## Configure Ansible Automation Platform details

Connect Red Hat Developer Hub to your automation controller by configuring the Ansible Automation Platform details. This configuration uses a Personal Access Token (PAT) to authenticate the plug-ins, which allows them to interact with your automation environment.

### About this task

Note:

The Ansible plug-ins continue to function regardless of the Ansible Automation Platform subscription status.

### Procedure

1.  Create a Personal Access Token (PAT) with "read and write” scope in automation controller, following the [Applications](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_token_based_authentication#gw-token-based-authentication "Token-based authentication permits authentication of third-party tools and services with the platform through integrated OAuth 2 token support. Ansible Automation Platform utilizes both OAuth Tokens and Personal Access Tokens (PATs).") section of *Access management and authentication*.
2.  Edit your custom Red Hat Developer Hub config map, for example `app-config-rhdh`.
3.  Add your Ansible Automation Platform details to `app-config-rhdh.yaml`.   1.  Set the `baseURL` key with your automation controller URL.
2.  Set the `token` key with the generated token value that you created in Step 1.
3.  Set the `checkSSL` key to `true` or `false`. If `checkSSL` is set to `true`, the Ansible plug-ins verify whether the SSL certificate is valid.

```
data:
app-config-rhdh.yaml: |
...
ansible:
...
rhaap:
baseUrl: '<https://MyControllerUrl>'
token: '<AAP Personal Access Token>'
checkSSL: true
```
Note:
You are responsible for protecting your Red Hat Developer Hub installation from external and unauthorized access. Manage the backend authentication key like any other secret. Meet strong password requirements, do not expose it in any configuration files, and only inject it into configuration files as an environment variable.

## Add Ansible plug-ins software templates

Add Ansible Automation Platform software templates to your Red Hat Developer Hub instance so users can create new Ansible playbooks and collection projects based on Ansible best practices.

### Procedure

1.  Edit your custom Red Hat Developer Hub config map, for example `app-config-rhdh`.
2.  Add the following code to your Red Hat Developer Hub `app-config-rhdh.yaml` file.

```
data:
app-config-rhdh.yaml: |
catalog:
...
locations:
...
- type: url
target: https://github.com/ansible/ansible-rhdh-templates/blob/main/all.yaml
rules:
- allow: [Template]
```

## Configure Role Based Access Control

Red Hat Developer Hub offers Role-based Access Control (RBAC) functionality. RBAC can then be applied to the Ansible plug-ins content.

### Procedure

Assign the following roles:

- Members of the `admin:superUsers` group can select templates in the **Create** tab of the Ansible plug-ins to create playbook and collection projects.

- Members of the `admin:users` group can view templates in the **Create** tab of the Ansible plug-ins. The following example adds RBAC to Red Hat Developer Hub.



```
data:
app-config-rhdh.yaml: |
plugins:
...
permission:
enabled: true
rbac:
admin:
users:
- name: user:default/<user-scm-ida>
superUsers:
- name: user:default/<user-admin-idb>
```
For more information about permission policies and managing RBAC, refer to the [*Authorization in Red Hat Developer Hub*](https://docs.redhat.com/en/documentation/red_hat_developer_hub/1.6/html-single/authorization_in_red_hat_developer_hub/index) guide for Red Hat Developer Hub.
