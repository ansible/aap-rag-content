# 2. Prerequisites for Installing Red Hat Ansible Automation Platform on Microsoft Azure
## 2.3. Azure resource quotas and infrastructure limits
### 2.3.1. Regional vCPU limits




The Azure resources used during the deployment of the managed application temporarily exceed the resource requirements in [Ansible Automation Platform on Microsoft Azure infrastructure usage](https://docs.redhat.com/en/documentation/ansible_on_clouds/2.x/html-single/red_hat_ansible_automation_platform_on_microsoft_azure_guide/index#con-azure-infrastructure-usage_azure-intro) . The `Total Regional vCPUs` quota is temporarily consumed when deploying the managed application.

Every Azure region has a separate `Total Regional vCPUs` quota. To prevent installation failure, ensure that you have at least 80 DDSv5 and 8 DSV3 vCPUs available in the Azure region where you want to deploy the managed application.

You can view the resource quotas for your subscription from the Azure console. Open the **My Quotas** page and select the region where you wish to deploy the managed application to view your allocation and usage metrics for that region. Ensure that you have selected a single region. Viewing all regions at once does not show the limitations of a single Azure region.

