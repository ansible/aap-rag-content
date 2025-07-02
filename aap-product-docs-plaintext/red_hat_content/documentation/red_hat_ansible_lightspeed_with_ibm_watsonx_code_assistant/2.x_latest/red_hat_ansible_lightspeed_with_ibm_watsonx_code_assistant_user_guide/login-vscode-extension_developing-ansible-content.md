# 4. Developing Ansible content
## 4.2. Installing and configuring the Ansible VS Code extension
### 4.2.4. Logging in to Ansible Lightspeed through the Ansible VS Code extension




After installing and configuring the VS Code extension, you can log in to the Ansible Lightspeed service.

#### 4.2.4.1. Sign-in options




Red Hat Ansible Lightspeed provides different sign-in methods depending on whether you are using the cloud service or the on-premise deployment.

-  **Ansible Lightspeed on-premise deployments**

Users are authenticated using your Red Hat Ansible Automation Platform login.

To sign in, you can use the **Connect** button in the Ansible Lightspeed view, or the **Sign in with Ansible Lightspeed to use Ansible** option in theAccountsmenu. Once prompted in the browser, select **Log in with Ansible Automation Platform** , and log in with the authorization mechanism that your automation controller is configured with.


-  **Ansible Lightspeed cloud service**

Users are authenticated using Red Hat Single Sign-On (RH-SSO).

To sign in from VS Code, you can use the **Connect** button in the Ansible Lightspeed view, or the **Sign in with Ansible Lightspeed to use Ansible** option in theAccountsmenu. Follow the on-screen prompts to log in and access the Ansible Lightspeed service using your RH-SSO.

Note
If you are using a cloud development environment at a domain unknown by Ansible Lightspeed, such as on-premise Red Hat OpenShift Dev Spaces, yourAccountssign-in menu provides the option **Sign-in with Red Hat to use Ansible** . This option uses a device code flow to successfully complete the sign-in process and requires the Red Hat Authentication extension v0.2.0 or later. If you require this authentication flow but don’t see the **Sign-in with Red Hat to use Ansible** option, ensure you are using the Ansible VS Code extension v24.5.2 or later.






#### 4.2.4.2. Procedure




1. Open the VS Code application.
1. Sign in using either the **Connect** button in the Ansible Lightspeed view or theAccountsmenu.


-  **Sign in using the Connect button** :


1. From the VS Code activity bar, click the **Ansible** icon.
1. In the **Ansible Lightspeed** view, click **Connect** .
1. Follow the on-screen prompts to sign in to Ansible Lightspeed.

-  **Sign in using theAccountsmenu** :


1. From the VS Code activity bar, click theAccountsmenu.
1. Sign in with Ansible Lightspeed to use Ansible or sign in with Red Hat to use Ansible, depending on the sign-in option you are presented with.

Note

- The sign-in options are displayed when the VS Code extension is in an active state. The extension is activated after you open the Ansible side panel or after you open an Ansible file in the VS Code editor. If you do not see this option, use the **Connect** button to link to the Ansible Lightspeed service.
- If you are using a cloud development environment at a domain unknown by Ansible Lightspeed, such as on-premise Red Hat OpenShift Dev Spaces, yourAccountssign-in menu provides the option **Sign-in with Red Hat to use Ansible** . This option uses a device code flow to successfully complete the sign-in process and requires the Red Hat Authentication extension v0.2.0 or later. If you require this authentication flow but don’t see the **Sign-in with Red Hat to use Ansible** option, ensure you are using the Ansible VS Code extension v24.5.2 or later.



1. Follow the on-screen prompts to sign in to Ansible Lightspeed.

On successful authentication, the login screen is displayed along with your username and your assigned user role.




