# 1. Red Hat Certified, validated, and Ansible Galaxy content in automation hub
## 1.1. Configuring Ansible automation hub remote repositories to synchronize content
### 1.1.1. Token management in automation hub




Before you can interact with automation hub by uploading or downloading collections, you must create an API token. The automation hub API token authenticates your `ansible-galaxy` client to the Red Hat automation hub server.

Note
Automation hub does not support basic authentication or authenticating through service accounts. You must authenticate using token management.



Your method for creating the API token differs according to the type of automation hub that you are using:

- Automation hub uses offline token management. See [Creating the offline token in automation hub](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_automation_content/index#proc-create-api-token_cloud-sync) .
- Private automation hub uses API token management. See [Creating the API token in private automation hub](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_automation_content/index#proc-create-api-token-pah_cloud-sync) .
- If you are using Keycloak to authenticate your private automation hub, follow the procedure for [Creating the offline token in automation hub](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_automation_content/index#proc-create-api-token_cloud-sync) .


#### 1.1.1.1. Creating the offline token in automation hub




In automation hub, you can create an offline token by using **Token management** . The offline token is a secret token used to protect your content.

**Procedure**

1. Navigate to [Ansible Automation Platform on the Red Hat Hybrid Cloud Console](https://console.redhat.com/ansible/automation-hub/token/) .
1. From the navigation panel, selectAutomation Hub→Connect to Hub.
1. Under **Offline token** , clickLoad Token.
1. Click theCopy to clipboardicon to copy the offline token.
1. Paste the API token into a file and store in a secure location.


Important
The offline token is a secret token used to protect your content. Store your token in a secure location.



The offline token is now available for configuring automation hub as your default collections server or for uploading collections by using the `ansible-galaxy` command line tool.

Note
Your offline token expires after 30 days of inactivity. For more on obtaining a new offline token, see [Keeping your offline token active](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_automation_content/index#con-offline-token-active_cloud-sync) .



#### 1.1.1.2. Creating the API token in private automation hub




In private automation hub, you can create an API token using API token management. The API token is a secret token used to protect your content.

**Prerequisites**

- Valid subscription credentials for Red Hat Ansible Automation Platform.


**Procedure**

1. Log in to your private automation hub.
1. From the navigation panel, selectAutomation Content→API token.
1. ClickLoad Token.
1. To copy the API token, click theCopy to clipboardicon.
1. Paste the API token into a file and store in a secure location.


Important
The API token is a secret token used to protect your content. Store your API token in a secure location.



The API token is now available for configuring automation hub as your default collections server or uploading collections using the `ansible-galaxy` command line tool.

Note
The API token does not expire.



#### 1.1.1.3. Keeping your offline token active




Offline tokens expire after 30 days of inactivity. You can keep your offline token from expiring by periodically refreshing your offline token.

Keeping an online token active is useful when an application performs an action on behalf of the user; for example, this allows the application to perform a routine data backup when the user is offline.

Note
If your offline token expires, you must [obtain a new one](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_automation_content/index#proc-create-api-token_cloud-sync) .



**Procedure**

- Run the following command to prevent your token from expiring:


```
curl https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token -d grant_type=refresh_token -d client_id="cloud-services" -d refresh_token="{{ user_token }}" --fail --silent --show-error --output /dev/null
```




