# 5. Connecting to Red Hat Ansible Automation Platform
## 5.3. Private deployments
### 5.3.1. Azure hosted virtual machine




A straightforward way to configure access for a small set of users to access private network resources on Azure networks is to create a jumpbox VM in a perimeter network (DMZ VNet) that users can remotely log into from the public internet. The jumpbox VM requires workstation features such as a GUI and browser.

Users can remotely log into the publicly accessible virtual machine from on-premises machines through VNC, RDP, or other screen-sharing protocols.

To access the Ansible Automation Platform web UIs on the Azure private network, users navigate to the URL using the browser on the jumpbox VM.

You connect the DMZ VNet to other Azure VNets through network peering, with routing rules established to send network traffic to the Ansible Automation Platform VNet.

The following diagram shows the topology for an example configuration of private network access via an Azure virtual machine.

![aap on azure private nw access vm](https://access.redhat.com/webassets/avalon/d/Ansible_on_Clouds-2.x-Red_Hat_Ansible_Automation_Platform_on_Microsoft_Azure_Guide-en-US/images/5813aeb8ca353af0662270b829907cf1/aap-on-azure-private-nw-access-vm.png)


- For more information about perimeter (DMZ) networks, refer to [Perimeter Networks](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/perimeter-networks) in the Microsoft _Azure Cloud Adoption Framework_ documentation.
- For more information about jumpboxes, refer to [About Azure bastion host and jumpboxes](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/cloud-scale-analytics/architectures/connect-to-environments-privately#about-azure-bastion-host-and-jumpboxes) in the Microsoft _Azure Cloud Adoption Framework_ documentation.


