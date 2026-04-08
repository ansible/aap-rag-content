# 5. Configuring Red Hat Ansible Automation Platform components on Red Hat Ansible Automation Platform Operator
## 5.3. Configuring automation hub on Red Hat OpenShift Container Platform web console
### 5.3.4. Finding and deleting PVCs




A persistent volume claim (PVC) is a storage volume used to store data that automation hub and automation controller applications use. This persistence is a key feature of static provisioning. If you redeploy an instance using the same name, the Operator must bind to these existing PVCs, allowing for data continuity across deployments. If you are confident that you no longer need a PVC, or have backed it up elsewhere, you can manually delete them.

**Procedure**

1. List the existing PVCs in your deployment namespace:


```
oc get pvc -n &lt;namespace&gt;
```


1. Identify the PVC associated with your previous deployment by comparing the old deployment name and the PVC name.
1. Delete the old PVC:


```
oc delete pvc -n &lt;namespace&gt; &lt;pvc-name&gt;
```




