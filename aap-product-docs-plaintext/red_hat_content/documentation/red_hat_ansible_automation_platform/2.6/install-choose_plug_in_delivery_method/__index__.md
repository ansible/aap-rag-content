# Plug-in delivery method

Ansible plug-ins for Red Hat Developer Hub support two delivery methods. Select the method that fits your environment.

Ansible automation portal supports two plug-in delivery methods:

- **OCI container delivery (recommended)**: Ansible automation portal automatically pulls an Open Container Initiative (OCI) container from `registry.redhat.io` that contains the plug-ins. Use this method for new installations.
- **HTTP plug-in registry (deprecated)**: Manually create an HTTP plug-in registry that hosts plug-in tarball files. This method is deprecated and will be removed in a future release of Ansible Automation Platform. Existing installations that use this method should migrate to OCI container delivery.


Note:

If you are installing Ansible automation portal in a disconnected or air-gapped OpenShift Container Platform environment, complete the pre-installation configuration in this chapter and then follow the procedures in the disconnected installation chapter. The disconnected installation chapter includes additional steps for mirroring container images, configuring registry authentication, and installing the Helm chart in isolated environments.
