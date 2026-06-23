# Configure proxy servers for egress traffic
## Configure component-level proxy settings

After using the RPM installation program, you must configure automation controller to use egress proxy.

### About this task

Note:

This is not required for containerized installers because Podman uses system configured proxy and redirects all the container traffic to the proxy.

For automation controller, set the `AWX_TASK_ENV` variable in `/api/v2/settings/`. To do this through the UI use the following procedure:

### Procedure

1.  From the navigation panel, select Settings> (and then)Automation Execution> (and then)Job.
2.  Click Edit.
3.  Add the variables to the **Extra Environment Variables** field
and set:

```
"AWX_TASK_ENV": {
"http_proxy": "http://external-proxy_0:3128",
"https_proxy": "http://external-proxy_0:3128",
"no_proxy": "localhost,127.0.0.0/8"
}
```

