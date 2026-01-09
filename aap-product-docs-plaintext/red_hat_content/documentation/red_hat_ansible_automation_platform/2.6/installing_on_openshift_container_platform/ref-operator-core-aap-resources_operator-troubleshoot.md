# 14. Troubleshooting the Red Hat Ansible Automation Platform Operator on OpenShift Container Platform
## 14.6. Core Ansible Automation Platform resources




The following table lists and describes the core custom resources (CRs) that the Ansible Automation Platform Operator manages. Understanding these resources will help you with advanced troubleshooting and configuration.

|  **Resource name** |  **Description** |
| --- | --- |
|  `ansibleautomationplatform` | CR for deploying the entire Ansible Automation Platform. |
|  `ansibleautomationplatformbackup` | CR for creating backups of the entire Ansible Automation Platform instance. |
|  `ansibleautomationplatformrestore` | CR for restoring the entire Ansible Automation Platform instance from a backup. |
|  `automationcontroller` | CR defining the desired state of an automation controller instance. |
|  `automationcontrollerbackup` | CR for creating backups of automation controller data and configuration. |
|  `automationcontrollerrestore` | CR for restoring the automation controller from a backup. |
|  `automationhub` | CR for deploying an automation hub (Galaxy) instance. |
|  `automationhubbackup` | CR for creating backups of automation hub data and configuration. |
|  `automationhubrestore` | CR for restoring automation hub from a backup. |
|  `eda` | CR for deploying an Event-Driven Ansible (EDA) instance. |
|  `edabackup` | CR for creating backups of EDA data and configuration. |
|  `edarestore` | CR for restoring EDA from a backup. |
|  `ansiblelightspeed` | CR for deploying an Red Hat Ansible Lightspeed instance. |


