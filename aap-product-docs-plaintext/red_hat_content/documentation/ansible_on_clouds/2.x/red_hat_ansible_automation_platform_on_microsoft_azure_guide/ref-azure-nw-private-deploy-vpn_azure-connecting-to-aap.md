# 5. Connecting to Red Hat Ansible Automation Platform
## 5.3. Private deployments
### 5.3.2. VPN




If your organization requires that many users access Ansible Automation Platform over a private connection, or if your organization already uses VPNs or direct connections with Azure, then this approach might be suitable.

In this configuration, your on-premises infrastructure is connected to Azure through a Network Application Gateway and has routing rules that can enable access to Ansible Automation Platform to any connected computer on the local network. The VNet connected to the Virtual Network Gateway is connected to other Azure VNets through network peering, with routing rules established to send network traffic to the Ansible Automation Platform VNet.

With this configuration, users can access Ansible Automation Platform through the application URL as if they were using the public access approach.

![aap on azure private nw access vpn](https://access.redhat.com/webassets/avalon/d/Ansible_on_Clouds-2.x-Red_Hat_Ansible_Automation_Platform_on_Microsoft_Azure_Guide-en-US/images/0b63828f43fc06901c9bff69f4b337a7/aap-on-azure-private-nw-access-vpn.png)


