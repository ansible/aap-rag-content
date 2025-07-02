# 5. Red Hat Ansible Automation Platform Service on AWS Service Definition
## 5.3. Execution plane
### 5.3.2. Networking




#### 5.3.2.1. Automation mesh




Ansible Automation Platform Service on AWS provides default “mesh-ingress” hop nodes. These hosted hop nodes allow execution nodes to poll for automation work through egress from a customer’s private network, eliminating the need to open inbound firewall ports. Hosted hop nodes use port 443 for inbound traffic.

The following is an example of an execution node in a private address space with egress-only internet access connected to Ansible Automation Platform Service on AWS through this model.

![Execution node in a private address space](https://access.redhat.com/webassets/avalon/d/Ansible_on_Clouds-2.x-Red_Hat_Ansible_Automation_Platform_Service_on_AWS-en-US/images/b67da351ac8afd1bb63c8e5afcc379c0/automation_mesh.png)


You can also configure the automation mesh with outbound connectivity from the control plane to your execution plane, allowing you to specify the ports used by the automation mesh.

You can use the [Automation mesh for managed cloud or operator environments](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/automation_mesh_for_managed_cloud_or_operator_environments/index) documentation for instructions.

#### 5.3.2.2. Connectivity




The execution plane can communicate with the control plane under the following conditions:

- Polling (mesh-ingress): Execution nodes must route stateful egress traffic to the Ansible Automation Platform deployment domain over port 443.
- Push: A configurable firewall port must be open in the customer’s remote networks to allow Ansible Automation Platform to push information to execution nodes.


You can configure automation mesh nodes behind firewalls, proxy servers, and similar services. These services route or proxy traffic originating from Ansible Automation Platform without altering headers, payload, or other information that would affect functionality of the automation mesh.

You can restrict access to the control plane by providing CIDR blocks to the Red Hat support team through a [Customer support request](https://access.redhat.com/support/cases/#/case/new/get-support?caseCreate=true) . This controls the inbound access to the control plane limiting it to the IP ranges you provide for traffic over the public internet. The application of these rules do not apply to traffic over PrivateLink. These restrictions do not affect outbound traffic that originates from the control plane.

