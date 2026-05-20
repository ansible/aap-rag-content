# 3. Manage containers in private automation hub
## 3.4. Setting up your container repository
### 3.4.4. Creating a credential

To pull automation execution environments images from a password or token-protected registry, you must create a credential.

In earlier versions of Ansible Automation Platform, you were required to deploy a registry to store execution environment images. On Ansible Automation Platform 2.0 and later, the system operates as if you already have a remote registry up and running. To store execution environment images, add the credentials of only your selected remote registries.

**Procedure**

1. Log in to Ansible Automation Platform.
2. From the navigation panel, select Automation Execution → Infrastructure → Credentials.
3. Click Create credential to create a new credential.
4. Enter an authorization **Name**, **Description**, and **Organization**.
5. In the **Credential Type** drop-down, select **Container Registry**.
6. Enter the **Authentication URL**. This is the remote registry address.
7. Enter the **Username** and **Password or Token** required to log in to the remote registry.
8. Optional: To enable SSL verification, select **Verify SSL**.
9. Click Create credential.

