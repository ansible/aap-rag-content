# 4. Red Hat Ansible Automation Platform on Microsoft Azure post-deployment requirements
## 4.1. Private network peering for private deployments
### 4.1.3. Direct peering




You can use direct peering to directly connect virtual networks. When two networks are peered, Azure updates routes between them so that traffic automatically flows between them.

The direct peering method is easier to configure than the hub-and-spoke model. However, the number of direct network peerings is limited. Direct peering becomes difficult to manage as the number of virtual networks grows, because each new network requires peering to all other networks.

#### 4.1.3.1. Configuring direct network peering




You can configure network peering between your Azure network and your VNet in the **Virtual Networks** page of the Azure Portal.

Within the Azure console, the Azure virtual network is known as _this virtual network_ , and the VNet that you want to peer with is known as _remote virtual network_ .

In the **Virtual Networks** page in the Azure portal, use the following settings to configure the Azure network and the VNet that you want to peer with the Ansible Automation Platform on Microsoft Azure app:

**Procedure**

1. Under **Remote virtual network** , select the settings for the virtual network that you want to peer with Azure:


-  **Summary** :


-  **Peering link name** : _<aap_to_hub_peering_link_name>_
-  **Subscription** : Select the subscription where you deployed the Ansible Automation Platform on Microsoft Azure.
-  **Virtual network** : Select the Ansible Automation Platform on Microsoft Azure virtual network: vnet-<aap_identifier>-<region>

-  **Peering settings** :


-  **Traffic to remote virtual network** : _Allow_
-  **Traffic forwarded from remote virtual network** : _Allow_
-  **Virtual network gateway or Route Server** : _Use the remote virtual network’s gateway or Route server_


1. Under **Local virtual network** , select the settings the Ansible Automation Platform on Microsoft Azure virtual network:


-  **Summary** :


-  **Peering link name** : _<hub_to_aap_peering_link_name>_
-  **Traffic to remote virtual network** : _Allow_
-  **Traffic forwarded from remote virtual network** : _Allow_
-  **Enable this virtual network to use peered VNet’s remote gateway or Route Sever** : _Enabled_


1. After you have configured direct network peering, traffic routes between Ansible Automation Platform on Microsoft Azure and private hosts and IPs on your VNet.


**Additional resources**

-  [Create a peering](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-peering#create-a-peering)
-  [Virtual network peering](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-peering-overview)


