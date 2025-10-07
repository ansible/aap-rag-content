# 2. Managing collections in automation hub
## 2.4. Managing remote configurations in automation hub
### 2.4.1. Creating a remote configuration in automation hub




You can use Red Hat Ansible Automation Platform to create a remote configuration to an external collection source. Then, you can sync the content from those collections to your custom repositories.

**Procedure**

1. Log in to Ansible Automation Platform.
1. From the navigation panel, selectAutomation Content→Remotes.
1. ClickCreate Remote.
1. Enter a **Name** for the remote configuration.
1. Enter the **URL** for the remote server, including the path for the specific repository.

Note
To find the remote server URL and repository path, navigate toAutomation Content→Repositories, select theMore Actionsicon **⋮** , and selectCopy CLI configuration.




1. To sync signed collections only, check the box labeled **Signed collections only** .
1. To sync dependencies, check the box labeled **Sync all dependencies** . To turn off dependency syncing, leave this box unchecked.
1. Configure the credentials to the remote server by entering a **Token** or **Username** and **Password** required to access the external collection.

Note
To generate a token from the navigation panel, selectAutomation Content→API token, clickLoad tokenand copy the token that is loaded.




1. To access collections from console.redhat.com, enter the **SSO URL** to sign in to the identity provider (IdP).
1. Select or create a **Requirements file** to identify the collections and version ranges to synchronize with your custom repository. For example, to download only the kubernetes and AWS collection versions 5.0.0 or later the requirements file would look like this:


```
Collections:     	  - name: community.kubernetes    	  - name: community.aws     		version:”&gt;=5.0.0”
```


1. Optional: To configure your remote further, use the options available under **Show advanced options** :


1. If there is a corporate proxy in place for your organization, enter a **Proxy URL** , **Proxy Username** and **Proxy Password** .
1. Enable or disable transport layer security using the **TLS validation** checkbox.
1. If digital certificates are required for authentication, enter a **Client key** and **Client certificate** .
1. If you are using a self-signed SSL certificate for your server, enter the PEM encoded client certificate used for authentication in the **CA certificate** field.
1. To accelerate the speed at which collections in this remote can be downloaded, specify the number of collections that can be downloaded in tandem in the **Download concurrency** field.
1. To limit the number of queries per second on this remote, specify a **Rate Limit** .

Note
Some servers can have a specific rate limit set, and if exceeded, synchronization fails.







