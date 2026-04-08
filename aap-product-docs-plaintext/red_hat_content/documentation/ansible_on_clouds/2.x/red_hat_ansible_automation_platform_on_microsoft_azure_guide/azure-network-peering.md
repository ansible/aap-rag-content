# 4. Red Hat Ansible Automation Platform on Microsoft Azure post-deployment requirements
## 4.1. Private network peering for private deployments




Deploying Ansible Automation Platform on Microsoft Azure creates an independent managed resource group with its own Azure virtual network (VNet). By default, the platform can only send requests to external networks through the public internet.

To enable access to resources in private, internet-gapped deployments, you must configure Azure network peering between your private VNets and the managed application VNet of Ansible Automation Platform.

Azure network peering allows:

- Private communication between multiple Azure VNets.
- Private transit routing between Azure VNets and external VPN-routed networks, which can include on-premises systems or other cloud environments.


Each Azure networking configuration is unique. To enable user access to Ansible Automation Platform, collaborate with your Azure administrators to establish connections between the platform’s deployment, your VNets, and external VPN-routed networks.

Note
Network peering must be configured by Azure administrators in your organization who are familiar with Azure networking. Configuring network changes to your Azure account can cause outages or other disruptions.

The network peering procedures described in this document are not supported by Red Hat, as the processes and services are controlled and managed by Microsoft Azure. Contact Microsoft for assistance in peering Azure networks.

While every effort has been made to align with Microsoft’s documentation for this content, there may be drift in accuracy over time. [Microsoft’s documentation](https://docs.microsoft.com/en-us/azure/virtual-network/virtual-network-peering-overview) is the definitive source for information about networking topics for Azure.



Azure offers different ways to peer private networks. These are typically divided into two categories:

-  **Hub-and-spoke peering** : In this topology, there is a centralized hub VNet that other virtual networks peer with. This hub network has mechanisms to route traffic through transit routing. Cloud networks, including VPN/Express Connect connections with on-premises and other cloud networks, can communicate through the hub VNet.
-  **Azure Virtual WAN (VWAN)** : Azure Virtual WAN is a networking service that provides simplified hub-and-spoke network modeling across Azure, on-premises, and other VPN/Direct Connect networks. For more about VWAN, refer to Microsoft’s [Virtual WAN documentation](https://learn.microsoft.com/en-us/azure/virtual-wan/virtual-wan-about) .
-  **Direct peering** : Private networks are individually connected to one another with no routing hops between them. This is a simpler peering model: it is useful when you only want to connect a few networks.


Refer to [Choose between virtual network peering and VPN gateways](https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/hybrid-networking/vnet-peering) in the Microsoft _Application architecture fundamentals guide_ to determine the correct peering approach for your organization.

