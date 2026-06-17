+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/configure-assembly_configuring_proxy_support"
template = "docs/aem-title.html"
title = "Configure proxy support to manage network configuration - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/configure-configure_a_proxy_to_communicate_with_external_systems/", "Configure a proxy to communicate with external systems"]]
category = "Configure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/configure-assembly_configuring_proxy_support/aem-page/configure-assembly_configuring_proxy_support.html"
last_crumb = "Configure proxy support to manage network configuration"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Configure proxy support to manage network configuration"
oversized = "false"
page_slug = "configure-assembly_configuring_proxy_support"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/configure-assembly_configuring_proxy_support"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/configure-assembly_configuring_proxy_support/toc/toc.json"
type = "aem-page"
+++

# Configure proxy support to manage network configuration

You can configure Red Hat Ansible Automation Platform to communicate with traffic by using a proxy. Proxy servers act as an intermediary for requests from clients seeking resources from other servers.

A client connects to the proxy server, requesting some service or available resource from a different server, and the proxy server evaluates the request as a way to simplify and control its complexity. The following sections describe the supported proxy configurations and how to set them up.

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

### Configure known proxies

Learn how to configure a list of known proxies for your automation controller, add the proxy IP addresses to the **Proxy IP Allowed List** field in the System Settings page.

#### Procedure

1.  From the navigation panel, select Settings> (and then)Automation Execution> (and then)System.
2.  In the **Proxy IP Allowed List** field, enter IP addresses that are permitted to connect to your automation controller, using the syntax in the following example:
       **Example Proxy IP Allowed List**

```
[
  "example1.proxy.com:8080",
  "example2.proxy.com:8080"
]
```
  Important:

  - **Proxy IP Allowed List** requires proxies in the list are properly sanitizing header input and correctly setting an `X-Forwarded-For` value equal to the real source IP of the client. Automation controller can rely on the IP addresses and hostnames in **Proxy IP Allowed List** to provide non-spoofed values for `X-Forwarded-For`.
  - Do not configure `HTTP_X_FORWARDED_FOR` as an item in **Remote Host Headers** unless **all** of the following conditions are satisfied:
    * You are using a proxied environment with ssl termination;
    * The proxy provides sanitization or validation of the `X-Forwarded-For` header to prevent client spoofing;
    * `/etc/tower/conf.d/remote_host_headers.py` defines `PROXY_IP_ALLOWED_LIST` that contains only the originating IP addresses of trusted proxies or load balancers.

3.  Click Save to save the settings.

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

### Enable sticky sessions for automation hub

By default, an application load balancer routes each request independently to a registered target based on the chosen load balancing algorithm.

To avoid authentication errors when running multiple instances of automation hub behind a load balancer, you must enable sticky sessions. Enabling sticky sessions sets a custom application cookie that matches the cookie configured on the load balancer to enable stickiness. This custom cookie can include any of the cookie attributes required by the application.
