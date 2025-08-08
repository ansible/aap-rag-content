# 4. Deploying the Ansible Lightspeed intelligent assistant on OpenShift Container Platform
## 4.5. Deploying the Ansible Lightspeed intelligent assistant
### 4.5.1. Installing and configuring the Ansible Automation Platform operator




Install and configure the Ansible Automation Platform operator on the OpenShift Container Platform, so that you can deploy and use the Ansible Lightspeed intelligent assistant.

#### 4.5.1.1. Installing the Ansible Automation Platform operator




Install the Ansible Automation Platform operator on OpenShift Container Platform.


<span id="proc-install-aap-operator_deploying-chatbot-operator"></span>
**Procedure**

1. Log in to Red Hat OpenShift Container Platform.
1. Navigate toOperators→OperatorHub.
1. Search for Ansible Automation Platform and clickInstall.
1. Select an **Update Channel** :


-  **stable-2.x** : installs a namespace-scoped operator, which limits deployments of automation hub and automation controller instances to the namespace the operator is installed in, this is suitable for most cases. The stable-2.x channel does not require administrator privileges and utilizes fewer resources because it only monitors a single namespace.
-  **stable-2.x-cluster-scoped** : installs the Ansible Automation Platform Operator in a single namespace that manages Ansible Automation Platform custom resources and deployments in all namespaces. The Ansible Automation Platform Operator requires administrator privileges for all namespaces in the cluster.

1. Select **Installation Mode** , **Installed Namespace** , and **Approval Strategy** .
1. ClickInstall.



**Verification**

The installation process begins. When installation finishes, a modal appears notifying you that the Ansible Automation Platform Operator is installed in the specified namespace.


- ClickView Operatorto view your newly installed Ansible Automation Platform Operator and verify the following operator custom resources are present:


| {ControllerNameStart} | {HubNameStart} | {EDAName} (EDA) | {LightspeedShortName} |
| --- | --- | --- | --- |
| - Automation Controller
- Automation Controller Backup
- Automation Controller Restore
- Automation Controller Mesh Ingress | - Automation Hub
- Automation Hub Backup
- Automation Hub Restore | - EDA
- EDA Backup
- EDA Restore | - Ansible Lightspeed |


- Verify that the Ansible Automation Platform operator displays a **Succeeded** status.


#### 4.5.1.2. Configuring the Ansible Automation Platform operator




After installing the Ansible Automation Platform Operator in your namespace, configure the Ansible Automation Platform operator to link your components to the platform gateway.

##### 4.5.1.2.1. Linking your components to the platform gateway




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

You must also verify that all the pods are running successfully. Perform the following steps:

1. Navigate toWorkloads→Pods.
1. Switch to the project named as described in the namespace metadata in the **YAML** configuration view.
1. Verify that all pods display either a **Running** or **Completed** status, with no pods displaying an error status.


