# 5. Configuring Red Hat Ansible Automation Platform components on Red Hat Ansible Automation Platform Operator
## 5.4. Configure static storage for Ansible Automation Platform
### 5.4.2. Pre-create Persistent Volume Claims for manual provisioning




Follow this process to manually prepare storage for an Ansible Automation Platform installation when dynamic provisioning is disabled.

**Prerequisites**

- You have an active OpenShift Container Platform CLI ( `    oc` ) session.
- You have defined Persistent Volumes (PVs) that meet the minimum size and access mode requirements for your components.


**Procedure**

1. Identify the name you intend to use for your `    AnsibleAutomationPlatform` deployment (for example, `    myaap` ).
1. Create a PVC manifest for the PostgreSQL database using the required naming convention: `    postgres-15-&lt;deployment_name&gt;-0` .
1. Ensure the `    accessModes` and `    resources.requests.storage` match your manually provisioned PV.
1. Apply the PVC manifest:


```
oc apply -f postgres-pvc.yaml
```


1. Repeat these steps for other components, such as automation hub, using the correct naming conventions.
1. Leave the `    storage_class` fields empty or omit them from the specification. This forces the Operator to use the pre-created PVCs.

Note
Unlike core components, the `    AnsibleAutomationPlatformBackup` and `    Restore` custom resources provide a `    backup_pvc` parameter. You must use this parameter to specify your custom PVC name instead of relying on naming conventions.






**Verification**

- Check the status of the PVCs to ensure they are in a `    Bound` state:


```
oc get pvc -n &lt;namespace&gt;
```




