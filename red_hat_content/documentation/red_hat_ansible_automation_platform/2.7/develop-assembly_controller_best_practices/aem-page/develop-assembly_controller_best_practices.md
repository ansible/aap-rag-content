+++
template = "docs/aem-title.html"
title = "Best practices for automation execution - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_controller_best_practices"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_controller_best_practices/", "Best practices for automation execution"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-assembly_controller_best_practices/aem-page/develop-assembly_controller_best_practices.html"
last_crumb = "Best practices for automation execution"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Best practices for automation execution"
oversized = "false"
page_slug = "develop-assembly_controller_best_practices"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-assembly_controller_best_practices"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-assembly_controller_best_practices/toc/toc.json"
type = "aem-page"
+++

# Best practices for automation execution

Adopt these best practices to help ensure scalable, maintainable, and highly efficient automation. This guidance focuses on using source control, dynamic inventories, and robust file structures within automation controller.

## Use source control

Automation controller supports playbooks stored directly on the server. Therefore, you must store your playbooks, roles, and any associated details in source control.

This way you have an audit trail describing when and why you changed the rules that are automating your infrastructure. Additionally, it permits sharing of playbooks with other parts of your infrastructure or team.

## Ansible file and directory structure

Follow recommended directory structures for Ansible projects to organize playbooks, inventories, and variables. A consistent layout improves maintainability and scaling.

To ensure reliable and consistent automation, follow these best practices for managing your content:

- Package reusable content, such as roles, modules, and plugins into Ansible Collections.
- Reference all necessary Collections for a project in the project’s `requirements.yml` file. These dependencies are automatically installed into the execution environment (EE) at runtime, but only if they are not already present in the EE image.
- Do not import content from other projects or common file-system locations, such as `/opt`, at runtime. All content must be explicitly defined within the EE.
- Working directory: The playbook directory is used as the current working directory at runtime. However, always use the `playbook_dir` variable instead of relying on the current working directory path.


Warning:

Automation controller does not support interactive features.

- Avoid using the `vars_prompt` feature, as automation controller does not permit interactive questions. For user input, use [Surveys in job templates](/documentation/en-us/red_hat_ansible_automation_platform/2.7/get_started-assembly_gs_auto_op#controller-surveys-in-job-templates "Surveys provide a way to prompt users for input when launching a job from a job template. This input can then be used as variables in the playbook run.").
- Do not use the `pause` feature without a timeout. Automation controller does not permit canceling a pause interactively. If `pause` is necessary, you must set a timeout.

## Use dynamic inventory sources

Define an inventory synchronization process by using dynamic sources, such as a cloud provider or CMDB, to help ensure your infrastructure inventory in automation controller stays consistently up-to-date.

Note:

Edits and additions to Inventory host variables persist beyond an inventory synchronization as long as `--overwrite_vars` is **not** set.

## Variable management for inventory

Variables associated with hosts and groups in an inventory can be managed in several ways in automation controller.

Keep variable data with the hosts and groups definitions (see the inventory editor), rather than using `group_vars/` and `host_vars/`. If you use dynamic inventory sources, automation controller can synchronize such variables with the database while the **Overwrite Variables** option is not set.

## Autoscale

Use the "callback" feature to permit newly booting instances to request configuration for auto-scaling scenarios or provisioning integration.

## Larger host counts

Set "forks" on a job template to larger values to increase parallelism of execution runs.

## Continuous integration / Continuous deployment

Continuous Integration (CI) and Continuous Deployment (CD) are development practices that require developers to integrate code into a shared repository several times a day.

Each integration can then be verified by an automated build and automated tests. CI/CD is a method to deliver applications to customers by introducing automation into the stages of app development.

The main concepts attributed to CI/CD are continuous integration, continuous delivery, and continuous deployment. Automation controller can be integrated with CI/CD systems to enable automated provisioning, configuration management, application deployment, and other IT tasks as part of the CI/CD pipeline.

For a Continuous Integration system, such as Jenkins, to create a job, it must make a `curl` request to a job template. The credentials to the job template must not require prompting for any particular passwords.
