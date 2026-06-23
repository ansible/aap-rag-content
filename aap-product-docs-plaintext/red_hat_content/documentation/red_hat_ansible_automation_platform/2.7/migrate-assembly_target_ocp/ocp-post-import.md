# Prepare the OpenShift Container Platform target environment and import migration content
## Reconcile the target environment post-import

After importing your migration artifact, perform the following steps to reconcile your target environment.

### Procedure

1.  Modify the Django `SECRET_KEY` secrets to match the source platform.
2.  Deprovision and reconfigure platform gateway service nodes.
3.  Re-run platform gateway nodes and services register logic.
4.  Convert container-specific settings to OpenShift Container Platform-appropriate formats.
5.  Reconcile container resource allocations to OpenShift Container Platform resources.

