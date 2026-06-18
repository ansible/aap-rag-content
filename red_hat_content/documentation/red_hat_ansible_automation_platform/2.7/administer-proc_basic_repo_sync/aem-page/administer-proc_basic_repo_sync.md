+++
title = "Synchronize repositories in automation hub - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_basic_repo_sync"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_working_with_namespaces/", "Manage collection access and permissions with namespaces"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-proc_basic_repo_sync/aem-page/administer-proc_basic_repo_sync.html"
last_crumb = "Synchronize repositories in automation hub"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Synchronize repositories in automation hub"
oversized = "false"
page_slug = "administer-proc_basic_repo_sync"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/administer-proc_basic_repo_sync"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-proc_basic_repo_sync/toc/toc.json"
type = "aem-page"
+++

# Synchronize repositories in automation hub

Synchronize repositories in automation hub to update your custom repository with the latest collections from a configured remote.

## Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select Automation Content> (and then)Repositories.
3.  Locate your repository in the list and click More Actions icon **⋮**, then select **Sync repository**. All collections in the configured remote are downloaded to your custom repository. To check the status of the collection sync, select Automation Content> (and then)Task Management from the navigation panel.

  Note:
      To limit repository synchronization to specific collections within a remote, you can identify specific collections to be pulled by using a `requirements.yml` file.

## Export automation content from automation hub

When collections are finalized, you can import them to a location where they can be distributed to others across your organization.

### Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select Automation Content> (and then)Collections. The **Collections** page displays all collections across all repositories. You can search for a specific collection.
3.  Click into the collection that you want to export. The collection details page opens.
4.  From the **Install** tab, select **Download tarball**. The .tar file is downloaded to your default browser downloads folder. You can now import it to the location of your choosing.

## Import automation content to automation hub

As an automation content creator, you can import a collection to your custom repository.

### About this task

To use a collection in your custom repository, first import the collection into your namespace so the automation hub administrator can approve it.

### Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select Automation Content> (and then)Namespaces. The **Namespaces** page displays all of the namespaces available.
3.  Select the namespace to which you want to add your collection.
4.  Select the **Collections** tab.
5.  Click Upload Collection.
6.  Enter or browse to select a collection file.
7.  Select the repository pipeline to add the collection. The choices are **Staging repos** and **Repositories without pipeline**.
8.  Click Upload collection. The **Imports** screen displays a summary of tests and notifies you if the collection upload is successful or has failed. To find your imports, on your namespace click the More Actions icon **⋮** and select **Imports**.

  Note:
      If the collection is not approved, it is not displayed in the published repository.
