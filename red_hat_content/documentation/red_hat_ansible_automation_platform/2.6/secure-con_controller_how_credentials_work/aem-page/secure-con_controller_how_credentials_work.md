+++
title = "How credentials work - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-con_controller_how_credentials_work"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_controller_credentials/", "Configure credentials to authenticate remote systems and services"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-con_controller_how_credentials_work/aem-page/secure-con_controller_how_credentials_work.html"
last_crumb = "How credentials work"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "How credentials work"
oversized = "false"
page_slug = "secure-con_controller_how_credentials_work"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/secure-con_controller_how_credentials_work"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-con_controller_how_credentials_work/toc/toc.json"
type = "aem-page"
+++

# How credentials work

Credentials in automation controller store the information required to authenticate to remote systems and services. Credentials include usernames and passwords, SSH keys, tokens, and other sensitive data. Automation controller encrypts sensitive credential data in the database to enhance security.

Automation controller uses SSH to connect to remote hosts. To pass the key from automation controller to SSH, the key must be decrypted before it can be written to a named pipe. Automation controller uses that pipe to send the key to SSH, so that the key is never written to disk. If passwords are used, automation controller handles them by responding directly to the password prompt and decrypting the password before writing it to the prompt.

The **Credentials** page shows credentials that are currently available. The default view is collapsed (Compact), showing the credential name, and credential type.

From this screen you can edit ![Edit](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/leftpencil.png), duplicate ![Copy](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/copy.png) or delete ⋮ a credential.

 Note:

It is possible to create duplicate credentials with the same name and without an organization. However, it is not possible to create two duplicate credentials in the same organization.

 **Example**

1. Create two machine credentials with the same name but without an organization.

2. Use the module `ansible.controller.export` to export the credentials.

3. Use the module `ansible.controller.import` in a different automation execution node.

4. Check the imported credentials. When you export two duplicate credentials and then import them in a different node, only one credential is imported.
