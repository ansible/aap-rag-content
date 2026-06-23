# Install Ansible automation portal in air-gapped OpenShift Container Platform environments
## Prerequisites for disconnected installation

Review the mandatory subscriptions, permissions, and platform access required before starting the disconnected installation of the Ansible automation portal.

Fulfilling these prerequisites helps ensure a successful deployment.

- You have a valid subscription to Red Hat Ansible Automation Platform.
- You have access to an instance of Red Hat Ansible Automation Platform with the appropriate permissions to create an OAuth application.
- You have access to a Red Hat OpenShift Container Platform instance with the appropriate permissions within your project to create an application.
- You have installed `oc`, the OpenShift command-line interface (CLI) tool, on your local machine.
- You have installed Helm 3.10 or newer.
- You have installed `skopeo` and `podman` for mirroring container images and plug-in artifacts.
- You have internet access to pull images and charts from public repositories, including `registry.redhat.io`.
- A Red Hat pull secret that allows you to pull images from `registry.redhat.io`.
- You have a method to provide the Ansible plug-ins in the disconnected environment:
* For OCI delivery: A method to mirror the OCI artifacts image referenced by `imageTagInfo`.
* For HTTP plug-in registry: The ability to host the plug-in tarball files.
- You have registry credentials for the registry endpoint used by the dynamic plug-in installer.


Important:

The image versions and compatibility requirements vary between Helm chart releases. Before you begin, consult the [Ansible Automation Portal Lifecycle](https://access.redhat.com/page/ansible-automation-platform-self-service-automation-portal-lifecycle) page for version mappings between the Helm chart, Red Hat Developer Hub, and PostgreSQL.

