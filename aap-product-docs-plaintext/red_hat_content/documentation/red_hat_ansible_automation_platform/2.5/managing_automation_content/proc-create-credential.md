# 3. Manage containers in private automation hub
## 3.4. Setting up your container repository
### 3.4.4. Creating a credential




To pull automation execution environments images from a password or token-protected registry, you must create a credential.

In earlier versions of Ansible Automation Platform, you were required to deploy a registry to store execution environment images. On Ansible Automation Platform 2.0 and later, the system operates as if you already have a remote registry up and running. To store execution environment images, add the credentials of only your selected remote registries.

**Procedure**

1. Log in to Ansible Automation Platform.
1. From the navigation panel, selectAutomation Execution→Infrastructure→Credentials.
1. ClickCreate credentialto create a new credential.
1. Enter an authorization **Name** , **Description** , and **Organization** .
1. In the **Credential Type** drop-down, select **Container Registry** .
1. Enter the **Authentication URL** . This is the remote registry address.
1. Enter the **Username** and **Password or Token** required to log in to the remote registry.
1. Optional: To enable SSL verification, select **Verify SSL** .
1. ClickCreate credential.


