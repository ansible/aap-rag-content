# 3. Installing the Red Hat Edge Manager on Ansible Automation Platform
## 3.2. Set up the OAuth application for Ansible Automation Platform
### 3.2.1. Setting up the OAuth application automatically

Automatic setup of an OAuth application by generating an OAuth token within Ansible Automation Platform and adding it to your configuration file. Upon service startup, the application is automatically created, and the client ID updated.

**Procedure**

1. Generate an OAuth token in Ansible Automation Platform:


1. From the navigation panel, select Access Management → Users.

2. Select a user with write permissions to the **Default** organization (admin user recommended).

3. Click the **Tokens** tab for that user.

4. Click Create token and enter the relevant details.


1. **Scope**: Select **Write**.

2. Go to the [Integrating with Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/managing_device_fleets_with_the_red_hat_edge_manager/assembly-edge-manager-install#edge-manager-integrate-aap) section for the steps to edit your `service-config.yaml` file and complete setting up the OAuth application automatically.

