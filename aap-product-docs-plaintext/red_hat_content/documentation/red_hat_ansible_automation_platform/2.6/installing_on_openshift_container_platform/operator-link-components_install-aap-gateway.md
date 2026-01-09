# 2. Installing Red Hat Ansible Automation Platform gateway on Red Hat OpenShift Container Platform
## 2.1. Linking your components to the platform gateway




After installing the Ansible Automation Platform Operator in your namespace you can set up your **Ansible Automation Platform** instance. Then link all the platform components to a single user interface.

**Procedure**

1. Log in to Red Hat OpenShift Container Platform.
1. Navigate toOperators→Installed Operators.
1. Select your Ansible Automation Platform Operator deployment.
1. Select the **Details** tab.
1. On the **Ansible Automation Platform** tile clickCreate instance.
1. From the **Create Ansible Automation Platform** page enter a name for your instance in the **Name** field.
1. ClickYAML viewand replace the `    spec` section with the following:


```
spec:      database:        resource_requirements:          requests:            cpu: 200m            memory: 512Mi        storage_requirements:          requests:            storage: 100Gi          controller:        disabled: false          eda:        disabled: false          hub:        disabled: false        storage_type: file        file_storage_storage_class: &lt;read-write-many-storage-class&gt;        file_storage_size: 10Gi
```


1. You must specify your desired value for the `    &lt;read-write-many-storage-class&gt;` placeholder.
1. ClickCreate.


**Verification**

**Verify instance deployment (UI):**


1. Navigate toOperators→Installed Operators.
1. Select your Ansible Automation Platform Operator deployment.
1. Select the **All instances** tab.
1. Verify that the **Ansible Automation Platform** instance, **Automation Controller** , **Event-Driven Ansible** , and **Automation Hub** instances are listed.


**Verify pod status (UI):**

1. Navigate toWorkloads→Pods.
1. Switch to the project (namespace) where you deployed the instance.
1. Verify that all related pods display a **Running** or **Completed** status.


**Verify Platform Route (CLI):**

Run the following command to confirm the URL for accessing the platform gateway:

```
oc get route
```

