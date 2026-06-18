# Set up VMs for use in mesh

Prepare Red Hat Enterprise Linux virtual machines by setting up SSH access and enabling repositories. Deploying these VMs as nodes helps expand the execution capacity of your automation mesh.

## Procedure

1.  SSH into each of the RHEL instances and perform the following steps. Depending on your network access and controls, SSH proxies or other access models might be required. Use the following command:

```
ssh [username]@[host_ip_address]
```
For example, for an Ansible Automation Platform instance running on Amazon Web Services.

```
ssh ec2-user@10.0.0.6
```

2.  Create or copy an SSH key that can be used to connect from the hop node to the execution node in later steps. This can be a temporary key used just for the automation mesh configuration, or a long-lived key. The SSH user and key are used in later steps.
3.  Enable your RHEL subscription with `baseos` and `appstream` repositories. Ansible Automation Platform RPM repositories are only available through subscription-manager, not the *Red Hat Update Infrastructure* (RHUI). If you attempt to use any other Linux footprint, including RHEL with RHUI, this causes errors.

```
sudo subscription-manager register --auto-attach
```
If Simple Content Access is enabled for your account, use:

```
sudo subscription-manager register
```
For more information about Simple Content Access, see [Getting started with simple content access](https://docs.redhat.com/en/documentation/subscription_central/1-latest/html/getting_started_with_simple_content_access/index).

4.  Enable Ansible Automation Platform subscriptions and the proper Red Hat Ansible Automation Platform channel:
For RHEL 8

```
# subscription-manager repos --enable ansible-automation-platform-2.5-for-rhel-8-x86_64-rpms
```
For RHEL 9

```
# subscription-manager repos --enable ansible-automation-platform-2.5-for-rhel-9-x86_64-rpms
```
For ARM

```
# subscription-manager repos --enable ansible-automation-platform-2.5-for-rhel-aarch64-rpms
```

5.  Ensure the packages are up to date:


```
sudo dnf upgrade -y
```

6.  Install the ansible-core packages on the machine where the downloaded bundle is to run:


```
sudo dnf install -y ansible-core
```
Note:
Ansible core is required on the machine that runs the automation mesh configuration bundle playbooks. This document assumes that happens on the execution node. However, this step can be omitted if you run the playbook from a different machine. You cannot run directly from the control node, this is not currently supported, but future support expects that the control node has direct connectivity to the execution node.

## Add execution or hop nodes to scale your infrastructure

To expand job capacity, create a standalone **execution node** that can be added to run alongside a deployment of automation controller. These execution nodes are not part of the automation controller Kubernetes cluster.

### About this task

The control nodes run in the cluster connect and submit work to the execution nodes through Receptor.

These execution nodes are registered in automation controller as type `execution` instances, meaning they are only used to run jobs, not dispatch work or handle web requests as control nodes do.

Important:

When creating an execution node, make sure the system time zone on the execution node matches `settings.TIME_ZONE` (default is 'UTC') on automation controller. Fact caching relies on comparing modified times of artifact files, and these modified times are not time zone-aware. Therefore, it is critical that the timezones of the execution nodes match automation controller’s time zone setting.

**Hop nodes** can be added to sit between the control plane of automation controller and standalone execution nodes. These hop nodes are not part of the Kubernetes cluster and are registered in automation controller as an instance of type `hop`, meaning they only handle inbound and outbound traffic for otherwise unreachable nodes in different or more strict networks.

The following procedure demonstrates how to set the node type for the hosts.

Note:

By default, Red Hat Ansible Automation Platform Service on AWS includes two hop nodes that you can peer execution nodes to.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Instances.
2.  On the **Instances** list page, click Add instance. The **Add Instance** window opens.
![Create new Instance](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/instances_create_new.png)
An instance requires the following attributes:

- **Host name**: (required) Enter a fully qualified domain name (public DNS) or IP address for your instance. This field is equivalent to `hostname` for installer-based deployments.  Note:
If the instance uses private DNS that cannot be resolved from the control cluster, DNS lookup routing fails, and the generated SSL/TLS certificates is invalid. Use the IP address instead.

- Optional: **Description**: Enter a description for the instance.

- **Instance state**: This field is auto-populated, indicating that it is being installed, and cannot be modified.

- **Listener port**: This port is used for the receptor to listen on for incoming connections. You can set the port to one that is appropriate for your configuration. This field is equivalent to `listener_port` in the API. The default value is 27199, though you can set your own port value.

- **Instance type**: Only `execution` and `hop` nodes can be created. Operator based deployments do not support Control or Hybrid nodes. Options:

* **Enable instance**: Check this box to make it available for jobs to run on an execution node.
* Check the **Managed by policy** box to enable policy to dictate how the instance is assigned.
* **Peers from control nodes**:
+ If you are configuring a hop node:
- If the hop node needs to have requests pushed directly from automation controller, then check the **Peers from Control** box.
- If the hop node is peered to another hop node, then make sure **Peers from Control** is not checked.
+ If you are configuring an execution node:
- If the execution node needs to have requests pushed directly from automation controller, then check the **Peers from Control** box.
- If the execution node is peered to a hop node, then make sure that **Peers from Control** is not checked.

3.  Click Associate peers.
4.  To view a graphical representation of your updated topology, see [Topology view](/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-assembly_controller_topology_viewer#assembly-controller-topology-viewer "Use the Topology View to view node type, node health, and specific details about each node if you already have a mesh topology deployed.").  Note:
Complete the following steps from any computer that has SSH access to the newly created instance.

5.  Click the ![Download](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/download.png) icon next to **Download Bundle** to download the tar file that includes this new instance and the files necessary to install the created node into the automation mesh. The install bundle has TLS certificates and keys, a certificate authority, and a proper Receptor configuration file.

```
receptor-ca.crt
work-public-key.pem
receptor.key
install_receptor.yml
inventory.yml
group_vars/all.yml
requirements.yml
```

6.  Extract the downloaded `tar.gz` Install Bundle from the location where you downloaded it. To ensure that these files are in the correct location on the remote machine, the install bundle includes the `install_receptor.yml` playbook.
7.  Before running the `ansible-playbook` command, edit the following fields in the `inventory.yml` file:


```
all:
hosts:
remote-execution:
ansible_host: localhost # change to the mesh node host name
ansible_user: <username> # user provided
ansible_ssh_private_key_file: ~/.ssh/<id_rsa>
```
- Ensure `ansible_host` is set to the IP address or DNS of the node.
- Set `ansible_user` to the username running the installation.
- Set `ansible_ssh_private_key_file` to contain the filename of the private key used to connect to the instance.
- The content of the `inventory.yml` file serves as a template and has variables for roles that are applied during the installation and configuration of a receptor node in a mesh topology. You can change some of the other fields, or replace the file in its entirety for advanced scenarios. For more information, see [Role Variables](https://github.com/ansible/receptor-collection/blob/main/README.md).

8.  For a node that uses a private DNS, add the following line to `inventory.yml`:


```
ansible_ssh_common_args: <your ssh ProxyCommand setting>
```
This instructs the `install-receptor.yml` playbook to use the proxy command to connect through the local DNS node to the private node.

9.  When the attributes are configured, click Save. The **Details** page of the created instance opens.
10.  Save the file to continue.
11.  The system that is going to run the install bundle to setup the remote node and run `ansible-playbook` requires the `ansible.receptor` collection to be installed:


```
ansible-galaxy collection install ansible.receptor
```
or

```
ansible-galaxy install -r requirements.yml
```
- Installing the receptor collection dependency from the `requirements.yml` file consistently retrieves the receptor version specified there. Additionally, it retrieves any other collection dependencies that might be needed in the future.
- Install the receptor collection on all nodes where your playbook will run, otherwise an error occurs.

12.  If `receptor_listener_port` is defined, the machine also requires an available open port on which to establish inbound TCP connections, for example, 27199. Run the following command to open port 27199 for receptor communication (Make sure you have port 27199 open in your firewall):


```
sudo firewall-cmd --permanent --zone=public --add-port=27199/tcp
```

13.  Run the following playbook on the machine where you want to update your automation mesh:


```
ansible-playbook -i inventory.yml install_receptor.yml
```
Note:
OpenSSL is required for this playbook. You can install it by running the following command:

```
openssl -v
```
If it returns then a version OpenSSL is installed. Otherwise you need to install OpenSSL with:

```
sudo dnf install -y openssl
```
After this playbook runs, your automation mesh is configured.


![Instances list view](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/instances_list_view2.png)
Note:
It might be the case that some servers do not listen on the receptor port (the default is 27199)

Suppose you have a Control plane with nodes A, B, and C

The following is a peering set up for three controller nodes:

Controller node A → Controller node B

Controller node A → Controller node C

Controller node B → Controller node C

You can force the listener by setting

`receptor_listener=True`

However, a connection Controller B → A is likely to be rejected as that connection already exists.

This means that nothing connects to Controller A as Controller A is creating the connections to the other nodes, and the following command does not return anything on Controller A:

`[root@controller1 ~]# ss -ntlp | grep 27199 [root@controller1 ~]#`

The RPM installer creates a strongly connected peering between the control plane nodes with a least privileged approach and opens the TCP listener only on those nodes where it is required. All the receptor connections are bidirectional, so when the connection is created, the receptor can communicate in both directions.

To remove an instance from the mesh, see [Removing instances](/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-proc_run_jobs_on_execution_nodes#ref-removing-instances "From the Instances page, you can add, remove or run health checks on your nodes.").

## Create an instance group

You can create instance groups with Automation controller to organize and manage your instances.

### About this task

Use the following procedure to create a new instance group.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Instance Groups.
2.  Click Create group and select **Create instance group** from the list.
3.  Enter the appropriate details into the following fields:

- **Name**: Names must be unique and must not be named "controller".
- **Policy instance minimum**: Enter the minimum number of instances to automatically assign to this group when new instances come online.
- **Policy instance percentage**: Use the slider to select a minimum percentage of instances to automatically assign to this group when new instances come online.  Note:
Policy instance fields are not required to create a new instance group. If you do not specify values, then the **Policy instance minimum** and **Policy instance percentage** default to 0.

- **Max concurrent jobs**: Specify the maximum number of forks that can be run for any given job.
- **Max forks**: Specify the maximum number of concurrent jobs that can be run for any given job.  Note:
The default value of 0 for **Max concurrent jobs** and **Max forks** denotes no limit. For more information, see [Instance group capacity limits](/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-con_controller_configure_instance_groups#controller-instance-group-capacity "There is external business logic that can drive the need to limit the concurrency of jobs sent to an instance group, or the maximum number of forks to be consumed.").

4.  Click Create instance group, or, if you have edited an existing Instance Group click Save instance group

### What to do next

When you have successfully created the instance group the **Details** tab of the newly created instance group enables you to review and edit your instance group information.

You can also edit **Instances** and review **Jobs** associated with this instance group:


![Instance group successfully created](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/ug-instance-group-created.png)

## Associate instances to an instance group

Learn how to associate instances to an instance group in automation controller.

### Procedure

1.  Select the **Instances** tab on the **Details** page of an Instance Group.
2.  Click Associate instance.
3.  Click the checkbox next to one or more available instances from the list to select the instances you want to associate with the instance group and click Confirm
