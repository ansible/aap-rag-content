# 2. Configuring proxy support for Red Hat Ansible Automation Platform
## 2.3. Configuring a reverse proxy through a load balancer




A reverse proxy manages external requests to servers, offering load balancing and concealing server identities for added security. You can support a reverse proxy server configuration by adding `HTTP_X_FORWARDED_FOR` to the **Remote Host Headers** field in the Systems Settings. The `X-Forwarded-For` (XFF) HTTP header field identifies the originating IP address of a client connecting to a web server through an HTTP proxy or load balancer.

**Procedure**

1. From the navigation panel, selectSettings→Automation Execution→System.
1. In the **Remote Host Headers** field, enter the following values:


```
[      "HTTP_X_FORWARDED_FOR",      "REMOTE_ADDR",      "REMOTE_HOST"    ]
```


1. Add the lines below to `    /etc/tower/conf.d/custom.py` to ensure the application uses the correct headers:


```
USE_X_FORWARDED_PORT = True    USE_X_FORWARDED_HOST = True
```


1. ClickSaveto save the settings.


