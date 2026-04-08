# 4. Upgrading the Ansible plug-ins on a Helm installation on OpenShift Container Platform
## 4.1. Upgrade with OCI container delivery




To upgrade the Ansible plug-ins when using OCI delivery, update the version tag in the package URL for each plug-in entry.

**Procedure**

1. Log in to your OpenShift Container Platform instance.
1. In the OpenShift Developer UI, navigate to **Helm** → **developer-hub** → **Actions** → **Upgrade** → **Yaml view** .
1. In the `    global.dynamic.plugins` list, update the version tag at the end of each `    package` URL:


```
plugins:      - disabled: false        package: 'oci://registry.redhat.io/ansible-automation-platform/automation-portal:2.1!ansible-plugin-backstage-rhaap'        pluginConfig:          ...      - disabled: false        package: 'oci://registry.redhat.io/ansible-automation-platform/automation-portal:2.1!ansible-plugin-scaffolder-backend-module-backstage-rhaap'        pluginConfig:          ...
```


1. Click **Upgrade** .

The Red Hat Developer Hub pods restart and pull the new plug-in version.




**Verification**

1. In the OpenShift UI, click **Topology** .
1. Verify that the Red Hat Developer Hub instance is available.


