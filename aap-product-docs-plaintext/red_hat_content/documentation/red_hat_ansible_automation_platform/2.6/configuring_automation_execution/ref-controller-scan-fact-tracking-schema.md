# 9. Logging and Aggregation
## 9.1. Loggers
### 9.1.3. Scan / fact / system tracking data schema




This section describes the schema for log messages produced by the scan/fact/system tracking logger in automation controller.

These contain detailed dictionary-type fields that are either services, packages, or files.

-  `    services` : For services scans, this field is included and has keys based on the name of the service.

Note
Periods are not allowed by elastic search in names, and are replaced with "_" by the log formatter.




-  `    package` : Included for log messages from package scans.
-  `    files` : Included for log messages from file scans.
-  `    host` : Name of the host the scan applies to.
-  `    inventory_id` : The inventory id the host is inside of.


This logger also includes the common fields in [Log message schema](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/configuring_automation_execution/assembly-controller-logging-aggregation#ref-controller-log-message-schema) .

