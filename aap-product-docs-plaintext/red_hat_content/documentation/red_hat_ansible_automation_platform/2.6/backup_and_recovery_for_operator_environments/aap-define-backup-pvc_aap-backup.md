# 2. Creating Red Hat Ansible Automation Platform backup resources
## 2.2. Define custom backup Persistent Volume Claims




Define custom Persistent Volume Claims (PVCs) to control backup storage allocation for each Ansible Automation Platform component. Specify unique PVC names, storage classes, and volume sizes at both global and component levels to differentiate between backup runs.

**Prerequisites**

- You have an active Red Hat Ansible Automation Platform deployment on OpenShift Container Platform.
- You have the `    oc` CLI tool installed and cluster administrator access.


**Procedure**

1. Create a backup YAML file, for example `    custom-pvc-backup.yaml` , that defines the `    backup_pvc` and `    create_backup_pvc` parameters for each component:


```
apiVersion: aap.ansible.com/v1alpha1    kind: AnsibleAutomationPlatformBackup    metadata:      name: aapbackup    spec:      backup_pvc: custom-aap-backup-pvc<span id="CO1-1"><!--Empty--></span><span class="callout">1</span>backup_storage_class: nfs-local-rwx      backup_storage_requirements: 7Gi      create_backup_pvc: true<span id="CO1-2"><!--Empty--></span><span class="callout">2</span>deployment_name: aap      controller:<span id="CO1-3"><!--Empty--></span><span class="callout">3</span>backup_pvc: custom-controller-backup-pvc        backup_resource_requirements:          limits:            cpu: "4"            memory: 8Gi          requests:            cpu: "2"            memory: 4Gi        backup_storage_class: standard-csi        backup_storage_requirements: 7Gi        create_backup_pvc: true      eda:        backup_pvc: custom-eda-backup-pvc        backup_storage_class: standard-csi        backup_storage_requirements: 7Gi        create_backup_pvc: true      hub:        backup_pvc: custom-hub-backup-pvc        backup_storage_class: nfs-local-rwx        backup_storage_requirements: 7Gi        create_backup_pvc: true
```


1. Apply the configuration:


```
$ oc apply -f custom-pvc-backup.yaml
```




**Verification**

- Confirm that the PVCs were created:


```
$ oc get pvc -n &lt;namespace&gt;
```

The output displays the custom PVCs for each component:


```
NAME                             STATUS   VOLUME       CAPACITY   ACCESS MODES   STORAGECLASS    custom-aap-backup-pvc            Bound    pv-aap       7Gi        RWX            nfs-local-rwx    custom-controller-backup-pvc     Bound    pv-ctrl      7Gi        RWO            standard-csi    custom-eda-backup-pvc            Bound    pv-eda       7Gi        RWO            standard-csi    custom-hub-backup-pvc            Bound    pv-hub       7Gi        RWX            nfs-local-rwx
```




