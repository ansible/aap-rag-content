# 2. Installing the Ansible plug-ins with a Helm chart on OpenShift Container Platform
## 2.5. Required configuration
### 2.5.6. Adding Ansible plug-ins software templates




Red Hat Ansible provides software templates for Red Hat Developer Hub to provision new playbooks and collection projects based on Ansible best practices.

**Procedure**

1. Edit your custom Red Hat Developer Hub config map, for example `    app-config-rhdh` .
1. Add the following code to your Red Hat Developer Hub `    app-config-rhdh.yaml` file.


```
data:      app-config-rhdh.yaml: |        catalog:          ...          locations:            ...            - type: url              target: https://github.com/ansible/ansible-rhdh-templates/blob/main/all.yaml              rules:                - allow: [Template]
```




**Additional resources**

-  [Managing templates](https://docs.redhat.com/en/documentation/red_hat_developer_hub/1.2/html-single/administration_guide_for_red_hat_developer_hub/assembly-admin-templates#assembly-admin-templates)


