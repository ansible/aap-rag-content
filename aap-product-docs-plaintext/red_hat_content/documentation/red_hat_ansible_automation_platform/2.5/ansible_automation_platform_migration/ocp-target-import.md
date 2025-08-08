# 7. Target environment
## 7.2. OpenShift Container Platform
### 7.2.2. Importing the migration content to the target environment




To import your environment, scale down Ansible Automation Platform components, restore databases, replace encryption secrets, and scale services back up.

Note
This guide assumes you have the latest version of Ansible Automation Platform named 'aap' in the default 'aap' namespace and all default database names and database users.



**Procedure**

1. Begin by scaling down the Ansible Automation Platform deployment using `    idle_aap` .


```
oc patch ansibleautomationplatform aap --type merge -p '{"spec":{"idle_aap":true}}'
```

Wait for component pods to stop. Only the 6 Operator pods will remain running.


```
NAME                                                          READY   STATUS      RESTARTS   AGE    pod/aap-controller-migration-4.6.13-5swc6                     0/1     Completed   0          160m    pod/aap-gateway-operator-controller-manager-6b75c95458-4zrxv  2/2     Running     0          26h    pod/ansible-lightspeed-operator-controller-manager-b674c55b8-qncjp 2/2     Running     0          45h    pod/automation-controller-operator-controller-manager-6b79d48d4cchn 2/2     Running     0          45h    pod/automation-hub-operator-controller-manager-5cd674c984-5njfj 2/2     Running     0          45h    pod/eda-server-operator-controller-manager-645f4db5-d2flt     2/2     Running     0          45h    pod/resource-operator-controller-manager-86b8f7bb54-cvz6d     2/2     Running     0          45h
```


1. Scale down the Ansible Automation Platform Gateway Operator and Ansible Automation Platform Controller Operator.


```
oc scale --replicas=0 deployment aap-gateway-operator-controller-manager automation-controller-operator-controller-manager
```

Example output:


```
deployment.apps/aap-gateway-operator-controller-manager scaled    deployment.apps/automation-controller-operator-controller-manager scaled
```


1. Scale up the idled Postgres `    StatefulSet` .


```
oc scale --replicas=1 statefulset.apps/aap-postgres-15
```


1. Create a temporary Persistent Volume Claim (PVC) with appropriate settings and sizing.

`    aap-temp-pvc.yaml`


```
apiVersion: v1    kind: PersistentVolumeClaim    metadata:      name: aap-temp-pvc      namespace: aap    spec:      accessModes:        - ReadWriteOnce      resources:        requests:          storage: 200Gi
```


```
oc create -f aap-temp-pvc.yaml
```


1. Obtain the existing PostgreSQL image to use for temporary deployment.


```
echo $(oc get pod/aap-postgres-15-0 -o jsonpath="{.spec.containers[*].image}")
```


1. Create a temporary PostgreSQL deployment with the mounted temporary PVC.

`    aap-temp-postgres.yaml`


```
kind: Deployment    apiVersion: apps/v1    metadata:      name: aap-temp-postgres    spec:      replicas: 1      selector:        matchLabels:          app: aap-temp-postgres      template:        metadata:          labels:            app: aap-temp-postgres        spec:          containers:            - name: aap-temp-postgres              image: &lt;postgres image from previous step&gt;              command:                - /bin/sh                - '-c'                - sleep infinity              imagePullPolicy: Always              securityContext:                runAsNonRoot: true                allowPrivilegeEscalation: false              volumeMounts:                - name: aap-temp-pvc                  mountPath: /tmp/aap-temp-pvc          volumes:            - name: aap-temp-pvc              persistentVolumeClaim:                claimName: aap-temp-pvc
```


```
oc create -f aap-temp-postgres.yaml
```


1. Copy the export artifact to the temporary PostgreSQL pod.

First, obtain the pod name and set it as an environment variable:


```
export AAP_TEMP_POSTGRES=$(oc get pods --no-headers -o custom-columns="metadata.name" | grep aap-temp-postgres)
```

