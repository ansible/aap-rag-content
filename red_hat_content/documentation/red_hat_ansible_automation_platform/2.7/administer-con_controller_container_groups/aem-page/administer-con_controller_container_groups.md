+++
template = "docs/aem-title.html"
title = "Control where automation runs with container groups - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-con_controller_container_groups"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-define_where_automation_runs_with_host_and_node_groupings/", "Define where automation runs with host and node groupings"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-con_controller_container_groups/aem-page/administer-con_controller_container_groups.html"
last_crumb = "Control where automation runs with container groups"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Control where automation runs with container groups"
oversized = "false"
page_slug = "administer-con_controller_container_groups"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/administer-con_controller_container_groups"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-con_controller_container_groups/toc/toc.json"
type = "aem-page"
+++

# Control where automation runs with container groups

Ansible Automation Platform supports container groups, which enable you to run jobs in automation controller regardless of whether automation controller is installed as a standalone, in a virtual environment, or in a container.

Container groups act as a pool of resources within a virtual environment.

You can create instance groups to point to an OpenShift container. These are job environments that are provisioned on-demand as a pod that exists only for the duration of the playbook run. This is known as the ephemeral execution model and ensures a clean environment for every job run.

In some cases, you might want to set container groups to be "always-on", which you can configure through the creation of an instance.

 Note:

Container groups upgraded from versions before automation controller 4.0 revert back to default and remove the old pod definition, clearing out all custom pod definitions in the migration.

Container groups are different from execution environments in that execution environments are container images and do not use a virtual environment. For more information, see*Define, create, and build execution environments* in the Related Links section.

## Create a container group

You can create a `ContainerGroup` in automation controller to run jobs in containers on an OpenShift or Kubernetes cluster.

### Before you begin

