# Configure proxy support to manage network configuration
## Enable proxy support through a load balancer
### Configure a reverse proxy through a load balancer

A reverse proxy manages external requests, providing load balancing and security. To support this, add `HTTP_X_FORWARDED_FOR` to the **Remote Host Headers** in System Settings. This header identifies the client’s original IP address when connecting through a proxy or load balancer.

#### Procedure

1.  From the navigation panel, select Settings> (and then)Automation Execution> (and then)System.
2.  In the **Remote Host Headers** field, enter the following values:


```
[
"HTTP_X_FORWARDED_FOR",
"REMOTE_ADDR",
"REMOTE_HOST"
]
```

3.  Add the lines below to `/etc/tower/conf.d/custom.py` to ensure the application uses the correct headers:


```
USE_X_FORWARDED_PORT = True
USE_X_FORWARDED_HOST = True
```

4.  Click Save to save the settings.

