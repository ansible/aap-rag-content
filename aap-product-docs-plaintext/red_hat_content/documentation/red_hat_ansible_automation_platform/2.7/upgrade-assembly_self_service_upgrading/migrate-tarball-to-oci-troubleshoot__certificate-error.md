# Upgrade Ansible automation portal
## Troubleshooting the migration
### x509 certificate errors for private registries

**Symptom:** Init container logs show `x509: certificate signed by unknown authority` or `x509: certificate has expired`.

**Cause:** Your mirror registry uses a self-signed or internal CA certificate that the `skopeo` utility cannot verify.

**Resolution:** Mount your CA certificate into the init container at the per-registry trust path. Obtain your CA certificate bundle (including the full chain), create a ConfigMap, and update your Helm values to mount it. For detailed instructions, see the RHDH documentation: [Install plugins from OCI registries by using custom certificates](https://redhat-developer.github.io/red-hat-developers-documentation-rhdh/main/plugins-rhdh-install/#rinstall-plugins-from-oci-registries-by-using-custom-certificates).

