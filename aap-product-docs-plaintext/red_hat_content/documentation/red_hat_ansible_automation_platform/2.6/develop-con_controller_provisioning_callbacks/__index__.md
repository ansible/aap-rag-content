# Increase capacity through cloud bursting by provisioning callbacks

Provisioning Callbacks are a feature of automation controller that enable a host to start a playbook run against itself, rather than waiting for a user to launch a job to manage the host from the automation controller console.

Provisioning Callbacks are only used to run playbooks on the calling host and are meant for cloud bursting. Cloud bursting is a cloud computing configuration that enables a private cloud to access public cloud resources by "bursting" into a public cloud when computing demand spikes.

**Example**

New instances with a need for client to server communication for configuration, such as transmitting an authorization key, not to run a job against another host. This provides for automatically configuring the following:

- A system after it has been provisioned by another system (such as AWS auto-scaling, or an operating system provisioning system such as Kickstart or preseed).
- Launching a job programmatically without invoking the automation controller API directly.


The job template launched only runs against the host requesting the provisioning.

This is often accessed with a firstboot type script or from `cron`.

## Enable Provisioning Callbacks

Use the following procedure to enable provisioning callbacks for a job template.

### Procedure

To enable callbacks, check the **Provisioning callback** option in the job template. This displays **Provisioning callback details** for the job template.

Note:

If you intend to use automation controller’s provisioning callback feature with a dynamic inventory, set **Update on Launch** for the inventory group used in the job template.

Callbacks also require a host config key, to ensure that foreign hosts with the URL cannot request configuration. Give a custom value for the **Host config key**. The host key can be reused across many hosts to apply this job template against multiple hosts. If you want to control what hosts are able to request configuration, you can change the key can at any time.

## Use REST manually to callback

You can use the REST API to trigger automation controller callbacks manually.

### Procedure

1.  Examine the callback URL in the UI, in the form: https://<CONTROLLER_SERVER_NAME>/api/v2/job_templates/7/callback/

- The "7" in the sample URL is the job template ID in automation controller.

2.  Ensure that the request from the host is a POST. The following is an example using `curl` (all on a single line):


```
curl -k -i -H 'Content-Type:application/json' -XPOST -d '{"host_config_key": "redhat"}' \
https://<CONTROLLER_SERVER_NAME>/api/v2/job_templates/7/callback/
```

3.  Ensure that the requesting host is defined in your inventory for the callback to succeed.

### Results

Successful requests result in an entry on the **Jobs** tab, where you can view the results and history. You can access the callback by using REST, but the suggested method of using the callback is to use one of the example scripts that includes automation controller:

- `/usr/share/awx/request_tower_configuration.sh` (Linux/UNIX)
- `/usr/share/awx/request_tower_configuration.ps1` (Windows)


Their usage is described in the source code of the file by passing the `-h` flag, as the following shows:

```
./request_tower_configuration.sh -h
Usage: ./request_tower_configuration.sh <options>


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

Note:

This is an example script. Edit this script if you need more dynamic behavior when detecting failure scenarios, as any non-200 error code might not be a transient error requiring retry.

You can use callbacks with dynamic inventory in automation controller. For example, when pulling cloud inventory from one of the supported cloud providers. In these cases, along with setting **Update On Launch**, ensure that you configure an inventory cache timeout for the inventory source, to avoid hammering of your cloud’s API endpoints. Since the `request_tower_configuration.sh` script polls once per minute for up to ten minutes, a suggested cache invalidation time for inventory (configured on the inventory source itself) would be one or two minutes.

Running the `request_tower_configuration.sh` script from a cron job is not recommended, however, a suggested cron interval is every 30 minutes. Repeated configuration can be handled by scheduling automation controller so that the primary use of callbacks by most users is to enable a base image that is bootstrapped into the latest configuration when coming online. Running at first boot is best practice. First boot scripts are init scripts that typically self-delete, so you set up an init script that calls a copy of the `request_tower_configuration.sh` script and make that into an auto scaling image.

If automation controller fails to locate the host either by name or IP address in one of your defined inventories, the request is denied. When running a job template in this way, ensure that the host initiating the playbook run against itself is in the inventory. If the host is missing from the inventory, the job template fails with a **No Hosts Matched** type error message.

If your host is not in the inventory and **Update on Launch** is checked for the inventory group, automation controller attempts to update cloud based inventory sources before running the callback.

## Pass extra variables to Provisioning Callbacks

You can pass `extra_vars` in Provisioning Callbacks the same way you can in a regular job template. To pass `extra_vars`, the data sent must be part of the body of the POST as application or JSON, as the content type.

### Procedure

Pass extra variables by using one of these methods:

- Use the following JSON format as an example when adding your own `extra_vars` to be passed:

```
'{"extra_vars": {"variable1":"value1","variable2":"value2",...}}'
```

- Pass extra variables to the job template call using `curl`:

```
root@localhost:~$ curl -f -H 'Content-Type: application/json' -XPOST \
-d '{"host_config_key": "redhat", "extra_vars": "{\"foo\": \"bar\"}"}' \
https://<CONTROLLER_SERVER_NAME>/api/v2/job_templates/7/callback
```
