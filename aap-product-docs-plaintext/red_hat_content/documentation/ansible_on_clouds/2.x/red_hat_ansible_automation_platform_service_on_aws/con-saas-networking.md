# 5. Red Hat Ansible Automation Platform Service on AWS Service Definition
## 5.3. Execution plane
### 5.3.2. Networking




Understand the automation mesh architecture and the connectivity requirements for the execution plane

#### 5.3.2.1. Automation mesh




Ansible Automation Platform Service on AWS provides default “mesh-ingress” hop nodes. These hosted hop nodes allow execution nodes to poll for automation work through egress from a customer’s private network, eliminating the need to open inbound firewall ports. Hosted hop nodes use port 443 for inbound traffic.

The following is an example of an execution node in a private address space with egress-only internet access connected to Ansible Automation Platform Service on AWS through this model.

![Execution node in a private address space](https://access.redhat.com/webassets/avalon/d/Ansible_on_Clouds-2.x-Red_Hat_Ansible_Automation_Platform_Service_on_AWS-en-US/images/b67da351ac8afd1bb63c8e5afcc379c0/automation_mesh.png)


You can also configure the automation mesh with outbound connectivity from the control plane to your execution plane, allowing you to specify the ports used by the automation mesh.

You can use the [Automation mesh for managed cloud or operator environments](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/automation_mesh_for_managed_cloud_or_operator_environments/index) documentation for instructions.

#### 5.3.2.2. PrivateLink configuration types




The PrivateLink configuration offers both ingress, for UI/API access to the Ansible Automation Platform control plane, and egress, for the control plane to connect to your private resources. For more information, see section [AWS PrivateLink connectivity into the Ansible Automation Platform control plane](https://docs.redhat.com/en/documentation/ansible_on_clouds/2.x/html/red_hat_ansible_automation_platform_service_on_aws/saas-private-link#aws_privatelink_connectivity_into_the_ansible_automation_platform_control_plane) .

-  **Ingress PrivateLink:** Connects your VPC to the Ansible Automation Platform control plane (for UI/API access). Requires a support ticket providing your AWS Account ID and Region.
-  **Egress PrivateLink:** Connects the Ansible Automation Platform control plane to your private resources (for example, private automation hub). This requires a separate support ticket to authorize the connection to your Endpoint Service.


#### 5.3.2.3. Connectivity




The execution plane can communicate with the control plane under the following conditions:

- Polling (mesh-ingress): Execution nodes must route stateful egress traffic to the Ansible Automation Platform deployment domain over port 443.
- Push: A configurable firewall port must be open in the customer’s remote networks to allow Ansible Automation Platform to push information to execution nodes.


You can configure automation mesh nodes behind firewalls, proxy servers, and similar services. These services route or proxy traffic originating from Ansible Automation Platform without altering headers, payload, or other information that would affect functionality of the automation mesh.

You can restrict access to the control plane by providing CIDR blocks to the Red Hat support team through a [Customer support request](https://access.redhat.com/support/cases/#/case/new/get-support?caseCreate=true) . This controls the inbound access to the control plane limiting it to the IP ranges you provide for traffic over the public internet. The application of these rules do not apply to traffic over PrivateLink. These restrictions do not affect outbound traffic that originates from the control plane.

Important
Customers **must** allowlist the following wildcard domain in their local firewalls to permit the SRE team’s maintenance and monitoring:

-  `    *.redhat.com`




