# 2. Hardening Ansible Automation Platform
## 2.3. Initial configuration
### 2.3.2. Configure centralized logging




Centralized logging is essential to assist in monitoring system security and performing large-scale log analysis. The _Confidentiality, Integrity, and Availability_ (CIA) triad, which originated from a combination of ideas from the US military and government, is the model that is the foundation for proper security system development and best practices. Centralized logging falls under the Integrity aspect to assist in identifying if data or systems have been tampered with. The logging to a centralized system enables troubleshooting automation across multiple systems by collecting all logs in the single location, therefore making it easier to identify issues, analyze trends, and correlate events from different servers, especially in a complex Ansible Automation Platform deployment. Manually checking individual machines would be time consuming so centralized logging is valuable with debugging in addition to meeting security best practices. This ensures the overall system health and stability and assists in identifying potential security threats. In addition to the logging configuration, the failure to log due to storage capacity, hardware failure as well as high availability architecture should be taken into consideration.

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


#### 2.3.2.1. Setting up logging




To set up logging to any of the aggregator types for centralized logging follow these steps:

**Procedure**

1. From the navigation panel, selectSettings→Automation Execution→Logging.
1. On the **Logging settings** page, clickEdit.
1. You can configure the following options:


-  **Logging Aggregator** : Enter the hostname or IP address that you want to send logs to.
-  **Logging Aggregator Port** : Specify the port for the aggregator if it requires one.

Note
When the connection type is HTTPS, you can enter the hostname as a URL with a port number, after which, you are not required to enter the port again. However, TCP and UDP connections are determined by the hostname and port number combination, rather than URL. Therefore, in the case of a TCP or UDP connection, supply the port in the specified field. If a URL is entered in the **Logging Aggregator** field instead, its hostname portion is extracted as the hostname.




