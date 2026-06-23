# Best practices for setting up secure logging
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