Test the environment variable:


```
echo $AAP_TEMP_POSTGRES
```

Example output:


```
aap-temp-postgres-7b6c57f87f-s2ldp
```

Copy the artifact and checksum to the PVC:


```
oc cp artifact.tar $AAP_TEMP_POSTGRES:/tmp/aap-temp-pvc/    oc cp artifact.tar.sha256 $AAP_TEMP_POSTGRES:/tmp/aap-temp-pvc/
```


1. Restore databases to Ansible Automation Platform PostgreSQL using the temporary PostgreSQL pod.

First, obtain PostgreSQL passwords for all three databases and the PostgreSQL admin password:


```
echo    for secret in aap-controller-postgres-configuration aap-hub-postgres-configuration aap-gateway-postgres-configuration    do      echo $secret      echo "PASSWORD: `oc get secrets $secret -o jsonpath="{.data['password']}" | base64 -d`"      echo "USER: `oc get secrets $secret -o jsonpath="{.data['username']}" | base64 -d`"      echo "DATABASE: `oc get secrets $secret -o jsonpath="{.data['database']}" | base64 -d`"      echo    done &amp;&amp; echo "POSTGRES ADMIN PASSWORD: `oc get secrets aap-gateway-postgres-configuration -o jsonpath="{.data['postgres_admin_password']}" | base64 -d`"
```

Enter into the temporary PostgreSQL deployment and change directory to the mounted PVC containing the copied artifact:


```
oc exec -it deployment.apps/aap-temp-postgres /bin/bash
```

Inside the pod, change directory to `    /tmp/aap-temp-pvc` and list its contents:


```
cd /tmp/aap-temp-pvc &amp;&amp; ls -1
```

Example output:


```
total 2240    -rw-r--r-- 1 1000900000 1000900000 2273280 Jun 13 17:41 artifact.tar    -rw-r--r-- 1 1000900000 1000900000      79 Jun 13 17:42 artifact.tar.sha256    drwxrws---. 2 root       1000900000   16384 Jun 13 17:40 lost+found
```

Verify the archive:


```
sha256sum --check artifact.tar.sha256
```

Example output:


```
artifact.tar: OK
```

Extract the artifact and verify its contents:


```
tar xf artifact.tar &amp;&amp; cd artifact &amp;&amp; sha256sum --check sha256sum.txt
```

Example output:


```
./controller/controller.pgc: OK     ./gateway/gateway.pgc: OK     ./hub/hub.pgc: OK
```

Drop the automation controller database:


```
dropdb -h aap-postgres-15 automationcontroller
```

Alter the user temporarily with the `    CREATEDB` role:


```
postgres=# ALTER USER automationcontroller WITH CREATEDB;
```

Create the database:


```
createdb -h aap-postgres-15 -U automationcontroller automationcontroller
```

Revert temporary user permission:


```
postgres=# ALTER USER automationcontroller WITH NOCREATEDB;
```

Restore the automation controller database:


```
pg_restore --clean-if-exists --no-owner -h aap-postgres-15 -U automationcontroller -d automationcontroller controller/controller.pgc
```

Restore the automation hub database:


```
pg_restore --clean-if-exists --no-owner -h aap-postgres-15 -U automationhub -d automationhub hub/hub.pgc
```

Restore the platform gateway database:


```
pg_restore --clean-if-exists --no-owner -h aap-postgres-15 -U gateway -d gateway gateway/gateway.pgc
```

Exit the pod:


```
exit
```


1. Replace database field encryption secrets.


```
oc set data secret/aap-controller-secret-key secret_key="&lt;unencoded controller_secret_key value from secrets.yml&gt;"    oc set data secret/aap-db-fields-encryption-secret secret_key="&lt;unencoded gateway_secret_key value from secrets.yml&gt;"    oc set data secret/aap-hub-db-fields-encryption database_fields.symmetric.key="&lt;unencoded hub_db_fields_encryption_key value from secrets.yml&gt;"
```


