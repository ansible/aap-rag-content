# 5. Migrating Red Hat Ansible Automation Platform to Red Hat Ansible Automation Platform Operator
## 5.2. Preparing for migration
### 5.2.4. Verifying network connectivity




To ensure successful migration of your data, verify that you have network connectivity from your new operator deployment to your old deployment database.

**Prerequisites**

Take note of the host and port information from your existing deployment. This information is located in the postgres.py file located in the conf.d directory.


**Procedure**

1. Create a YAML file to verify the connection between your new deployment and your old deployment database:


```
apiVersion: v1    kind: Pod    metadata:        name: dbchecker    spec:      containers:        - name: dbchecker          image: registry.redhat.io/rhel8/postgresql-13:latest          command: ["sleep"]          args: ["600"]
```


1. Apply the connection checker yaml file to your new project deployment:


```
oc project ansible-automation-platform    oc apply -f connection_checker.yaml
```


1. Verify that the connection checker pod is running:


```
oc get pods
```


1. Connect to a pod shell:


```
oc rsh dbchecker
```


1. After the shell session opens in the pod, verify that the new project can connect to your old project cluster:


```
pg_isready -h &lt;old-host-address&gt; -p &lt;old-port-number&gt; -U AutomationContoller
```

**Example**


```
&lt;old-host-address&gt;:&lt;old-port-number&gt; - accepting connections
```





