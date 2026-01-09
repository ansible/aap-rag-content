# 3. Installing the Ansible plug-ins with the Operator on OpenShift Container Platform
## 3.7. Adding a custom ConfigMap




Create a custom Red Hat Developer Hub ConfigMap, typically named `app-config-rhdh` , to store custom application settings.

**Procedure**

- Create a Red Hat Developer Hub ConfigMap following the procedure in the [Creating and using config maps](https://docs.redhat.com/en/documentation/openshift_container_platform/4.15/html-single/nodes/index#configmaps) section of the OpenShift Container Platform _Nodes_ guide. The following examples use a custom ConfigMap named `    app-config-rhdh` .

To edit your custom ConfigMap, log in to the OpenShift UI and navigate toSelect Project ( developerHubProj )→ConfigMaps→{developer-hub}-app-config→EditConfigMaps→app-config-rhdh.




