# Configure automation hub tokens

You must authenticate your hub instance before you can upload or download collections.

Note:

Automation hub does not support basic authentication or authenticating through service accounts.

Your method for creating the API token differs according to the type of automation hub that you are using:

- Automation hub uses offline token management. See Creating the offline token in automation hub.
- Private automation hub uses API token management. See Creating the API token in private automation hub.
- If you are using Keycloak to authenticate your private automation hub, follow the procedure for Creating the offline token in automation hub.

## Create the offline token in automation hub

In automation hub, you can create an offline token using **Token management**. The offline token is a secret token used to protect your content, so be sure to store it in a secure location.

### About this task

Note:

Your offline token expires after 30 days of inactivity.

### Procedure

1.  Navigate to [Ansible Automation Platform on the Red Hat Hybrid Cloud Console](https://console.redhat.com/ansible/automation-hub/token/).
2.  From the navigation panel, select Automation Hub> (and then)Connect to Hub.
3.  Under **Offline token**, click Load Token.
4.  Click the Copy to clipboard icon to copy the offline token.
5.  Paste the token into a file and store in a secure location.

### What to do next

The offline token is now available for configuring automation hub as your default collections server or for uploading collections by using the `ansible-galaxy` command line tool.

## Refresh the offline token

Offline tokens expire after 30 days of inactivity. You can keep your offline token from expiring by refreshing it periodically.

### About this task

Refreshing the offline token to keep it active is useful when an application performs an action on behalf of the user. For example, this allows the application to perform a routine data backup when the user is offline.

Note:

If your offline token expires, you must obtain a new one.

### Procedure

Run the following command to refresh the offline token:

```
curl https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token -d grant_type=refresh_token -d client_id="cloud-services" -d refresh_token="{{ user_token }}" --fail --silent --show-error --output /dev/null
```

## Create the API token in private automation hub

In private automation hub, you can create an API token using API token management. The API token is a secret token used to protect your content, so be sure to store it in a secure location.

### Before you begin

- Valid subscription credentials for Red Hat Ansible Automation Platform.

### About this task

Note:

The API token does not expire.

### Procedure

1.  Log in to your private automation hub.
2.  From the navigation panel, select Automation Content> (and then)API token.
3.  Click Load Token.
4.  To copy the API token, click the Copy to clipboard icon.
5.  Paste the API token into a file and store in a secure location.

### What to do next

The API token is now available for configuring automation hub as your default collections server or uploading collections using the `ansible-galaxy` command line tool.
