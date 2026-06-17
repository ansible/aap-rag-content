# Install Ansible Automation Platform Operator from the CLI

Use these instructions to install the Ansible Automation Platform Operator on Red Hat OpenShift Container Platform from the OpenShift Container Platform command-line interface (CLI) using the `oc` command.

## Install the Ansible Automation Platform Operator in a namespace

Use this procedure to subscribe a namespace to an operator.

### Before you begin

- Access to Red Hat OpenShift Container Platform using an account with operator installation permissions.
- The OpenShift Container Platform CLI `oc` command is installed on your local system. Refer to [Installing the OpenShift CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.15/html/cli_tools/openshift-cli-oc#installing-openshift-cli) in the Red Hat OpenShift Container Platform product documentation for further information.

### About this task

Important:

You cannot deploy Ansible Automation Platform in the default namespace on your OpenShift Cluster. The 'ansible-automation-platform' namespace is recommended. You can use a custom namespace, but it should run only Ansible Automation Platform.

### Procedure

1.  Create a project for the operator.

```
oc new-project ansible-automation-platform
```

2.  Create a file called sub.yaml.
3.  Add the following YAML code to the sub.yaml file.

```
---
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
name: ansible-automation-platform-operator
namespace: ansible-automation-platform
spec:
targetNamespaces:
- ansible-automation-platform
---
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
name: ansible-automation-platform
namespace: ansible-automation-platform
spec:
channel: 'stable-2.6'
installPlanApproval: Automatic
name: ansible-automation-platform-operator
source: redhat-operators
sourceNamespace: openshift-marketplace
---
```
This file creates a `Subscription` object called `ansible-automation-platform` that subscribes the `ansible-automation-platform` namespace to the `ansible-automation-platform-operator` operator.

4.  Run the oc apply command to create the objects specified in the sub.yaml file:


```
oc apply -f sub.yaml
```

5.  Verify the CSV PHASE reports "Succeeded" before proceeding using the oc get csv -n ansible-automation-platform command:


```
oc get csv -n ansible-automation-platform

NAME                               DISPLAY                       VERSION              REPLACES                           PHASE
aap-operator.v2.6.0-0.1728520175   Ansible Automation Platform   2.6.0+0.1728520175   aap-operator.v2.6.0-0.1727875185   Succeeded
```

6.  Create an `AnsibleAutomationPlatform` object called `example` in the `ansible-automation-platform` namespace. To change the Ansible Automation Platform and its components from `example`, edit the *name* field in the `metadata:` section and replace example with the name you want to use:

```
oc apply -f - <<EOF
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
name: example
namespace: ansible-automation-platform
spec:
# Platform
image_pull_policy: IfNotPresent
# Components
controller:
disabled: false
eda:
disabled: false
hub:
disabled: false
## Modify to contain your RWM storage class name
storage_type: file
file_storage_storage_class: <your-read-write-many-storage-class>
file_storage_size: 10Gi

## uncomment if using S3 storage for Content pod
# storage_type: S3
# object_storage_s3_secret: example-galaxy-object-storage

## uncomment if using Azure storage for Content pod
# storage_type: azure
# object_storage_azure_secret: azure-secret-name
lightspeed:
disabled: true
EOF
```
