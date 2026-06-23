# Update the deployment URL
## Sign in to Ansible automation portal

Log in to the deployed Ansible automation portal using your existing Ansible Automation Platform credentials. The portal uses these credentials for authentication.

### Before you begin

- You have configured an OAuth application in Ansible Automation Platform for Ansible automation portal.
- You have configured a user account in Ansible Automation Platform.

### Procedure

1.  In a browser, navigate to the URL for Ansible automation portal to open the sign-in page.
![Self-service sign-in page](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/self-service-sign-in-page.png)
2.  Click Sign In.
3.  The sign-in page for Ansible Automation Platform appears:
![Ansible Automation Platform sign-in page](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/rhaap-sign-in-page.png)
4.  Enter your Ansible Automation Platform credentials and click **Log in**.
5.  The Ansible automation portal web console opens.

If you are using custom or self-signed SSL certificates and when attempting to log in to Ansible automation portal, it displays the error:

`Login failed; caused by Error: Failed to send POST request: fetch failed`

This error indicates that Ansible automation portal cannot verify the SSL certificate from your Ansible Automation Platform instance.

To resolve this issue, configure Ansible automation portal to trust your custom CA certificate.

Note:

While you can disable SSL validation by setting `checkSSL: false` in the Helm chart configuration, this approach is not recommended for production environments as it reduces security. Instead, configure Ansible automation portal to trust your custom CA certificate.
