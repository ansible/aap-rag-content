# 1. Introduction to Red Hat Ansible Automation Platform on Microsoft Azure
## 1.3. Application Architecture
### 1.3.2. Private deployment




A private deployment of Ansible Automation Platform resides in an isolated Azure VNet with no access from external sources: traffic to and from the public internet and other Azure VNets and subnets is blocked.

To access the URL for the Ansible Automation Platform user interfaces, you must configure network peering.

After you have configured peering and routing, you can access Ansible Automation Platform through a VM on a connected Azure subnet, or directly if your organization has transit routing set up between Azure and your local network.

Note
No two Azure networking configurations are the same. To allow user access to your Ansible Automation Platform URL, your organization needs to work with your Azure administrators to connect the private access deployment.



The following diagram outlines the application resources and architecture that are deployed into the managed application resource group on a private deployment of Ansible Automation Platform on Microsoft Azure into your Azure subscription. The IP ranges change based on the networking address range you set on deployment.

![aap on azure private deployment](https://access.redhat.com/webassets/avalon/d/Ansible_on_Clouds-2.x-Red_Hat_Ansible_Automation_Platform_on_Microsoft_Azure_Guide-en-US/images/cccc9c904ab44793c49b0d2dedebd634/aap-on-azure-private-deployment.png)


