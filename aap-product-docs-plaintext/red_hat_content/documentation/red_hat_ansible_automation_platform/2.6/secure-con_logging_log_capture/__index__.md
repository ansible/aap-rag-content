# Best practices for setting up secure logging

Visibility and analytics are important pillars of Enterprise Security and Zero Trust architectures. Logging is key to capturing actions and auditing.

You can manage logging and auditing by using the built-in audit support described in the Auditing the system section of the Security hardening for Red Hat Enterprise Linux guide. Ansible Automation Platform’s built-in logging and activity stream logs all change within Red Hat Ansible Automation Platform and automation logs for auditing purposes.

Ansible Automation Platform and the underlying Red Hat Enterprise Linux systems should be configured to collect logging and auditing centrally, rather than reviewing it on the local system. Configure Ansible Automation Platform to use external logging to compile log records from multiple components within the Ansible Automation Platform server. The events occurring must be time-correlated to conduct accurate forensic analysis.

Another critical capability of logging is the ability to use cryptography to protect the integrity of log tools. Log data includes all information (for example, log records, log settings, and log reports) needed to successfully log information system activity. It is common for attackers to replace the log tools or inject code into the existing tools to hide or erase system activity from the logs. To address this risk, log tools must be cryptographically signed so that you can identify when the log tools have been modified, manipulated, or replaced. For example, one way to validate that the log tool(s) have not been modified, manipulated or replaced is to use a checksum hash against the tool file(s). This ensures the integrity of the tool(s) has not been compromised.

## Configure centralized logging

Configure centralized logging to collect all Ansible Automation Platform logs in a single location. Consolidating this data makes it easier to troubleshoot issues, detect tampering, and helps ensure the overall security and stability of your environment.

There are several additional benefits including:

- The data is sent in JSON format over a HTTP connection using minimal service-specific tweaks engineered in a custom handler or through an imported library. The types of data that are most useful to the controller are job fact data, job events/job runs, activity stream data, and log messages.
- Deeper insights into the automation process by analyzing logs from different parts of the infrastructure, including playbook execution details, task outcomes, and system events.
- Identifying performance bottlenecks and optimizing the Ansible playbooks by analyzing execution times and resource usage from the logs.
- Centralized logging helps meet compliance mandates by providing a single source of truth for auditing purposes.
- Third Party integration with a centralized log management platform like Splunk, Logstash, ElasticSearch, or Loggly to collect and analyze logs.


The logging aggregator service works with the following monitoring and data analysis systems:

- Splunk
- Loggly
- Sumologic
- Elastic stack (formerly ELK stack)

## Set up logging

To set up logging to any of the aggregator types for centralized logging follow these steps:

### Procedure

-  From the navigation panel, select Settings> (and then)Automation Execution> (and then)Logging.
-  On the **Logging settings** page, click Edit.
-  You can configure the following options:

* **Logging Aggregator**: Enter the hostname or IP address that you want to send logs to.
* **Logging Aggregator Port**: Specify the port for the aggregator if it requires one.  Note:
When the connection type is HTTPS, you can enter the hostname as a URL with a port number, after which, you are not required to enter the port again. However, TCP and UDP connections are determined by the hostname and port number combination, rather than URL. Therefore, in the case of a TCP or UDP connection, supply the port in the specified field. If a URL is entered in the **Logging Aggregator** field instead, its hostname portion is extracted as the hostname.

