# Use session authentication

You can use session authentication when logging in to the platform gateway API or UI to manually create resources, such as inventories, projects, and job templates, and start jobs in the browser.

## About this task

With this method, you can remain logged in for a prolonged period of time, not just for that HTTP request. For example, when browsing the API or UI in a browser such as Chrome or Mozilla Firefox. When you log in, a session cookie is created. You can remain logged in when navigating to different pages across the platform.

The following image represents the communication that occurs between the client and server in a session:


![Session authentication architecture](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/session-auth-architecture.png)


Use the curl tool to see the activity that occurs when you log in through platform gateway.

## Procedure

1.  Use `GET` to go to the `/api/login/` endpoint to get the `csrftoken` cookie:


```
$ curl -k -c - https://<gateway server name>/api/gateway/v1/login/

$YOUR_AAP_URL FALSE / TRUE 1780539778 csrftoken GODXonA5LyV1uAs8zvcD2k12DQJC74oB
```

2.  Extract the `csrftoken` value from the cookie returned in the first step.
3.  `POST` to the `/api/login/` endpoint with username, password, and `X-CSRFToken=<token-value>`:


```
curl -X POST -H 'Content-Type: application/x-www-form-urlencoded' \

--referer https://<gateway server name>/api/gateway/v1/login/ \

-H 'X-CSRFToken: <token-value>' \

--data 'username=admin&password=$YOUR_ADMIN_PASSWORD' \

--cookie 'csrftoken=GODXonA5LyV1uAs8zvcD2k12DQJC74oB' \

https://<gateway server name>/api/gateway/v1/login/ -k -D - -o /dev/null
```

4.  Access and test the APIs that need authentication, for example `/api/controller/v2/settings/all/`:

Note:
latform gateway performs all of these steps when you olog into the UI or API in the browser. You must use this procedure only when authenticating in the browser. For programmatic integration with platform gateway, see [OAuth2 token authentication](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-con_controller_api_oauth2_token#controller-api-oauth2-token "OAuth (Open Authorization) is an open standard for token-based authentication and authorization. OAuth 2 authentication is commonly used when interacting with the platform gateway API programmatically.").

```
$ curl -X GET -H 'Cookie: <cookieID>;' https://<gateway server name>/api/controller/v2/settings/all/ -k
```

## Results

The following shows a typical response:

```
Server: nginx
Date: <current date>
Content-Type: text/html; charset=utf-8
Content-Length: 0
Connection: keep-alive
Location: /accounts/profile/
X-API-Session-Cookie-Name: awx_sessionid
Expires: <date>
Cache-Control: max-age=0, no-cache, no-store, must-revalidate, private
Vary: Cookie, Accept-Language, Origin
Session-Timeout: 1800
Content-Language: en
X-API-Total-Time: 0.377s
X-API-Request-Id: 700826696425433fb0c8807cd40c00a0
Access-Control-Expose-Headers: X-API-Request-Id
Set-Cookie: userLoggedIn=true; Path=/
Set-Cookie: current_user=<user cookie data>; Path=/
Set-Cookie: csrftoken=<csrftoken>; Path=/; SameSite=Lax
Set-Cookie: awx_sessionid=<your session id>; expires=<date>; HttpOnly; Max-Age=1800; Path=/; SameSite=Lax
Strict-Transport-Security: max-age=15768000
```
When a user is successfully authenticated with this method, the server responds with a header called `X-API-Session-Cookie-Name`, indicating the configured name of the session cookie. The default value is `awx_session_id` which you can see later in the `Set-Cookie` headers.

Note:

You can change the session expiration time by specifying it in the `SESSION_COOKIE_AGE` parameter.
