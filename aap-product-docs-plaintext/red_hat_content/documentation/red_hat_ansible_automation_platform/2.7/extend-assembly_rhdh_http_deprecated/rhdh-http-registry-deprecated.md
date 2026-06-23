# Install Ansible plug-ins using an HTTP plug-in registry (deprecated)
## Install Ansible plug-ins using an HTTP plug-in registry (deprecated)

The HTTP plug-in registry method is deprecated and will be removed in a future release. Red Hat recommends using OCI-based plug-in delivery instead.

Important:

The HTTP plug-in registry method is deprecated and will be removed in a future release. Red Hat recommends using OCI-based plug-in delivery as described in the main installation procedure. For disconnected environments, use OCI image mirroring instead of an HTTP registry.

The following procedures describe how to install the Ansible plug-ins using an HTTP plug-in registry hosted in your OpenShift Container Platform cluster. This method requires downloading plug-in tarballs, creating an HTTP registry in the cluster, and referencing the plug-ins by HTTP URL with SHA integrity hashes.

