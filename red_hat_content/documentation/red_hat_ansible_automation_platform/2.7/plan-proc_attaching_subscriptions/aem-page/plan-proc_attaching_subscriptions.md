+++
title = "Attach your Ansible Automation Platform subscription - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/plan-proc_attaching_subscriptions"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/plan-proc_attaching_subscriptions/", "Attach your Ansible Automation Platform subscription"]]
category = "Plan"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/plan-proc_attaching_subscriptions/aem-page/plan-proc_attaching_subscriptions.html"
last_crumb = "Attach your Ansible Automation Platform subscription"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Attach your Ansible Automation Platform subscription"
oversized = "false"
page_slug = "plan-proc_attaching_subscriptions"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/plan-proc_attaching_subscriptions"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/plan-proc_attaching_subscriptions/toc/toc.json"
type = "aem-page"
+++

# Attach your Ansible Automation Platform subscription

You **must** have valid subscriptions on all nodes before installing Red Hat Ansible Automation Platform.

## About this task

Note:

Simple Content Access (SCA) is now the default subscription method for all Red Hat accounts. With SCA, you must register your systems to Red Hat Subscription Management (RHSM) or Satellite to access content. Traditional pool-based subscription attachment commands (such as `subscription-manager attach --pool` or `subscription-manager attach --auto`) are no longer required. For more information, see [Simple Content Access](https://access.redhat.com/articles/simple-content-access).

## Procedure

 Register your system with Red Hat Subscription Management:

```
$ sudo subscription-manager register --username <$INSERT_USERNAME_HERE> --password <$INSERT_PASSWORD_HERE>
```
With Simple Content Access (SCA), registration is the only step required to access Ansible Automation Platform content.

Note:

For accounts still using legacy subscription pools, you might have to manually attach subscriptions using the commands shown in the troubleshooting section.

## Results

1. Refresh the subscription information on your system:

```
$ sudo subscription-manager refresh
```

2. Verify your registration:

```
$ sudo subscription-manager identity
```
     This command displays your system identity, name, organization name, and organization ID, confirming successful registration.

- For legacy accounts not using SCA, you might have to manually attach subscriptions:

```
$ sudo subscription-manager list --available --all | grep -A 30 "Ansible Automation Platform"
```
     This command displays the subscription details including the Pool ID. Look for the `Pool ID:` line in the output.

     Once you have identified the correct Pool ID, attach the subscription:



```
$ sudo subscription-manager attach --pool=<pool_id>
```
  Note:
      Do not use MCT4022 as a `pool_id` as it can cause subscription attachment to fail.

- For legacy accounts not using SCA, if you are unable to locate certain packages that came bundled with the Ansible Automation Platform installer, or if you are seeing a `Repositories disabled by configuration` message, use the following steps to identify and enable the required repository:
  1. List available repositories:

```
$ sudo subscription-manager repos --list | grep -i ansible-automation-platform
```

  2. Identify the repository name that matches your RHEL version, Ansible Automation Platform version, and architecture (for example, `ansible-automation-platform-2.6-for-rhel-9-x86_64-rpms`).
  3. Enable the repository:

```
$ sudo subscription-manager repos --enable <repository_name>
```