* **Logging Aggregator Type**: Click to select the aggregator service from the list:
* **Logging Aggregator Username**: Enter the username of the logging aggregator if required.
* **Logging Aggregator Password/Token**: Enter the password of the logging aggregator if required.
* **Loggers to Send Data to the Log Aggregator Form**: All four types of data are pre-populated by default. Click the tooltip ![Help](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/question-circle.png) icon next to the field for additional information on each data type. Delete the data types you do not want.
* **Cluster wide unique identifier**: Use this to uniquely identify instances.
* **Logging Aggregator Protocol**: Click to select a connection type (protocol) to communicate with the log aggregator. Subsequent options vary depending on the selected protocol.
* **TCP Connection Timeout**: Specify the connection timeout in seconds. This option is only applicable to HTTPS and TCP log aggregator protocols.
* **Logging Aggregator Level Threshold**: Select the level of severity you want the log handler to report.
* **Maximum number of messages that can be stored in the log action queue**:Defines how large the `rsyslog` action queue can grow in number of messages stored. This can have an impact on memory use. When the queue reaches 75% of this number, the queue starts writing to disk (`queue.highWatermark` in `rsyslog`). When it reaches 90%, `NOTICE`, `INFO`, and `DEBUG` messages start to be discarded (`queue.discardMark` with `queue.discardSeverity=5`).
* **Maximum disk persistence for rsyslogd action queuing (in GB)**: The amount of data to store (in gigabytes) if an `rsyslog` action takes time to process an incoming message (defaults to 1). Equivalent to the `rsyslogd queue.maxdiskspace` setting on the action (e.g. `omhttp`). It stores files in the directory specified by `LOG_AGGREGATOR_MAX_DISK_USAGE_PATH`.
* **File system location for rsyslogd disk persistence**: Location to persist logs that should be retried after an outage of the external log aggregator (defaults to `/var/lib/awx`). Equivalent to the `rsyslogd queue.spoolDirectory` setting.: Configure a specific error message. When the API encounters an issue with a request, it typically returns an HTTP error code in the 400 range along with an error. When this happens, an error message is generated in the log that follows the following pattern:
* **Log Format For API 4XX Errors:** When the API encounters an issue with a request, it typically returns an HTTP error code in the 400 range along with an error. When this happens, an error message is generated in the log that follows the following pattern: `' status {status_code} received by user {user_name} attempting to access {url_path} from {remote_addr} '`

-  You can set the following options:

* **Log System Tracking Facts Individually**: Click the tooltip ![Help](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/question-circle.png) icon for additional information, such as whether or not you want to turn it on, or leave it off by default.

-  Review your entries for your chosen logging aggregation.   * **Enable External Logging**: Select this checkbox if you want to send logs to an external log aggregator.
* **Enable/disable HTTPS certificate verification**: Certificate verification is enabled by default for the HTTPS log protocol. Select this checkbox if you want the log handler to verify the HTTPS certificate sent by the external log aggregator before establishing a connection.
* **Enable rsyslogd debugging**: Select this checkbox to enable high verbosity debugging for `rsyslogd`. Useful for debugging connection issues for external log aggregation.

-  Click Save or Cancel to abandon the changes.

## Configure LDAP logging

Enable debug logging for LDAP in the platform gateway settings to capture detailed authentication messages. Reviewing these logs ensures that you can effectively troubleshoot and resolve LDAP connection issues.

### Procedure

1.  Edit the gateway settings file:
1.  On Ansible Automation Platform 2.6 Containerized, the file is `~/aap/gateway/etc/settings.py` (as the user running the platform gateway container).
2.  On Ansible Automation Platform 2.6 RPM-based, the file is `/etc/ansible-automation-platform/gateway/settings.py`.

```
(...)
CACHES['fallback']['LOCATION'] = '/var/cache/ansible-automation-platform/gateway'

LOGGING['loggers']['aap']['level'] = 'INFO'
LOGGING['loggers']['ansible_base']['level'] = 'INFO'
LOGGING['loggers']['django_auth_ldap']['level'] = 'DEBUG'      ######      add this line

(...)
```

2.  Restart the platform gateway service or container:
1.  On Ansible Automation Platform 2.6 Containerized, restart the platform gateway service so that it restarts the platform gateway container:

Note:
Ensure that you run `` systemctl with the `--user` `` flag as follows:

+ `$ systemctl --user restart automation-gateway`

2.  On Ansible Automation Platform 2.6 RPM-based, use the `automation-gateway-service` command:
`# automation-gateway-service restart`

## Implement security control

