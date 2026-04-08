# 7. Target environment
## 7.3. Managed Ansible Automation Platform
### 7.3.2. Reconciling the target environment post-migration




Update necessary configurations after migrating to Managed Ansible Automation Platform.

**Procedure**

1. Log in to the Managed Ansible Automation Platform instance by using the local administrator account to confirm that data was imported.
1. Perform the following actions based on the configuration of the source deployment:


1. Reconfigure Single Sign-On (SSO) authenticators and mappings to reflect the new URLs.
1. Update private automation hub content to reflect the new URLs.


1. Run the following command to update the automation hub repositories:


```
curl -d '{\"verify_checksums\": true }' -X POST -k https://&lt;platform url&gt;/api/galaxy/pulp/api/v3/repair/ -u &lt;admin_user&gt;:&lt;admin_password&gt;
```


1. Perform a sync on any repositories configured in automation hub.
1. Push any custom execution environments from the source automation hub to the target automation hub.

1. Reconfigure automation mesh.

1. After migration, you can request standard Site Reliability Engineering (SRE) tasks through support tickets, such as configuration of custom certificates, a custom domain, or connectivity through private endpoints.



<span id="idm140013699397040"></span>
