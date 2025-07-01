# 5. Migrating Red Hat Ansible Automation Platform to Red Hat Ansible Automation Platform Operator
## 5.2. Preparing for migration
### 5.2.3. Creating a postgresql configuration secret




For migration to be successful, you must provide access to the database for your existing deployment.

**Procedure**

1. Create a YAML file for your postgresql configuration secret:


```
apiVersion: v1    kind: Secret    metadata:      name: &lt;resourcename&gt;-old-postgres-configuration      namespace: &lt;target namespace&gt;    stringData:      host: "&lt;external ip or url resolvable by the cluster&gt;"      port: "&lt;external port, this usually defaults to 5432&gt;"      database: "&lt;desired database name&gt;"      username: "&lt;username to connect as&gt;"      password: "&lt;password to connect with&gt;"    type: Opaque
```


1. Apply the postgresql configuration yaml to the cluster:


```
oc apply -f &lt;old-postgres-configuration.yml&gt;
```

