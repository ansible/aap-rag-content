+++
title = "Build a custom decision environment for Event-Driven Ansible - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/proc_eda_build_a_custom_decision_environment_1"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/proc_eda_build_a_custom_decision_environment_1/aem-page/proc_eda_build_a_custom_decision_environment_1.html"
last_crumb = "Build a custom decision environment for Event-Driven Ansible"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Build a custom decision environment for Event-Driven Ansible"
oversized = "false"
page_slug = "proc_eda_build_a_custom_decision_environment_1"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/proc_eda_build_a_custom_decision_environment_1"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/proc_eda_build_a_custom_decision_environment_1/toc/toc.json"
type = "aem-page"
+++

# Build a custom decision environment for Event-Driven Ansible

Customize a decision environment container image to ensure your rulebook activations run with the precise, custom-maintained collections and dependencies they require.

## Before you begin

- Ansible Automation Platform > = 2.5
- Event-Driven Ansible
- Ansible Builder > = 3.0

Important:

- Use the correct Event-Driven Ansible controller decision environment in Ansible Automation Platform to prevent rulebook activation failure.   * If you want to connect Event-Driven Ansible controller to Ansible Automation Platform 2.4, you must use `registry.redhat.io/ansible-automation-platform-24/de-minimal-rhel9:latest` (recommended) or `registry.redhat.io/ansible-automation-platform-24/de-minimal-rhel8:latest`
  * If you want to connect Event-Driven Ansible controller to Ansible Automation Platform 2.5, you must use `registry.redhat.io/ansible-automation-platform-25/de-minimal-rhel9:latest` (recommended) or `registry.redhat.io/ansible-automation-platform-25/de-minimal-rhel8:latest`
  * If you want to connect Event-Driven Ansible controller to Ansible Automation Platform 2.6, you must use `registry.redhat.io/ansible-automation-platform-26/de-minimal-rhel9:latest`

## Procedure

1.  Use `de-minimal` as the base image with Ansible Builder to build your custom decision environments. This image is built from a base image provided by Red Hat at [Ansible Automation Platform minimal decision environment](https://catalog.redhat.com/software/containers/ansible-automation-platform-25/de-minimal-rhel9/650a5672a370728c710acaab). Important:
  The `ansible.eda` collection is already installed in the `de-minimal `base image. To prevent Ansible Builder from attempting to reinstall it, add `ansible.eda` to the `exclude.all_from_collections` list as shown in the following examples.

The following is an example of the Ansible Builder definition file that uses `de-minimal` as a base image to build a custom decision environment with the ansible.eda collection:

```
version: 3

    images:
  base_image:
    name: 'registry.redhat.io/ansible-automation-platform-25/de-minimal-rhel9:latest'

    dependencies:
  galaxy:
    collections:
      - name: servicenow.itsm
  python_interpreter:
    package_system: "python3.12"
  exclude:
    all_from_collections:
      # ansible.eda is already installed in de-minimal
      - ansible.eda

    options:
  package_manager_path: /usr/bin/microdnf
```

2.  Optional: If you need other Python packages or RPMs, add the following to a single definition file:
  

```
version: 3

    images:
  base_image:
    name: 'registry.redhat.io/ansible-automation-platform-25/de-minimal-rhel9:latest'

    dependencies:
  galaxy:
    collections:
      - name: servicenow.itsm
  python:
    - six
    - psutil
  python_interpreter:
    package_system: "python3.12"
  exclude:
    all_from_collections:
      # ansible.eda is already installed in de-minimal
      - ansible.eda

    options:
  package_manager_path: /usr/bin/microdnf
```
