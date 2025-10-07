# 1. Installing Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform
## 1.3. Deploying the Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform
### 1.3.1. Installing the Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform




When installing your Ansible Automation Platform Operator you have a choice of a namespace-scoped operator or a cluster-scoped operator. This depends on the update channel you choose, stable-2.x or cluster-scoped-2.x.

A namespace-scoped operator is confined to one namespace, offering tighter security. A cluster-scoped operator spans multiple namespaces, which grants broader permissions.

If you are managing multiple Ansible Automation Platform instances with the same Ansible Automation Platform Operator version, use the cluster-scoped operator, which uses a single operator to manage all Ansible Automation Platform custom resources in your cluster.

If you need multiple operator versions in the same cluster, you must use the namespace-scoped operator. The operator and the deployment share the same namespace. This can also be helpful when debugging because the operator logs pertain to custom resources in that namespace only.

Note
For information about the Ansible Automation Platform Operator system requirements and infrastructure topology see [Operator topologies](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/tested_deployment_models/ocp-topologies) in _Tested deployment models_ .



For help with installing a namespace or cluster-scoped operator see the following procedure.

Important
You cannot deploy Ansible Automation Platform in the default namespace on your OpenShift Cluster. The `aap` namespace is recommended. You can use a custom namespace, but it should run only Ansible Automation Platform.



**Prerequisites**

- You have installed the Red Hat Ansible Automation Platform catalog in OperatorHub.
- You have created a `    StorageClass` object for your platform and a persistent volume claim (PVC) with `    ReadWriteMany` access mode. See [Dynamic provisioning](https://docs.openshift.com/container-platform/4.15/storage/dynamic-provisioning.html) for details.
- To run Red Hat OpenShift Container Platform clusters on Amazon Web Services (AWS) with `    ReadWriteMany` access mode, you must add NFS or other storage.


- For information about the AWS Elastic Block Store (EBS) or to use the `        aws-ebs` storage class, see [Persistent storage using AWS Elastic Block Store](https://docs.redhat.com/en/documentation/openshift_container_platform/4.10/html-single/storage/index#persistent-storage-aws) .
- To use multi-attach `        ReadWriteMany` access mode for AWS EBS, see [Attaching a volume to multiple instances with Amazon EBS Multi-Attach](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volumes-multi.html) .



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


| Automation controller | Automation hub | Event-Driven Ansible (EDA) | Red Hat Ansible Lightspeed |
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


