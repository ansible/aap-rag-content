+++
title = "Configure collections from source management to run in a project - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-ref_projects_collections_support"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_controller_projects/", "Logically group playbooks with projects"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-ref_projects_collections_support/aem-page/develop-ref_projects_collections_support.html"
last_crumb = "Configure collections from source management to run in a project"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure collections from source management to run in a project"
oversized = "false"
page_slug = "develop-ref_projects_collections_support"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-ref_projects_collections_support"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-ref_projects_collections_support/toc/toc.json"
type = "aem-page"
+++

# Configure collections from source management to run in a project

Automation controller supports project-specific Ansible collections in job runs.

If you specify a collections requirements file in the SCM at `collections/requirements.yml`, automation controller installs collections in that file in the implicit project synchronization before a job run.

Automation controller has a system-wide setting that enables collections to be dynamically downloaded from the `collections/requirements.yml` file for SCM projects. You can turn off this setting in the **Job Settings** screen from the navigation panel Settings> (and then)Automation Execution> (and then)Job, by unchecking the **Enable Collection(s) Download** box.

Roles and collections are locally cached for performance reasons, and you select **Update revision on launch** in the project **Options** to ensure this:

 Note:

If you also have collections installed in your execution environment, the collections specified in the project’s `requirements.yml` file will take precedence when running a job. This precedence applies regardless of the version of the collection. For example, if the collection specified in `requirements.yml` is older than the collection within the execution environment, the collection specified in `requirements.yml` is used.

## Use collections with automation hub

Before automation controller can use automation hub as the default source for collections content, you must create an API token in the automation hub UI. You then specify this token in automation controller.

### About this task

Use the following procedure to connect to private automation hub or automation hub, the only difference is which URL you specify.

### Procedure

1.  Go to <https://console.redhat.com/ansible/automation-hub/token>.
2.  Click Load token.
3.  Click the copy ![Copy](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/copy.png) icon to copy the API token to the clipboard.
4.  Create a credential by choosing one of the following options:
  1.  To use automation hub, create an automation hub credential by using the copied token and pointing to the URLs shown in the **Server URL** and **SSO URL** fields of the token page:

    - **Galaxy Server URL** = `<https://console.redhat.com/ansible/automation-hub/token>`

  2.  To use private automation hub, create an automation hub credential using a token retrieved from the **Repo Management** dashboard of your private automation hub and pointing to the published repository URL as shown:
             ![image](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/projects-ah-repo-mgmt-repos-published.png)

        You can create different repositories with different namespaces or collections in them. For each repository in automation hub you must create a different credential.

  3.  Copy the **Ansible CLI URL** from the UI in the format of `/https://$<hub_url>/api/galaxy/content/<repo you want to pull from>` into the **Galaxy Server URL** field of **Create Credential**:
            For UI specific instructions, see [Red Hat Certified, validated, and Ansible Galaxy content in automation hub](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_managing_cert_valid_content "With Ansible automation hub, you can access and curate a unique set of collections from all forms of Ansible content.").

5.  Go to the organization for which you want to synchronize content from and add the new credential to the organization. This enables you to associate each organization with the credential, or repository, that you want to use content from.  **Example**

    You have two repositories:

  - *Prod*: `Namespace 1` and `Namespace 2`, each with collection `A` and `B` so: `namespace1.collectionA:v2.0.0` and `namespace2.collectionB:v2.0.0`

  - *Stage*: `Namespace 1` with only collection `A` so: `namespace1.collectionA:v1.5.0` on , you have a repository URL for *Prod* and *Stage*. You can create a credential for each one.

         Then you can assign different levels of access to different organizations. For example, you can create a `Developers` organization that has access to both repository, while an Operations organization just has access to the **Prod** repository only.

         For UI specific instructions, see [Configuring user access for container repositories in private automation hub](/documentation/en-us/red_hat_ansible_automation_platform/2.7/con_create_groups "You can create and assign permissions to a team in private automation hub that enables users to access specified features in the system.").

6.  If automation hub has self-signed certificates, use the toggle to enable the setting **Ignore Ansible Galaxy SSL Certificate Verification** in **Job Settings**. For automation hub, which uses a signed certificate, use the toggle to disable it instead. This is a global setting:
7.  Create a project, where the source repository specifies the necessary collections in a requirements file located in the `collections/requirements.yml` file.
8.  In the **Projects** list view, click the sync ![Update](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/sync.png) icon to update this project. Automation controller fetches the Galaxy collections from the `collections/requirements.yml` file and reports it as changed. The collections are installed for any job template using this project.  Note:
      If updates are required from Galaxy or Collections, a sync is performed that downloads the required roles, consuming that much more space in your /tmp file. In cases where you have a large project (around 10 GB), disk space on `/tmp` may be an issue.

## Manage playbooks manually

Manage Ansible playbooks and directories directly on the automation controller filesystem. This approach helps ensure proper file ownership and permissions when you cannot use source control.

### Procedure

-  Create one or more directories to store playbooks under the Project Base Path, for example, `/var/lib/awx/projects/`.
-  Create or copy playbook files into the playbook directory.
-  Ensure that the playbook directory and files are owned by the same UNIX user and group that the service runs as.
-  Ensure that the permissions are appropriate for the playbook directories and files.

- If you have not added any Ansible Playbook directories to the base project path, an error message is displayed. Choose one of the following options to troubleshoot this error:
  * Create the appropriate playbook directories and check out playbooks from your SCM.
  * Copy playbooks into the appropriate playbook directories.
