# Configure your Ansible Automation Platform deployment
## Find and delete PVCs

A persistent volume claim (PVC) is a storage volume used to store data that automation hub and automation controller applications use.

### About this task

This persistence is a key feature of static provisioning. If you redeploy an instance using the same name, the Operator must bind to these existing PVCs, allowing for data continuity across deployments. If you are confident that you no longer need a PVC, or have backed it up elsewhere, you can manually delete them.

### Procedure

1.  List the existing PVCs in your deployment namespace:


```
oc get pvc -n <namespace>
```

2.  Identify the PVC associated with your previous deployment by comparing the old deployment name and the PVC name.
3.  Delete the old PVC:


```
oc delete pvc -n <namespace> <pvc-name>
```

