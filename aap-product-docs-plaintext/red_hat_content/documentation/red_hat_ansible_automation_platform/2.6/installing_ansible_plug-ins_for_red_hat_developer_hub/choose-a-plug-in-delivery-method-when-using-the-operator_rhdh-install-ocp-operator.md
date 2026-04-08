# 3. Installing the Ansible plug-ins with the Operator on OpenShift Container Platform
## 3.4. Choose a plug-in delivery method when using the Operator




Ansible plug-ins for Red Hat Developer Hub support two delivery methods. Choose the method that fits your environment:

+ * **OCI container (recommended)** : Red Hat Developer Hub pulls the Ansible plug-ins directly from `registry.redhat.io` as OCI artifacts during startup.

-  **HTTP plug-in registry** : Manually download the Ansible plug-ins tarball file and deploy an HTTP plug-in registry in your OpenShift cluster. Use this method if your environment cannot pull OCI artifacts from `    registry.redhat.io` .


Complete one of the following procedures before configuring the dynamic plug-ins.

