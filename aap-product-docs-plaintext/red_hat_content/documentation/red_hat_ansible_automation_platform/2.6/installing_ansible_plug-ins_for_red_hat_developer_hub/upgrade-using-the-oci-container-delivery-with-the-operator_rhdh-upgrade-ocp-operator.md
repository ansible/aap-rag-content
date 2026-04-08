# 5. Upgrading the Ansible plug-ins on an Operator installation on OpenShift Container Platform
## 5.1. Upgrade using the OCI container delivery with the Operator




To upgrade the Ansible plug-ins when using OCI delivery, update the version tag in the `package` URL in your plug-ins ConfigMap.

**Procedure**

1. Log in to your OpenShift Container Platform instance.
1. Navigate to **ConfigMaps** and select the **rhaap-dynamic-plugins-config** map.
1. Select the **YAML** tab.
1. In the **plugins** list, update the version tag at the end of each **package** URL:


```
plugins:      - disabled: false        package: 'oci://registry.redhat.io/ansible-automation-platform/automation-portal:2.1!ansible-plugin-backstage-rhaap'        pluginConfig:          ...      - disabled: false        package: 'oci://registry.redhat.io/ansible-automation-platform/automation-portal:2.1!ansible-plugin-scaffolder-backend-module-backstage-rhaap'        pluginConfig:          ...
```


1. Click **Save** .

Red Hat Developer Hub detects the configuration change and reloads the plug-ins.




**Verification**

1. In the OpenShift UI, click **Topology** .
1. Verify that the Red Hat Developer Hub instance is available.


