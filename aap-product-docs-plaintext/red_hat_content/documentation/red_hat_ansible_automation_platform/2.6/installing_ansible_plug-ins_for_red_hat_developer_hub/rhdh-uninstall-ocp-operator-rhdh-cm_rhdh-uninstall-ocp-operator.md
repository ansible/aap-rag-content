# 7. Uninstalling an Operator installation on OpenShift Container Platform
## 7.2. Removing Ansible Automation Platform and Dev Spaces from the custom Red Hat Developer Hub ConfigMap




To remove Ansible Automation Platform and Dev Spaces configuration from an Operator installation, you must edit the custom Red Hat Developer Hub ConfigMap.

**Procedure**

1. Open the custom Red Hat Developer Hub ConfigMap where you added configuration for the templates and for connecting to Ansible Automation Platform and Dev Spaces. In this example, the Red Hat Developer Hub ConfigMap name is `    app-config-rhdh` .


```
kind: ConfigMap    apiVersion: v1    metadata:     name: rhdh-app-config    data:     app-config-custom.yaml: |       ...       catalog:         ...         locations: # Remove the YAML entry below the 'locations' YAML key           - type: url             target: https://github.com/ansible/ansible-rhdh-templates/blob/main/all.yaml             rules:               - allow: [Template]         ...       # Remove the entire 'ansible' YAML key and all sub-entries       ansible:         devSpaces:           baseUrl: '&lt;https://YOUR_DEV_SPACES_URL&gt;'         creatorService:           baseUrl: '127.0.0.1'           port: '8000'         rhaap:           baseUrl: '&lt;https://YOUR_AAP_URL&gt;'           token: &lt;REDACTED&gt;           checkSSL: false
```


1. Remove the `    url` in the `    locations:` block to delete the templates from the RHDH instance.
1. Remove the `    ansible:` block to delete the Ansible-specific configuration.
1. ClickSave.


