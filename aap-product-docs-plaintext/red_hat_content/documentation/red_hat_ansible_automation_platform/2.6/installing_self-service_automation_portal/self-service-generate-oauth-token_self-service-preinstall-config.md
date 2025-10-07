# 3. Pre-installation configuration
## 3.4. Generating a token for Ansible Automation Platform admin user authentication




You must create a token in Ansible Automation Platform. The token is used in an OpenShift secret for Ansible Automation Platform authentication.

**Procedure**

1. Log in to your instance of Ansible Automation Platform as the `    admin` user.
1. Navigate toAccess Management→Users.
1. Select the `    admin` user.
1. Select the **Tokens** tab
1. ClickCreate Token.
1. Select your OAuth application. In the **Scope** menu, select `    Read` .

![Create OAuth token](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Installing_self-service_automation_portal-en-US/images/c8c80a59e8a0c3ea8c7184c7a7eb243f/self-service-generate-oauth-token.png)



1. ClickCreate Tokento generate the token.
1. Save the new token.

The token is used in an OpenShift secret that is fetched by the Helm chart.




