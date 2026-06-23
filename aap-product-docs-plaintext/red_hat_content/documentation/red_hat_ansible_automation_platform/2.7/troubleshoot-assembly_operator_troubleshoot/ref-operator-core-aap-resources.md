# Troubleshoot your Operator-based deployment of Ansible Automation Platform
## Core Ansible Automation Platform resources

The following table lists and describes the core custom resources (CRs) that the Ansible Automation Platform Operator manages. Understanding these resources will help you with advanced troubleshooting and configuration.

| **Resource name**                       | **Description**                                                                     |
| --------------------------------------- | ----------------------------------------------------------------------------------- |
| <br> `ansibleautomationplatform`        | <br>CR for deploying the entire Ansible Automation Platform.                        |
| <br> `ansibleautomationplatformbackup`  | <br>CR for creating backups of the entire Ansible Automation Platform instance.     |
| <br> `ansibleautomationplatformrestore` | <br>CR for restoring the entire Ansible Automation Platform instance from a backup. |
| <br> `automationcontroller`             | <br>CR defining the desired state of an automation controller instance.             |
| <br> `automationcontrollerbackup`       | <br>CR for creating backups of automation controller data and configuration.        |
| <br> `automationcontrollerrestore`      | <br>CR for restoring the automation controller from a backup.                       |
| <br> `automationhub`                    | <br>CR for deploying an automation hub (Galaxy) instance.                           |
| <br> `automationhubbackup`              | <br>CR for creating backups of automation hub data and configuration.               |
| <br> `automationhubrestore`             | <br>CR for restoring automation hub from a backup.                                  |
| <br> `eda`                              | <br>CR for deploying an Event-Driven Ansible (EDA) instance.                        |
| <br> `edabackup`                        | <br>CR for creating backups of EDA data and configuration.                          |
| <br> `edarestore`                       | <br>CR for restoring EDA from a backup.                                             |
| <br> `ansiblelightspeed`                | <br>CR for deploying an Red Hat Ansible Lightspeed instance.                        |

