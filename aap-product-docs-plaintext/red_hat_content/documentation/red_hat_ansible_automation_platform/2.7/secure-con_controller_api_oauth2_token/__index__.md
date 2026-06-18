# OAuth 2 token authentication

OAuth (Open Authorization) is an open standard for token-based authentication and authorization. OAuth 2 authentication is commonly used when interacting with the platform gateway API programmatically.

You provide an OAuth 2 token with each API request through the Authorization header. Unlike Basic authentication, OAuth 2 tokens have a configurable timeout and are scopable. Tokens have a configurable expiration time and can be revoked for one user or for the entire platform gateway system by an administrator if needed. You can do this with the *revoke_oauth2_tokens* management command, or by using the API as explained in Revoke an access token.

The different methods for obtaining OAuth 2 access tokens in automation controller include the following:

- Personal access tokens (PAT)
- Application token: Password grant type
- Application token: Implicit grant type
- Application token: Authorization Code grant type


You can create an OAuth 2 token in the API or in the Access Management> (and then)OAuth Applications tab of the platform gateway UI.

For the purpose of this example, use the PAT method for creating a token in the API. After you create it, you can set the scope.

Note:

You can configure the expiration time of the token system-wide..

Token authentication is the recommended method for any programmatic use of the platform gateway API, such as Python scripts or tools such as curl.

**Curl example**

Create a token through the platform gateway tokens endpoint:

```
curl -u user:password -k -X POST https://<gateway server name>/api/gateway/v1/tokens/
```
This call returns JSON data with the following:


![API OAuth2 JSON](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/api-oauth2-json-returned-token-value.png)


You can use the value of the `token` property to perform a `GET` request for a resource, such as Hosts:

```
curl -k -X GET \
-H “Content-Type: application/json”
-H “Authorization: Bearer <oauth2-token-value>” \
https://<platform-host>/api/controller/v2/hosts/
```
You can also run a job by making a `POST` to the job template that you want to start:

```
curl -k -X POST \
-H "Authorization: Bearer <oauth2-token-value>" \
-H "Content-Type: application/json" \
--data '{"limit" : "ansible"}' \
https://<platform-host>/api/controller/v2/job_templates/14/launch/
```

## Enable external users to create OAuth 2 tokens

By default, external users such as those created by single sign-on are not able to generate OAuth tokens for security purposes.

### Procedure

1.  From the navigation panel, select Settings> (and then)Platform gateway.
2.  Select Edit platform gateway settings.
3.  Enable the option to **Allow external users to create OAuth2 tokens**.
