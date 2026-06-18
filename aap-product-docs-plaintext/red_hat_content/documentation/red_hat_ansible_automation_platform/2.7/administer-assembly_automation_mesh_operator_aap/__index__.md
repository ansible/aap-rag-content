# Scale with automation mesh in an operator environment

Scaling your automation mesh is available on OpenShift deployments of Red Hat Ansible Automation Platform and is possible through adding or removing nodes from your cluster dynamically, using the **Instances** resource of the Ansible Automation Platform UI, without running the installation script.

Instances serve as nodes in your mesh topology. Automation mesh enables you to extend the footprint of your automation. The location where you launch a job can be different from the location where the ansible-playbook runs.

To manage instances from the Ansible Automation Platform UI, you must have System Administrator or System Auditor permissions.

In general, the more processor cores (CPU) and memory (RAM) a node has, the more jobs that can be scheduled to run on that node at once.

## Prerequisites

The automation mesh is dependent on hop and execution nodes running on *Red Hat Enterprise Linux* (RHEL). Your Red Hat Ansible Automation Platform subscription grants you ten Red Hat Enterprise Linux licenses that can be used for running components of Ansible Automation Platform.

For more information about Red Hat Enterprise Linux subscriptions, see **Registering the system and managing subscriptions** in the Red Hat Enterprise Linux documentation.

The following steps prepare the RHEL instances for deployment of the automation mesh.

1. You require a Red Hat Enterprise Linux operating system. Each node in the mesh requires a static IP address, or a resolvable DNS hostname that Ansible Automation Platform can access.
2. Ensure that you have the minimum requirements for the RHEL virtual machine before proceeding. For more information, see the **System requirements**.
3. Deploy the RHEL instances within the remote networks where communication is required. For information about creating virtual machines, see **Creating Virtual Machines** in the *Red Hat Enterprise Linux* documentation. Remember to scale the capacity of your virtual machines sufficiently so that your proposed tasks can run on them.   - RHEL ISOs can be obtained from access.redhat.com.
- RHEL cloud images can be built using Image Builder from console.redhat.com.
