# 3. Configuring Ansible Automation Platform to use egress proxy
## 3.4. Enabling a configurable proxy environment for AWS inventory synchronization

To enable a configurable proxy environment for AWS inventory synchronization, you can manually edit the override configuration file or set the configuration in the platform UI:

1. Manually edit `/usr/lib/systemd/system/receptor.service.d/override.conf` and add the following `http_proxy` environment variables there:

http_proxy:<value>
https_proxy:<value>
proxy_username:<value>
Proxy_password:<value>

Or

2. To do this through the UI use the following procedure:

**Procedure**

1. From the navigation panel, select Settings → Automation Execution → Job.

2. Click Edit.

3. Add the variables to the **Extra Environment Variables** field

For example: *

"AWX_TASK_ENV": {
"no_proxy": "localhost,127.0.0.0/8,10.0.0.0/8",
"http_proxy": "http://proxy_host:3128/",
"https_proxy": "http://proxy_host:3128/"
},

