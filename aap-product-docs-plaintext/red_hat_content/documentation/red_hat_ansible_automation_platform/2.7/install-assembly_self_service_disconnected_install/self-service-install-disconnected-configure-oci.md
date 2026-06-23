# Install Ansible automation portal in air-gapped OpenShift Container Platform environments
## Configure the Helm chart for air-gapped OCI delivery

Configure Helm chart values for disconnected OCI plug-in delivery by setting the mirror registry, plug-in mode, and container image references.

### About this task

Set the following values in your Helm values file for a disconnected installation with OCI delivery:

```
redhat-developer-hub:
global:
pluginMode: oci
imageTagInfo: "<plugin-version>"
imageRegistry: "<your-mirror-registry-host>"
catalogIndex:
image:
registry: "<your-mirror-registry-host>"
upstream:
backstage:
image:
repository: rhdh/rhdh-hub-rhel9
tag: "<platform-version>"
postgresql:
image:
repository: rhel9/postgresql-15
tag: "latest"
```


Note:

Set `imageRegistry` and `catalogIndex.image.registry` to the registry host only (for example, `mirror.example.com` or `mirror.example.com:5000`). Use a hostname that cluster nodes can resolve and pull from. Do not include a repository path in `imageRegistry`. Setting `imageRegistry` does not override the catalog index registry; you must set `catalogIndex.image.registry` separately.

Note:

If your mirror uses a non-standard path for the Ansible plug-in OCI image, set `ociPluginImage` to the full image path (for example, `<your-mirror-registry-host>/custom-path/automation-portal`).

### Procedure

Complete the standard install steps using these values.

