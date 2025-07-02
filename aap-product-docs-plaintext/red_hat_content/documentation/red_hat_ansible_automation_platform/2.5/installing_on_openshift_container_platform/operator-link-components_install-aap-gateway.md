# 2. Configuring the Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform
## 2.1. Linking your components to the platform gateway




After installing the Ansible Automation Platform Operator in your namespace you can set up your **Ansible Automation Platform** instance. Then link all the platform components to a single user interface.

**Procedure**

1. Log in to Red Hat OpenShift Container Platform.
1. Navigate toOperators→Installed Operators.
1. Select your Ansible Automation Platform Operator deployment.
1. Select the **Details** tab.
1. On the **Ansible Automation Platform** tile clickCreate instance.
1. From the **Create Ansible Automation Platform** page enter a name for your instance in the **Name** field.
1. ClickYAML viewand paste the following:


```
spec:      database:        resource_requirements:          requests:            cpu: 200m            memory: 512Mi        storage_requirements:          requests:            storage: 100Gi          controller:        disabled: false          eda:        disabled: false          hub:        disabled: false        storage_type: file        file_storage_storage_class: &lt;read-write-many-storage-class&gt;        file_storage_size: 10Gi
```


1. ClickCreate.


**Verification**

Go to your Ansible Automation Platform Operator deployment and clickAll instancesto verify if all instances deployed correctly. You should see the **Ansible Automation Platform** instance and the deployed **AutomationController** , **EDA** , and **AutomationHub** instances here.


Alternatively you can check by the command line, run: `oc get route`

