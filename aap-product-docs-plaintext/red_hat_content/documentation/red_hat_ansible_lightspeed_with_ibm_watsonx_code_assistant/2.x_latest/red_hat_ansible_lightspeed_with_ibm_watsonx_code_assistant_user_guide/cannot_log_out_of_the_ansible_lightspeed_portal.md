# 8. Troubleshooting
## 8.2. Troubleshooting Red Hat Ansible Lightspeed on-premise deployment errors
### 8.2.1. Cannot log out of the Ansible Lightspeed portal




After you log out from the Ansible Lightspeed portal, you are redirected to the automation controller API page instead of Ansible Lightspeed.

This error indicates that the logout redirect URI was not configured while setting up your Red Hat Ansible Lightspeed on-premise deployment. You must configure the logout redirect URI by adding the **LOGOUT_ALLOWED_HOSTS** entry to the YAML file.

