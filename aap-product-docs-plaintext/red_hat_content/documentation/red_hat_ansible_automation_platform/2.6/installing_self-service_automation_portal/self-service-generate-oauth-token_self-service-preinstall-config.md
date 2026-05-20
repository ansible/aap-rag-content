# 3. Pre-installation configuration
## 3.4. Generate an API token for Ansible Automation Platform authentication

You must create an API token in Ansible Automation Platform. The token is used in an OpenShift secret for Ansible Automation Platform authentication.

**Procedure**

1. Log in to your instance of Ansible Automation Platform as a user with Ansible Automation Platform administrator privileges.

2. Navigate to Access Management → API Tokens to display the **API Tokens** page.

3. Click Create API Token.

4. Add a description and select your OAuth application.

5. In the **Scope** menu, select `Write`.


![Create API Token dialog showing the Scope set to Write](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Installing_self-service_automation_portal-en-US/images/7207c1dcccbc007a2f3fb9f956c34db6/self-service-generate-oauth-token.png)

6. Click Create Token to generate the token.

7. Save the new token.

The token is used in an OpenShift secret that is fetched by the Helm chart.

