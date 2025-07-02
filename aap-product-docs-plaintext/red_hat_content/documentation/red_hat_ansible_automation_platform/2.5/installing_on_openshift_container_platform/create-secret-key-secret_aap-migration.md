# 5. Migrating Red Hat Ansible Automation Platform to Red Hat Ansible Automation Platform Operator
## 5.2. Preparing for migration
### 5.2.2. Creating a secret key secret




To migrate your data to Ansible Automation Platform Operator on OpenShift Container Platform, you must create a secret key. If you are migrating automation controller, automation hub, and Event-Driven Ansible you must have a secret key for each that matches the secret key defined in the inventory file during your initial installation. Otherwise, the migrated data remains encrypted and unusable after migration.

Note
When specifying the symmetric encryption secret key on the custom resources, note that for automation controller the field is called `secret_key_name` . But for automation hub and Event-Driven Ansible, the field is called `db_fields_encryption_secret` .



Note
In the Kubernetes secrets, automation controller and Event-Driven Ansible use the same stringData key ( `secret_key` ) but, automation hub uses a different key ( `database_fields.symmetric.key` ).



**Procedure**

1. Locate the old secret keys in the inventory file you used to deploy Ansible Automation Platform in your previous installation.
1. Create a YAML file for your secret keys:


```
---    apiVersion: v1    kind: Secret    metadata:      name: &lt;controller-resourcename&gt;-secret-key      namespace: &lt;target-namespace&gt;    stringData:      secret_key: &lt;content of /etc/tower/SECRET_KEY from old controller&gt;    type: Opaque    ---    apiVersion: v1    kind: Secret    metadata:      name: &lt;eda-resourcename&gt;-secret-key      namespace: &lt;target-namespace&gt;    stringData:      secret_key: &lt;/etc/ansible-automation-platform/eda/SECRET_KEY&gt;    type: Opaque    ---    apiVersion: v1    kind: Secret    metadata:      name: &lt;hub-resourcename&gt;-secret-key      namespace: &lt;target-namespace&gt;    stringData:      database_fields.symmetric.key: &lt;/etc/pulp/certs/database_fields.symmetric.key&gt;    type: Opaque
```

Note
If `    admin_password_secret` is not provided, the operator looks for a secret named `    &lt;resourcename&gt;-admin-password` for the admin password. If it is not present, the operator generates a password and creates a secret from it named `    &lt;resourcename&gt;-admin-password` .




1. Apply the secret key YAML to the cluster:


```
oc apply -f &lt;yaml-file&gt;
```




