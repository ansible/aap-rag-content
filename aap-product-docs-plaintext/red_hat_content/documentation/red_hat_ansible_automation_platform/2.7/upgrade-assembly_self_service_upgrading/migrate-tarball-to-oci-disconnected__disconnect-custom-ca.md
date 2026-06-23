# Upgrade Ansible automation portal
## Migrating in air-gapped and disconnected environments
### Using custom CA certificates for private registries

If your mirror registry uses a self-signed or internal CA certificate, the `install-dynamic-plugins` init container will fail with an `x509: certificate signed by unknown authority` error. You must mount your CA certificate into the init container.

The recommended approach is to create a ConfigMap and mount it at the per-registry trust path. For complete instructions, see the RHDH documentation on installing plug-ins from OCI registries by using custom certificates.

