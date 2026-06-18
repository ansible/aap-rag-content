+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/proc_using_content_signing_services_in_pah"
title = "Secure your automation content with signatures - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/proc_using_content_signing_services_in_pah/aem-page/proc_using_content_signing_services_in_pah.html"
last_crumb = "Secure your automation content with signatures"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Secure your automation content with signatures"
oversized = "false"
page_slug = "proc_using_content_signing_services_in_pah"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/proc_using_content_signing_services_in_pah"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/proc_using_content_signing_services_in_pah/toc/toc.json"
type = "aem-page"
+++

# Secure your automation content with signatures

After you have configured content signing on your private automation hub, you can manually sign a new collection or replace an existing signature with a new one.

## About this task

When users download a specific collection, the signature indicates that the collection is for them and has not been modified after certification.

You can use content signing on private automation hub in the following scenarios:

- Your system does not have automatic signing configured and you must use a manual signing process to sign collections.
- The current signatures on the automatically configured collections are corrupted and need new signatures.
- You need additional signatures for previously signed content.
- You want to rotate signatures on your collections.

## Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select Automation Content> (and then)Collection Approvals. The Approval dashboard opens and displays a list of collections.
3.  Click the thumbs up icon next to the collection you want to approve. On the modal that appears, check the box confirming that you want to approve the collection, and click Approve and sign collections.

## Results

- Navigate to Automation Content> (and then)Collections to verify that the collections you signed and approved are displayed.
