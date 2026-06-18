+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_operator_scaling_down_aap"
title = "Scale down your Ansible Automation Platform Operator deployment - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_operator_install_operator/", "Install on OpenShift Container Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_operator_scaling_down_aap/aem-page/install-proc_operator_scaling_down_aap.html"
last_crumb = "Scale down your Ansible Automation Platform Operator deployment"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Scale down your Ansible Automation Platform Operator deployment"
oversized = "false"
page_slug = "install-proc_operator_scaling_down_aap"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-proc_operator_scaling_down_aap"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_operator_scaling_down_aap/toc/toc.json"
type = "aem-page"
+++

# Scale down your Ansible Automation Platform Operator deployment

You can scale down all Ansible Automation Platform deployments and StatefulSets by using the `idle_aap` variable. This is useful for scenarios such as upgrades, migrations, or disaster recovery.

## About this task

## Procedure

1.  Log in to Red Hat OpenShift Container Platform.
2.  Go to Operators> (and then)Installed Operators.
3.  Select your Ansible Automation Platform Operator deployment.
4.  Select **All Instances** and go to your **AnsibleAutomationPlatform** instance.
5.  Click the **⋮** icon and then select Edit AnsibleAutomationPlatform.
6.  In the **YAML view** paste the following YAML code under the `spec:` section:
  

```
idle_aap: true
```

7.  Click Save.

## What to do next

Setting the `idle_aap` value to `true` scales down all active deployments. Setting the value to `false` scales the deployments back up.
