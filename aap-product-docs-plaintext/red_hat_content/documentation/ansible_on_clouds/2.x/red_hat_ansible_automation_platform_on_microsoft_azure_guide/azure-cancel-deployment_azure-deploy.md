# 3. Deploying Red Hat Ansible Automation Platform on Microsoft Azure
## 3.5. Canceling Ansible Automation Platform on Microsoft Azure deployments




You can gracefully cancel a Ansible Automation Platform on Microsoft Azure deployment.

**Procedure**

1. Login to the deployment engine to display the progress of the deployment steps in the **Ansible Automation Platform Deployment Engine** page. Refer to [Monitoring deployments on the Ansible Automation Platform Deployment Engine](https://docs.redhat.com/en/documentation/ansible_on_clouds/2.x/html-single/red_hat_ansible_automation_platform_on_microsoft_azure_guide/index#azure-monitor-deployment-engine_azure-deploy) for information on accessing and logging into the **Ansible Automation Platform Deployment Engine** page.
1. To cancel the deployment, clickCancel Deploymentand confirm.


**Verification**

- To confirm you cancelled the deployment processes on Azure, navigate to the **Overview** page for the managed resource group in which you deployed Ansible Automation Platform and select **Deployments** .


Important
Canceling the deployment does not delete the managed application from your Azure subscription. To avoid incurring costs for the managed application and other resources that are still running, you must delete them.

To delete Azure resources, navigate to the resource group for your deployment in the Azure portal. Select the resources you want to delete and clickDelete. For more information about deleting resources, refer to [Manage Azure resources by using the Azure portal](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resources-portal) in the Microsoft Azure documentation.



