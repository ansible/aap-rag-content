# 2. Logging in to self-service automation portal
## 2.1. Signing in to self-service automation portal

Log in to the deployed self-service automation portal using your existing Ansible Automation Platform credentials. The portal uses these credentials for authentication.

**Prerequisites**

- You have configured an OAuth application in Ansible Automation Platform for self-service automation portal.
- You have configured a user account in Ansible Automation Platform.

**Procedure**

1. In a browser, navigate to the URL for self-service automation portal to open the sign-in page.


![Self-service sign-in page](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Using_self-service_automation_portal-en-US/images/7301d2b380047719b3fda17728454b83/self-service-sign-in-page.png)

2. Click Sign In.

3. The sign-in page for Ansible Automation Platform appears:


![Ansible Automation Platform sign-in page](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Using_self-service_automation_portal-en-US/images/cd442c9292d68a910b63db55552d026f/rhaap-sign-in-page.png)

4. Enter your Ansible Automation Platform credentials and click **Log in**.

5. The self-service automation portal web console opens.

**Troubleshooting**

If you are using custom or self-signed SSL certificates and when attempting to log in to self-service automation portal, it displays the error:

`Login failed; caused by Error: Failed to send POST request: fetch failed`

This error indicates that self-service automation portal cannot verify the SSL certificate from your Ansible Automation Platform instance.

To resolve this issue, configure self-service automation portal to trust your custom CA certificate. For more information, see [Section 2.2, “Configuring custom SSL certificates for self-service automation portal”](#self-service-configure-custom-ssl_self-service-login "2.2.&nbsp;Configuring custom SSL certificates for self-service automation portal").

Note

While you can disable SSL validation by setting `checkSSL: false` in the Helm chart configuration, this approach is not recommended for production environments as it reduces security. Instead, configure self-service automation portal to trust your custom CA certificate.

