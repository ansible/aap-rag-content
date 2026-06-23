# Control where automation runs with container groups
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

