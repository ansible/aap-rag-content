# 10. Authenticating in the API
## 10.3. OAuth 2 token authentication




OAuth (Open Authorization) is an open standard for token-based authentication and authorization. OAuth 2 authentication is commonly used when interacting with the automation controller API programmatically. Similar to Basic authentication, you are given an OAuth 2 token with each API request through the Authorization header. Unlike Basic authentication, OAuth 2 tokens have a configurable timeout and are scopable. Tokens have a configurable expiration time and can be easily revoked for one user or for the entire automation controller system by an administrator if needed. You can do this with the [revoke_oauth2_tokens](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication/gw-token-based-authentication#ref-controller-revoke-oauth2-token) management command, or by using the API as explained in [Revoke an access token](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication/gw-token-based-authentication#ref-controller-revoke-access-token) .

The different methods for obtaining OAuth2 access tokens in automation controller include the following:

- Personal access tokens (PAT)
- Application token: Password grant type
- Application token: Implicit grant type
- Application token: Authorization Code grant type


A user needs to create an OAuth 2 token in the API or in theAccess Management→OAuth Applicationstab of the platform gateway UI. For more information about creating tokens through the UI, see [Adding tokens](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication/gw-token-based-authentication#proc-controller-apps-create-tokens) .

For the purpose of this example, use the PAT method for creating a token in the API. After you create it, you can set the scope.

Note
You can configure the expiration time of the token system-wide. For more information, see [Configuring access to external applications with token-based authentication](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication/gw-token-based-authentication) .



Token authentication is best used for any programmatic use of the automation controller API, such as Python scripts or tools such as curl.

**Curl example**

```
curl -u user:password -k -X POST https://&lt;controller-host&gt;/api/v2/tokens/
```


This call returns JSON data with the following:

![API OAuth2 JSON](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Automation_execution_API_overview-en-US/images/cb31ed26ba3b04eb7bec60ec711189e6/api_oauth2_json_returned_token_value.png)


You can use the value of the `token` property to perform a `GET` request for an automation controller resource, such as Hosts:

```
curl -k -X POST \
-H “Content-Type: application/json”
-H “Authorization: Bearer &lt;oauth2-token-value&gt;” \
https://&lt;controller-host&gt;/api/v2/hosts/
```

You can also run a job by making a `POST` to the job template that you want to start:

```
curl -k -X POST \
-H "Authorization: Bearer &lt;oauth2-token-value&gt;" \
-H "Content-Type: application/json" \
--data '{"limit" : "ansible"}' \
https://&lt;controller-host&gt;/api/v2/job_templates/14/launch/
```

**Python example**

[awxkit](https://pypi.org/project/awxkit/) is an open source tool that makes it easy to use HTTP requests to access the automation controller API. You can have awxkit get a PAT on your behalf by using the awxkit login command. For more information, see [AWX Command Line Interface](https://docs.ansible.com/automation-controller/latest/html/controllercli/index.html) .


If you need to write custom requests, you can write a Python script by using Python library requests, such as the following example:

```
import requests
oauth2_token_value = 'y1Q8ye4hPvT61aQq63Da6N1C25jiA'   # your token value from controller
url = 'https://&lt;controller-host&gt;/api/v2/users/'
payload = {}
headers = {'Authorization': 'Bearer ' + oauth2_token_value,}

# makes request to controller user endpoint
response = requests.request('GET', url, headers=headers, data=payload,
allow_redirects=False, verify=False)

# prints json returned from controller with formatting
print(json.dumps(response.json(), indent=4, sort_keys=True))
```

**Additional resources**

For more information about obtaining OAuth2 access tokens and how to use OAuth 2 in the context of external applications, see [Configuring access to external applications with token-based authentication](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication/gw-token-based-authentication) .



<span id="enabling_external_users_to_create_oauth_2_tokens"></span>
#### Enabling external users to create OAuth 2 tokens


By default, external users such as those created by single sign-on are not able to generate OAuth tokens for security purposes.

**Procedure**

1. From the navigation panel, selectSettings→Platform gateway.
1. SelectEdit platform gateway settings.
1. Enable the option to **Allow external users to create OAuth2 tokens** .


