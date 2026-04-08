# 4. Red Hat Ansible Automation Platform on Microsoft Azure post-deployment requirements
## 4.1. Private network peering for private deployments
### 4.1.1. Hub-and-spoke peering (Transit routes)




The Hub-and-spoke peering model establishes a centralized hub VNet for managing private network communication and transit routing between your existing spoke networks and the dedicated Ansible Automation Platform VNet.

Note
Updating route tables incorrectly can break your network. Only execute the steps in these procedures if you are confident that you can reverse any unexpected network behavior.



#### 4.1.1.1. Hub-and-spoke peering process overview




Understand the necessary preparation and three core steps for enabling private network communication after deploying the managed application.

**Prerequisites**

- You have deployed Ansible Automation Platform on Microsoft Azure.
- You have configured and tested an Azure VNet hub-and-spoke implementation in your Azure tenant. This prerequisite requires many Azure resources to be configured, including a Virtual Network Gateway.
- You have configured transit routing between your spoke networks, including your VPNs. Refer to [Configure VPN gateway transit for virtual network peering](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-peering-gateway-transit) in the Microsoft Azure documentation for instructions.
- You have identified the following:


- The CIDR blocks of your existing VNets (including VPNs and direct connects) that need access to Ansible Automation Platform on Microsoft Azure UIs.
- The CIDR blocks of your existing VNets (including VPNs and direct connects) that contain hosts or endpoints for Ansible Automation Platform on Microsoft Azure.
- The CIDR blocks of the Ansible Automation Platform on Microsoft Azure VNet from the managed resource group of the application. Refer to [Finding the CIDR Block of the managed resource group](https://docs.redhat.com/en/documentation/ansible_on_clouds/2.x/html-single/red_hat_ansible_automation_platform_on_microsoft_azure_guide/index#proc-azure-find-cluster-cidr_azure-hub-spoke-peering) for instructions.



Before peering any networks, ensure that there is no network address space overlap between your private VNets and your Ansible Automation Platform on Microsoft Azure network.

**Procedure**

1. Find the CIDR Block for the Ansible Automation Platform on Microsoft Azure managed application Kubernetes cluster. See [Finding the CIDR Block of the managed application Kubernetes cluster](https://docs.redhat.com/en/documentation/ansible_on_clouds/2.x/html-single/red_hat_ansible_automation_platform_on_microsoft_azure_guide/index#proc-azure-find-cluster-cidr_azure-hub-spoke-peering) .
1. Configure Network Peering with the Ansible Automation Platform Subnet. See [Configuring Network Peering with the Ansible Automation Platform Subnet](https://docs.redhat.com/en/documentation/ansible_on_clouds/2.x/html-single/red_hat_ansible_automation_platform_on_microsoft_azure_guide/index#proc-azure-nw-peering-aap-subnet_azure-hub-spoke-peering) .
1. Update the route tables:


1. Configure route tables from your existing networks to send traffic to the managed application CIDR. You must add routes to the routing tables of every network requesting Ansible Automation Platform user interfaces and of every network that will have automation performed against its resources. See [Routing to Ansible Automation Platform on Microsoft Azure](https://docs.redhat.com/en/documentation/ansible_on_clouds/2.x/html-single/red_hat_ansible_automation_platform_on_microsoft_azure_guide/index#proc-azure-route-to-azure_azure-hub-spoke-peering) .
1. Configure routing to your VNets for each spoke network that you would like Ansible Automation Platform to communicate with, for automation or for accessing the user interfaces. See [Routing to your VNets](https://docs.redhat.com/en/documentation/ansible_on_clouds/2.x/html-single/red_hat_ansible_automation_platform_on_microsoft_azure_guide/index#proc-azure-route-to-vnets_azure-hub-spoke-peering) .



#### 4.1.1.2. Finding the CIDR Block of the managed resource group




You can use the **Resource Groups** page to find the CIDR Block of the managed resource group.

**Procedure**

1. Navigate to the **Resource Groups** page in the Azure portal.
1. Click the managed resource group for Red Hat Ansible Automation Platform on Microsoft Azure. The resource group name is prefixed with “-mrg”.
1. Select the VNet within the resource group to view its settings in the **Overview** page.


**Verification**

The CIDR block of the cluster is displayed in the **Address Space** .


**Additional resources**

-  [View virtual networks and settings](https://learn.microsoft.com/en-us/azure/virtual-network/manage-virtual-network#view-virtual-networks-and-settings)


#### 4.1.1.3. Configuring network peering with the Ansible Automation Platform subnet




Within the Azure console, the Azure virtual network (VNet) is known as _this virtual network_ , and the VNet that you want to peer with is known as _remote virtual network_ .

In the **Virtual Networks** page in the Azure portal, use the following settings to configure peering between the Azure VNet and the VNet that you want to peer with the Ansible Automation Platform on Microsoft Azure app:

**Procedure**

1. Under **Remote virtual network** , select the settings for the virtual network that you want to peer with Azure:


-  **Summary** :


-  **Peering link name** : _<aap_to_hub_peering_link_name>_
-  **Peering settings** :


-  **Traffic to remote virtual network** : _Allow_
-  **Traffic forwarded from remote virtual network** : _Allow_



1. Under **Local virtual network** , select **Settings** the Ansible Automation Platform on Microsoft Azure virtual network:


-  **Summary** :


-  **Peering link name** : _<hub_to_aap_peering_link_name>_
-  **Peering settings** :


-  **Traffic to remote virtual network** : _Allow_
-  **Traffic forwarded from remote virtual network** : _Allow_
-  **Enable this virtual network to use peered VNet’s remote gateway or Route Sever** : _Enabled_





**Additional resources**

-  [Create a peering](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-peering#create-a-peering)


#### 4.1.1.4. Updating the route tables




Route tables in the Azure portal are sets of rules, known as routes, that determine how network traffic is directed between subnets, virtual networks (VNets), on-premises networks, and the internet.

**Procedure**

1. Before you update the route tables, confirm that you satisfy the [Prerequisites](https://docs.redhat.com/en/documentation/ansible_on_clouds/2.x/html-single/red_hat_ansible_automation_platform_on_microsoft_azure_guide/index#proc-azure-hub-spoke-peering_azure-hub-spoke-peering) for the hub-and-spoke peering process.


##### 4.1.1.4.1. Routing to Ansible Automation Platform on Microsoft Azure




Use the **Route Tables** page in the Azure portal to route traffic to Ansible Automation Platform.

**Procedure**

1. Navigate to **Route Tables** in the Azure portal.
1. As part of your hub-and-spoke configuration, you created one or more route tables to define the routes between the networks. Click on one of these route tables.
1. From the route table menu bar, click **Routes** > **Add** .
1. Configure routes from your existing networks to send traffic to Ansible Automation Platform. You must configure routes for any network requesting Ansible Automation Platform user interfaces and for any network that will have automation performed against its resources. For each route that you add, enter the following information:


-  **Route name** : Enter a route name for the Ansible Automation Platform managed application network
-  **Address Prefix** : The CIDR block of the managed application kubernetes cluster
-  **Next Hop Type** : _Virtual network gateway_

1. Click **OK** to save the new route to the route list.
1. Repeat this procedure for all other route tables where you want to route traffic to Ansible Automation Platform.


##### 4.1.1.4.2. Routing to your VNets




Add a route for each spoke network that you would like Ansible Automation Platform to communicate with, for automation or for accessing the user interfaces.

**Procedure**

1. Navigate to **Route Tables** in the Azure portal.
1. In the list of route tables, select the route table for the Ansible Automation Platform on Microsoft Azure managed application.

The name of the Ansible Automation Platform route table uses the following convention:


```
aks-agentpool-&lt;numbers&gt;-routetable
```


1. From the route table menu bar, click **Routes** > **Add** .
1. Configure routing to your VNets for each spoke network that you would like Ansible Automation Platform to communicate with, for both automation or accessing the user interfaces.
1. For each route that you add, enter the following information:


-  **Route name** : Enter a route name for the spoke network that you want Ansible Automation Platform to route to
-  **Address Prefix** : The CIDR block of the spoke network
-  **Next Hop Type** : _Virtual network gateway_

1. Click **OK** to save the new route to the route list.


**Verification**

After you have configured the routing rules, traffic is routed to and from Ansible Automation Platform on Azure through your hub network.


##### 4.1.1.4.3. Outbound routing through virtual appliances




If your organization uses Azure firewall services or third-party firewall appliances through a Virtual Appliance connection, you must configure outbound connectivity from the managed application, to enable Red Hat to maintain your application and to enable automation against external resources.

The easiest way to implement this is to create a firewall rule that allows all outbound traffic from port 443.

If you choose not to allow all outbound traffic from port 443, you must configure routes.

**Procedure**

1. For Red Hat to manage and upgrade Ansible Automation Platform on Microsoft Azure and execute security patching, any machine in the Azure Kubernetes service (AKS) cluster must be allowed to submit a request to pull updates for containers used by Ansible Automation Platform.


1. Add routes in the Ansible Automation Platform route table for outbound traffic from the full CIDR range of the Ansible Automation Platform on Microsoft Azure managed application to the domains listed in the [Azure Virtual Appliance Routing with Ansible Automation Platform on Azure](https://access.redhat.com/articles/6972355) article on the Red Hat Customer Portal.

1. You must also allow traffic from your firewall to any other external domain or IP address that you want Ansible Automation Platform to run automation jobs against. Otherwise, your firewall blocks connectivity between Ansible Automation Platform and destinations for automation.
1. Ansible Automation Platform requires a public DNS zone to provide SSL certificates. This public DNS zone is in the managed resource group of the deployment. The platform must be able to communicate via DNS queries with the servers listed in the DNS zone to complete certificate challenges with our upstream provider. Blocking this communication prevents successful certificate renewal.


**Additional resources**

-  [Create a route](https://learn.microsoft.com/en-us/azure/virtual-network/manage-route-table#create-a-route)


