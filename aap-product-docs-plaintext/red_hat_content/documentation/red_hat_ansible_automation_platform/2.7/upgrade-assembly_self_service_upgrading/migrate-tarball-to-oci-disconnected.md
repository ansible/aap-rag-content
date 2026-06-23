# Upgrade Ansible automation portal
## Migrating in air-gapped and disconnected environments

For air-gapped or disconnected clusters, mirror the OCI images to your internal registry and configure the Helm chart to use your mirror.

For air-gapped or partially disconnected clusters, you must mirror the OCI images to your internal registry and configure the Helm chart to use your mirror instead of `registry.redhat.io`.

