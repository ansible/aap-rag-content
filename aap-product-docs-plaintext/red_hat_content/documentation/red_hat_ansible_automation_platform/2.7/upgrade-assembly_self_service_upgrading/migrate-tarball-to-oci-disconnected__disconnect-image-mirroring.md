# Upgrade Ansible automation portal
## Migrating in air-gapped and disconnected environments
### Mirroring Ansible plug-in images

The Ansible plug-in OCI artifacts must be mirrored to your internal registry. Mirror the images from a host with access to `registry.redhat.io`:

```
$ podman pull registry.redhat.io/ansible-automation-platform/automation-portal:<plugin-version>
$ podman tag registry.redhat.io/ansible-automation-platform/automation-portal:<plugin-version> \
<your-mirror-registry>/ansible-automation-platform/automation-portal:<plugin-version>
$ podman push <your-mirror-registry>/ansible-automation-platform/automation-portal:<plugin-version>
```
When mirroring, you must preserve the original repository path. For example, mirror `registry.redhat.io/ansible-automation-platform/automation-portal:2.2` to `<your-mirror-registry>/ansible-automation-platform/automation-portal:2.2`.

