# Manage collection access and permissions with namespaces

Namespaces are unique locations in automation hub to which you can upload and publish content collections.

Namespace access is governed by teams with permission to manage the content and related information that appears there. You can use namespaces in automation hub to organize collections developed within your organization for internal distribution and use.

If you are working with namespaces, you must have a team that has permissions to create, edit and upload collections to namespaces. Collections uploaded to a namespace require administrative approval before you can publish them and make them available for use.

## Create a content development team

Create a new team in Ansible Automation Platform to support content curation and development in your organization.

### Before you begin

- You have administrative permissions in Ansible Automation Platform and can create teams.

### About this task

Your team can contribute internally-developed collections for publication in private automation hub.

To help content developers create a namespace and upload their internally developed collections to private automation hub, first create a team and assign the required permissions.

### Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select Access Management> (and then)Teams and click Create team.
3.  Enter **Content Engineering** as a **Name** for the team.
4.  Select an **Organization** for the team.
5.  Click Create team. The team Details page opens.
6.  Select the **Roles** tab and then select the **Automation Content** tab.
7.  Click Add roles.
8.  Select **Namespace** from the **Resource type** list and click Next.
9.  Select the namespaces that will receive the new roles and click Next.
10.  Select the roles to apply to the selected namespaces and click Next.
11.  Review your selections and click Finish.
12.  Click Close to complete the process.

### What to do next

The new team is created with the permissions that you assigned. You can now add users to the team in the **Users** tab.

## Create a namespace

Create a namespace to organize collections that your content developers upload to automation hub.

### Before you begin

- You have **Add Namespaces** and **Upload to Namespaces** permissions.

### About this task

When creating a namespace, you can assign a team in automation hub as owners of that namespace.

Tip:

By default, namespaces used on Ansible Galaxy are also used on automation hub by the Ansible partner team. For questions, contact <ansiblepartners@redhat.com>.

### Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select Automation Content> (and then)Namespaces.
3.  Click Create namespace and enter a **Name** for your namespace.
4.  Optional: enter a description, company, logo URL, resources, or useful links in the appropriate fields.
5.  Click Create namespace.
6.  Select the **Team Access** tab and click Add roles to assign roles to your namespace.
7.  Select the team to which you want to grant a role, then click Next.
8.  Select the roles you want to apply to the selected team, and then click Next.
9.  Review your selections and click Finish.
10.  Click Close to complete the process.

### What to do next

Your content developers can now upload collections to your new namespace. In addition, teams with permissions to upload to the namespace can start adding their collections for approval. Collections in the namespace appear in the **Published** repository after approval.

## Edit namespace resources

Edit the information associated with the namespace and provide resources for your users to accompany collections included in the namespace.

### Before you begin

- You have **Change Namespaces** permissions.

### About this task

Customize your namespace by adding a logo and a description, and link users to your GitHub repository, issue tracker, or other online assets. You can also enter markdown text in the **Resources** field to include more information. This is helpful to users who use your content in their automation tasks.

### Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select Automation Content> (and then)Namespaces.
3.  Select the namespace you want to edit.
4.  Click the Edit namespace.
5.  Enter the relevant information in the fields.
6.  Optional: enter markdown information in the **Resources** field.
7.  Click Save namespace.

## Upload collections to a namespace

Upload internally-developed collections in `tar.gz` file format to your private automation hub namespace for review and approval by an automation hub administrator.

### Before you begin

- You have a namespace to which you can upload the collection.


Important:

Attempting to upload very large collections will result in an error.

Limit collection size to 200 mb when uploading to console.redhat.com or private automation hub.

