# Configure access to external applications with tokens
## Get started with OAuth Applications
### Refresh an access token after expiration

You can use a refresh token to request a new access token after the original token expires.

#### About this task

The default expiration for OAuth2 access tokens is 31,536,000 seconds (1 year). You can configure this value in the `OAUTH2_PROVIDER` settings in `etc/ansible-automation-platform/gateway/settings.py`.

When an access token expires, use the original refresh token to request a new access token without re-authorizing.

#### Procedure

1.  Make a POST request to the `/o/token/` endpoint with your client credentials in the Authorization header:


```
curl -X POST \
-H "Authorization: Basic <base64(client_id:client_secret)>" \
-d "grant_type=refresh_token" \
-d "refresh_token=<your_refresh_token>" \
https://<platform_gateway>/o/token/
```

Replace `<base64(client_id:client_secret)>` with the Base64-encoded string of your application client ID and client secret, separated by a colon.

Replace `<your_refresh_token>` with the refresh token returned in the original token response.

Replace `<platform_gateway>` with the hostname of your platform gateway.

2.  Verify that the response includes a new `access_token` and `refresh_token`.
The server revokes the previous refresh token after use.

#### What to do next

Note:

Refresh tokens expire after approximately 30 days (2,628,000 seconds) by default. After the refresh token expires, you must complete a full re-authorization. You can configure this value with the `REFRESH_TOKEN_EXPIRE_SECONDS` setting in `OAUTH2_PROVIDER` in `/etc/ansible-automation-platform/gateway/settings.py`.
