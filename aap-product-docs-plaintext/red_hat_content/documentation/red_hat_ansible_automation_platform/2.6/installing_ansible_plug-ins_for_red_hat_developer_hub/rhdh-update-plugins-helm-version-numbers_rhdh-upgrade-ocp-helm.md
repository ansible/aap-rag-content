# 4. Upgrading the Ansible plug-ins on a Helm installation on OpenShift Container Platform
## 4.4. Updating the Ansible plug-ins version numbers for a Helm installation




To upgrade the Ansible plug-ins, you must update the `imageTagInfo` parameter in the Helm chart configuration to the desired version. This triggers the Red Hat Developer Hub to pull the new container images directly from the Red Hat registry.

**Procedure**

1. Log in to your OpenShift Container Platform instance.
1. In the OpenShift Developer UI, navigate toHelm→developer-hub→Actions→Upgrade→Yaml view.
1. Locate the `    global` section.


```
...    global:      # Ensure OCI mode is enabled      pluginMode: oci          # UPDATE this value to the new desired version      imageTagInfo: "2.1"          # Note: Do not manually update 'plugins' packages;      # OCI mode handles the download automatically based on the tag above.      dynamic:        plugins: []
```


1. ClickUpgrade.

The Red Hat Developer Hub pods restart and pull the new plug-in versions.




**Verification**

1. In the OpenShift UI, click **Topology** .
1. Make sure that the Red Hat Developer Hub instance is available.


