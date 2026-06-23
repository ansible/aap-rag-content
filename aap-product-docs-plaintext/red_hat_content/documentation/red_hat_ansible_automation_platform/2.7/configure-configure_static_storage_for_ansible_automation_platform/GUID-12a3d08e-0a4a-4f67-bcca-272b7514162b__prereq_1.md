# Configure static storage for Ansible Automation Platform
## Pre-create Persistent Volume Claims for manual provisioning
### Before you begin

- You have an active OpenShift Container Platform CLI (`oc`) session.
- You have defined Persistent Volumes (PVs) that meet the minimum size and access mode requirements for your components.

### Procedure

1.  Identify the name you intend to use for your `AnsibleAutomationPlatform` deployment (for example, myaap).
2.  Create a PVC manifest for the PostgreSQL database using the required naming convention: `postgres-15-<deployment_name>-0`,
3.  Ensure the `accessModes` and `resources.requests.storage` match your manually provisioned PV.
4.  Apply the PVC manifest:


```
oc apply -f postgres-pvc.yaml
```

5.  Repeat these steps for other components, such as automation Hub, using the correct naming conventions.
6.  Leave the `storage_class` fields empty or omit them from the specification. This forces the Operator to use the pre-created PVCs.

Note:
Unlike core components, the `AnsibleAutomationPlatformBackup` and `Restore` custom resources provide a `backup_pvc` parameter. You must use this parameter to specify your custom PVC name instead of relying on naming conventions.

