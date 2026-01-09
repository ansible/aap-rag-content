# 2. Configuring proxy support for Red Hat Ansible Automation Platform
## 2.1. Enabling proxy support through a load balancer




A proxy server acts as an intermediary for requests from clients seeking resources from other servers. There are two types of proxy servers: forward proxies and reverse proxies.

A forward proxy deals with client traffic, regulating and securing it. To provide proxy server support, automation controller handles proxied requests (such as ALB, NLB , HAProxy, Squid, Nginx and tinyproxy in front of automation controller) using the **REMOTE_HOST_HEADERS** list variable in the automation controller settings. By default, **REMOTE_HOST_HEADERS** is set to `["REMOTE_ADDR", "REMOTE_HOST"]` .

To enable proxy server support, edit the **REMOTE_HOST_HEADERS** field in the settings page for your automation controller:

**Procedure**

1. From the navigation panel, selectSettings→Automation Execution→System.
1. ClickEdit
1. In the **Remote Host Headers** field, enter the following values:


```
[      "HTTP_X_FORWARDED_FOR",      "REMOTE_ADDR",      "REMOTE_HOST"    ]
```


1. ClickSaveto save your settings.

Automation controller determines the remote host’s IP address by searching through the list of headers in **Remote Host Headers** until the first IP address is located.




