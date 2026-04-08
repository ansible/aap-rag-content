# 10. Upgrading Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform
## 10.7. Upgrading an external database for platform gateway on Red Hat Ansible Automation Platform Operator




To upgrade from Ansible Automation Platform 2.4 to 2.6 with an external database, you must scale down your Operator deployment, upgrade your PostgreSQL, then scale your deployment back up.

**Prerequisites**

- A 2.4 automation controller and automation hub deployment with an external PostgreSQL 13 database
- A newly provisioned PostgreSQL 15 database for the new platform gateway component


**Procedure**

1. Create a secret `    postgres-config-gateway` with PostgreSQL 15 credentials for the platform gateway component. For example:


```
apiVersion: v1    kind: Secret    metadata:      name: postgres-config-gateway      namespace: aap    stringData:      host: "&lt;DB_HOST_OR_IP&gt;"      port: "&lt;DB_PORT&gt;"     # default is 5432      database: "&lt;DB_NAME&gt;" # for example "gateway"      username: "&lt;DB_USER&gt;" # for example "gateway"      password: "&lt;DB_PASSWORD&gt;"      sslmode: "prefer"      type: "unmanaged"    type: Opaque
```


1. Add your newly created secret to your Ansible Automation Platform instance:


```
spec:      postgres_configuration_secret: postgres-config-gateway
```


1. Scale down your deployments in their respective namespaces using:

`    oc scale deployment --replicas=0 -n &lt;component-namespace&gt; &lt;component-deployment&gt;`


1. Automation controller:


1.  `            automation-controller-operator-controller-manager`
1.  `            &lt;controller-name&gt;-controller-task`
1.  `            &lt;controller-name&gt;-controller-web`

1. Automation hub:


1.  `            automation-hub-operator-controller-manager`
1.  `            &lt;hub-name&gt;-hub-api`
1.  `            &lt;hub-name&gt;-hub-content`
1.  `            &lt;hub-name&gt;-hub-redis`
1.  `            &lt;hub-name&gt;-hub-worker`

1. The remaining operators:


1.  `            ansible-lightspeed-operator-controller-manager`
1.  `            eda-server-operator-controller-manager`
1.  `            resource-operator-controller-manager`


1. Upgrade your PostgreSQL 13 to PostgreSQL 15.
1. Scale your deployments back up using:

`    oc scale deployment --replicas=1 -n &lt;component-namespace&gt; &lt;component-deployment&gt;`


1. Log in to Red Hat OpenShift Container Platform.
1. Navigate toOperators→Installed Operators.
1. Click the ⋮ icon next to your deployment and then clickEdit Subscription.
1. From the **Details** tab, selectUpdate Channel.
1. Select **stable-2.6** as the channel and clickSave.
1. Deploy Ansible Automation Platform 2.6 using the following custom resource (CR):


```
apiVersion: aap.ansible.com/v1alpha1    kind: AnsibleAutomationPlatform    metadata:      name: aap    spec:          database:        database_secret: postgres-config-gateway          controller:        name: existing-controller          eda:        disabled: true          hub:        name: existing-hub
```




**Verification**

To verify your upgrade was successful, go to your users, collection, job history or similar and confirm that they are on the new 2.6 instance and in the new PostgreSQL 15 databases.


