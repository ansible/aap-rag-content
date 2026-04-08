# 1. Red Hat Certified, validated, and Ansible Galaxy content in automation hub
## 1.1. Configuring remote repositories for content syncing
### 1.1.5. Revoking a token




To comply with security policies, you might occasionally need to revoke and regenerate a token.

Important
Using the command below will revoke all of your previously-generated offline tokens.



**Procedure**

1. Run the following command to revoke the token:


```
curl -X POST https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/revoke \      -d client_id="cloud-services" \      -d token="${REFRESH_TOKEN}"
```


1. To regenerate a token, follow the appropriate procedure in [Token management](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/managing_automation_content/managing-cert-valid-content#token-management-hub_cloud-sync) .


