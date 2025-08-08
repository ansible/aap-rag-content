# 1. Installing Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform
## 1.3. Installing the Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform
### 1.3.1. Prerequisites




- You have installed the Red Hat Ansible Automation Platform catalog in OperatorHub.
- You have created a `    StorageClass` object for your platform and a persistent volume claim (PVC) with `    ReadWriteMany` access mode. See [Dynamic provisioning](https://docs.openshift.com/container-platform/4.15/storage/dynamic-provisioning.html) for details.
- To run Red Hat OpenShift Container Platform clusters on Amazon Web Services (AWS) with `    ReadWriteMany` access mode, you must add NFS or other storage.


- For information about the AWS Elastic Block Store (EBS) or to use the `        aws-ebs` storage class, see [Persistent storage using AWS Elastic Block Store](https://docs.redhat.com/en/documentation/openshift_container_platform/4.10/html-single/storage/index#persistent-storage-aws) .
- To use multi-attach `        ReadWriteMany` access mode for AWS EBS, see [Attaching a volume to multiple instances with Amazon EBS Multi-Attach](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volumes-multi.html) .




<span id="proc-install-aap-operator_install-aap-operator"></span>
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


