# 3. Installing Red Hat Ansible Automation Platform
## 3.2. Inventory file examples based on installation scenarios
### 3.2.2. Setting registry_username and registry_password




When using the `registry_username` and `registry_password` variables for an online non-bundled installation, you need to create a new registry service account.

Registry service accounts are named tokens that can be used in environments where credentials will be shared, such as deployment systems.

**Procedure**

1. Go to [https://access.redhat.com/terms-based-registry/accounts](https://access.redhat.com/terms-based-registry/accounts) .
1. On the **Registry Service Accounts** page clickNew Service Account.
1. Enter a name for the account using only the allowed characters.
1. Optionally enter a description for the account.
1. ClickCreate.
1. Find the created account in the list by searching for your name in the search field.
1. Click the name of the account that you created.
1. Alternatively, if you know the name of your token, you can go directly to the page by entering the URL:


```
https://access.redhat.com/terms-based-registry/token/&lt;name-of-your-token&gt;
```


1. A **token** page opens, displaying a generated username (different from the account name) and a token.


1. If no token is displayed, clickRegenerate Token. You can also click this to generate a new username and token.

1. Copy the username (for example "1234567|testuser") and use it to set the variable `    registry_username` .
1. Copy the token and use it to set the variable `    registry_password` .


#### 3.2.2.1. Configuring Redis




Ansible Automation Platform offers a centralized Redis instance in both `standalone` and `clustered` topologies.

In RPM deployments, the Redis mode is set to `cluster` by default. You can change this setting in the inventory file `[all:vars]` section as in the following example:

```
[all:vars]
admin_password='&lt;password&gt;'
pg_host='data.example.com'
pg_port='5432'
pg_database='awx'
pg_username='awx'
pg_password='&lt;password&gt;'
pg_sslmode='prefer'  # set to 'verify-full' for client-side enforced SSL

registry_url='registry.redhat.io'
registry_username='&lt;registry username&gt;'
registry_password='&lt;registry password&gt;'

redis_mode=cluster
```

For more information about Redis, see [Caching and queueing system](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/planning_your_installation/ha-redis_planning) in _Planning your installation_ .