1. Clean up the temporary PostgreSQL and PVC.


```
oc delete -f aap-temp-postgres.yaml
```


```
oc delete -f aap-temp-pvc.yaml
```


1. Scale the platform gateway and automation controller Operators back up and wait for the platform gateway Operator reconciliation loop to complete.

The PostgreSQL `    StatefulSet` returns to idle.


```
oc scale --replicas=1 deployment aap-gateway-operator-controller-manager automation-controller-operator-controller-manager
```

Example output:


```
deployment.apps/aap-gateway-operator-controller-manager scaled    deployment.apps/automation-controller-operator-controller-manager scaled
```


```
oc logs -f $(oc get pods --no-headers -o custom-columns="metadata.name" | grep aap-gateway-operator)
```

Wait for reconciliation to stop.

Example output:


```
META: ending play    {"level":"info", "ts":"2025-06-12T15:41:29Z","logger":"runner", "msg": "Ansible-runner exited successfully", "job": "5672263053238024330","name":"aap", "namespace": "aap"}    PLAY RECAP ***********    localhost                  : ok=45   changed=0    unreachable=0    failed=0    skipped=63    rescued=0    ignored=0
```


1. Scale Ansible Automation Platform back up using `    idle_aap` .


```
oc patch ansibleautomationplatform aap --type merge -p '{"spec":{"idle_aap":false}}'
```

Example output:


```
ansibleautomationplatform.aap.ansible.com/aap patched
```


1. Wait for the `    aap-gateway` pod to be running and clean up old service endpoints.

Wait for the pod to be running.

Example output:


```
pod/aap-gateway-6c989b846c-47b91 2/2 Running 0 45s
```


```
for i in HTTPPort Route ServiceNode; do; oc exec -it deployment.apps/aap-gateway aap-gateway-manage shell -c 'from aap_gateway_api.models import '$i'; print('$i'.objects.all().delete())'; done
```

Example output:


```
(23, {'aap_gateway_api.ServiceAPIRoute': 4, 'aap_gateway_api.AdditionalRoute': 7, 'aap_gateway_api.Route': 11, 'aap_gateway_api.HTTPPort': 1})    (0, {})    (4, {'aap_gateway_api.ServiceNode': 4})
```


1. Run `    awx-manage` to deprovision instances.

Obtain the automation controller pod:


```
export AAP_CONTROLLER_POD=$(oc get pods --no-headers -o custom-columns=":metadata.name" | grep aap-controller-task)
```

Test the environment variable:


```
echo $AAP_CONTROLLER_POD
```

Example output:


```
aap-controller-task-759b6d9759-r59q9
```

Enter into the automation controller pod:


```
oc exec -it $AAP_CONTROLLER_POD /bin/bash    awx-manage list_instances
```

Example output:


```
bash-4.4$    [controlplane capacity=642 policy=100%]    aap-controller-task-759b6d9759-r59q9 capacity=642 node_type=control version=4.6.15 heartbeat="2025-06-12 21:39:48"    node1.example.org capacity=0 node_type=hybrid version=4.6.13 heartbeat="2025-05-30 17:22:11"    [default capacity=0 policy=100%]    node1.example.org capacity=0 node_type=hybrid version=4.6.13 heartbeat="2025-05-30 17:22:11"    node2.example.org capacity=0 node_type=execution version ansible-runner-2.4.1 heartbeat="2025-05-30 17:22:08"
```

Remove old nodes with `    awx-manage` , leaving only `    aap-controller-task` :


```
awx-manage deprovision_instance --host=node1.example.org    awx-manage deprovision_instance --host=node2.example.org
```


1. Run the `    curl` command to repair automation hub filesystem data.


```
curl -d '{"verify_checksums": true}' -X POST -k https://&lt;aap_url&gt;/api/galaxy/pulp/api/v3/repair/ -u &lt;admin_user&gt;:&lt;restored_admin_password&gt;
```




