# 2. Using Ansible Builder
## 2.10. Updating execution environment image locations




Update your execution environment image locations to use images hosted on your private automation hub. You can use execution environments from your private registry instead of the default registry.

**Procedure**

1. Log in to Ansible Automation Platform.
1. Create a container registry credential for your private automation hub:


1. From the navigation panel, selectAutomation Execution→Infrastructure→Credentials.
1. ClickCreate credential.
1. Enter your credential information:


-  **Name** : Enter a name, such as `            Private Hub Registry` .
-  **Credential Type** : Select **Container Registry** .
-  **Authentication URL** : Enter the URL of your private automation hub, such as `            https://automationhub.example.org` .
-  **Username** : Enter your private automation hub username.
-  **Password** or **Token** : Enter your private automation hub password or authentication token.
-  **Verify SSL** : Clear this checkbox if your private automation hub uses self-signed certificates.

1. ClickCreate credential.

1. Update the default execution environments to use images from your private automation hub:


1. From the navigation panel, selectAutomation Execution→Infrastructure→Execution Environments.
1. Locate the **Default execution environment** and click![Edit](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Creating_and_using_execution_environments-en-US/images/e5cb7f9b0cfe60ab5ba421bd17ecbb6a/leftpencil.png)
to edit it.
1. In the **Image** field, update the image path to point to your private automation hub, such as `        automationhub.example.org/ee-supported-rhel9:latest` .
1. In the **Registry Credential** field, select the container registry credential that you created.
1. ClickSave execution environment.
1. Locate the **Minimal execution environment** and click![Edit](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Creating_and_using_execution_environments-en-US/images/e5cb7f9b0cfe60ab5ba421bd17ecbb6a/leftpencil.png)
to edit it.
1. In the **Image** field, update the image path to point to your private automation hub, such as `        automationhub.example.org/ee-minimal-rhel9:latest` .
1. In the **Registry Credential** field, select the container registry credential that you created.
1. ClickSave execution environment.
1. Repeat these steps for any other execution environments that you want to update to use images from your private automation hub.



**Verification**

1. From the navigation panel, selectAutomation Execution→Infrastructure→Execution Environments.
1. Verify that your private automation hub execution environments appear in the list.
1. Optional: Create a test job template that uses one of the new execution environments and run it to confirm that automation controller can successfully pull and use the image from your private automation hub.


**Additional resources**

-  [Execution environments](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_automation_execution/assembly-controller-execution-environments)


