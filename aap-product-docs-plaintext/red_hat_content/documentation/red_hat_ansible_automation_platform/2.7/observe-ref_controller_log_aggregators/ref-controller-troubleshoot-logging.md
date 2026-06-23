# Configure third-party services
## Troubleshoot logging

This section provides information to help troubleshoot logging issues in automation controller.

**Logging Aggregation**

If you have sent a message with the test button to your configured logging service through http or https, but did not receive the message, check the `/var/log/tower/rsyslog.err` log file. This is where errors are stored if they occurred when authenticating rsyslog with an http or https external logging service. Note that if there are no errors, this file does not exist.

**API 4XX Errors**

You can include the API error message for 4XX errors by modifying the log format for those messages. Refer to the [Set up logging](/documentation/en-us/red_hat_ansible_automation_platform/2.7/observe-ref_controller_log_aggregators#proc-controller-set-up-logging "To set up logging to any of the aggregator types for centralized logging follow these steps:").

**LDAP**

You can enable logging messages for the LDAP adapter. For more information, see [Set up logging](/documentation/en-us/red_hat_ansible_automation_platform/2.7/observe-ref_controller_log_aggregators#proc-controller-set-up-logging "To set up logging to any of the aggregator types for centralized logging follow these steps:").

**SAML**

You can enable logging messages for the SAML adapter the same way you can enable logging for LDAP.
