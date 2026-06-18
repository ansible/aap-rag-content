+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_install_aap_operator"
title = "Install the Ansible Automation Platform Operator through OperatorHub - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_operator_install_operator/", "Install on OpenShift Container Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-assembly_install_aap_operator/aem-page/install-assembly_install_aap_operator.html"
last_crumb = "Install the Ansible Automation Platform Operator through OperatorHub"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Install the Ansible Automation Platform Operator through OperatorHub"
oversized = "false"
page_slug = "install-assembly_install_aap_operator"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-assembly_install_aap_operator"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-assembly_install_aap_operator/toc/toc.json"
type = "aem-page"
+++

# Install the Ansible Automation Platform Operator through OperatorHub

Use this procedure to guide you through deploying the Red Hat Ansible Automation Platform Operator through the **Operators** section on Red Hat OpenShift Container Platform, selecting the appropriate update channel and installation mode, and then verifying the successful deployment.

## Install the Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform

When installing your Ansible Automation Platform Operator you have a choice of a namespace-scoped operator or a cluster-scoped operator. This depends on the update channel you choose, stable-2.x or cluster-scoped-2.x.

### Before you begin

- You have installed the Red Hat Ansible Automation Platform catalog in OperatorHub.
- You have created a `StorageClass` object for your platform and a persistent volume claim (PVC) with `ReadWriteMany` access mode. See [Dynamic provisioning](https://docs.redhat.com/en/documentation/openshift_container_platform/4.15/html/storage/dynamic-provisioning) for details. See [Configure static storage for Ansible Automation Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.7/configure-configure_static_storage_for_ansible_automation_platform#GUID-e1c1cc2f-de6d-4bc1-a089-3572ae26c444 "Configure static storage when your environment does not support dynamic volume provisioning. This process ensures the Ansible Automation Platform Operator adopts manually created Persistent Volume Claims by using specific naming conventions.") for manual setup.
- To run Red Hat OpenShift Container Platform clusters on Amazon Web Services (AWS) with `ReadWriteMany` access mode, you must add NFS or other storage.   * For information about the AWS Elastic Block Store (EBS) or to use the `aws-ebs` storage class, see [Persistent storage using AWS Elastic Block Store](https://docs.redhat.com/en/documentation/openshift_container_platform/4.10/html-single/storage/index#persistent-storage-aws).
  * To use multi-attach `ReadWriteMany` access mode for AWS EBS, see [Attaching a volume to multiple instances with Amazon EBS Multi-Attach](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volumes-multi.html).

### About this task

A namespace-scoped operator is confined to one namespace, offering tighter security. A cluster-scoped operator spans multiple namespaces, which grants broader permissions.

If you are managing multiple Ansible Automation Platform instances with the same Ansible Automation Platform Operator version, use the cluster-scoped operator, which uses a single operator to manage all Ansible Automation Platform custom resources in your cluster.

If you need multiple operator versions in the same cluster, you must use the namespace-scoped operator. The operator and the deployment share the same namespace. This can also be helpful when debugging because the operator logs pertain to custom resources in that namespace only.

Note:

For information about the Ansible Automation Platform Operator system requirements and infrastructure topology see [Operator topologies](/documentation/en-us/red_hat_ansible_automation_platform/2.7/plan-ref_ocp_a_env_a "The Operator-based growth topology provides a smaller footprint deployment without redundancy for organizations getting started with Ansible Automation Platform on Red Hat OpenShift Container Platform.") in *Tested deployment models*.

For help with installing a namespace or cluster-scoped operator see the following procedure.

Important:

You cannot deploy Ansible Automation Platform in the default namespace on your OpenShift Cluster. The `aap` namespace is recommended. You can use a custom namespace, but it should run only Ansible Automation Platform.

### Procedure

1.  Log in to Red Hat OpenShift Container Platform.
2.  Navigate to Operators> (and then)OperatorHub.
3.  Search for Ansible Automation Platform and click Install.
4.  Select an **Update Channel**:

  - **stable-2.x**: installs a namespace-scoped operator, which limits deployments of automation hub and automation controller instances to the namespace the operator is installed in, this is suitable for most cases. The stable-2.x channel does not require administrator privileges and utilizes fewer resources because it only monitors a single namespace.
  - **stable-2.x-cluster-scoped**: installs the Ansible Automation Platform Operator in a single namespace that manages Ansible Automation Platform custom resources and deployments in all namespaces. The Ansible Automation Platform Operator requires administrator privileges for all namespaces in the cluster.

5.  Select **Installation Mode**, **Installed Namespace**, and **Approval Strategy**.
6.  Click Install.

### Results

The installation process begins. When installation finishes, a modal appears notifying you that the Ansible Automation Platform Operator is installed in the specified namespace.

- Click View Operator to view your newly installed Ansible Automation Platform Operator and verify the following operator custom resources are present:

| Automation controller                                                                                            | Automation hub                                            | Event-Driven Ansible (EDA) | Red Hat Ansible Lightspeed |
| ---------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- | -------------------------- | -------------------------- |
| Automation ControllerAutomation Controller BackupAutomation Controller RestoreAutomation Controller Mesh Ingress | Automation HubAutomation Hub BackupAutomation Hub Restore | EDAEDA BackupEDA Restore   | Ansible Lightspeed         |


- Verify that the Ansible Automation Platform operator displays a **Succeeded** status.
