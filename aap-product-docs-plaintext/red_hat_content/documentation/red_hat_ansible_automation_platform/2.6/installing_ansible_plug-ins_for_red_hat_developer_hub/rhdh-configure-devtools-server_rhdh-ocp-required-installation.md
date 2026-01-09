# 2. Installing the Ansible plug-ins with a Helm chart on OpenShift Container Platform
## 2.5. Required configuration
### 2.5.6. Configuring the Ansible Dev Tools Server




The `creatorService` URL is required for the Ansible plug-ins to provision new projects using the provided software templates.

**Procedure**

1. Edit your custom Red Hat Developer Hub config map, `    app-config-rhdh` , that you created in [Adding a custom ConfigMap](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/installing_ansible_plug-ins_for_red_hat_developer_hub/rhdh-install-ocp-helm_aap-plugin-rhdh-installing#rhdh-add-custom-configmap_rhdh-ocp-required-installation) .
1. Add the following code to your Red Hat Developer Hub `    app-config-rhdh.yaml` file.


```
kind: ConfigMap    apiVersion: v1    metadata:      name: app-config-rhdh    ...    data:      app-config-rhdh.yaml: |-        ansible:          creatorService:            baseUrl: 127.0.0.1            port: '8000'    ...
```




