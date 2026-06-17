+++
title = "Send log files to third-party aggregation services - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/observe-assembly_controller_logging_aggregation"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/observe-assembly_controller_logging_aggregation/", "Send log files to third-party aggregation services"]]
category = "Observe"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/observe-assembly_controller_logging_aggregation/aem-page/observe-assembly_controller_logging_aggregation.html"
last_crumb = "Send log files to third-party aggregation services"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Send log files to third-party aggregation services"
oversized = "false"
page_slug = "observe-assembly_controller_logging_aggregation"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/observe-assembly_controller_logging_aggregation"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/observe-assembly_controller_logging_aggregation/toc/toc.json"
type = "aem-page"
+++

# Send log files to third-party aggregation services

Logging enables sending detailed logs to third-party aggregation services. These feeds provide insights into Ansible Automation Platform controller use and technical trends. Data can be used to analyze infrastructure events, monitor for anomalies, and correlate events across multiple services.

The types of data that are most useful to automation controller are job fact data, job events or job runs, activity stream data, and log messages. The data is sent in JSON format over a HTTP connection by using minimal service-specific adjustments engineered in a custom handler or through an imported library.

The version of `rsyslog` that is installed by automation controller does not include the following `rsyslog` modules:

- rsyslog-udpspoof.x86_64
- rsyslog-libdbi.x86_64


After installing automation controller, you must only use the automation controller provided `rsyslog` package for any logging outside of automation controller that might have previously been done with the RHEL provided `rsyslog` package.

If you already use `rsyslog` for logging system logs on the automation controller instances, you can continue to use `rsyslog` to handle logs from outside of automation controller by running a separate `rsyslog` process (using the same version of rsyslog that automation controller uses), and pointing it to a separate `/etc/rsyslog.conf` file.

Use the `/api/v2/settings/logging/` endpoint to configure how the automation controller `rsyslog` process handles messages that have not yet been sent if your external logger goes offline:

- `LOG_AGGREGATOR_ACTION_MAX_DISK_USAGE_GB`: Maximum disk persistence for rsyslogd action queuing in GB. Specifies the amount of data to store (in gigabytes) during an outage of the external log aggregator (defaults to 1).

     Equivalent to the `rsyslogd queue.maxDiskSpace` setting.

- `LOG_AGGREGATOR_ACTION_QUEUE_SIZE`: Maximum number of messages that can be stored in the log action queue. Defines how large the rsyslog action queue can grow in number of messages stored. This can have an impact on memory use. When the queue reaches 75% of this number, the queue starts writing to disk (`queue.highWatermark` in `rsyslog`). When it reaches 90%, `NOTICE`, `INFO`, and `DEBUG` messages start to be discarded (`queue.discardMark` with 'queue.discardSeverity=5`).

     Equivalent to the `rsyslogd queue.size` setting on the action.

It stores files in the directory specified by `LOG_AGGREGATOR_MAX_DISK_USAGE_PATH`.

- `LOG_AGGREGATOR_MAX_DISK_USAGE_PATH`: Specifies the location to store logs that should be retried after an outage of the external log aggregator (defaults to `/var/lib/awx`). Equivalent to the `rsyslogd queue.spoolDirectory` setting.


For example, if `Splunk` goes offline, `rsyslogd` stores a queue on the disk until `Splunk` comes back online. By default, it stores up to 1GB of events (while Splunk is offline) but you can increase that to more than 1GB if necessary, or change the path where you save the queue.
