# 4. Setting up Red Hat Ansible Lightspeed for your organization
## 4.3. Setting up Red Hat Ansible Lightspeed on-premise deployment
### 4.3.2. Installing the Red Hat Ansible Automation Platform operator




Use this procedure to install the Ansible Automation Platform operator on the Red Hat OpenShift Container Platform.

**Prerequisites**

- You have installed and configured automation controller.


**Procedure**

1. Log in to the Red Hat OpenShift Container Platform as an administrator.
1. Create a namespace:


1. Go toAdministration→Namespaces.
1. Click **Create Namespace** .
1. Enter a unique name for the namespace.
1. Click **Create** .

1. Install the operator:


1. Go toOperators→OperatorHub.
1. Select the namespace where you want to install the Red Hat Ansible Automation Platform operator.
1. Search for the Ansible Automation Platform operator.
1. From the search results, select the Ansible Automation Platform (provided by Red Hat) tile.
1. Select an **Update Channel** . You can select either **stable-2.x** or **stable-2.x-cluster-scoped** as the channel.
1. Select the destination namespace if you selected “stable-2.x” as the update channel.
1. Select **Install** . It takes a few minutes for the operator to be installed.

1. Click **View Operator** to see the details of your newly installed Red Hat Ansible Automation Platform operator.


