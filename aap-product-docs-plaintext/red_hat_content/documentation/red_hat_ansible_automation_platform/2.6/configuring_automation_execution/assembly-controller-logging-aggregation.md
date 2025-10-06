# Chapter 9. Logging and Aggregation




Logging provides the capability to send detailed logs to third-party external log aggregation services. Services connected to this data feed serve as a means of gaining insight into automation controller use or technical trends. The data can be used to analyze events in the infrastructure, monitor for anomalies, and correlate events in one service with events in another.

The types of data that are most useful to automation controller are job fact data, job events or job runs, activity stream data, and log messages. The data is sent in JSON format over a HTTP connection using minimal service-specific adjustments engineered in a custom handler or through an imported library.

The version of `rsyslog` that is installed by automation controller does not include the following `rsyslog` modules:

- rsyslog-udpspoof.x86_64
- rsyslog-libdbi.x86_64


After installing automation controller, you must only use the automation controller provided `rsyslog` package for any logging outside of automation controller that might have previously been done with the RHEL provided `rsyslog` package.

If you already use `rsyslog` for logging system logs on the automation controller instances, you can continue to use `rsyslog` to handle logs from outside of automation controller by running a separate `rsyslog` process (using the same version of rsyslog that automation controller uses), and pointing it to a separate `/etc/rsyslog.conf` file.

Use the `/api/v2/settings/logging/` endpoint to configure how the automation controller `rsyslog` process handles messages that have not yet been sent in the event that your external logger goes offline:

-  `    LOG_AGGREGATOR_ACTION_MAX_DISK_USAGE_GB` : Maximum disk persistence for rsyslogd action queuing in GB.

Specifies the amount of data to store (in gigabytes) during an outage of the external log aggregator (defaults to 1).

Equivalent to the `    rsyslogd queue.maxDiskSpace` setting.


-  `    LOG_AGGREGATOR_ACTION_QUEUE_SIZE` : Maximum number of messages that can be stored in the log action queue.

Defines how large the rsyslog action queue can grow in number of messages stored. This can have an impact on memory use. When the queue reaches 75% of this number, the queue starts writing to disk ( `    queue.highWatermark` in `    rsyslog` ). When it reaches 90%, `    NOTICE` , `    INFO` , and `    DEBUG` messages start to be discarded ( `    queue.discardMark` with 'queue.discardSeverity=5`).

Equivalent to the `    rsyslogd queue.size` setting on the action.




It stores files in the directory specified by `LOG_AGGREGATOR_MAX_DISK_USAGE_PATH` .

-  `    LOG_AGGREGATOR_MAX_DISK_USAGE_PATH` : Specifies the location to store logs that should be retried after an outage of the external log aggregator (defaults to `    /var/lib/awx` ). Equivalent to the `    rsyslogd queue.spoolDirectory` setting.


For example, if `Splunk` goes offline, `rsyslogd` stores a queue on the disk until `Splunk` comes back online. By default, it stores up to 1GB of events (while Splunk is offline) but you can increase that to more than 1GB if necessary, or change the path where you save the queue.

