+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-con_controller_job_branch_overriding"
title = "Advanced configuration for jobs tied to source control management systems - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_ug_controller_jobs/", "Use jobs to run playbooks against an inventory of hosts"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-con_controller_job_branch_overriding/aem-page/develop-con_controller_job_branch_overriding.html"
last_crumb = "Advanced configuration for jobs tied to source control management systems"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Advanced configuration for jobs tied to source control management systems"
oversized = "false"
page_slug = "develop-con_controller_job_branch_overriding"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-con_controller_job_branch_overriding"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-con_controller_job_branch_overriding/toc/toc.json"
type = "aem-page"
+++

# Advanced configuration for jobs tied to source control management systems

In automation controller, you can configure projects to allow job templates to override the branch, tag, or reference used for source control.

Projects specify the branch, tag, or reference to use from source control in the `scm_branch` field. These are represented by the values specified in the **Type Details** fields:


![Project branching emphasized](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ug-scm-project-branching-emphasized.png)  


When creating or editing a job you have the option to **Allow branch override**. When this option is checked, project administrators can delegate branch selection to the job templates that use that project, requiring only project `use_role`.

## Source tree copy behavior

When automation controller runs a job, it creates a private copy of the project’s source tree for that job run.

Every job run has its own private data directory. This directory contains a copy of the project source tree for the given `scm_branch` that the job is running. Jobs are free to make changes to the project folder and make use of those changes while it is still running. This folder is temporary and is removed at the end of the job run.

If you check the **Clean** option, modified files are removed in automation controller’s local copy of the repository. This is done through use of the force parameter in its corresponding Ansible modules pertaining to git or sub-version.

## Project revision behavior

Automation controller integrates with SCM systems like Git to manage project revisions. This ensures the correct version of your project files is tracked and used consistently during job execution.

During a project update, the revision of the default branch (specified in the **Source control branch** field of the project) is stored when updated. If providing a non-default **Source control branch** (not a commit hash or tag) in a job, the newest revision is pulled from the source control remote immediately before the job starts. This revision is shown in the **Source control revision** field of the job and its project update.

As a result, offline job runs are impossible for non-default branches. To ensure that a job is running a static version from source control, use tags or commit hashes. Project updates do not save all branches, only the project default branch.

The **Source control branch** field is not validated, so the project must update to assure it is valid. If this field is provided or prompted for, the **Playbook** field of job templates is not validated, and you have to launch the job template to verify presence of the expected playbook.

## Git refspec

The **Source control refspec** field specifies the extra references the update should download from the remote. A refspec maps references from the remote repository to references in the local repository. If you leave this field blank, only the default references are fetched.

Examples include the following:

- `refs/:refs/remotes/origin/`: This fetches all references, including remotes of the remote
- `refs/pull/:refs/remotes/origin/pull/` (GitHub-specific): This fetches all refs for all pull requests
- `refs/pull/62/head:refs/remotes/origin/pull/62/head`: This fetches the ref for one GitHub pull request


For large projects, consider performance impact when using the first or second examples.

The **Source control refspec** parameter affects the availability of the project branch, and can enable access to references not otherwise available. Use the earlier examples to supply a pull request from the **Source control branch**, which is not possible without the **Source control refspec** field.

The Ansible git module fetches `refs/heads/` by default. This means that you can use a project’s branches, tags and commit hashes, as the **Source control branch** if **Source control refspec** is blank. The value specified in the **Source control refspec** field affects which **Source control branch** fields can be used as overrides. Project updates (of any type) perform an extra `git fetch` command to pull that refspec from the remote.

**Example** You can set up a project that enables branch override with the first or second refspec example. Use this in a job template that prompts for the **Source control branch**. A client can then start the job template when a new pull request is created, providing the branch `pull/N/head` and the job template can run against the provided GitHub pull request reference.