Some of the following examples of meeting compliance requirements come from the US DoD *Security Technical Implementation Guide*, but go back to integrity and security best practices.

### About this task

Automation controller must use external log providers that can collect user activity logs in independent, protected repositories to prevent modification or repudiation. Automation controller must be configured to use external logging to compile log records from multiple components within the server. The events occurring must be time-correlated in order to conduct accurate forensic analysis. In addition, the correlation must meet certain tolerance criteria.

The following steps implement the security control:

### Procedure

1.  Log in to automation controller as an administrator.
2.  From the navigation panel, select Settings> (and then)Automation Execution> (and then)Logging.
3.  On the **Logging settings** page, click Edit.
4.  Set the following fields:

- Set **Logging Aggregator** to `Not configured`. This is the default.
- Set **Enable External Logging** to `On`.
- Set **Logging Aggregator Level Threshold** to DEBUG.
- Set **TCP Connection Timeout** to 5 (the default) or to the organizational timeout.
- Set **Enable/disable HTTPS certificate verification** to `On`.

5.  Click Save. Automation controller must allocate log record storage capacity and shut down by default upon log failure (unless availability is an overriding concern). It is critical that when a system is at risk of failing to process logs, it detects and takes action to mitigate the failure. Log processing failures include software/hardware errors, failures in the log capturing mechanisms, and log storage capacity being reached or exceeded. During a failure, the application server must be configured to shut down unless the application server is part of a high availability system. When availability is an overriding concern, other approved actions in response to a log failure are as follows:

6.  If the failure was caused by the lack of log record storage capacity, the application must continue generating log records if possible (automatically restarting the log service if necessary), overwriting the oldest log records in a first-in-first-out manner.
7.  If log records are sent to a centralized collection server and communication with this server is lost or the server fails, the application must queue log records locally until communication is restored or until the log records are retrieved manually. Upon restoration of the connection to the centralized collection server, action must be taken to synchronize the local log data with the collection server. The following steps implement the security control:

1.  Open a web browser and navigate to the logging API, `/api/v2/settings/logging/`
Ensure that you are authenticated as an automation controller administrator.

2.  In the **Content** section, modify the following values:

- `LOG_AGGREGATOR_ACTION_MAX_DISK_USAGE_GB` = organization-defined requirement for log buffering.
- `LOG_AGGREGATOR_MAX_DISK_USAGE_PATH` = `/var/lib/awx`

3.  Click PUT.

## Implement security control for each host

Restrict access to automation controller log files using explicitly defined privileges. Protecting log confidentiality prevents attackers from gathering sensitive system details and helps ensure your environment is safe from privilege escalation or lateral movement.

### About this task

To implement the security control, use the following procedure:

### Procedure

1.  As a system administrator for each automation controller host, set the permissions and owner of the automation controller NGINX log directory:

-  `chmod 770 /var/log/nginx`
-  `chown nginx:root /var/log/nginx`

2.  Set the permissions and owner of the automation controller log directory:

-  `chmod 770 /var/log/tower`
-  `chown awx:awx /var/log/tower`

3.  Set the permissions and owner of the automation controller supervisor log directory:

-  `chmod 770 /var/log/supervisor/`
-  `chown root:root /var/log/supervisor/`
- If automation controller is not in an HA configuration, the administrator must reinstall automation controller.

## Implement security control for system administrators

Configure your automation controller web server to log detailed user session records. Capturing this data supports troubleshooting, debugging, and forensic analysis, and helps ensure you retain essential auditing tools for event investigations.

### About this task

Use the following procedure to implement the security control as a System Administrator for each automation controller host:

### Procedure

1.  From the navigation panel, select Settings> (and then)Automation Execution> (and then)System. The System Settings page is displayed.
2.  Click Edit.
3.  Set the following:

- **Enable Activity Stream** = On
- **Enable Activity Stream for Inventory Sync** = On
- **Organization Admins Can Manage Users and Teams** = On
- **All Users Visible to Organization Admins** = On

4.  Click Save.
