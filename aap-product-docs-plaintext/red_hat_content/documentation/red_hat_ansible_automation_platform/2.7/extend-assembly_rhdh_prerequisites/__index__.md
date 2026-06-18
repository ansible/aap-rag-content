# Prerequisites

Complete these prerequisites before installing the Ansible plug-ins for Red Hat Developer Hub.

## Prerequisites

To proceed, you must have Red Hat Developer Hub installed on Red Hat OpenShift Container Platform (RHOCP) and a valid subscription to Red Hat Ansible Automation Platform.

- Red Hat Developer Hub installed on Red Hat OpenShift Container Platform.   * For Helm installation, follow the steps in the Installing Red Hat Developer Hub on OpenShift Container Platform with the Helm chart section of *Installing Red Hat Developer Hub on OpenShift Container Platform*.
* For Operator installation, follow the steps in the Installing Red Hat Developer Hub on OpenShift Container Platform with the Operator section of *Installing Red Hat Developer Hub on OpenShift Container Platform*.
- A valid subscription to Red Hat Ansible Automation Platform.
- An OpenShift Container Platform instance with the appropriate permissions within your project to create an application.
- The Red Hat Developer Hub instance can query the automation controller API.
- Optional: To use the integrated learning paths, you must have outbound access to developers.redhat.com.

## Recommended RHDH preconfiguration

Red Hat recommends performing the following initial configuration tasks in Red Hat Developer Hub (RHDH). However, you can install the Ansible plug-ins for Red Hat Developer Hub before completing these tasks.

- Authentication in Red Hat Developer Hub
- Authorization in Red Hat Developer Hub


Note:

Red Hat provides a repository of software templates for RHDH that uses the `publish:github` action. To use these software templates, you must install the required GitHub dynamic plugins.
