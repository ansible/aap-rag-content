# Create a new application

When integrating an external web application with Ansible Automation Platform, the web application might need to create OAuth2 tokens on behalf of users of the web application.

## About this task

Creating an application with the Authorization Code grant type is the preferred way to do this for the following reasons:

- External applications can obtain a token for users, using their credentials.
- Compartmentalized tokens issued for a particular application, enables those tokens to be easily managed. For example, revoking all tokens associated with that application.

## Procedure

1.  From the navigation panel, select Access Management> (and then)OAuth Applications.
2.  Click Create OAuth application. The **Create Application** page opens.
3.  Enter the following details:


Name
(required) Enter a name for the application you want to create.

URL
(optional) Enter the URL of the external application. This link is added to the navigation panel for easy access. This setting is currently offered as a Technology Preview only.

Description
(optional) Include a short description for your application.

Organization
(required) Select an organization with which this application is associated.

Authorization grant type
(required) Select one of the grant types to use for the user to get tokens for this application. For more information, see [Application functions](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_token_based_authentication#ref-gw-application-functions "Several OAuth 2 utilities are available for authorization, token refresh, and revoke. You can specify the following grant types when creating an application:") for more information about grant types.

Client Type
(required) Select the level of security of the client device.

Redirect URIS
Provide a list of allowed URIs, separated by spaces. You need this if you specified the grant type to be **Authorization code**.

4.  Click Create OAuth application, or click Cancel to abandon your changes. The **Client ID** and **Client Secret** display in a window. This will be the only time the client secret will be shown.

Note:
The **Client Secret** is only created when the **Client type** is set to **Confidential**.

5.  Click the copy icon and save the client ID and client secret to integrate an external application with Ansible Automation Platform.

## Associate tokens with applications

You can view a list of users that have tokens to access an application by selecting the **Tokens** tab in the **OAuth Applications** details page.

### About this task

Note:

You can only create OAuth 2 Tokens for your own user, which means you can only configure or view tokens from your own user profile.

When authentication tokens have been configured, you can select the application to which the token is associated and the level of access that the token has.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Users.
2.  Select the username for your user profile to configure OAuth 2 tokens.
3.  Select the **Tokens** tab. When no tokens are present, the **Tokens** screen prompts you to add them.

4.  Click Create token to open the **Create Token** window.
5.  Enter the following details:


Application
Enter the name of the application with which you want to associate your token. Alternatively, you can search for it by clicking Browse. This opens a separate window that enables you to choose from the available options. Select **Name** from the filter list to filter by name if the list is extensive.

Note:
To create a Personal Access Token (PAT) that is not linked to any application, leave the Application field blank.

Description
(optional) Provide a short description for your token.

Scope
(required) Specify the level of access you want this token to have. The scope of an OAuth 2 token can be set as one of the following:

- **Write**: Allows requests sent with this token to add, edit and delete resources in the system.
- **Read**: Limits actions to read only. Note that the write scope includes read scope.

6.  Click Create token, or click Cancel to abandon your changes. The Token information is displayed with **Token** and **Refresh Token** information, and the expiration date of the token. This will be the only time the token and refresh token will be shown. You can view the token association and token information from the list view.

7.  Click the copy icon and save the token and refresh token for future use.

### Results

You can verify that the application now shows the user with the appropriate token by using the **Tokens** tab on the Applications details page.

1. From the navigation panel, select Access Management> (and then)OAuth Applications.

2. Select the application you want to verify from the **Applications** list view.

3. Select the **Tokens** tab. Your token should be displayed in the list of tokens associated with the application you chose.

## Application token functions

The `refresh` and `revoke` functions associated with tokens, for tokens at the `/o/` endpoints can currently only be carried out with application tokens.

## Refresh an existing access token

The following example shows an existing access token with a refresh token provided:

```
{
"id": 35,
"type": "access_token",
...
"user": 1,
"token": "omMFLk7UKpB36WN2Qma9H3gbwEBSOc",
"refresh_token": "AL0NK9TTpv0qp54dGbC4VUZtsZ9r8z",
"application": 6,
"expires": "2017-12-06T03:46:17.087022Z",
"scope": "read write"
}
```
The `/o/token/` endpoint is used for refreshing the access token:

```
curl -X POST \
-d "grant_type=refresh_token&refresh_token=AL0NK9TTpv0qp54dGbC4VUZtsZ9r8z" \
-u "gwSPoasWSdNkMDtBN3Hu2WYQpPWCO9SwUEsKK22l:fI6ZpfocHYBGfm1tP92r0yIgCyfRdDQt0Tos9L8a4fNsJjQQMwp9569eIaUBsaVDgt2eiwOGe0bg5m5vCSstClZmtdy359RVx2rQK5YlIWyPlrolpt2LEpVeKXWaiybo" \
http://<gateway>/o/token/ -i
```
Where `refresh_token` is provided by `refresh_token` field of the preceding access token.

The authentication information is of format `<client_id>:<client_secret>`, where `client_id` and `client_secret` are the corresponding fields of the underlying related application of the access token.

Note:

The special OAuth 2 endpoints only support using the `x-www-form-urlencoded`**Content-type**, so as a result, none of the `/o/*` endpoints accept `application/json`.

On success, a response displays in JSON format containing the new (refreshed) access token with the same scope information as the previous one:

```
HTTP/1.1 200 OK
Server: nginx/1.12.2
Date: Tue, 05 Dec 2017 17:54:06 GMT
Content-Type: application/json
Content-Length: 169
Connection: keep-alive
Content-Language: en
Vary: Accept-Language, Cookie
Pragma: no-cache
Cache-Control: no-store
Strict-Transport-Security: max-age=15768000

{"access_token": "NDInWxGJI4iZgqpsreujjbvzCfJqgR", "token_type": "Bearer", "expires_in": 315360000000, "refresh_token": "DqOrmz8bx3srlHkZNKmDpqA86bnQkT", "scope": "read write"}
```
The refresh operation replaces the existing token by deleting the original and then immediately creating a new token with the same scope and related application as the original one.

Verify that the new token is present and the old one is deleted in the `api/gateway/v1/tokens/` endpoint.

## Revoke an access token

You can revoke an access token by deleting the token in the platform UI, or by using the `/o/revoke-token/` endpoint.

Revoking an access token by this method is the same as deleting the token resource object, but it enables you to delete a token by providing its token value, and the associated `client_id` (and `client_secret` if the application is `confidential`). For example:

```
curl -X POST -d "token=rQONsve372fQwuc2pn76k3IHDCYpi7" \
-u "gwSPoasWSdNkMDtBN3Hu2WYQpPWCO9SwUEsKK22l:fI6ZpfocHYBGfm1tP92r0yIgCyfRdDQt0Tos9L8a4fNsJjQQMwp9569eIaUBsaVDgt2eiwOGe0bg5m5vCSstClZmtdy359RVx2rQK5YlIWyPlrolpt2LEpVeKXWaiybo" \
http://<gateway>/o/revoke_token/ -i
```


Note:

- The special OAuth 2 endpoints only support using the `x-www-form-urlencoded`**Content-type**, so as a result, none of the `/o/*` endpoints accept `application/json`.
- The **Allow External Users to Create Oauth2 Tokens** (`ALLOW_OAUTH2_FOR_EXTERNAL_USERS` in the API) setting is disabled by default. External users refer to users authenticated externally with a service such as LDAP, or any of the other SSO services. This setting ensures external users cannot create their own tokens. If you enable then disable it, any tokens created by external users in the meantime will still exist, and are not automatically revoked. This setting can be configured from the Settings> (and then)Platform gateway menu.

You can also revoke OAuth2 tokens by using the `manage` utility, see [Revoke oauth2 tokens](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-ref_controller_token_session_management#ref-controller-revoke-oauth2-token "Use this command to revoke OAuth2 tokens, both application tokens and personal access tokens (PAT). It revokes all application tokens (but not their associated refresh tokens), and revokes all personal access tokens. However, you can also specify a user for whom to revoke all tokens.").

On success, a response of `200 OK` is displayed. Verify the deletion by checking whether the token is present in the `api/gateway/v1/tokens/` endpoint.
