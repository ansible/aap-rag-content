# 3. Configuring Ansible Automation Platform to use egress proxy
## 3.4. Enabling a configurable proxy environment for AWS inventory synchronization




To enable a configurable proxy environment for AWS inventory synchronization, you can manually edit the override configuration file or set the configuration in the platform UI:

1. Manually edit `    /usr/lib/systemd/system/receptor.service.d/override.conf` and add the following `    http_proxy` environment variables there:


```
http_proxy:&lt;value&gt;    https_proxy:&lt;value&gt;    proxy_username:&lt;value&gt;    Proxy_password:&lt;value&gt;
```

Or


1. To do this through the UI use the following procedure:


**Procedure**

1. From the navigation panel, selectSettings→Automation Execution→Job.
1. ClickEdit.
1. Add the variables to the **Extra Environment Variables** field

For example: *




```
"AWX_TASK_ENV": {
"no_proxy": "localhost,127.0.0.0/8,10.0.0.0/8",
"http_proxy": "http://proxy_host:3128/",
"https_proxy": "http://proxy_host:3128/"
},
```

