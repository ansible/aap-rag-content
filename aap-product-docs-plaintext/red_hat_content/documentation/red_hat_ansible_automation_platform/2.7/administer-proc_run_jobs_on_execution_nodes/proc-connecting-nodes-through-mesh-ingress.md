# Run jobs on execution nodes
## Set up mesh ingress for environments that forbid inbound connections

If your network restricts inbound connections, using a hop node peered to the control plane can cause issues, as it requires a defined 'listener_port'. Instead, you can use *mesh ingress* as an alternative method for setting up your automation mesh.

### Before you begin

- Create node instances within the remote networks for execution nodes in the automation mesh.


Use the following procedure to set up mesh nodes.

### About this task

When you instantiate mesh ingress you set up a pod, or receptor hop node inside the kubernetes control cluster, registered to the database through the operator. It also creates a service, and a route URL that is used by the control plane to connect to the hop node, and automation controller.


![mesh ingress architecture](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/meshIngress.png)

### Procedure

1.  Create a YAML file (in this case named `oc_meshingress.yml`) to set up the mesh ingress node. Your file should resemble the following:

```
apiVersion: automationcontroller.ansible.com/v1alpha1
kind: AutomationControllerMeshIngress
metadata:
name:
namespace:
spec:
deployment_name: aap-controller
```
Where:

- **apiVersion**: defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and might reject unrecognized values. This value is static.

- **kind**: Is the type of node to create. Use the value `AutomationControllerMeshIngress`.

`AutomationControllerMeshIngress` controls the deployment and configuration of mesh ingress on automation controller.

- **name**: enter a name for the mesh ingress node.

- **namespace**: enter a name for the Kubernetes namespace to deploy the mesh ingress into. This must be in the same namespace as the automation controller that the mesh is connected to.

- **deployment_name**: is the automation controller instance that this mesh ingress is attached to. Provide the name of your automation controller instance.

2.  Apply this YAML file using:


```
oc apply -f oc_meshingress.yml
```
Run this playbook to creates the `AutomationControllerMeshIngress` resource. The operator creates a hop node in automation controller with the `name` you supplied.

3.  When the MeshIngress instance has been created, it appears in the Instances page.  Important:
Any instance that is to function as a remote execution node in "pull" mode need to be created after this procedure and must be configured as follows:

```
instance type: Execution
listener port: keep empty
options:
Enable instance: checked
Managed by Policy: as needed
Peers from control nodes: unchecked (this one is important)
```

4.  Associate this new instance with the hop node you created using the procedure in this paragraph
5.  Download the tarball.  Note:
Association with the hop node must be done before creating the tarball.

