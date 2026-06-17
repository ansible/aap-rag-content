+++
title = "Troubleshoot your Operator-based deployment of Ansible Automation Platform - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/troubleshoot-assembly_operator_troubleshoot"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/troubleshoot-assembly_operator_troubleshoot/", "Troubleshoot your Operator-based deployment of Ansible Automation Platform"]]
category = "Troubleshoot"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/troubleshoot-assembly_operator_troubleshoot/aem-page/troubleshoot-assembly_operator_troubleshoot.html"
last_crumb = "Troubleshoot your Operator-based deployment of Ansible Automation Platform"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Troubleshoot your Operator-based deployment of Ansible Automation Platform"
oversized = "false"
page_slug = "troubleshoot-assembly_operator_troubleshoot"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/troubleshoot-assembly_operator_troubleshoot"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/troubleshoot-assembly_operator_troubleshoot/toc/toc.json"
type = "aem-page"
+++

# Troubleshoot your Operator-based deployment of Ansible Automation Platform

Use the commands and procedures in this section to diagnose and resolve common issues with your Ansible Automation Platform deployment on OpenShift Container Platform. Topics include viewing logs, inspecting resources, and collecting diagnostic data for Red Hat Support.

## Understand the automation controller operator logs

If an **AutomationController** instance fails to deploy, check the `automation-controller-operator` container logs. These logs contain the installer role output required to debug deployment issues.

## View events in the OpenShift Container Platform

You can view events in the OpenShift Container Platform web console to monitor for errors and troubleshoot issues. This helps you quickly diagnose problems by examining the status of custom resources and their related events.

### About this task

You can debug by first reviewing the status conditions of the Ansible Automation Platform custom resource (CR) and then checking any nested CRs for errors.

### Procedure

1.  Log in to the OpenShift Container Platform web console.
2.  In the navigation menu, select Home> (and then)Events.
3.  Select your project from the project list.
4.  To view events for a specific resource, navigate to that resource’s page. Many resource pages, such as pods and deployments, have their own **Events** tab.
5.  Select a resource to bring you to the **Pod Details** page.

### Results

Check the **Conditions** section on the **Pod details** page to confirm no errors are listed in the **Message** column.

## View operator logs

The following procedure is an example of how to view the logs for an `automation-controller-operator` pod.

### Procedure

1.  To find the pod name, run:
  

```
oc get pods | grep operator
```

2.  To view the logs for the pod, run:
  

```
oc logs <operator-pod-name> -f
```
  1.  Alternatively, to view the logs without first getting the pod name, run:
  

```
oc logs deployments/automation-controller-operator-controller-manager -c automation-controller-manager -f
```

## Configure log verbosity

You can enable task output for debugging on any custom resources (CRs) by setting `no_log` to `false` in the component section of the `AnsibleAutomationPlatform` CR.

### About this task

The logs then show output for any failed tasks that originally had `no_log` set to `true`. All Ansible Automation Platform components (automation controller, automation hub, and Event-Driven Ansible) support the `no_log` setting.

### Procedure

1.  Edit the Ansible Automation Platform CR and set the `no_log` field to `false` for the component you want to debug. For automation controller:

```
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
  name: myaap
spec:
  controller:
    no_log: false
```

  For automation hub:

```
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
  name: myaap
spec:
  hub:
    no_log: false
```
  For Event-Driven Ansible

```
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
  name: myaap
spec:
  eda:
    no_log: false
```
  
  Note:
      This might expose sensitive data in the logs. On production clusters, this value must generally be set to `true` unless you are actively debugging an issue.

2.  To increase the Ansible Playbook verbosity from the operator, set the verbosity level using an annotation on the Ansible Automation Platform CR:
  

```
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
  name: myaap
  annotations:
    ansible.sdk.operatorframework.io/verbosity: "4"
spec:
  # ... component configuration ...
```

## Inspect a OpenShift Container Platform resource

To inspect a OpenShift Container Platform resource, you must use the `oc` command to get a summary or the full YAML definition of the resource.

### Procedure

1.  To view a human-readable summary of a resource, run:
  

```
oc describe -n <namespace> <resource> <resource-name>
```

2.  To view the complete YAML definition of a resource, use the `-o yaml` flag:
  

```
oc get -n <namespace> <resource> <resource-name> -o yaml
```
  - For example, to get the YAML for the `automationcontroller` custom resource, run:

```
oc get -n aap automationcontroller aap -o yaml
```

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

## Standard Kubernetes resources

Standard Kubernetes resources are a core part of the OpenShift Container Platform. The following table describes the standard resources you can inspect to troubleshoot the state and configuration of an application.

| **Resource name**     | **Description**                                                                                          |
| --------------------- | -------------------------------------------------------------------------------------------------------- |
| <br> `pod`            | <br>Smallest deployable unit containing one or more containers running the application workloads.        |
| <br> `deployment`     | <br>Manages pod configuration and scaling.                                                               |
| <br> `pvc`            | <br>A PersistentVolumeClaim (PVC) is a request for storage resources, used for persistent data storage.  |
| <br> `service`        | <br>Exposes pods as network services with stable IP addresses and DNS names within the cluster.          |
| <br> `ingress`        | <br>Manages external HTTP and HTTPS access to services within the cluster.                               |
| <br> `route`          | <br>An OpenShift-specific resource for exposing services externally (similar to an ingress).             |
| <br> `secrets`        | <br>Stores sensitive data like passwords, tokens, and certificates.                                      |
| <br> `serviceaccount` | <br>Provides identity for processes running in pods to access permissions to other Kubernetes resources. |

## Collect diagnostic data

Use the `oc adm must-gather` command to collect comprehensive diagnostic data about your cluster and the Ansible Automation Platform components. This data is essential when contacting Red Hat Support.

### Procedure

1.  To start the `must-gather` tool, run:
  

```
oc adm must-gather --image=registry.redhat.io/ansible-automation-platform-25/aap-must-gather-rhel8
```
  Note:
      For version 2.6, the base image name changes to `registry.redhat.io/ansible-automation-platform-26/aap-must-gather-rhel9`.

2.  View the collected data, use the `omc` tool to query the `must-gather` tarball as if it were a live cluster.

```
omc use <path-to-must-gather>
omc get pods
```
