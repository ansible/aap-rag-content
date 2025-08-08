# 7. Target environment
## 7.3. Managed Ansible Automation Platform
### 7.3.2. Reconciling the target environment post-migration




After a successful migration, perform the following tasks:

**Procedure**

1. Log in to the Managed Ansible Automation Platform instance by using the local administrator account to confirm that data was properly imported.
1. You might need to perform the following actions based on the configuration of the source deployment:


1. Reconfigure SSO authenticators and mappings to reflect the new URLs.
1. Update private automation hub content to reflect the new URLs.


1. Run the following command to update the automation hub repositories:


```
`curl -d '{"verify_checksums": true }' -X POST -k https://&lt;platform_url&gt;/api/galaxy/pulp/api/v3/repair/ -u &lt;admin_user&gt;:&lt;admin_password&gt;`
```


1. Perform a sync on any repositories configured in automation hub.
1. Push any custom execution environments from the source automation hub to the target automation hub.

1. Reconfigure automation mesh.

1. Following migration, you can request standard SRE tasks through support tickets for the SRE team to perform such as configuration of custom certificates, a custom domain, or connectivity through private endpoints.



<span id="idm139928868156544"></span>
