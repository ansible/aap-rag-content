# Manage collection access and permissions with namespaces
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
8.  Configure the credentials to the remote server by entering a **Token** or **Username** and **Password** required to access the external collection.

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

