# 10. Authenticating in the API
## 10.1. Using session authentication




You can use session authentication when logging in directly to the automation controller’s API or UI to manually create resources, such as inventories, projects, and job templates and start jobs in the browser.

With this method, you can remain logged in for a prolonged period of time, not just for that HTTP request. For example, when browsing the API or UI in a browser such as Chrome or Mozilla Firefox. When you log in, a session cookie is created, this means that you can remain logged in when navigating to different pages within automation controller.

The following image represents the communication that occurs between the client and server in a session:

![Session authentication architecture](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Automation_execution_API_overview-en-US/images/acd897bb1e8827242df14583c242d699/session-auth-architecture.png)


Use the curl tool to see the activity that occurs when you log in to automation controller.

**Procedure**

1. Use `    GET` to go to the `    /api/login/` endpoint to get the `    csrftoken` cookie:


```
$ curl -k -c - https://&lt;gateway server name&gt;/api/gateway/v1/login/        $YOUR_AAP_URL FALSE / TRUE 1780539778 csrftoken GODXonA5LyV1uAs8zvcD2k12DQJC74oB
```


1. Extract the `    csrftoken` value from the cookie returned in the first step.
1.  `    POST` to the `    /api/login/` endpoint with username, password, and `    X-CSRFToken=&lt;token-value&gt;` :


```
curl -X POST -H 'Content-Type: application/x-www-form-urlencoded' \        --referer https://&lt;gateway server name&gt;/api/gateway/v1/login/ \        -H 'X-CSRFToken: &lt;token-value&gt;' \        --data 'username=admin&amp;password=$YOUR_ADMIN_PASSWORD' \        --cookie 'csrftoken=GODXonA5LyV1uAs8zvcD2k12DQJC74oB' \        https://&lt;gateway server name&gt;/api/gateway/v1/login/ -k -D - -o /dev/null
```


1. Access and test the APIs that need authentication, for example `    /api/controller/v2/settings/all/` :

Note
All of this is done by automation controller when you log in to the UI or API in the browser, and you must only use it when authenticating in the browser. For programmatic integration with automation controller, see [OAuth2 token authentication](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/automation_execution_api_overview/index#controller-api-oauth2-token) .




```
$ curl -X GET -H 'Cookie: &lt;cookieID&gt;;' https://&lt;gateway server name&gt;/api/controller/v2/settings/all/ -k
```




**Verification**

The following shows a typical response:


```
Server: nginx
Date: &lt;current date&gt;
Content-Type: text/html; charset=utf-8
Content-Length: 0
Connection: keep-alive
Location: /accounts/profile/
X-API-Session-Cookie-Name: awx_sessionid
Expires: &lt;date&gt;
Cache-Control: max-age=0, no-cache, no-store, must-revalidate, private
Vary: Cookie, Accept-Language, Origin
Session-Timeout: 1800
Content-Language: en
X-API-Total-Time: 0.377s
X-API-Request-Id: 700826696425433fb0c8807cd40c00a0
Access-Control-Expose-Headers: X-API-Request-Id
Set-Cookie: userLoggedIn=true; Path=/
Set-Cookie: current_user=&lt;user cookie data&gt;; Path=/
Set-Cookie: csrftoken=&lt;csrftoken&gt;; Path=/; SameSite=Lax
Set-Cookie: awx_sessionid=&lt;your session id&gt;; expires=&lt;date&gt;; HttpOnly; Max-Age=1800; Path=/; SameSite=Lax
Strict-Transport-Security: max-age=15768000
```

When a user is successfully authenticated with this method, the server responds with a header called `X-API-Session-Cookie-Name` , indicating the configured name of the session cookie. The default value is `awx_session_id` which you can see later in the `Set-Cookie` headers.

Note
You can change the session expiration time by specifying it in the `SESSION_COOKIE_AGE` parameter.



