# 3. Configuring access to external applications with token-based authentication
## 3.2. Adding tokens
### 3.2.1. Application token functions




The `refresh` and `revoke` functions associated with tokens, for tokens at the `/o/` endpoints can currently only be carried out with application tokens.

#### 3.2.1.1. Refresh an existing access token




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
-d "grant_type=refresh_token&amp;refresh_token=AL0NK9TTpv0qp54dGbC4VUZtsZ9r8z" \
-u "gwSPoasWSdNkMDtBN3Hu2WYQpPWCO9SwUEsKK22l:fI6ZpfocHYBGfm1tP92r0yIgCyfRdDQt0Tos9L8a4fNsJjQQMwp9569eIaUBsaVDgt2eiwOGe0bg5m5vCSstClZmtdy359RVx2rQK5YlIWyPlrolpt2LEpVeKXWaiybo" \
http://&lt;gateway&gt;/o/token/ -i
```

Where `refresh_token` is provided by `refresh_token` field of the preceding access token.

The authentication information is of format `&lt;client_id&gt;:&lt;client_secret&gt;` , where `client_id` and `client_secret` are the corresponding fields of the underlying related application of the access token.

Note
The special OAuth 2 endpoints only support using the `x-www-form-urlencoded`  **Content-type** , so as a result, none of the `/o/*` endpoints accept `application/json` .



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

#### 3.2.1.2. Revoke an access token




You can revoke an access token by deleting the token in the platform UI, or by using the `/o/revoke-token/` endpoint.

Revoking an access token by this method is the same as deleting the token resource object, but it enables you to delete a token by providing its token value, and the associated `client_id` (and `client_secret` if the application is `confidential` ). For example:

```
curl -X POST -d "token=rQONsve372fQwuc2pn76k3IHDCYpi7" \
-u "gwSPoasWSdNkMDtBN3Hu2WYQpPWCO9SwUEsKK22l:fI6ZpfocHYBGfm1tP92r0yIgCyfRdDQt0Tos9L8a4fNsJjQQMwp9569eIaUBsaVDgt2eiwOGe0bg5m5vCSstClZmtdy359RVx2rQK5YlIWyPlrolpt2LEpVeKXWaiybo" \
http://&lt;gateway&gt;/o/revoke_token/ -i
```

Note
- The special OAuth 2 endpoints only support using the `    x-www-form-urlencoded`  **Content-type** , so as a result, none of the `    /o/*` endpoints accept `    application/json` .
- The **Allow External Users to Create Oauth2 Tokens** ( `    ALLOW_OAUTH2_FOR_EXTERNAL_USERS` in the API) setting is disabled by default. External users refer to users authenticated externally with a service such as LDAP, or any of the other SSO services. This setting ensures external users cannot create their own tokens. If you enable then disable it, any tokens created by external users in the meantime will still exist, and are not automatically revoked. This setting can be configured from theSettings→Platform gatewaymenu.




Alternatively, to revoke OAuth2 tokens, you can use the `manage` utility, see [Revoke oauth2 tokens](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#ref-controller-revoke-oauth2-token) .

On success, a response of `200 OK` is displayed. Verify the deletion by checking whether the token is present in the `api/gateway/v1/tokens/` endpoint.

