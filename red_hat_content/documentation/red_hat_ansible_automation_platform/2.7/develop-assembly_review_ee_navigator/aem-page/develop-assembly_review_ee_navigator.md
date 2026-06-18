+++
title = "Run a playbook to display execution environment contents - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_review_ee_navigator"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_intro_navigator/", "Emulate a platform environment locally with automation content navigator"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-assembly_review_ee_navigator/aem-page/develop-assembly_review_ee_navigator.html"
last_crumb = "Run a playbook to display execution environment contents"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Run a playbook to display execution environment contents"
oversized = "false"
page_slug = "develop-assembly_review_ee_navigator"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-assembly_review_ee_navigator"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-assembly_review_ee_navigator/toc/toc.json"
type = "aem-page"
+++

# Run a playbook to display execution environment contents

As a content developer, you can review your automation execution environment with automation content navigator and display the packages and collections included in the automation execution environments. Automation content navigator runs a playbook to extract and display the results.

## Review automation execution environments from automation content navigator

Use the automation content navigator text-based interface to review your automation execution environments. This allows you to quickly inspect packages, versions, and collections installed in the environment.

### Before you begin

- Automation execution environments

### Procedure

1.  Review the automation execution environments included in your automation content navigator configuration.

```
$ ansible-navigator images
```

![List of automation execution environments](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/navigator-images-list.png)  

2.  Type the number of the automation execution environment you want to delve into for more details.  
![Automation execution environment details](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/navigator-image-details.png)  
      You can review the packages and versions of each installed automation execution environment and the Ansible version any included collections.

3.  Optional: pass in the automation execution environment that you want to use. This becomes the primary and is the automation execution environment that automation content navigator uses.

```
$ ansible-navigator images --eei registry.example.com/example-enterprise-ee:latest
```

### Results

- Review the automation execution environment output.  
![Automation execution environment output](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/navigator-image-details.png)  