In scenarios that require a complete environment with multiple collections and dependencies, use an execution environment. See [Pull execution environments for use in automation hub](/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-con_container_registry#obtain-images "Before you can push execution environments to your private automation hub, you must first pull them from an existing registry and tag them for use.")for more information.

### About this task

When approved, the collection moves to the **Published** content repository where automation hub users can view and download it.

Note:

Format your collection file name as follows: <my_namespace-my_collection-1.0.0.tar.gz>

### Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select Automation Content> (and then)Namespaces and select a namespace.
3.  Select the **Collections** tab.
4.  Click Upload collection.
5.  Click Browse next to the **Collection file** field.
6.  Select the collection to upload.
7.  Select one of the following options:

-  **Staging repos**
-  **Repositories without pipeline**

8.  Click Upload collection.

### Results

To verify whether the collection uploaded successfully or if it failed, navigate to Automation Content> (and then)Namespaces and click the More Actions icon **⋮**, then select **Imports**. There you will find a summary of tests indicating whether the import was successful.

## Review your namespace import logs

Review the status of collections uploaded to your namespaces to evaluate success or failure of the process.

### Before you begin

- You have access to a namespace to which you can upload collections.

### About this task

Imported collection information includes:

Status
completed or failed

Approval status
waiting for approval or approved

Version
the version of the uploaded collection

Import log
activities executed during the collection import

### Procedure

1.  Log in to your Ansible Automation Platform.
2.  From the navigation panel, select Automation Content> (and then)Namespaces.
3.  Select a namespace.
4.  Click the More Actions icon **⋮** and select **Imports**.
5.  Use the search field or locate an imported collection from the list.
6.  Click the imported collection.
7.  Review collection import details to determine the status of the collection in your namespace.

## Delete a collection

You can further manage your collections by deleting content, if the content has no dependencies.

### Before you begin

- The content being deleted does not have dependencies with other content.
- You have **Delete Collections** permissions.

### About this task

The **Dependencies** tab on a collection displays a list of other collections that use the current collection.

### Procedure

1.  Log in to your Ansible Automation Platform.
2.  From the navigation panel, select Automation Content> (and then)Collections.
3.  Before deleting the collection, check to see if it has collections that are dependent on it:

- Click the **Dependencies** tab for that collection. If it is blank, you will be able to delete the collection. If the **Dependencies** tab is not blank, you must delete these dependencies before you can delete the collection.

4.  Click the collection to delete.
5.  Click the More Actions icon **⋮**, and then select an option:
1.  **Delete version from system** removes the specific version of the collection from the entire instance, including all repositories and namespaces.
2.  **Delete version from repository** removes the specific version of the collection from the repository where it was uploaded. This does not affect the collection in other repositories or namespaces.
3.  **Delete entire collection from repository** removes all versions of the entire collection from the repository where it was uploaded, but does not affect other repositories or namespaces.
4.  **Delete entire collection from system** removes all versions of the entire collection from the instance, including all repositories and namespaces.
6.  When the confirmation window opens, verify that the collection or version number is correct, and then select **Delete**.

## Delete a namespace

You can delete unwanted namespaces to manage storage on your automation hub server.

### Before you begin

- The namespace you are deleting does not have a collection with dependencies.
- You have **Delete namespace** permissions.

### About this task

First, ensure that the namespace you want to delete does not contain a collection with dependencies.

### Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select Automation Content> (and then)Namespaces.
3.  Click the namespace to be deleted.
4.  Click the More Actions icon **⋮**, then click Delete namespace. Note:
If the Delete namespace button is disabled, the namespace contains a collection with dependencies. Review the collections in this namespace, and delete any dependencies.

### Results

The namespace that you deleted, as well as its associated collections, is now deleted and removed from the namespace list view.

## Create a remote configuration in automation hub

Remote configurations allow you to sync content to your custom repositories from an external collection source.

### About this task

In automation hub, you can create a remote configuration to an external collection source. Then, you can sync the content from those collections to your custom repositories.

### Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select Automation Content> (and then)Remotes.
3.  Click Create Remote.
4.  Enter a **Name** for the remote configuration.
5.  Enter the **URL** for the remote server, including the path for the specific repository. Note:
To find the remote server URL and repository path, navigate to Automation Content> (and then)Repositories, select the More Actions icon **⋮**, and select Copy CLI configuration.

6.  To sync signed collections only, check the box labeled **Signed collections only**.
7.  To sync dependencies, check the box labeled **Sync all dependencies**. To turn off dependency syncing, leave this box unchecked.
8.  Configure the credentials to the remote server by entering a **Token** or **Username** and **Password** required to access the external collection. Note:
To generate a token from the navigation panel, select Automation Content> (and then)API token, click Load token and copy the token that is loaded.

9.  To access collections from console.redhat.com, enter the **SSO URL** to sign in to the identity provider (IdP).
10.  Select or create a **Requirements file** to identify the collections and version ranges to synchronize with your custom repository. For example, to download only the kubernetes and AWS collection versions 5.0.0 or later the requirements file would look like this:


```
Collections:
- name: community.kubernetes
- name: community.aws
version:”>=5.0.0”
```

11.  Optional: To configure your remote further, use the options available under **Show advanced options**:
1.  If there is a corporate proxy in place for your organization, enter a **Proxy URL**, **Proxy Username** and **Proxy Password**.
2.  Enable or disable transport layer security using the **TLS validation** checkbox.
3.  If digital certificates are required for authentication, enter a **Client key** and **Client certificate**.
4.  If you are using a self-signed SSL certificate for your server, enter the PEM encoded client certificate used for authentication in the **CA certificate** field.
5.  To accelerate the speed at which collections in this remote can be downloaded, specify the number of collections that can be downloaded in tandem in the **Download concurrency** field.
6.  To limit the number of queries per second on this remote, specify a **Rate Limit**. Note:
Some servers can have a specific rate limit set, and if exceeded, synchronization fails.

### Assign access to a remote configuration

After you create a remote configuration, you must provide access to it before anyone can use it.

#### Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select Automation Content> (and then)Remotes.
3.  Click into your repository in the list, and then select the **Team Access** tab.
4.  Click Add roles.
5.  Select the team to which you want to grant a role, then click Next.
6.  Select the roles you want to apply to the selected team, and then click Next.
7.  Review your selections and click Finish.
8.  Click Close to complete the process.
