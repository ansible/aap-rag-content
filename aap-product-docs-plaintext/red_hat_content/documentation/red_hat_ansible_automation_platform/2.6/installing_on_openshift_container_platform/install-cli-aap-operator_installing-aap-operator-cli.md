# 1. Installing Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform
## 1.3. Installing Red Hat Ansible Automation Platform Operator from the Red Hat OpenShift Container Platform CLI
### 1.3.1. Installing the Ansible Automation Platform Operator in a namespace




Use this procedure to subscribe a namespace to an operator.

Important
You cannot deploy Ansible Automation Platform in the default namespace on your OpenShift Cluster. The 'ansible-automation-platform' namespace is recommended. You can use a custom namespace, but it should run only Ansible Automation Platform.



**Prerequisites**

- Access to Red Hat OpenShift Container Platform using an account with operator installation permissions.
- The OpenShift Container Platform CLI `    oc` command is installed on your local system. Refer to [Installing the OpenShift CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.15/html/cli_tools/openshift-cli-oc#installing-openshift-cli) in the Red Hat OpenShift Container Platform product documentation for further information.


**Procedure**

1. Create a project for the operator.


```
oc new-project ansible-automation-platform
```


1. Create a file called `    sub.yaml` .
1. Add the following YAML code to the `    sub.yaml` file.


```
---    apiVersion: operators.coreos.com/v1    kind: OperatorGroup    metadata:      name: ansible-automation-platform-operator      namespace: ansible-automation-platform    spec:      targetNamespaces:        - ansible-automation-platform    ---    apiVersion: operators.coreos.com/v1alpha1    kind: Subscription    metadata:      name: ansible-automation-platform      namespace: ansible-automation-platform    spec:      channel: 'stable-2.6'      installPlanApproval: Automatic      name: ansible-automation-platform-operator      source: redhat-operators      sourceNamespace: openshift-marketplace    ---
```

This file creates a `    Subscription` object called `    <span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">ansible-automation-platform</span></em></span>` that subscribes the `    ansible-automation-platform` namespace to the `    ansible-automation-platform-operator` operator.


1. Run the `    <span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">oc apply</span></strong></span>` command to create the objects specified in the `    sub.yaml` file:


```
oc apply -f sub.yaml
```


1. Verify the CSV PHASE reports "Succeeded" before proceeding using the `    oc get csv -n ansible-automation-platform` command:


```
oc get csv -n ansible-automation-platform        NAME                               DISPLAY                       VERSION              REPLACES                           PHASE    aap-operator.v2.6.0-0.1728520175   Ansible Automation Platform   2.6.0+0.1728520175   aap-operator.v2.6.0-0.1727875185   Succeeded
```


1. Create an `    AnsibleAutomationPlatform` object called `    <span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">example</span></em></span>` in the `    ansible-automation-platform` namespace.

To change the Ansible Automation Platform and its components from `    <span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">example</span></em></span>` , edit the _name_ field in the `    metadata:` section and replace example with the name you want to use:


```
oc apply -f - &lt;&lt;EOF    apiVersion: aap.ansible.com/v1alpha1    kind: AnsibleAutomationPlatform    metadata:      name: example      namespace: ansible-automation-platform    spec:      # Platform      image_pull_policy: IfNotPresent      # Components      controller:        disabled: false      eda:        disabled: false      hub:        disabled: false        ## Modify to contain your RWM storage class name        storage_type: file        file_storage_storage_class: &lt;your-read-write-many-storage-class&gt;        file_storage_size: 10Gi            ## uncomment if using S3 storage for Content pod        # storage_type: S3        # object_storage_s3_secret: example-galaxy-object-storage            ## uncomment if using Azure storage for Content pod        # storage_type: azure        # object_storage_azure_secret: azure-secret-name      lightspeed:        disabled: true    EOF
```




**Additional resources**

-  [Installing from OperatorHub using the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.15/html/operators/user-tasks#olm-installing-operator-from-operatorhub-using-cli_olm-installing-operators-in-namespace)