- A namespace that you can launch into. Every cluster has a "default" namespace, but you can use a specific namespace.
- A service account that has the roles that enable it to launch and manage pods in this namespace. For more information, see [Creating a service account in OpenShift Container Platform or Kubernetes](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-con_controller_container_groups#controller-create-service-account "Use service accounts in an OpenShift cluster or Kubernetes to run jobs in a container group through automation controller. After the service account is created, its credentials are provided to automation controller in the form of an OpenShift or Kubernetes API Bearer Token credential.").
- If you are using execution environments in a private registry, and have a container registry credential associated with them in automation controller, the service account also needs the roles to get, create, and delete secrets in the namespace. If you do not want to give these roles to the service account, you can pre-create the `ImagePullSecrets` and specify them on the pod spec for the `ContainerGroup`. In this case, the execution environment must not have a container registry credential associated, or automation controller attempts to create the secret for you in the namespace.
- A token associated with that service account. An OpenShift or Kubernetes Bearer Token.
- A CA certificate associated with the cluster.

### About this task

A `ContainerGroup` is a type of `InstanceGroup` that has an associated credential you can use to connect to an OpenShift cluster.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Instance Groups.
2.  Click Create group and select **Create container group**.
3.  Enter a name for your new container group and select the credential you created before to associate it to the container group.
4.  Click Create container group.
5.  Check the **Customize pod spec** box and edit the **Pod spec override** to include the namespace and service account name that you used in the previous steps.

## Create a service account in OpenShift Container Platform or Kubernetes

Use service accounts in an OpenShift cluster or Kubernetes to run jobs in a container group through automation controller. After the service account is created, its credentials are provided to automation controller in the form of an OpenShift or Kubernetes API Bearer Token credential.

### Procedure

1.  To create a service account, download and use the following sample service account example, `containergroup sa` and change it as required to obtain the credentials:
  

```
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: containergroup-service-account
  namespace: containergroup-namespace
---
kind: Role
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: role-containergroup-service-account
  namespace: containergroup-namespace
rules:
  - verbs:
      - get
      - list
      - watch
      - create
      - update
      - patch
      - delete
    apiGroups:
      - ''
    resources:
      - pods
  - verbs:
      - get
    apiGroups:
      - ''
    resources:
      - pods/log
  - verbs:
      - create
    apiGroups:
      - ''
    resources:
      - pods/attach
  - verbs:
      - get
      - create
      - delete
    apiGroups:
      - ''
    resources:
      - secrets
---
kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: role-containergroup-service-account-binding
  namespace: containergroup-namespace
subjects:
- kind: ServiceAccount
  name: containergroup-service-account
  namespace: containergroup-namespace
roleRef:
  kind: Role
  name: role-containergroup-service-account
  apiGroup: rbac.authorization.k8s.io
```

2.  Apply the configuration from `containergroup-sa.yml`:
  

```
oc apply -f containergroup-sa.yml
```

3.  Get an API token by generating a service account token:
  

```
oc create token containergroup-service-account --duration=$((365*24))h > containergroup-sa.token
```

4.  Get the CA certificate:
  

```
oc get secret -n openshift-ingress wildcard-tls -o jsonpath='{.data.ca\.crt}' | base64 -d > containergroup-ca.crt
```

5.  Use the contents of `containergroup-sa.token` and `containergroup-ca.crt` to provide the information for the [OpenShift or Kubernetes API Bearer Token](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-con_controller_container_groups#controller-create-service-account "Use service accounts in an OpenShift cluster or Kubernetes to run jobs in a container group through automation controller. After the service account is created, its credentials are provided to automation controller in the form of an OpenShift or Kubernetes API Bearer Token credential.") required for the container group.   1.  To create a container group, create a [OpenShift or Kubernetes API Bearer Token](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-con_controller_container_groups#controller-create-service-account "Use service accounts in an OpenShift cluster or Kubernetes to run jobs in a container group through automation controller. After the service account is created, its credentials are provided to automation controller in the form of an OpenShift or Kubernetes API Bearer Token credential.") credential to use with your container group.

## Customize the pod specification

Ansible Automation Platform provides a simple default pod specification, however, you can provide a custom YAML or JSON document that overrides the default pod specification.

### About this task

This field uses any custom fields such as `ImagePullSecrets`, that can be "serialized" as valid pod JSON or YAML. A full list of options can be found in the [Pods and Services](https://docs.openshift.com/online/pro/architecture/core_concepts/pods_and_services.html) section of the OpenShift documentation.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Instance Groups.
2.  Click Create group and select **Create container group**.
3.  Check the option for **Customize pod spec**.
4.  Enter a custom Kubernetes or OpenShift Pod specification in the **Pod spec override** field.  
![Customize pod specification](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ag-instance-group-customize-cg-pod.png)  
5.  Click Create container group.  Note:
      The image when a job launches is determined by which execution environment is associated with the job. If you associate a container registry credential with the execution environment, then automation controller attempts to make an `ImagePullSecret` to pull the image. If you prefer not to give the service account permission to manage secrets, you must pre-create the `ImagePullSecret` and specify it on the pod specification, and omit any credential from the execution environment used.

    For more information, see the [Allowing Pods to Reference Images from Other Secured Registries](https://access.redhat.com/RegistryAuthentication#allowing-pods-to-reference-images-from-other-secured-registries-8) section of the *Red Hat Container Registry Authentication* article.

6.  When you have created the container group successfully, the **Details** tab of the newly created container group remains, which enables you to review and edit your container group information. This is the same menu that is opened if you click the ![Edit](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/leftpencil.png) icon from the **Instance Groups** list view. You can also edit **Instances** and review **Jobs** associated with this instance group.


![Instance group successfully created](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ag-instance-group-successfully-created.png)  
    Container groups and instance groups are labeled accordingly.

## Verify the container group functions

Verify the deployment and termination of your container.

### Procedure

1.  Create a mock inventory and associate the container group to it by populating the name of the container group in the **Instance groups** field. For more information, see [Add a new inventory](/documentation/en-us/red_hat_ansible_automation_platform/2.7/proc_controller_adding_new_inventory "To add a new inventory, you must configure permissions, groups, hosts, and sources, then view the completed jobs.").  
![Create test inventory](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ag-inventories-create-new-test-inventory.png)  
2.  Create the `localhost` host in the inventory with the following variables:
  

```
{'ansible_host': '127.0.0.1', 'ansible_connection': 'local'}
```

3.  Launch an ad hoc job against the localhost using the *ping* or *setup* module. Even though the **Machine Credential** field is required, it does not matter which one is selected for this test:  
![Launch ad hoc localhost](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ag-inventories-launch-adhoc-localhost.png)  

![Launch ad hoc localhost 2](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ag-inventories-launch-adhoc-localhost2.png)  

### Results

You can see in the **Jobs** details view that the container was reached successfully by using one of the ad hoc jobs.

If you have an OpenShift UI, you can see pods appear and disappear as they deploy and end. You can also use the CLI to perform a `get pod` operation on your namespace to watch these same events occurring in real-time.

## Container capacity limits

When using container groups in automation controller, you can set capacity limits for the containers that run the jobs.

Capacity limits and quotas for containers are defined by objects in the Kubernetes API:

- To set limits on all pods within a given namespace, use the `LimitRange` object. For more information see the [Quotas and Limit Ranges](https://docs.openshift.com/online/pro/dev_guide/compute_resources.html#overview) section of the OpenShift documentation.
- To set limits directly on the pod definition launched by automation controller, see [Customizing the pod specification](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-con_controller_container_groups#controller-customize-pod-spec "Ansible Automation Platform provides a simple default pod specification, however, you can provide a custom YAML or JSON document that overrides the default pod specification.") and the [Compute Resources](https://docs.openshift.com/online/pro/dev_guide/compute_resources.html#dev-compute-resources) section of the OpenShift documentation.


 Note:

Container groups do not use the capacity algorithm that normal nodes use. You need to set the number of forks at the job template level. If you configure forks in automation controller, that setting is passed along to the container.
