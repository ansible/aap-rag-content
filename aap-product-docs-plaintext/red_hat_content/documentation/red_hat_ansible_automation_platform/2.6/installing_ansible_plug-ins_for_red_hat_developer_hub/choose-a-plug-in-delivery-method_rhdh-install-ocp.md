# 2. Installing the Ansible plug-ins with a Helm chart on OpenShift Container Platform
## 2.3. Choose a plug-in delivery method




Ansible plug-ins for Red Hat Developer Hub support two delivery methods. Choose the method that fits your environment:

-  **OCI container (recommended)** : Red Hat Developer Hub pulls the Ansible plug-ins directly from registry.redhat.io as OCI artifacts during startup. You do not need to use any manual file downloads or plug-in registry deployment.
-  **HTTP plug-in registry** : Manually download the Ansible plug-ins tarball files, deploy an HTTP plug-in registry in your OpenShift cluster, and configure Red Hat Developer Hub to pull plug-ins from that registry. Use this method if your environment cannot pull OCI artifacts from `    registry.redhat.io` .


Complete one of the following procedures before configuring the Ansible plug-ins in the Required configuration section.

