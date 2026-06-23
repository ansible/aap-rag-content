# Create an OAuth application
## Generate an API token for Ansible Automation Platform authentication

You must create an API token in Ansible Automation Platform. The token is used in an OpenShift secret for Ansible Automation Platform authentication.

### Procedure

1.  Log in to your instance of Ansible Automation Platform as a user with Ansible Automation Platform administrator privileges.
2.  Navigate to Access Management> (and then)API Tokens to display the API Tokens page.
3.  Click Create API Token.
4.  Add a description and select your OAuth application.
5.  In the Scope menu, select `Write`.

![Create API Token dialog showing the Scope set to Write](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/self-service-generate-oauth-token.png)

6.  Click Create Token to generate the token.
7.  Save the new token.
The token is used in an OpenShift secret that is fetched by the Helm chart.
