+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-disable_the_automation_intelligent_assistant_on_an_operator_based_deployment"
template = "docs/aem-title.html"
title = "Disable the automation intelligent assistant on an operator-based deployment - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-disable_or_remove_the_automation_intelligent_assistant/", "Disable or remove the automation intelligent assistant"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-disable_the_automation_intelligent_assistant_on_an_operator_based_deployment/aem-page/extend-disable_the_automation_intelligent_assistant_on_an_operator_based_deployment.html"
last_crumb = "Disable the automation intelligent assistant on an operator-based deployment"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Disable the automation intelligent assistant on an operator-based deployment"
oversized = "false"
page_slug = "extend-disable_the_automation_intelligent_assistant_on_an_operator_based_deployment"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/extend-disable_the_automation_intelligent_assistant_on_an_operator_based_deployment"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-disable_the_automation_intelligent_assistant_on_an_operator_based_deployment/toc/toc.json"
type = "aem-page"
+++

# Disable the automation intelligent assistant on an operator-based deployment

Use this procedure to disable the automation intelligent assistant on an operator-based Ansible Automation Platform deployment on OpenShift Container Platform.

## Before you begin

- You have administrator access to the OpenShift Container Platform cluster.
- The Ansible Automation Platform operator is installed and the automation intelligent assistant is deployed.

## Procedure

1.  Log in to OpenShift Container Platform as a platform administrator.
2.  Navigate to Operators> (and then)Installed Operators.
3.  From the list of installed operators, select the Ansible Automation Platform operator.
4.  Locate and select the Ansible Automation Platform custom resource, and then click the required app.
5.  Select the YAML tab.
6.  In the `spec` section, locate the `lightspeed` subsection and set `disabled` to `true`:
  

```
spec:
  lightspeed:
    disabled: true
```

7.  Click **Save**.
8.  Wait for the operator to reconcile. This prevents the Lightspeed custom resource from being recreated after deletion.
9.  Navigate to Operators> (and then)Ansible Automation Platform operator> (and then)AnsibleLightspeedand delete the AnsibleLightspeed custom resource named lightspeed.
  Alternatively, delete the custom resource from the command line:

```
oc delete ansiblelightspeed lightspeed -n <namespace>
```

10.  Wait for the Lightspeed pods to terminate. This process can take several minutes.

## What to do next

**Verification**

1. Navigate to Workloads> (and then)Pods.
2. Filter with the term "lightspeed" and confirm that no Lightspeed pods are in Running status.
3. Access the Ansible Automation Platform web interface and confirm that the chat icon is no longer displayed in the top navigation bar.
