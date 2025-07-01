# 3. Pre-installation configuration
## 3.2. Generating a token for user authentication




You must create a token in Ansible Automation Platform. The token is used in an OpenShift secret for Ansible Automation Platform authentication.

**Procedure**

1. Log in to your instance of Ansible Automation Platform as the `    admin` user.
1. Navigate toAccess Management→Users.
1. Select the `    admin` user.
1. Select the **Tokens** tab
1. Click **Create Token** .
1. Select your OAuth application. In the **Scope** menu, select `    Write` .

![Create OAuth token](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Installing_Ansible_Automation_Platform_self-service_technology_preview-en-US/images/c8c80a59e8a0c3ea8c7184c7a7eb243f/self-service-generate-oauth-token.png)



1. Click **Create Token** to generate the token.
1. Save the new token.

The token is used in an OpenShift secret that is fetched by the Helm chart.




