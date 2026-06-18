+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-ref_controller_credential_gitlab_pat"
title = "GitLab Personal Access Token credential type - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_credentials/", "Configure credentials to authenticate remote systems and services"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-ref_controller_credential_gitlab_pat/aem-page/secure-ref_controller_credential_gitlab_pat.html"
last_crumb = "GitLab Personal Access Token credential type"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "GitLab Personal Access Token credential type"
oversized = "false"
page_slug = "secure-ref_controller_credential_gitlab_pat"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-ref_controller_credential_gitlab_pat"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-ref_controller_credential_gitlab_pat/toc/toc.json"
type = "aem-page"
+++

# GitLab Personal Access Token credential type

Select this credential to access GitLab by using a *Personal Access Token* (PAT), which you can get through GitLab.

For more information, see [Setting up a GitLab webhook](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_ug_controller_work_with_webhooks#controller-set-up-gitlab-webhook "Automation controller has the ability to run jobs based on a triggered webhook event coming in. Job status information (pending, error, success) can be sent back only for pull request events.").

GitLab PAT credentials require a value in the **Token** field, which is provided in your GitLab profile settings.

Use this credential to establish an API connection to GitLab for use in webhook listener jobs, to post status updates.
