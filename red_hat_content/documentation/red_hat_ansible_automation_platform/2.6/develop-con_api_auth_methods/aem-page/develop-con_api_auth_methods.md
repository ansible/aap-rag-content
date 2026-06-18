+++
title = "Authenticate through the API - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-con_api_auth_methods"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_controller_api_tools/", "Use the REST API to browse, query, filter, and authenticate"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-con_api_auth_methods/aem-page/develop-con_api_auth_methods.html"
last_crumb = "Authenticate through the API"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Authenticate through the API"
oversized = "false"
page_slug = "develop-con_api_auth_methods"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/develop-con_api_auth_methods"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-con_api_auth_methods/toc/toc.json"
type = "aem-page"
+++

# Authenticate through the API

Ansible Automation Platform provides a visual dashboard for out-of-the-box control while providing a REST API to integrate with your other tools on a deeper level.

The platform supports several authentication methods to integrate automation into existing tools and processes. This ensures that the right people can access platform resources.

You can use the following authentication methods in the API:

## Use session authentication

You can use session authentication when logging in to the platform gateway API or UI to manually create resources, such as inventories, projects, and job templates, and start jobs in the browser.

### About this task

With this method, you can remain logged in for a prolonged period of time, not just for that HTTP request. For example, when browsing the API or UI in a browser such as Chrome or Mozilla Firefox. When you log in, a session cookie is created. You can remain logged in when navigating to different pages across the platform.

The following image represents the communication that occurs between the client and server in a session:


![Session authentication architecture](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/session-auth-architecture.png)  


Use the curl tool to see the activity that occurs when you log in through platform gateway.

### Procedure

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

### Results

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

## Basic authentication

Basic authentication is stateless. You must send the base64-encoded username and password along with each request through the Authorization header. You can use this method for API calls from curl requests, Python scripts, or individual requests to the API.

OAuth 2 token authentication through platform gateway is the recommended method for accessing the API.

The following is an example of basic authentication with curl:

```
# the --user flag adds this Authorization header for us
curl -X GET --user 'user:password' https://<gateway server name>/api/gateway/v1/tokens/ -k -L
```

## Disable basic authentication

You can disable basic authentication for security purposes.

### Procedure

1.  From the navigation panel, select Settings> (and then)Platform gateway.
2.  Click Edit platform gateway settings.
3.  Disable the option **Gateway basic auth enabled**.
4.  Click Save platform gateway settings.

## OAuth 2 token authentication

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


![API OAuth2 JSON](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/api-oauth2-json-returned-token-value.png)  


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

## Single sign-on authentication

Single sign-on (SSO) authentication methods are different from other methods because the authentication of the user happens external to platform gateway, such as Google SSO, Microsoft Azure SSO, SAML, or GitHub.

You can configure SSO authentication through platform gateway to integrate with a central identity provider in your organization. Once you have configured an SSO method, an option for that SSO is available on the login screen. If you select that option, the platform redirects you to the identity provider, for example GitHub, where you present your credentials. If the identity provider verifies you successfully, platform gateway creates a user linked to your GitHub user (if this is your first time logging in with this SSO method) and logs you in.
