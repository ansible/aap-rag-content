# 6. Job templates
## 6.16. Provisioning Callbacks
### 6.16.2. Using REST manually to callback




To callback manually using REST:

**Procedure**

1. Examine the callback URL in the UI, in the form: https://<CONTROLLER_SERVER_NAME>/api/v2/job_templates/7/callback/


- The "7" in the sample URL is the job template ID in automation controller.

1. Ensure that the request from the host is a POST. The following is an example using `    curl` (all on a single line):


```
curl -k -i -H 'Content-Type:application/json' -XPOST -d '{"host_config_key": "redhat"}' \                      https://&lt;CONTROLLER_SERVER_NAME&gt;/api/v2/job_templates/7/callback/
```


1. Ensure that the requesting host is defined in your inventory for the callback to succeed.


**Verification**

Successful requests result in an entry on the **Jobs** tab, where you can view the results and history. You can access the callback by using REST, but the suggested method of using the callback is to use one of the example scripts that includes automation controller:


-  `    /usr/share/awx/request_tower_configuration.sh` (Linux/UNIX)
-  `    /usr/share/awx/request_tower_configuration.ps1` (Windows)


Their usage is described in the source code of the file by passing the `-h` flag, as the following shows:

```
./request_tower_configuration.sh -h
Usage: ./request_tower_configuration.sh &lt;options&gt;


Request server configuration from Ansible Tower.


OPTIONS:
-h      Show this message
-s      Controller server (e.g. https://ac.example.com) (required)
-k      Allow insecure SSL connections and transfers
-c      Host config key (required)
-t      Job template ID (required)
-e      Extra variables
```

This script can retry commands and is therefore a more robust way to use callbacks than a simple `curl` request. The script retries once per minute for up to ten minutes.

Note
This is an example script. Edit this script if you need more dynamic behavior when detecting failure scenarios, as any non-200 error code may not be a transient error requiring retry.



You can use callbacks with dynamic inventory in automation controller. For example, when pulling cloud inventory from one of the supported cloud providers. In these cases, along with setting **Update On Launch** , ensure that you configure an inventory cache timeout for the inventory source, to avoid hammering of your cloud’s API endpoints. Since the `request_tower_configuration.sh` script polls once per minute for up to ten minutes, a suggested cache invalidation time for inventory (configured on the inventory source itself) would be one or two minutes.

Running the `request_tower_configuration.sh` script from a cron job is not recommended, however, a suggested cron interval is every 30 minutes. Repeated configuration can be handled by scheduling automation controller so that the primary use of callbacks by most users is to enable a base image that is bootstrapped into the latest configuration when coming online. Running at first boot is best practice. First boot scripts are init scripts that typically self-delete, so you set up an init script that calls a copy of the `request_tower_configuration.sh` script and make that into an auto scaling image.

**Troubleshooting**

If automation controller fails to locate the host either by name or IP address in one of your defined inventories, the request is denied. When running a job template in this way, ensure that the host initiating the playbook run against itself is in the inventory. If the host is missing from the inventory, the job template fails with a **No Hosts Matched** type error message.


If your host is not in the inventory and **Update on Launch** is checked for the inventory group, automation controller attempts to update cloud based inventory sources before running the callback.

