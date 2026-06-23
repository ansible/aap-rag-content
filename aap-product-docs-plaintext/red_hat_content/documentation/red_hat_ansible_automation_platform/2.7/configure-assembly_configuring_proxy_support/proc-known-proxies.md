# Configure proxy support to manage network configuration
## Enable proxy support through a load balancer
### About known proxies

When automation controller is configured with `REMOTE_HOST_HEADERS = ['HTTP_X_FORWARDED_FOR', 'REMOTE_ADDR', 'REMOTE_HOST']`, it assumes that the value of `X-Forwarded-For` has originated from the load balancer sitting in front of automation controller.

#### About this task

If automation controller is reachable without use of the load balancer, or if the proxy does not validate the header, the value of `X-Forwarded-For` can be falsified to fake the originating IP addresses.

Using `HTTP_X_FORWARDED_FOR` in the `REMOTE_HOST_HEADERS` setting poses a vulnerability.

To avoid this, you can configure a list of known proxies that are allowed.

#### Procedure

1.  From the navigation panel, select Settings> (and then)Automation Execution> (and then)System.
2.  Enter a list of proxy IP addresses from which the service should trust custom remote header values in the **Proxy IP Allowed List** field. Note:
Load balancers and hosts that are not on the known proxies list result in a rejected request.

