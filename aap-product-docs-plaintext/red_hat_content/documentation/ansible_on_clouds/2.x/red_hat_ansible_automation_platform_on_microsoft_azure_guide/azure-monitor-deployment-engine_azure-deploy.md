# 3. Deploying Red Hat Ansible Automation Platform on Microsoft Azure
## 3.4. Monitoring deployments on the Ansible Automation Platform Deployment Engine

The deployment engine displays information about your Ansible Automation Platform on Microsoft Azure deployment. You can monitor the progress of the deployment, restart failed deployment steps, and cancel the deployment.

When you begin deploying Ansible Automation Platform on Microsoft Azure, the Azure interface displays the **Overview** page for the deployment. The **Overview** page displays the deployment status.

**Procedure**

1. When the status in the **Overview** page shows "Your deployment is complete", navigate to the deployed managed application.

2. Click **Parameters and Outputs** in the **Settings** menu for the deployed managed application.


- **Note:** Approximately 10 minutes into the deployment process, the **Outputs** section of the **Parameters and Outputs** page displays a link to the **`deploymentEngineUrl`**.

3. Copy the link and paste it in another browser tab to open the login page for the deployment engine.

4. Log in to the deployment using the following credentials:


- **Username**: *admin*
- **Password**: Use the *Administrator Password* that you chose when configuring your deployment.

5. The deployment driver displays a message indicating that your deployment is underway. Click Log in with Red Hat account. The **Red Hat login** page opens.

6. In the **Red Hat login** page, enter your credentials if you already have a Red Hat account.


1. If you do not have a Red Hat account, click Register for a Red Hat account to create one.

**Verification**

After logging in with your Red Hat account, the Ansible Automation Platform Deployment Engine page opens.

