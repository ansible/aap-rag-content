# 3. Deploying Red Hat Ansible Automation Platform on Microsoft Azure
## 3.2. Provisioning Ansible Automation Platform on Microsoft Azure




When you initiate the deployment of the Red Hat Ansible Automation Platform managed app from Azure marketplace, a form is displayed in the **Create Red Hat Ansible Automation Platform on Microsoft Azure** window.

Before you fill in the form, decide whether you want to create a public or private deployment of Ansible Automation Platform on Microsoft Azure:

- Public deployments allow ingress to the Ansible Automation Platform on Microsoft Azure user interfaces over the public internet. No configuration is required to access the application URL.
- Private deployments are created in an isolated Azure VNet that blocks access from the public internet. To access Ansible Automation Platform on Microsoft Azure user interfaces, you must configure network peering and routing.


You create the network configuration for the Ansible Automation Platform on Microsoft Azure VNet when you initiate the deployment. Refer to your network configuration plan before deploying the managed application. For information about planning your network configuration, see [Network](https://docs.redhat.com/en/documentation/ansible_on_clouds/2.x/html-single/red_hat_ansible_automation_platform_on_microsoft_azure_guide/index#con-azure-network_azure-install-prerequisites) .

Complete the form to provision Red Hat Ansible Automation Platform infrastructure and resources into your Azure tenant.

**Procedure**

1. Click the **Basics** tab and enter values for your deployment in the following fields in the form:


-  **Subscription** : Select **Ansible on Clouds** .
-  **Resource Group** : Create or select a resource group where you want to deploy the managed application.
-  **Region** : The Azure region where the application is deployed.
-  **Application Name** : A unique name for the managed application.
-  **Administrator Password** : Create an administrator password for your deployment.

The _Administrator Password_ must contain at least 8 characters, and must include uppercase letters, lowercase letters, and numbers.


-  **Confirm Administrator Password** : Confirm the _Administrator Password_ .
-  **Access** : Choose whether your deployment is public or private.
-  **Managed Resource Group** : A resource group for the managed application infrastructure.

Keep this resource group isolated from other resource groups, including the _Resource Group_ where you deployed the managed application.



1. Store the information that you entered in the form in a secure place. You must provide the _Administrator password_ to access your Ansible Automation Platform.
1. ClickNext
1. Follow the steps in [Red Hat Ansible Automation Platform on Microsoft Azure Networking Preparation](https://access.redhat.com/articles/6973251) to configure your network configuration.
1. ClickNext.
1. Click the **Business continuity** tab.
1. From the **Disaster Recovery** list, select an option to enable or disable disaster recovery.
1. From the **Tags** tab, you can select the resources you want to apply a tag to, otherwise, the default applies.
1. Select the **Deployment** tab.
1. Note the following requirements in the description:


- You must have a Red Hat account.
- To use Ansible Automation Platform, you must have a valid subscription linked to your Red Hat account.
- You must use the Deployment Driver during deployment.

1. Select the checkboxes to indicate that you understand these requirements.
1. ClickReview + Create.
1. If the information you entered in the form is valid, the window displays **Validation Passed** .
1. Select **I agree** to accept the Co-Admin Access Permissions terms and conditions.
1. ClickCreateto begin the provisioning process for the application.


**Verification**

The application begins provisioning.


You can use the deployment engine to view the progress of your deployment a few minutes after the Azure console displays "Your deployment is complete". See [Monitoring deployments on the Ansible Automation Platform Deployment Engine](https://docs.redhat.com/en/documentation/ansible_on_clouds/2.x/html-single/red_hat_ansible_automation_platform_on_microsoft_azure_guide/index#azure-monitor-deployment-engine_azure-deploy) for more information.

It may take 30 minutes or longer for the infrastructure and software to fully provision.

After provisioning is complete, you can access and log in to your new Ansible Automation Platform instance. For help with configuring your automation controller and automation hub instances see [Configuring automation execution](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/configuring_automation_execution/index) and [Managing automation content](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/managing_automation_content) respectively.

