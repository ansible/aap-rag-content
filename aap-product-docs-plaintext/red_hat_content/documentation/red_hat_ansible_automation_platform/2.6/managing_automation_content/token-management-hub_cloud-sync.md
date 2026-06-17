# 1. Red Hat Certified, validated, and Ansible Galaxy content in automation hub
## 1.1. Configuring remote repositories for content syncing
### 1.1.1. Token management in automation hub

You must create an API token before you can upload or download collections. The automation hub API token authenticates your `ansible-galaxy` client to the Red Hat automation hub server.

Note

Automation hub does not support basic authentication or authenticating through service accounts. You must authenticate using token management.

Your method for creating the API token differs according to the type of automation hub that you are using:

- Automation hub uses offline token management. See [Creating the offline token in automation hub](#proc-create-api-token_cloud-sync "1.1.2.&nbsp;Creating the offline token in automation hub").
- Private automation hub uses API token management. See [Creating the API token in private automation hub](#proc-create-api-token-pah_cloud-sync "1.1.3.&nbsp;Creating the API token in private automation hub").
- If you are using Keycloak to authenticate your private automation hub, follow the procedure for [Creating the offline token in automation hub](#proc-create-api-token_cloud-sync "1.1.2.&nbsp;Creating the offline token in automation hub").

