# 11. Projects
## 11.5. Collections support
### 11.5.1. Using collections with automation hub




Before automation controller can use automation hub as the default source for collections content, you must create an API token in the automation hub UI. You then specify this token in automation controller.

Use the following procedure to connect to private automation hub or automation hub, the only difference is which URL you specify.

**Procedure**

1. Go to [https://console.redhat.com/ansible/automation-hub/token](https://console.redhat.com/ansible/automation-hub/token) .
1. ClickLoad token.
1. Click the copy![Copy](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/df17e3afcfb728d4887b97e8605bd65c/copy.png)
icon to copy the API token to the clipboard.
1. Create a credential by choosing one of the following options:


1. To use automation hub, create an automation hub credential by using the copied token and pointing to the URLs shown in the **Server URL** and **SSO URL** fields of the token page:


-  **Galaxy Server URL** = `            <a class="link" href="https://console.redhat.com/ansible/automation-hub/token">https://console.redhat.com/ansible/automation-hub/token</a>`

1. To use private automation hub, create an automation hub credential using a token retrieved from the **Repo Management** dashboard of your private automation hub and pointing to the published repository URL as shown:

![image](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/a0939361183a30bca2cf6c0f666223e3/projects-ah-repo-mgmt-repos-published.png)


You can create different repositories with different namespaces or collections in them. For each repository in automation hub you must create a different credential.


1. Copy the **Ansible CLI URL** from the UI in the format of `        /https://$&lt;hub_url&gt;/api/galaxy/content/&lt;repo you want to pull from&gt;` into the **Galaxy Server URL** field of **Create Credential** :

For UI specific instructions, see [Red Hat Certified, validated, and Ansible Galaxy content in automation hub](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/managing_automation_content/managing-cert-valid-content) .



1. Go to the organization for which you want to synchronize content from and add the new credential to the organization. This enables you to associate each organization with the credential, or repository, that you want to use content from.

**Example**

You have two repositories:



-  _Prod_ : `        Namespace 1` and `        Namespace 2` , each with collection `        A` and `        B` so: `        namespace1.collectionA:v2.0.0` and `        namespace2.collectionB:v2.0.0`
-  _Stage_ : `        Namespace 1` with only collection `        A` so: `        namespace1.collectionA:v1.5.0` on , you have a repository URL for _Prod_ and _Stage_ .

You can create a credential for each one.

Then you can assign different levels of access to different organizations. For example, you can create a `        Developers` organization that has access to both repository, while an Operations organization just has access to the **Prod** repository only.

For UI specific instructions, see [Configuring user access for container repositories in private automation hub](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_automation_content/index#configuring-user-access-containers) .



1. If automation hub has self-signed certificates, use the toggle to enable the setting **Ignore Ansible Galaxy SSL Certificate Verification** in **Job Settings** . For automation hub, which uses a signed certificate, use the toggle to disable it instead. This is a global setting:
1. Create a project, where the source repository specifies the necessary collections in a requirements file located in the `    collections/requirements.yml` file. For information about the syntax to use, see [Using Ansible collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html#install-multiple-collections-with-a-requirements-file) in the Ansible documentation.
1. In the **Projects** list view, click the sync![Update](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/8ca24410ba90c880998d13dfe67a52b0/sync.png)
icon to update this project. Automation controller fetches the Galaxy collections from the `    collections/requirements.yml` file and reports it as changed. The collections are installed for any job template using this project.


Note
If updates are required from Galaxy or Collections, a sync is performed that downloads the required roles, consuming that much more space in your /tmp file. In cases where you have a large project (around 10 GB), disk space on `/tmp` may be an issue.



**Additional resources**

For more information about collections, see [Using Ansible Collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) .


For more information about how Red Hat publishes one of these official collections, which can be used to automate your install directly, see the [AWX Ansible Collection](https://github.com/ansible/awx/blob/devel/awx_collection/README.md) documentation.

