# 1. Red Hat Certified, validated, and Ansible Galaxy content in automation hub
## 1.1. Configuring remote repositories for content syncing
### 1.1.4. Refreshing the offline token




Offline tokens expire after 30 days of inactivity. You can keep your offline token from expiring by refreshing it periodically.

Refreshing the offline token to keep it active is useful when an application performs an action on behalf of the user. For example, this allows the application to perform a routine data backup when the user is offline.

Note
If your offline token expires, you must [obtain a new one](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_automation_content/index#proc-create-api-token_cloud-sync) .



**Procedure**

- Run the following command to refresh the offline token:


```
curl https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token -d grant_type=refresh_token -d client_id="cloud-services" -d refresh_token="{{ user_token }}" --fail --silent --show-error --output /dev/null
```




