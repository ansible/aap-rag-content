# 9. Logging and Aggregation
## 9.4. Troubleshooting logging





<span id="logging_aggregation"></span>
##### Logging Aggregation


If you have sent a message with the test button to your configured logging service through http or https, but did not receive the message, check the `/var/log/tower/rsyslog.err` log file. This is where errors are stored if they occurred when authenticating rsyslog with an http or https external logging service. Note that if there are no errors, this file does not exist.


<span id="api_4xx_errors"></span>
##### API 4XX Errors


You can include the API error message for 4XX errors by modifying the log format for those messages. Refer to the [API 4XX Error Configuration](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#proc-controller-api-4xx-error-config) .


<span id="ldap"></span>
##### LDAP


You can enable logging messages for the LDAP adapter. For more information, see [API 4XX Error Configuration](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#proc-controller-api-4xx-error-config) .


<span id="saml"></span>
##### SAML


You can enable logging messages for the SAML adapter the same way you can enable logging for LDAP.

