+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-define__create__and_build_execution_environments"
template = "docs/aem-title.html"
title = "Define, create, and build execution environments - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-define__create__and_build_execution_environments/", "Define, create, and build execution environments"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-define__create__and_build_execution_environments/aem-page/administer-define__create__and_build_execution_environments.html"
last_crumb = "Define, create, and build execution environments"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Define, create, and build execution environments"
oversized = "false"
page_slug = "administer-define__create__and_build_execution_environments"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/administer-define__create__and_build_execution_environments"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-define__create__and_build_execution_environments/toc/toc.json"
type = "aem-page"
+++

# Define, create, and build execution environments

Run automation consistently across nodes with execution environments, which are container images that contain everything you need to run your automation.

An execution environment is a containerized runtime that provides the following benefits:

- A consistent environment in which to run automation jobs
- Portability and scalability, as you can run automation jobs on any node, including controller and execution nodes
- Security and governance, as you can control what's inside the runtime environment; and you can have approved, signed, and verified container images
- Improved efficiency, as developers need not spend time troubleshooting environment dependencies

Execution environments contain:

- Ansible core
- Required collections
- Python and other system dependencies
- Other libraries that your automation may require

Ansible Builder is a command line tool that automates the process of building automation execution environments by using metadata defined in various Ansible Collections or created by the user. You build an execution environment before you can create it using automation controller. After building it, you push it to a repository (such as quay) and then, when creating an execution environment in the UI with automation controller, you must point to that repository to use it in Ansible Automation Platform to use it, for example, in a job template.

With Ansible Builder, you can easily create a customizable automation execution environments definition file that specifies the content you want included in your automation execution environments such as Ansible Core, Python, Collections, third-party Python requirements, and system level packages. This enables you to fulfill all of the necessary requirements and dependencies to get jobs running.
