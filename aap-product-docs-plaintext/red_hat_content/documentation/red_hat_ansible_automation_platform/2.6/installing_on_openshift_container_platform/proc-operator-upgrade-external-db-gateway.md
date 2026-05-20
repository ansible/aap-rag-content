# 10. Upgrading Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform
## 10.7. Upgrading an external database for platform gateway on Red Hat Ansible Automation Platform Operator

To upgrade from Ansible Automation Platform 2.4 to 2.6 with an external database, you must scale down your Operator deployment, upgrade your PostgreSQL, then scale your deployment back up.

**Prerequisites**

- A 2.4 automation controller and automation hub deployment with an external PostgreSQL 13 database
- A newly provisioned PostgreSQL 15 database for the new platform gateway component

**Procedure**

1. Create a secret `postgres-config-gateway` with PostgreSQL 15 credentials for the platform gateway component. For example:

apiVersion: v1
kind: Secret
metadata:
name: postgres-config-gateway
namespace: aap
stringData:
host: "<DB_HOST_OR_IP>"
port: "<DB_PORT>"     # default is 5432
database: "<DB_NAME>" # for example "gateway"
username: "<DB_USER>" # for example "gateway"
password: "<DB_PASSWORD>"
sslmode: "prefer"
type: "unmanaged"
type: Opaque

2. Add your newly created secret to your Ansible Automation Platform instance:

spec:
postgres_configuration_secret: postgres-config-gateway

3. Scale down your deployments in their respective namespaces using:

`oc scale deployment --replicas=0 -n <component-namespace> <component-deployment>`


1. Automation controller:


1. `automation-controller-operator-controller-manager`
2. `<controller-name>-controller-task`
3. `<controller-name>-controller-web`

2. Automation hub:


1. `automation-hub-operator-controller-manager`
2. `<hub-name>-hub-api`
3. `<hub-name>-hub-content`
4. `<hub-name>-hub-redis`
5. `<hub-name>-hub-worker`

3. The remaining operators:


1. `ansible-lightspeed-operator-controller-manager`
2. `eda-server-operator-controller-manager`
3. `resource-operator-controller-manager`

4. Upgrade your PostgreSQL 13 to PostgreSQL 15.

5. Scale your deployments back up using:

`oc scale deployment --replicas=1 -n <component-namespace> <component-deployment>`

6. Log in to Red Hat OpenShift Container Platform.

7. Navigate to Operators → Installed Operators.

8. Click the ⋮ icon next to your deployment and then click Edit Subscription.

9. From the **Details** tab, select Update Channel.

10. Select **stable-2.6** as the channel and click Save.

11. Deploy Ansible Automation Platform 2.6 using the following custom resource (CR):

apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
name: aap
spec:

database:
database_secret: postgres-config-gateway

controller:
name: existing-controller

eda:
disabled: true

hub:
name: existing-hub

**Verification**

To verify your upgrade was successful, go to your users, collection, job history or similar and confirm that they are on the new 2.6 instance and in the new PostgreSQL 15 databases.

