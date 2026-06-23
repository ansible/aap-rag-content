# Configure static storage for Ansible Automation Platform
## Pre-create Persistent Volume Claims for manual provisioning
### Results

Check the status of the PVCs to ensure they are in a Bound state:

```
oc get pvc -n <namespace>
```

