# 9. Logging and Aggregation
## 9.2. Setting up logging




Use the following procedure to set up logging to any of the aggregator types.

**Procedure**

1. From the navigation panel, selectSettings→Automation Execution→Logging.
1. On the **Logging settings** page, clickEdit.

![Logging settings page](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Configuring_automation_execution-en-US/images/1bb0edd62ed76f01477b27e60e4382c1/logging-settings.png)



1. You can configure the following options:


-  **Logging Aggregator** : Enter the hostname or IP address that you want to send logs to.
-  **Logging Aggregator Port** : Specify the port for the aggregator if it requires one.

Note
When the connection type is HTTPS, you can enter the hostname as a URL with a port number, after which, you are not required to enter the port again. However, TCP and UDP connections are determined by the hostname and port number combination, rather than URL. Therefore, in the case of a TCP or UDP connection, supply the port in the specified field. If a URL is entered in the **Logging Aggregator** field instead, its hostname portion is extracted as the hostname.




-  **Logging Aggregator Type** : Click to select the aggregator service from the list:

![Logging types](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Configuring_automation_execution-en-US/images/6413f8fbf68267cd5e93c29799e3b094/configure-controller-system-logging-types.png)



-  **Logging Aggregator Username** : Enter the username of the logging aggregator if required.
-  **Logging Aggregator Password/Token** : Enter the password of the logging aggregator if required.
-  **Loggers to Send Data to the Log Aggregator Form** : All four types of data are pre-populated by default. Click the tooltip![Help](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Configuring_automation_execution-en-US/images/0c17081b1d1293156a760e9a6e06634a/question_circle.png)
icon next to the field for additional information on each data type. Delete the data types you do not want.
-  **Cluster wide unique identifier** : Use this to uniquely identify instances.
-  **Logging Aggregator Protocol** : Click to select a connection type (protocol) to communicate with the log aggregator. Subsequent options vary depending on the selected protocol.
-  **TCP Connection Timeout** : Specify the connection timeout in seconds. This option is only applicable to HTTPS and TCP log aggregator protocols.
-  **Logging Aggregator Level Threshold** : Select the level of severity you want the log handler to report.
-  **Maximum number of messages that can be stored in the log action queue** :Defines how large the `        rsyslog` action queue can grow in number of messages stored. This can have an impact on memory use. When the queue reaches 75% of this number, the queue starts writing to disk ( `        queue.highWatermark` in `        rsyslog` ). When it reaches 90%, `        NOTICE` , `        INFO` , and `        DEBUG` messages start to be discarded ( `        queue.discardMark` with `        queue.discardSeverity=5` ).
-  **Maximum disk persistence for rsyslogd action queuing (in GB)** : The amount of data to store (in gigabytes) if an `        rsyslog` action takes time to process an incoming message (defaults to 1). Equivalent to the `        rsyslogd queue.maxdiskspace` setting on the action (e.g. `        omhttp` ). It stores files in the directory specified by `        LOG_AGGREGATOR_MAX_DISK_USAGE_PATH` .
-  **File system location for rsyslogd disk persistence** : Location to persist logs that should be retried after an outage of the external log aggregator (defaults to `        /var/lib/awx` ). Equivalent to the `        rsyslogd queue.spoolDirectory` setting.
-  **Log Format For API 4XX Errors** : Configure a specific error message. For more information, see [API 4XX Error Configuration](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/configuring_automation_execution/assembly-controller-logging-aggregation#proc-controller-api-4xx-error-config) .

1. You can set the following options:


-  **Log System Tracking Facts Individually** : Click the tooltip![Help](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Configuring_automation_execution-en-US/images/0c17081b1d1293156a760e9a6e06634a/question_circle.png)
icon for additional information, such as whether or not you want to turn it on, or leave it off by default.

1. Review your entries for your chosen logging aggregation. The following example is set up for Splunk:

![Splunk logging example](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Configuring_automation_execution-en-US/images/b01e2e7a7b8238744eab032d08f14c78/configure-controller-system-logging-splunk-example.png)



-  **Enable External Logging** : Select this checkbox if you want to send logs to an external log aggregator.
-  **Enable/disable HTTPS certificate verification** : Certificate verification is enabled by default for the HTTPS log protocol. Select this checkbox if you want the log handler to verify the HTTPS certificate sent by the external log aggregator before establishing a connection.
-  **Enable rsyslogd debugging** : Select this checkbox to enable high verbosity debugging for `        rsyslogd` . Useful for debugging connection issues for external log aggregation.

1. ClickSaveorCancelto abandon the changes.


