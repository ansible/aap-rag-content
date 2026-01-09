# 5. Upgrading the Ansible plug-ins on an Operator installation on OpenShift Container Platform
## 5.3. Updating the Ansible plug-ins version numbers for an Operator installation




You must edit the dedicated plug-ins ConfigMap, such as `rhaap-dynamic-plugins-config` , replacing the old version numbers and SHA values in the configuration to trigger a restart and update of the plug-ins.

**Procedure**

1. Log in to your OpenShift Container Platform instance.
1. In the OpenShift UI, open the ConfigMap where you added the Ansible plug-ins during installation. This example uses a ConfigMap file called `    rhaap-dynamic-plugins-config` .
1. Update `    x.y.z` with the version numbers for the updated Ansible plug-ins.
1. Update the integrity values for each plug-in with the `    .integrity` value from the corresponding extracted Ansible plug-ins `    .tar` file.


```
kind: ConfigMap    apiVersion: v1    metadata:     name: rhaap-dynamic-plugins-config    data:     dynamic-plugins.yaml: |       ...       plugins: # Update the Ansible plug-in entries below with the updated plugin versions         - disabled: false           package: 'http://plugin-registry:8080/ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz'           integrity: &lt;SHA512 value&gt; # Use hash in ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz.integrity    	 ...         - disabled: false           package: &gt;-             http://plugin-registry:8080/ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz           integrity: &lt;SHA512 value&gt; # Use hash in ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz.integrity    	 ...
```


1. ClickSave.

The developer hub pods restart and the plug-ins are installed.




**Verification**

1. In the OpenShift UI, click **Topology** .
1. Make sure that the Red Hat Developer Hub instance is available.


