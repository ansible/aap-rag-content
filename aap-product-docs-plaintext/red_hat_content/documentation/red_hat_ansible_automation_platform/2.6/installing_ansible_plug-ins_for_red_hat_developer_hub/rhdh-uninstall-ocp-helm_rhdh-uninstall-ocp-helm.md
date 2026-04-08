# 6. Uninstalling the Ansible plug-ins from a Helm installation on OpenShift Container Platform
## 6.1. Uninstalling a Helm chart installation




To uninstall the Ansible plug-ins from a Helm chart installation, you remove templates using the ansible:content:create action first. Then, you delete the plug-in configuration from the Helm chart YAML, remove the extraContainers section, and delete the Ansible block from the custom ConfigMap. Finally, you restart the deployment.

**Procedure**

1. In Red Hat Developer Hub, remove any software templates that use the `    ansible:content:create` action.
1. In the OpenShift Developer UI, navigate toHelm→developer-hub→Actions→Upgrade→Yaml view.
1. Remove the Ansible plug-ins configuration under the `    plugins` section.


```
global:      dynamic:        plugins:          - disabled: false            package: 'oci://registry.redhat.io/ansible-automation-platform/automation-portal:2.1!ansible-plugin-backstage-rhaap'            pluginConfig:              ...          - disabled: false            package: 'oci://registry.redhat.io/ansible-automation-platform/automation-portal:2.1!ansible-plugin-scaffolder-backend-module-backstage-rhaap'            pluginConfig:              ...
```

For HTTP plug-in registry, remove the `    <a class="link" href="http://plugin-registry:8080/">http://plugin-registry:8080/</a>...` entries instead.


1. Remove the `    extraContainers` section.


```
upstream:      backstage:        ...        extraContainers:          - command:              - adt              - server            image: &gt;-              registry.redhat.io/ansible-automation-platform-26/ansible-dev-tools-rhel9:latest            imagePullPolicy: IfNotPresent            name: ansible-devtools-server            ports:              - containerPort: 8000
```


1. ClickUpgrade.
1. Edit your custom Red Hat Developer Hub config map, for example `    app-config-rhdh` .
1. Remove the `    ansible` section.
1. Restart the Red Hat Developer Hub deployment.
1. If you used OCI delivery, delete the registry auth secret:


```
oc delete secret &lt;deployment-name&gt;-dynamic-plugins-registry-auth
```


1. If you used the HTTP plug-in registry method, remove the plug-in registry application:


```
oc delete all -l app=plugin-registry
```




