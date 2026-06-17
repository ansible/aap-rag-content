+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_operator_install_planning"
title = "Plan your installation of Ansible Automation Platform on Red Hat OpenShift Container Platform - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_operator_install_operator/", "Install on OpenShift Container Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-assembly_operator_install_planning/aem-page/install-assembly_operator_install_planning.html"
last_crumb = "Plan your installation of Ansible Automation Platform on Red Hat OpenShift Container Platform"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Plan your installation of Ansible Automation Platform on Red Hat OpenShift Container Platform"
oversized = "false"
page_slug = "install-assembly_operator_install_planning"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-assembly_operator_install_planning"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-assembly_operator_install_planning/toc/toc.json"
type = "aem-page"
+++

# Plan your installation of Ansible Automation Platform on Red Hat OpenShift Container Platform

Red Hat Ansible Automation Platform is supported on both Red Hat Enterprise Linux and Red Hat OpenShift.

OpenShift operators help install and automate day-2 operations of complex, distributed software on Red Hat OpenShift Container Platform. The Ansible Automation Platform Operator enables you to deploy and manage Ansible Automation Platform components on Red Hat OpenShift Container Platform.

You can use this section to help plan your Red Hat Ansible Automation Platform installation on your Red Hat OpenShift Container Platform environment. Before installing, review the supported installation scenarios to determine which meets your requirements.

## About Ansible Automation Platform Operator

The Ansible Automation Platform Operator provides cloud-native, push-button deployment of new Ansible Automation Platform instances in your OpenShift environment.

The Ansible Automation Platform Operator includes resource types to deploy and manage instances of automation controller and private automation hub.

It also includes automation controller job resources for defining and launching jobs inside your automation controller deployments.

Deploying Ansible Automation Platform instances with a Kubernetes native operator offers several advantages over launching instances from a playbook deployed on Red Hat OpenShift Container Platform, including upgrades and full lifecycle support for your Red Hat Ansible Automation Platform deployments.

You can install the Ansible Automation Platform Operator from the Red Hat Operators catalog in OperatorHub.

## OpenShift Container Platform version compatibility

For supported OpenShift Container Platform versions, see the Red Hat Ansible Automation Platform Life Cycle page.

## Supported installation scenarios for Red Hat OpenShift Container Platform

You can use the OperatorHub on the Red Hat OpenShift Container Platform web console to install Ansible Automation Platform Operator.

Alternatively, you can install Ansible Automation Platform Operator from the OpenShift Container Platform command-line interface (CLI), `oc`.

After you have installed Ansible Automation Platform Operator you must create an **Ansible Automation Platform** custom resource (CR). This enables you to manage Ansible Automation Platform components from a single unified interface known as the platform gateway. In version 2.7, you must create an Ansible Automation Platform CR, even if you have an existing automation controller, automation hub, or Event-Driven Ansible, components.

If existing components have already been deployed, you must specify these components on the Ansible Automation Platform CR. You must create the custom resource in the same namespace as the existing components.

| **Supported scenarios**                                                                                                                                                                                                                                                                                                                                                                     | **Supported scenarios with existing components**                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ansible Automation Platform CR for blank slate install with automation controller, automation hub, and Event-Driven Ansible enabledAnsible Automation Platform CR with just automation controller enabledAnsible Automation Platform CR with just automation controller, automation hub enabledAnsible Automation Platform CR with just automation controller, Event-Driven Ansible enabled | Ansible Automation Platform CR created in the same namespace as an existing automation controller CR with the automation controller name specified on the Ansible Automation Platform CR specSame with automation controller and automation hubSame with automation controller, automation hub, and Event-Driven AnsibleSame with automation controller and Event-Driven Ansible |

## Ansible Automation Platform Operator CSRF management

In Ansible Automation Platform version 2.7 the Ansible Automation Platform Operator on OpenShift Container Platform creates OpenShift Routes and configures your Cross-site request forgery (CSRF) settings automatically.

When using external ingress, you must configure your CSRF on the ingress.

Important:

In previous versions CSRF was configurable through the automation controller user interface, in version 2.7 automation controller settings are still present but have no impact on CSRF settings for the platform gateway.

The following table helps to clarify which settings are applicable for which component.

| **UI setting**       | **Applicable for**        |
| -------------------- | ------------------------- |
| <br>Subscription     | <br>automation controller |
| <br>platform gateway | <br>platform gateway      |
| <br>User Preferences | <br>User interface        |
| <br>System           | <br>Automation controller |
| <br>Job              | <br>Automation controller |
| <br>Logging          | <br>Automation controller |
| <br>Troubleshooting  | <br>Automation controller |

## Additional resources

To learn more about OpenShift Container Platform OperatorHub you can review OpenShift Container Platform documentation.
