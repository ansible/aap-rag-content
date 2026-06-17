# Uninstall an Operator installation on OpenShift Container Platform

To delete the dynamic plug-ins from your installation, you must edit the ConfigMaps that reference Ansible.

The deployment auto reloads when the ConfigMaps are updated. You do not need to reload the deployment manually.

## Remove the Ansible plug-ins from the ConfigMap

To remove the Ansible plug-ins from an Operator installation, you must edit the custom ConfigMap that references the plug-ins. You can either delete the entire plug-in entry block or simply disable the plug-ins by setting the disabled attribute to `true`.

### Procedure

1.  Open the custom ConfigMap where you referenced the Ansible plug-ins. For this example, the ConfigMap name is `rhaap-dynamic-plugins-config`.
2.  Locate the dynamic plug-ins in the `plugins:` block.   - To disable the plug-ins, update the `disabled` attribute to `true` for the three plug-ins.
- To delete the plug-ins, delete the lines that reference the plug-ins from the `plugins:` block:

```
kind: ConfigMap
apiVersion: v1
metadata:
name: rhaap-dynamic-plugins-config
data:
dynamic-plugins.yaml: |
...
plugins: # Remove the Ansible plug-ins entries below the ‘plugins’ YAML key
- disabled: false
package: 'http://plugin-registry:8080/ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz'
integrity: <SHA512 value>
...
- disabled: false
package: >-
http://plugin-registry:8080/ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz
integrity: <SHA512 value>
...
```

3.  Click Save.

## Remove Ansible Automation Platform and Dev Spaces from the custom Red Hat Developer Hub ConfigMap

To remove Ansible Automation Platform and Dev Spaces configuration from an Operator installation, you must edit the custom Red Hat Developer Hub ConfigMap.

### Procedure

1.  Open the custom Red Hat Developer Hub ConfigMap where you added configuration for the templates and for connecting to Ansible Automation Platform and Dev Spaces. In this example, the Red Hat Developer Hub ConfigMap name is `app-config-rhdh`.

```
kind: ConfigMap
apiVersion: v1
metadata:
name: rhdh-app-config
data:
app-config-custom.yaml: |
...
catalog:
...
locations: # Remove the YAML entry below the 'locations' YAML key
- type: url
target: https://github.com/ansible/ansible-rhdh-templates/blob/main/all.yaml
rules:
- allow: [Template]
...
# Remove the entire 'ansible' YAML key and all sub-entries
ansible:
devSpaces:
baseUrl: '<https://YOUR_DEV_SPACES_URL>'
creatorService:
baseUrl: '127.0.0.1'
port: '8000'
rhaap:
baseUrl: '<https://YOUR_AAP_URL>'
token: <REDACTED>
checkSSL: false
```

2.  Remove the `url` in the `locations:` block to delete the templates from the RHDH instance.
3.  Remove the `ansible:` block to delete the Ansible-specific configuration.
4.  Click Save.

## Uninstall the sidecar container

To remove the sidecar container for Ansible development tools from the developer-hub pod, you must modify the base ConfigMap for the Red Hat Developer Hub deployment.

### Procedure

1.  In the OpenShift console, select the **Topology** view.
2.  Click **More actions ⋮** on the developer-hub instance and select **Edit backstage** to edit the base ConfigMap.
3.  Select the **YAML** tab.
4.  In the editing pane, remove the `containers` block for the sidecar container from the `spec.deployment.patch.spec.template.spec` block:


```
...
spec:
deployment:
patch:
spec:
template:
spec:
containers:
- command:
- adt
- server
image: ghcr.io/ansible/community-ansible-dev-tools:latest
imagePullPolicy: always
ports:
- containerPort: 8000
protocol: TCP
terminationMessagePolicy: file
```

5.  Click Save.
