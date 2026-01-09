# 7. Uninstalling an Operator installation on OpenShift Container Platform
## 7.1. Removing the Ansible plug-ins from the ConfigMap




To remove the Ansible plug-ins from an Operator installation, you must edit the custom ConfigMap that references the plug-ins. You can either delete the entire plug-in entry block or simply disable the plug-ins by setting the disabled attribute to `true` .

**Procedure**

1. Open the custom ConfigMap where you referenced the Ansible plug-ins. For this example, the ConfigMap name is `    rhaap-dynamic-plugins-config` .
1. Locate the dynamic plug-ins in the `    plugins:` block.


- To disable the plug-ins, update the `        disabled` attribute to `        true` for the three plug-ins.
- To delete the plug-ins, delete the lines that reference the plug-ins from the `        plugins:` block:


```
kind: ConfigMap        apiVersion: v1        metadata:         name: rhaap-dynamic-plugins-config        data:         dynamic-plugins.yaml: |           ...           plugins: # Remove the Ansible plug-ins entries below the ‘plugins’ YAML key             - disabled: false               package: 'http://plugin-registry:8080/ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz'               integrity: &lt;SHA512 value&gt;        	 ...             - disabled: false               package: &gt;-                 http://plugin-registry:8080/ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz               integrity: &lt;SHA512 value&gt;        	 ...
```



1. ClickSave.


