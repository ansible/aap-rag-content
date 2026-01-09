# 1. Red Hat Certified, validated, and Ansible Galaxy content in automation hub
## 1.1. Configuring remote repositories for content syncing
### 1.1.1. Token management in automation hub




You must create an API token before you can upload or download collections. The automation hub API token authenticates your `ansible-galaxy` client to the Red Hat automation hub server.

Note
Automation hub does not support basic authentication or authenticating through service accounts. You must authenticate using token management.



Your method for creating the API token differs according to the type of automation hub that you are using:

- Automation hub uses offline token management. See [Creating the offline token in automation hub](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_automation_content/index#proc-create-api-token_cloud-sync) .
- Private automation hub uses API token management. See [Creating the API token in private automation hub](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_automation_content/index#proc-create-api-token-pah_cloud-sync) .
- If you are using Keycloak to authenticate your private automation hub, follow the procedure for [Creating the offline token in automation hub](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_automation_content/index#proc-create-api-token_cloud-sync) .


