# Configure proxy support to manage network configuration
## Enable proxy support through a load balancer

A proxy server acts as an intermediary for requests from clients seeking resources from other servers. There are two types of proxy servers: forward proxies and reverse proxies.

### About this task

A forward proxy deals with client traffic, regulating and securing it. To provide proxy server support, automation controller handles proxied requests (such as ALB, NLB , HAProxy, Squid, Nginx and tinyproxy in front of automation controller) using the **REMOTE_HOST_HEADERS** list variable in the automation controller settings. By default, **REMOTE_HOST_HEADERS** is set to `["REMOTE_ADDR", "REMOTE_HOST"]`.

To enable proxy server support, edit the **REMOTE_HOST_HEADERS** field in the settings page for your automation controller:

### Procedure

1.  From the navigation panel, select Settings> (and then)Automation Execution> (and then)System.
2.  Click Edit
3.  In the **Remote Host Headers** field, enter the following values:


```
[
"HTTP_X_FORWARDED_FOR",
"REMOTE_ADDR",
"REMOTE_HOST"
]
```

4.  Click Save to save your settings.

### Results

Automation controller determines the remote host’s IP address by searching through the list of headers in **Remote Host Headers** until the first IP address is located.

