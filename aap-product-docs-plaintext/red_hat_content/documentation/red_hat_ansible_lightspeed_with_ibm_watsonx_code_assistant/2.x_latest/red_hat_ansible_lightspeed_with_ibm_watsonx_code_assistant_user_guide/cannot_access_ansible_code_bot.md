# 8. Troubleshooting
## 8.4. Troubleshooting Ansible code bot errors
### 8.4.1. Cannot access Ansible code bot




After you install Ansible code bot and attempt to log in, you receive the following error message:

`Your organization does not have a valid Red Hat Ansible Lightspeed subscription`

After you install Ansible code bot, you are redirected to a page that shows an active subscription status, as shown in the following image:


<span id="idm140399988745328"></span>
**Figure 8.1. Ansible code bot login screen with an active subscription**

![Ansible code bot login screen with an active subscription](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant-2.x_latest-Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant_User_Guide-en-US/images/fda088caedb124480b7fc92dbd751962/code_bot_login_screen.png)




If the login screen displays an inactive subscription status, Ansible code bot does not scan your Git repositories. The error occurs because your organization does not have a valid Ansible Automation Platform subscription. To resolve this error, ensure that you are part of an organization that has a valid Red Hat Ansible Automation Platform subscription.

