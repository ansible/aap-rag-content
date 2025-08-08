# 1. Installing Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform
## 1.3. Installing the Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform




Note
For information about the Ansible Automation Platform Operator system requirements and infrastructure topology see [Operator topologies](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/tested_deployment_models/ocp-topologies) in _Tested deployment models_ .



When installing your Ansible Automation Platform Operator you have a choice of a namespace-scoped operator or a cluster-scoped operator. This depends on the update channel you choose, stable-2.x or cluster-scoped-2.x.

A namespace-scoped operator is confined to one namespace, offering tighter security. A cluster-scoped operator spans multiple namespaces, which grants broader permissions.

If you are managing multiple Ansible Automation Platform instances with the same Ansible Automation Platform Operator version, use the cluster-scoped operator, which uses a single operator to manage all Ansible Automation Platform custom resources in your cluster.

If you need multiple operator versions in the same cluster, you must use the namespace-scoped operator. The operator and the deployment share the same namespace. This can also be helpful when debugging because the operator logs pertain to custom resources in that namespace only.

For help with installing a namespace or cluster-scoped operator see the following procedure.

Important
You cannot deploy Ansible Automation Platform in the default namespace on your OpenShift Cluster. The `aap` namespace is recommended. You can use a custom namespace, but it should run only Ansible Automation Platform.



