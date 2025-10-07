# 6. Uninstalling the Ansible plug-ins from a Helm installation on OpenShift Container Platform
## 6.1. Uninstalling a Helm chart installation




**Procedure**

1. In Red Hat Developer Hub, remove any software templates that use the `    ansible:content:create` action.
1. In the OpenShift Developer UI, navigate toHelm→developer-hub→Actions→Upgrade→Yaml view.
1. Remove the Ansible plug-ins configuration under the `    plugins` section.


```
...    global:    ...        plugins:          - disabled: false            integrity: &lt;SHA512 value&gt;            package: 'http://plugin-registry:8080/ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz'            pluginConfig:              dynamicPlugins:                frontend:                  ansible.plugin-backstage-rhaap:                    appIcons:                      - importName: AnsibleLogo                        name: AnsibleLogo                    dynamicRoutes:                      - importName: AnsiblePage                        menuItem:                          icon: AnsibleLogo                          text: Ansible                        path: /ansible          - disabled: false            integrity: &lt;SHA512 value&gt;            package: &gt;-              http://plugin-registry:8080/ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz            pluginConfig:              dynamicPlugins:                backend:                  ansible.plugin-scaffolder-backend-module-backstage-rhaap: null
```


1. Remove the `    extraContainers` section.


```
upstream:      backstage: |        ...        extraContainers:          - command:              - adt              - server            image: &gt;-              registry.redhat.io/ansible-automation-platform-25/ansible-dev-tools-rhel8:latest            imagePullPolicy: IfNotPresent            name: ansible-devtools-server            ports:              - containerPort: 8000        image:          pullPolicy: Always          pullSecrets:            - ...            - rhdh-secret-registry        ...
```


1. ClickUpgrade.
1. Edit your custom Red Hat Developer Hub config map, for example `    app-config-rhdh` .
1. Remove the `    ansible` section.


```
data:      app-config-rhdh.yaml: |        ...        ansible:          analytics:            enabled: true          devSpaces:            baseUrl: '&lt;https://MyOwnDevSpacesUrl/&gt;'          creatorService:            baseUrl: '127.0.0.1'            port: '8000'          rhaap:            baseUrl: '&lt;https://MyAapSubcriptionUrl&gt;'            token: '&lt;TopSecretAAPToken&gt;'            checkSSL: true          automationHub:            baseUrl: '&lt;https://MyOwnPAHUrl/&gt;'
```


1. Restart the Red Hat Developer Hub deployment.
1. Remove the `    plugin-registry` OpenShift application.


```
oc delete all -l app=plugin-registry
```




