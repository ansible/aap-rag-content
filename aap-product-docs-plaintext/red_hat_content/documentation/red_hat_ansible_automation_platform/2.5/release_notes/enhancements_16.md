# 10. Patch releases
## 10.14. Ansible Automation Platform patch release December 18, 2024
### 10.14.1. Enhancements




#### 10.14.1.1. Ansible Automation Platform




- Added help text to all missing fields in Ansible Automation Platform gateway and `    django-ansible-base` . (AAP-37068)
- Consistently formatted sentence structure for `    help_text` , and provided more context in the help text where it was vague.(AAP-37016)
- Added dynamic preferences for usage by Automation Analytics.(AAP-36710)


-  `        INSIGHTS_TRACKING_STATE` : Enables the service to gather data on automation and send it to Automation Analytics.
-  `        RED_HAT_CONSOLE_URL` : This setting is used to to configure the upload URL for data collection for Automation Analytics.
-  `        REDHAT_USERNAME` : Username used to send data to Automation Analytics.
-  `        REDHAT_PASSWORD` : Password for the account used to send data to Automation Analytics.
-  `        SUBSCRIPTIONS_USERNAME` : Username is used to retrieve subscription and content information.
-  `        SUBSCRIPTIONS_PASSWORD` : Password is used to retrieve subscription and content information.
-  `        AUTOMATION_ANALYTICS_GATHER_INTERVAL` : interval in seconds at which Automation Analytics gathers data.

- Added an enabled flag for turning authenticator maps on or off. (AAP-36709)
-  `    aap-metrics-utility` has been updated to 0.4.1. (AAP-36393)
- Added the setting `    trusted_header_timeout_in_ns` to timegate `    X_TRUSTED_PROXY_HEADER` validation in the `    django-ansible-base` libraries used by Ansible Automation Platform components. (AAP-36712)


#### 10.14.1.2. Documentation updates




- With this update, the Ansible Automation Platform Operator growth topology and Ansible Automation Platform Operator enterprise topology have been updated to include s390x (IBM Z) architecture test support.


#### 10.14.1.3. Event-Driven Ansible




- Extended the scope of the `    log_level` and debug settings. (AAP-33669)
- A project can now be synced with the Event-Driven Ansible collection modules. (AAP-32264)
- In the Rulebook activation create form, selecting a project is now required before selecting a rulebook.(AAP-28082)
- TheCreate credentialsbutton is now visible irrespective of whether there are any existing credentials or not.(AAP-23707)


