# 9. Logging and Aggregation
## 9.1. Loggers
### 9.1.6. Logging aggregator services




The logging aggregator service works with the following monitoring and data analysis systems:

-  [Splunk](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/configuring_automation_execution/assembly-controller-logging-aggregation#ref-controller-logging-splunk)
-  [Loggly](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/configuring_automation_execution/assembly-controller-logging-aggregation#ref-controller-logging-loggly)
-  [Sumologic](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/configuring_automation_execution/assembly-controller-logging-aggregation#ref-controller-logging-sumologic)
-  [Elastic Stack (formerly ELK stack)](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/configuring_automation_execution/assembly-controller-logging-aggregation#ref-controller-logging-elastic-stack)


#### 9.1.6.1. Splunk




Automation controller’s Splunk logging integration uses the Splunk HTTP Collector.

When configuring a SPLUNK logging aggregator, add the full URL to the HTTP Event Collector host, as in the following example:

```
https://&lt;yourcontrollerfqdn&gt;/api/v2/settings/logging

{
"LOG_AGGREGATOR_HOST": "https://&lt;yoursplunk&gt;:8088/services/collector/event",
"LOG_AGGREGATOR_PORT": null,
"LOG_AGGREGATOR_TYPE": "splunk",
"LOG_AGGREGATOR_USERNAME": "",
"LOG_AGGREGATOR_PASSWORD": "$encrypted$",
"LOG_AGGREGATOR_LOGGERS": [
"awx",
"activity_stream",
"job_events",
"system_tracking"
],
"LOG_AGGREGATOR_INDIVIDUAL_FACTS": false,
"LOG_AGGREGATOR_ENABLED": true,
"LOG_AGGREGATOR_CONTROLLER_UUID": ""
}
```

Note
The Splunk HTTP Event Collector listens on port 8088 by default, so you must provide the full HEC event URL (with the port number) for `LOG_AGGREGATOR_HOST` for incoming requests to be processed successfully.



Typical values are shown in the following example:

![Splunk logging example](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Configuring_automation_execution-en-US/images/b0db7d685d31affdac498d9ddb9068ed/logging-splunk-controller-example.png)


For more information on configuring the HTTP Event Collector, see the [Splunk documentation](https://docs.splunk.com/Documentation/Splunk/latest/Data/UsetheHTTPEventCollector) .

#### 9.1.6.2. Loggly




The Loggly logging aggregator integration allows you to send logs from the controller to your Loggly account using Loggly’s HTTP endpoint.

For more information on sending logs through Loggly’s HTTP endpoint, see the [Loggly documentation](https://documentation.solarwinds.com/en/success_center/loggly/content/admin/http-endpoint.htm?cshid=loggly_http-endpoint) .

Loggly uses the URL convention shown in the **Logging Aggregator** field in the following example:

![Loggly example](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Configuring_automation_execution-en-US/images/008b6e0f5fbec294de34cc57d86d3efd/logging-loggly-tower-example.png)


#### 9.1.6.3. Sumologic




In Sumologic, create a search criteria containing the JSON files that provide the parameters used to collect the data you need.

![Sumologic logging](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Configuring_automation_execution-en-US/images/f41da76412f68448067b968a0a615bee/logging_sumologic_main.png)


#### 9.1.6.4. Elastic stack (formerly ELK stack)




The elastic stack is a collection of open source products for searching, analyzing, and visualizing log data in real time.

If you are setting up your own version of the elastic stack, the only change you require is to add the following lines to the logstash `logstash.conf` file:

```
filter {
json {
source =&gt; "message"
}
}
```

Note
Backward-incompatible changes were introduced with Elastic 5.0.0, and different configurations might be required depending on what version you are using.



