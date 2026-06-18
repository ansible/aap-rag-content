# Plug-in delivery method

Ansible automation portal supports two plug-in delivery methods. Use OCI container delivery for new installations, or plan to migrate from the deprecated HTTP plug-in registry.

- **OCI container delivery (recommended):** Ansible automation portal pulls an Open Container Initiative (OCI) image from `registry.redhat.io` that contains the Ansible plug-ins. Use this method for new installations and production deployments.
- **HTTP plug-in registry (deprecated):** You deploy an in-cluster HTTP service that hosts plug-in tarball files. This method is deprecated and will be removed in a future release of Ansible Automation Platform. If you already use this method, plan to migrate to OCI container delivery.


Important:

Set `redhat-developer-hub.global.pluginMode` to `oci`. The chart default is `tarball`. Before you install, confirm your environment is supported on the Ansible automation portal lifecycle page (portal version, Ansible Automation Platform compatibility, and OpenShift Container Platform compatibility).

Note:

For a disconnected cluster, complete the prerequisites in this guide, then continue with the disconnected installation guide.
