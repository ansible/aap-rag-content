+++
template = "docs/aem-title.html"
title = "Validate the restored deployment and complete post-import tasks - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/validate_the_restored_deployment_and_complete_post_import_tasks"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/validate_the_restored_deployment_and_complete_post_import_tasks/aem-page/validate_the_restored_deployment_and_complete_post_import_tasks.html"
last_crumb = "Validate the restored deployment and complete post-import tasks"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Validate the restored deployment and complete post-import tasks"
oversized = "false"
page_slug = "validate_the_restored_deployment_and_complete_post_import_tasks"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/validate_the_restored_deployment_and_complete_post_import_tasks"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/validate_the_restored_deployment_and_complete_post_import_tasks/toc/toc.json"
type = "aem-page"
+++

# Validate the restored deployment and complete post-import tasks

Verify that the restored deployment is healthy and complete any post-import tasks before using it in production. Some steps are conditional on which components were in the artifact and whether hostnames changed.

## Before you begin

- The `ansible.aap_snapshot.artifact_import` playbook completed without errors.
- The gateway admin password for the restored deployment is available.
- `oc` CLI access to the OCP namespace is available.

## Procedure

1.  Log in to the Ansible Automation Platform UI using the `admin` username and the platform gateway admin password.
      Retrieve the Ansible Automation Platform UI URL with the following command:

```
oc get route -n aap -l app.kubernetes.io/component=aap-gateway
```

    If your deployment uses a non-default instance name, replace `aap-gateway` with `<aap_instance_name>-gateway`.

    If login fails, verify that `gateway_admin_password` in your inventory matched the source deployment's password.

2.  In the navigation panel, select Automation Execution > Infrastructure > Instance Groups and verify that the expected instance groups are present.
3.  If any instance group names differ from the source deployment, reassign resources to the correct instance groups.
4.  If Event-Driven Ansible was included and the gateway hostname changed, from the navigation panel select Automation Decisions > Infrastructure > Credentials and update any Automation Controller credentials to the new controller URL.
5.  Register execution nodes through the Ansible Automation Platform UI or API.
      From the navigation panel, select Automation Execution > Infrastructure > Instances. The reconcile phase deprovisions instances with no recent heartbeat but does not register new ones.

6.  If the post-import advisory includes the message `Hub content was not migrated - run content sync manually`, trigger a content sync.
      From the navigation panel, select Automation Content > Repositories, then sync each repository from its configured remote registry.

7.  If the source deployment used custom TLS certificates, reapply them to the OCP namespace.
      The collection does not seed TLS certificate material from the artifact. Only encryption keys (`SECRET_KEY` values) are seeded. For the Ansible Automation Platform Operator CR fields that control TLS injection, see the documentation for renewing and changing SSL/TLS certificates and keys.

8.  Verify that all components are healthy:
  

```
oc get ansibleautomationplatform -n aap
oc get automationcontroller,automationhub,automationgateway,automationedacontroller -n aap
```
