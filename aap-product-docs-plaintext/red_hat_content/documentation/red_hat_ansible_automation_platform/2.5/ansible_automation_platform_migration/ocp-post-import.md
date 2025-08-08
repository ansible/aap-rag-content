# 7. Target environment
## 7.2. OpenShift Container Platform
### 7.2.3. Reconciling the target environment post-import




After importing your migration artifact, perform the following steps to reconcile your target environment.

**Procedure**

1. Modify the Django `    SECRET_KEY` secrets to match the source platform.
1. Deprovision and reconfigure platform gateway service nodes.
1. Re-run platform gateway nodes and services register logic.
1. Convert container-specific settings to OpenShift Container Platform-appropriate formats.
1. Reconcile container resource allocations to OpenShift Container Platform resources.