-  **Logging Aggregator Type** : Click to select the aggregator service from the list:
-  **Logging Aggregator Username** : Enter the username of the logging aggregator if required.
-  **Logging Aggregator Password/Token** : Enter the password of the logging aggregator if required.
-  **Loggers to Send Data to the Log Aggregator Form** : All four types of data are pre-populated by default. Click the tooltip![Help](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Hardening_and_compliance-en-US/images/0c17081b1d1293156a760e9a6e06634a/question_circle.png)
icon next to the field for additional information on each data type. Delete the data types you do not want.
-  **Cluster wide unique identifier** : Use this to uniquely identify instances.
-  **Logging Aggregator Protocol** : Click to select a connection type (protocol) to communicate with the log aggregator. Subsequent options vary depending on the selected protocol.
-  **TCP Connection Timeout** : Specify the connection timeout in seconds. This option is only applicable to HTTPS and TCP log aggregator protocols.
-  **Logging Aggregator Level Threshold** : Select the level of severity you want the log handler to report.
-  **Maximum number of messages that can be stored in the log action queue** :Defines how large the `        rsyslog` action queue can grow in number of messages stored. This can have an impact on memory use. When the queue reaches 75% of this number, the queue starts writing to disk ( `        queue.highWatermark` in `        rsyslog` ). When it reaches 90%, `        NOTICE` , `        INFO` , and `        DEBUG` messages start to be discarded ( `        queue.discardMark` with `        queue.discardSeverity=5` ).
-  **Maximum disk persistence for rsyslogd action queuing (in GB)** : The amount of data to store (in gigabytes) if an `        rsyslog` action takes time to process an incoming message (defaults to 1). Equivalent to the `        rsyslogd queue.maxdiskspace` setting on the action (e.g. `        omhttp` ). It stores files in the directory specified by `        LOG_AGGREGATOR_MAX_DISK_USAGE_PATH` .
-  **File system location for rsyslogd disk persistence** : Location to persist logs that should be retried after an outage of the external log aggregator (defaults to `        /var/lib/awx` ). Equivalent to the `        rsyslogd queue.spoolDirectory` setting.
-  **Log Format For API 4XX Errors** : Configure a specific error message. For more information, see [API 4XX Error Configuration](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/configuring_automation_execution/assembly-controller-logging-aggregation#proc-controller-api-4xx-error-config) .



Set the following options:

-  **Log System Tracking Facts Individually** : Click the tooltip![Help](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Hardening_and_compliance-en-US/images/0c17081b1d1293156a760e9a6e06634a/question_circle.png)
icon for additional information, such as whether or not you want to turn it on, or leave it off by default.


1. Review your entries for your chosen logging aggregation.

-  **Enable External Logging** : Select this checkbox if you want to send logs to an external log aggregator.
-  **Enable/disable HTTPS certificate verification** : Certificate verification is enabled by default for the HTTPS log protocol. Select this checkbox if you want the log handler to verify the HTTPS certificate sent by the external log aggregator before establishing a connection.
-  **Enable rsyslogd debugging** : Select this checkbox to enable high verbosity debugging for `    rsyslogd` . Useful for debugging connection issues for external log aggregation.


1. ClickSaveorCancelto abandon the changes.



#### 2.3.2.2. Configuring LDAP logging




The following steps enable the LDAP logging:

To enable logging for LDAP, use the following procedure.

**Procedure**

1. Edit the gateway settings file:


1. On Ansible Automation Platform2.6 Containerized, the file is `        ~/aap/gateway/etc/settings.py` (as the user running the platform gateway container).
1. On Ansible Automation Platform2.6 RPM-based, the file is `        /etc/ansible-automation-platform/gateway/settings.py` .


```
(...)          CACHES['fallback']['LOCATION'] = '/var/cache/ansible-automation-platform/gateway'                  LOGGING['loggers']['aap']['level'] = 'INFO'          LOGGING['loggers']['ansible_base']['level'] = 'INFO'          LOGGING['loggers']['django_auth_ldap']['level'] = 'DEBUG'      ######      add this line                  (...)
```



1. Restart the platform gateway service or container:


1. On Ansible Automation Platform2.6 Containerized, restart the platform gateway service so that it restarts the platform gateway container:

Note
Ensure that you run `        systemctl with the `--user`` flag as follows:

+ `        $ systemctl --user restart automation-gateway`




1. On Ansible Automation Platform2.6 RPM-based, use the `        automation-gateway-service` command:

`        # automation-gateway-service restart`





#### 2.3.2.3. Implementing security control




Some of the following examples of meeting compliance requirements come from the US DoD _Security Technical Implementation Guide_ , but go back to integrity and security best practices.

Automation controller must use external log providers that can collect user activity logs in independent, protected repositories to prevent modification or repudiation. Automation controller must be configured to use external logging to compile log records from multiple components within the server. The events occurring must be time-correlated in order to conduct accurate forensic analysis. In addition, the correlation must meet certain tolerance criteria.

The following steps implement the security control:

**Procedure**

1. Log in to automation controller as an administrator.
1. From the navigation panel, selectSettings→Automation Execution→Logging.
1. On the **Logging settings** page, clickEdit.
1. Set the following fields:


- Set **Logging Aggregator** to `        Not configured` . This is the default.
- Set **Enable External Logging** to `        On` .
- Set **Logging Aggregator Level Threshold** to DEBUG.
- Set **TCP Connection Timeout** to 5 (the default) or to the organizational timeout.
- Set **Enable/disable HTTPS certificate verification** to `        On` .

1. ClickSave.


Automation controller must allocate log record storage capacity and shut down by default upon log failure (unless availability is an overriding concern). It is critical that when a system is at risk of failing to process logs, it detects and takes action to mitigate the failure. Log processing failures include software/hardware errors, failures in the log capturing mechanisms, and log storage capacity being reached or exceeded. During a failure, the application server must be configured to shut down unless the application server is part of a high availability system. When availability is an overriding concern, other approved actions in response to a log failure are as follows:

1. If the failure was caused by the lack of log record storage capacity, the application must continue generating log records if possible (automatically restarting the log service if necessary), overwriting the oldest log records in a first-in-first-out manner.
1. If log records are sent to a centralized collection server and communication with this server is lost or the server fails, the application must queue log records locally until communication is restored or until the log records are retrieved manually. Upon restoration of the connection to the centralized collection server, action must be taken to synchronize the local log data with the collection server.

The following steps implement the security control:


1. Open a web browser and navigate to the logging API, `        /api/v2/settings/logging/`

Ensure that you are authenticated as an automation controller administrator.


1. In the **Content** section, modify the following values:


-  `            LOG_AGGREGATOR_ACTION_MAX_DISK_USAGE_GB` = organization-defined requirement for log buffering.
-  `            LOG_AGGREGATOR_MAX_DISK_USAGE_PATH` = `            /var/lib/awx` ..ClickPUT.




#### 2.3.2.4. Implementing security control for each host




Automation controller’s log files must be accessible by explicitly defined privilege. A failure of the confidentiality of automation controller log files would enable an attacker to identify key information about the system that they might not otherwise be able to obtain that would enable them to enumerate more information to enable escalation or lateral movement.

To implement the security control, use the following procedure:

**Procedure**

1. As a system administrator for each automation controller host, set the permissions and owner of the automation controller NGINX log directory:


-  `        chmod 770 /var/log/nginx`
-  `        chown nginx:root /var/log/nginx`

1. Set the permissions and owner of the automation controller log directory:


-  `        chmod 770 /var/log/tower`
-  `        chown awx:awx /var/log/tower`

1. Set the permissions and owner of the automation controller supervisor log directory:


-  `        chmod 770 /var/log/supervisor/`
-  `        chown root:root /var/log/supervisor/`



Automation controller must be configured to fail over to another system in the event of log subsystem failure. Automation controller hosts must be capable of failing over to another automation controller host which can handle application and logging functions upon detection of an application log processing failure. This enables continual operation of the application and logging functions while minimizing the loss of operation for the users and loss of log data.

- If automation controller is not in an HA configuration, the administrator must reinstall automation controller.


