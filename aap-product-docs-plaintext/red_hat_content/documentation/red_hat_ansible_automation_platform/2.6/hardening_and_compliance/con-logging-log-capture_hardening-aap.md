# 2. Hardening Ansible Automation Platform
## 2.1. Planning considerations
### 2.1.5. Logging and log capture




Visibility and analytics is an important pillar of Enterprise Security and Zero Trust architectures. Logging is key to capturing actions and auditing.

You can manage logging and auditing of the Ansible Automation Platform infrastructure nodes by using the built-in audit support described in [Auditing the system](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/auditing-the-system_security-hardening) . Ansible Automation Platform’s built-in logging and activity stream logs all change within Red Hat Ansible Automation Platform and automation logs for auditing purposes. More detailed information is available in the [Logging and Aggregation](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/configuring_automation_execution/assembly-controller-logging-aggregation) section of Configuring automation execution.

Ansible Automation Platform and the underlying Red Hat Enterprise Linux systems should be configured to collect logging and auditing centrally, rather than reviewing it on the local system. Configure Ansible Automation Platform to use external logging to compile log records from multiple components within the Ansible Automation Platform server. The events occurring must be time-correlated to conduct accurate forensic analysis.

Another critical capability of logging is the ability to use cryptography to protect the integrity of log tools. Log data includes all information (for example, log records, log settings, and log reports) needed to successfully log information system activity. It is common for attackers to replace the log tools or inject code into the existing tools to hide or erase system activity from the logs. To address this risk, log tools must be cryptographically signed so that you can identify when the log tools have been modified, manipulated, or replaced. For example, one way to validate that the log tool(s) have not been modified, manipulated or replaced is to use a checksum hash against the tool file(s). This ensures the integrity of the tool(s) has not been compromised.

