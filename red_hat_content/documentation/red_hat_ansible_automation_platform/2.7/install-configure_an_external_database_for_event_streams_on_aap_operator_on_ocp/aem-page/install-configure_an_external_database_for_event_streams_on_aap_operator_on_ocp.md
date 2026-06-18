+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-configure_an_external_database_for_event_streams_on_aap_operator_on_ocp"
title = "Configure an external database for event streams in Operator on OpenShift Container Platform - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_operator_install_operator/", "Install on OpenShift Container Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-configure_an_external_database_for_event_streams_on_aap_operator_on_ocp/aem-page/install-configure_an_external_database_for_event_streams_on_aap_operator_on_ocp.html"
last_crumb = "Configure an external database for event streams in Operator on OpenShift Container Platform"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure an external database for event streams in Operator on OpenShift Container Platform"
oversized = "false"
page_slug = "install-configure_an_external_database_for_event_streams_on_aap_operator_on_ocp"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-configure_an_external_database_for_event_streams_on_aap_operator_on_ocp"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-configure_an_external_database_for_event_streams_on_aap_operator_on_ocp/toc/toc.json"
type = "aem-page"
+++

# Configure an external database for event streams in Operator on OpenShift Container Platform

The Ansible Automation Platform Operator automatically creates a dedicated PostgreSQL user (`eda_event_stream`) for Event-Driven Ansible event stream operations. This user has minimal privileges (`CONNECT` only) to reduce the security impact if credentials are exposed in decision environments.

## Before you begin

- The external database must run an Ansible Automation Platform-supported version of PostgreSQL: version 15, 16, or 17.

## Procedure

1.  Create an `event_stream_postgres_configuration_secret` YAML file:
  

```
----
apiVersion: v1
kind: Secret
metadata:
 name: eda-event-stream-postgres-configuration
 namespace: <target_namespace>
stringData:
    host: "<external_ip_or_url_resolvable_by_the_cluster>"
    port: "<external_port>"
    database: "<desired_database_name>"
    username: "eda_event_stream"
    password: "<password_to_connect_with>"
    sslmode: "prefer"
    type: "unmanaged"
  type: Opaque
----
```

2.  Apply the secret to your cluster:
  

```
----
$ oc create -f eda-event-stream-postgres-configuration-secret.yml
----
```

3.  When creating your `AnsibleAutomationPlatform` custom resource, specify the secret under the Event-Driven Ansible spec:
  

```
----
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
  name: myaap
  namespace: ansible-automation-platform
spec:
 eda:
  event_stream:
   postgres_configuration_secret: eda-event-stream-postgres-configuration
----
```
