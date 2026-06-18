+++
title = "Run jobs on execution nodes - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_run_jobs_on_execution_nodes"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_automation_mesh_operator_aap/", "Scale with automation mesh in an operator environment"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-proc_run_jobs_on_execution_nodes/aem-page/administer-proc_run_jobs_on_execution_nodes.html"
last_crumb = "Run jobs on execution nodes"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Run jobs on execution nodes"
oversized = "false"
page_slug = "administer-proc_run_jobs_on_execution_nodes"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/administer-proc_run_jobs_on_execution_nodes"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-proc_run_jobs_on_execution_nodes/toc/toc.json"
type = "aem-page"
+++

# Run jobs on execution nodes

You must specify where jobs run from, or they default to running in the control cluster. To do this, set up a Job Template. For more information about Job Templates, see [Standardize and streamline automation with automation job templates](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_ug_controller_job_templates "You can create both Job templates and Workflow job templates from Automation Execution > Templates .").

## Procedure

1.  The **Templates** list view shows job templates that are currently available. From this screen you can launch ![Launch](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/rightrocket.png), edit ![Edoit](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/leftpencil.png), and duplicate ![Duplicate](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/copy.png) a workflow job template.
2.  Select the job you want and click the ![Launch](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/rightrocket.png) icon.
3.  Select the **Instance Group** on which you want to run the job. Note that a System Administrator must grant you or your team permissions to be able to use an instance group in a job template. If you select multiple jobs templates, the order in which you select them sets the execution precedence.
4.  Click Next.
5.  Click Launch.

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

## Create a pull secret to run the default execution environment on remote nodes

If you are using the default execution environment provided with automation controller to run on remote execution nodes, you must add a pull secret in automation controller that has the credential for pulling the execution environment image.

### About this task

 Note:

This does not apply to Ansible Automation Platform on Microsoft Azure.

Create a pull secret on the automation controller namespace and configure the `ee_pull_credentials_secret` parameter in the Operator as follows:

### Procedure

1.  Create a secret using the following command:
  

```
oc create secret generic ee-pull-secret \
     --from-literal=username=<username> \
     --from-literal=password=<password> \
     --from-literal=url=registry.redhat.io
```

2.  Add `ee_pull_credentials_secret` and `ee-pull-secret` to the specification by editing the deployment specification:
  

```
oc edit automationcontrollers aap-controller-o yaml
```
    and add the following:

```
spec
  ee_pull_credentials_secret=ee-pull-secret
```

3.  To manage instances from the automation controller UI, you must have System Administrator or System Auditor permissions.

## Use custom signed certificates in managed cloud and operator environments

Execution nodes verify incoming connections by ensuring the x509 certificate was issued by a trusted Certificate Authority (CA). You might want to provide your own CA for this validation. If no CA is provided. Controller Operator generates a self-signed CA during installation.

### About this task

The control nodes on the Kubernetes cluster communicate with execution nodes through mutual TLS/TCP connections, running using receptor. Controller Operator generates a self-signed CA during installation by using OpenSSL.

### Procedure

1.  If custom `ca.crt` and `ca.key` are stored locally, run the following:
       `kubectl create secret tls controller-demo-12345-receptor-ca \ --cert=/path/to/ca.crt --key=/path/to/ca.key`

    The secret should be named `<Controller Custom Resource name>-receptor-ca`. In this example the Controller CR name is `controller-demo-12345`.

    Replace `controller-demo-12345` with your Controller Custom Resource name.

2.  If this secret is created after automation controller is deployed, run the following to restart the deployment:
       `kubectl rollout restart deployment controller-demo-12345`

   Warning:
      Changing the receptor CA breaks connections to any existing execution nodes. These nodes enter an unavailable state, and jobs cannot run on them. You must download and re-run the install bundle for each execution node. This replaces the TLS certificate files with those signed by the new CA. The execution nodes then appear in a ready state after a few minutes.

## Remove instances

From the **Instances** page, you can add, remove or run health checks on your nodes.

 Note:

You must follow the procedures for installing RHEL packages for any additional nodes you create. If you peer this additional node to an existing hop node, you must also install the Install Bundle on each node.

Use the check boxes next to an instance to select it to remove it, or run a health check against it.

 Note:

- If a node is removed using the UI, then the node is "removed" and does not show a status. If you delete the VM of the node before it is removed in the UI, it will show an error.
- You only need to reinstall the Install Bundle if the topology changes the communication pattern, that is, hop nodes change or you add nodes.

When a button is disabled, you do not have permission for that particular action. Contact your Administrator to grant you the required level of access.

If you are able to remove an instance, you receive a prompt for confirmation.

 Note:

You can still remove an instance even if it is active and jobs are running on it. Automation controller waits for jobs running on this node to complete before removing it.

## Upgrade receptors

A software update addresses any issues or bugs to provide a better experience of working with the technology. Anyone with administrative rights can update the receptor on an execution node.

### About this task

Red Hat recommends performing updates to the receptor after any Ansible Automation Platform control plane updates. This ensures you are using the latest version. The best practice is to perform regular updates outside of any updates to the control plane.

### Procedure

1.  Check the current receptor version:
  

```
receptor --version
```

2.  Update the receptor:
  

```
sudo dnf update ansible-runner receptor -y
```
   Note:
      To upgrade all packages (not just the receptor), use `dnf update`, then reboot with `reboot`.

3.  Verify the installation. After the update is complete, check the receptor version again to verify the update:
  

```
receptor --version
```

4.  Restart the receptor service:
  

```
sudo systemctl restart receptor
```

5.  Ensure the receptor is working correctly and is properly connected to the controller or other nodes in the system.
