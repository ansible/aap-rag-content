+++
template = "docs/aem-title.html"
title = "Run playbooks with ansible-navigator using the assistant - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-run_playbooks_with_ansible_navigator_using_the_assistant"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_lightspeed_intro/", "Build automation faster with Red Hat Ansible Lightspeed code assistant"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-run_playbooks_with_ansible_navigator_using_the_assistant/aem-page/develop-run_playbooks_with_ansible_navigator_using_the_assistant.html"
last_crumb = "Run playbooks with ansible-navigator using the assistant"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Run playbooks with ansible-navigator using the assistant"
oversized = "false"
page_slug = "develop-run_playbooks_with_ansible_navigator_using_the_assistant"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-run_playbooks_with_ansible_navigator_using_the_assistant"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-run_playbooks_with_ansible_navigator_using_the_assistant/toc/toc.json"
type = "aem-page"
+++

# Run playbooks with `ansible-navigator` using the assistant

After you have built a suitable execution environment, you can ask the assistant to generate the correct `ansible-navigator` command to execute your playbook in that particular environment.

## Procedure

1. Ask the assistant to generate a command that runs the playbook in your execution environment. For example:
  

```
Generate a command that runs this playbook in the execution environment <your-file-name>
```

    The assistant then generates an appropriate `ansible-navigator` command, ensuring the `--execution-environment-image` flag points to your newly built tag.

  A generated command might look like the following:

```
ansible-navigator run playbook.yml --execution-environment-image webserver-ee:1.0 --mode stdout
```

2. In the VS Code terminal, execute the command to run your automation within the custom environment.
