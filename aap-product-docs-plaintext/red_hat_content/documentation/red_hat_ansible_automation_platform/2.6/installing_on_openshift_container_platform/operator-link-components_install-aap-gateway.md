# 2. Installing Red Hat Ansible Automation Platform gateway on Red Hat OpenShift Container Platform
## 2.1. Linking your components to the platform gateway

After installing the Ansible Automation Platform Operator in your namespace you can set up your **Ansible Automation Platform** instance. Then link all the platform components to a single user interface.

**Procedure**

1. Log in to Red Hat OpenShift Container Platform.

2. Navigate to Operators → Installed Operators.

3. Select your Ansible Automation Platform Operator deployment.

4. Select the **Details** tab.

5. On the **Ansible Automation Platform** tile click Create instance.

6. From the **Create Ansible Automation Platform** page enter a name for your instance in the **Name** field.

7. Click YAML view and replace the `spec` section with the following:

spec:
database:
resource_requirements:
requests:
cpu: 200m
memory: 512Mi
storage_requirements:
requests:
storage: 100Gi

controller:
disabled: false

eda:
disabled: false

hub:
disabled: false
storage_type: file
file_storage_storage_class: <read-write-many-storage-class>
file_storage_size: 10Gi

8. You must specify your desired value for the `<read-write-many-storage-class>` placeholder.

9. Click Create.

**Verification**

**Verify instance deployment (UI):**

1. Navigate to Operators → Installed Operators.
2. Select your Ansible Automation Platform Operator deployment.
3. Select the **All instances** tab.
4. Verify that the **Ansible Automation Platform** instance, **Automation Controller**, **Event-Driven Ansible**, and **Automation Hub** instances are listed.

**Verify pod status (UI):**

1. Navigate to Workloads → Pods.
2. Switch to the project (namespace) where you deployed the instance.
3. Verify that all related pods display a **Running** or **Completed** status.

**Verify Platform Route (CLI):**

Run the following command to confirm the URL for accessing the platform gateway:

oc get route

