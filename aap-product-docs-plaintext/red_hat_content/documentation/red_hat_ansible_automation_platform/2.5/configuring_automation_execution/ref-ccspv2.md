# 12. Usage reporting with metrics-utility
## 12.5. Report types
### 12.5.1. CCSPv2




CCSPv2 is a report which shows the following:

- Directly and indirectly managed node usage
- The content of all inventories
- Content usage


The primary use of this report is for partners under the [CCSP](https://connect.redhat.com/en/programs/certified-cloud-service-provider) program, but all customers can use it to obtain on-premise reporting showing managed nodes, jobs and content usage across their automation controller organizations.

Set the report type using `METRICS_UTILITY_REPORT_TYPE=CCSPv2` .

### 12.5.2. Optional collectors for `gather` command




You can use the following optional collectors for the `gather` command:

-  `    main_jobhostsummary`


- If present by default, this incrementally collects data from the `        main_jobhostsummary` table in the automation controller database, containing information about jobs runs and managed nodes automated.

-  `    main_host`


- This collects daily snapshots of the `        main_host` table in the automation controller database and has managed nodes and hosts present across automation controller inventories.

-  `    main_jobevent`


- This incrementally collects data from the `        main_jobevent` table in the automation controller database and contains information about which modules, roles, and Ansible collections are being used.

-  `    main_indirectmanagednodeaudit`


- This incrementally collects data from the `        main_indirectmanagednodeaudit` table in the automation controller database and contains information about indirectly managed nodes.


```
# Example with all optional collectors        export METRICS_UTILITY_OPTIONAL_COLLECTORS="main_host,main_jobevent,main_indirectmanagednodeaudit"
```





### 12.5.3. Optional sheets for `build_report` command




You can use the following optional sheets for the `build_report` command:

-  `    ccsp_summary`


- This is a landing page specifically for partners under CCSP program. This report takes additional parameters to customize the summary page. For more information, see the following example:


```
export METRICS_UTILITY_PRICE_PER_NODE=11.55 # in USD        export METRICS_UTILITY_REPORT_SKU=MCT3752MO        export METRICS_UTILITY_REPORT_SKU_DESCRIPTION="EX: Red Hat Ansible Automation Platform, Full Support (1 Managed Node, Dedicated, Monthly)"        export METRICS_UTILITY_REPORT_H1_HEADING="CCSP NA Direct Reporting Template"        export METRICS_UTILITY_REPORT_COMPANY_NAME="Partner A"        export METRICS_UTILITY_REPORT_EMAIL="email@email.com"        export METRICS_UTILITY_REPORT_RHN_LOGIN="test_login"        export METRICS_UTILITY_REPORT_PO_NUMBER="123"        export METRICS_UTILITY_REPORT_END_USER_COMPANY_NAME="Customer A"        export METRICS_UTILITY_REPORT_END_USER_CITY="Springfield"        export METRICS_UTILITY_REPORT_END_USER_STATE="TX"        export METRICS_UTILITY_REPORT_END_USER_COUNTRY="US"
```



-  `    jobs`


- This is a list of automation controller jobs launched. It is grouped by job template.

-  `    managed_nodes`


- This is a deduplicated list of managed nodes automated by automation controller.

-  `    indirectly_managed_nodes`


- This is a deduplicated list of indirect managed nodes automated by automation controller.

-  `    inventory_scope`


- This is a deduplicated list of managed nodes present across all inventories of automation controller.

-  `    usage_by_organizations`


- This is a list of all automation controller organizations with several metrics showing the organizations usage. This provides data suitable for doing internal chargeback.

-  `    usage_by_collections`


- This is a list of Ansible collections used in a automation controller job runs.

-  `    usage_by_roles`


- This is a list of roles used in automation controller job runs.

-  `    usage_by_modules`


- This is a list of modules used in automation controller job runs.

-  `    managed_nodes_by_organization`


- This generates a sheet per organization, listing managed nodes for every organization with the same content as the managed_nodes sheet.

-  `    data_collection_status`


- This generates a sheet with the status of every data collection done by the `        gather` command for the date range the report is built for.



To outline the quality of data collected it also lists:

- unusual gaps between collections (based on collection_start_timestamp)
- gaps in collected intervals (based on since vs until)


```
# Example with all optional sheets    export METRICS_UTILITY_OPTIONAL_CCSP_REPORT_SHEETS='ccsp_summary,jobs,managed_nodes,indirectly_managed_nodes,inventory_scope,usage_by_organizations,usage_by_collections,usage_by_roles,usage_by_modules,data_collection_status'
```




### 12.5.4. Filtering reports by organization




To filter your report so that only certain organizations are present, use this environment variable with a semicolon separated list of organization names.

`export METRICS_UTILITY_ORGANIZATION_FILTER="ACME;Organization 1"`

This renders only the data from these organizations in the built report. This filter currently does not have any effect on the following optional sheets:

-  `    usage_by_collections`
-  `    usage_by_roles`
-  `    usage_by_modules`


### 12.5.5. Selecting a date range for your CCSPv2 report




The default behavior of the CCSPv2 report is to build a report for the previous month. The following examples describe how to override this default behavior to select a specific date range for your report:

```
# Build report for a specific month
metrics-utility build_report --month=2025-03

# Build report for a specific date range, icluding the prvided days
metrics-utility build_report --since=2025-03-01 --until=2025-03-31

# Build report for a last 6 months from a current date
metrics-utility build_report --since=6months

# Build report for a last 6 months from a current date overriding an exisitng report
metrics-utility build_report --since=6months --force
```

### 12.5.6. `RENEWAL_GUIDANCE`




The `RENEWAL_GUIDANCE` report provides historical usage from the HostMetric table, applying deduplication and showing real historical usage for renewal guidance purposes.

To generate this report, set the report type to `METRICS_UTILITY_REPORT_TYPE=RENEWAL_GUIDANCE` .

Important
This report is currently a tech preview solution. It is designed to provide more information than automation controller when built in the `awx-manage host_metric` command.



#### 12.5.6.1. Storage and invocation




The `RENEWAL_GUIDANCE` report supports the use of only local disk storage to store the report results. This report does not have a gather data step. It reads directly from the controller HostMetric table, so it does not store any raw data under the `METRICS_UTILITY_SHIP_PATH` .

```
# All parameters the RENEWAL_GUIDANCE report needs
export METRICS_UTILITY_SHIP_TARGET=controller_db
export METRICS_UTILITY_REPORT_TYPE=RENEWAL_GUIDANCE
export METRICS_UTILITY_SHIP_PATH=/path_to_built_report/...

# Will generate report for 12 months back with epehemeral nodes being nodes
# automated for less than 1 month.
metrics-utility build_report --since=12months --ephemeral=1month
```

#### 12.5.6.2. Showing ephemeral usage




The `RENEWAL_GUIDANCE` report has the capability to list additional sheets with ephemeral usage if the `–ephemeral` parameter is provided. Using the parameter `--ephemeral=1month` , you can define ephemeral nodes as any managed node that has been automated for a maximum of one month, then never automated again. Using this parameter, the total ephemeral usage of the 12-month period is computed as maximum ephemeral nodes used over all 1-month rolling date windows. This sheet is also added into the report.

```
# Will generate report for 12 months back with epehemeral nodes being nodes
# automated for less than 1 month.
metrics-utility build_report --since=12months --ephemeral=1month
```

#### 12.5.6.3. Selecting a date range for your `RENEWAL_GUIDANCE` report




The `RENEWAL_GUIDANCE` report requires a `since` parameter as the parameter is not supported due to the nature of the HostMetric data and is always set to `now` . To override a report date range that has already been built, use parameter `–force` with the command. For more information, see the following examples:

```
# Build report for a specific date range, including the provided days
metrics-utility build_report --since=2025-03-01

# Build report for a last 12 months from a current date
metrics-utility build_report --since=12months

# Build report for a last 12 months from a current date overriding an existing report
metrics-utility build_report --since=12months --force
```

### 12.5.7. CCSP




`CCSP` is the original report format. It does not include many of the customization of CCSPv2, and it is intended to be used only for the CCSP partner program.

### 12.5.8. Optional collectors for `gather` command




You can use the following optional collectors for the `gather` command:

-  `    main_jobhostsummary`


- If present by default, this incrementally collects the `        main_jobhostsummary` table from the automation controller database, containing information about jobs runs and managed nodes automated.

-  `    main_host`


- This collects daily snapshots of the `        main_host` table from the automation controller database and has managed nodes/hosts present across automation controller inventories,

-  `    main_jobevent`


- This incrementally collects the `        main_jobevent` table from the automation controller database and contains information about which modules, roles, and ansible collections are being used.

- main_indirectmanagednodeaudit


- This incrementally collects the `        main_indirectmanagednodeaudit` table from the automation controller database and contains information about indirectly managed nodes,



```
# Example with all optional collectors
export METRICS_UTILITY_OPTIONAL_COLLECTORS="main_host,main_jobevent,main_indirectmanagednodeaudit"
```

### 12.5.9. Optional sheets for `build_report` command




You may use the following optional sheets for the `build_report` command:

-  `    ccsp_summary`


- This is a landing page specifically for partners under the CCSP program. It shows managed node usage by each automation controller organization.
- This report takes additional parameters to customize the summary page. For more information, see the following example:


```
export METRICS_UTILITY_PRICE_PER_NODE=11.55 # in USD        export METRICS_UTILITY_REPORT_SKU=MCT3752MO        export METRICS_UTILITY_REPORT_SKU_DESCRIPTION="EX: Red Hat Ansible Automation Platform, Full Support (1 Managed Node, Dedicated, Monthly)"        export METRICS_UTILITY_REPORT_H1_HEADING="CCSP Reporting &lt;Company&gt;: ANSIBLE Consumption"        export METRICS_UTILITY_REPORT_COMPANY_NAME="Company Name"        export METRICS_UTILITY_REPORT_EMAIL="email@email.com"        export METRICS_UTILITY_REPORT_RHN_LOGIN="test_login"        export METRICS_UTILITY_REPORT_COMPANY_BUSINESS_LEADER="BUSINESS LEADER"        export METRICS_UTILITY_REPORT_COMPANY_PROCUREMENT_LEADER="PROCUREMENT LEADER"
```



-  `    managed_nodes`


- This is a deduplicated list of managed nodes automated by automation controller.

-  `    indirectly_managed_nodes`


- This is a deduplicated list of indirect managed nodes automated by automation controller.

-  `    inventory_scope`


- This is a deduplicated list of managed nodes present across all inventories of automation controller.

-  `    usage_by_collections`


- This is a list of Ansible collections used in automation controller job runs.

-  `    usage_by_roles`


- This is a list of roles used in automation controller job runs. * `        usage_by_modules`
- This is a list of modules used in automation controllerjob runs.



```
# Example with all optional sheets
export METRICS_UTILITY_OPTIONAL_CCSP_REPORT_SHEETS='ccsp_summary,managed_nodes,indirectly_managed_nodes,inventory_scope,usage_by_collections,usage_by_roles,usage_by_modules'
```

### 12.5.10. Selecting a date range for your CCSP report




The default behavior of this report is to build a report for the previous month. The following examples describe how to override this default behavior to select a specific date range for your report:

```
# Builds report for a previous month
metrics-utility build_report

# Build report for a specific month
metrics-utility build_report --month=2025-03

# Build report for a specific month overriding an existing report
metrics-utility build_report --month=2025-03 --force
```

# Chapter 13. Secret management system




Users and system administrators upload machine and cloud credentials so that automation can access machines and external services on their behalf. By default, sensitive credential values such as SSH passwords, SSH private keys, and API tokens for cloud services are stored in the database after being encrypted.

With external credentials backed by credential plugins, you can map credential fields (such as a password or an SSH Private key) to values stored in a `secret management system` instead of providing them to automation controller directly.

Automation controller provides a secret management system that include integrations for:

- AWS Secrets Manager Lookup
- Centrify Vault Credential Provider Lookup
-  _CyberArk Central Credential Provider_ Lookup (CCP)
- CyberArk Conjur Secrets Manager Lookup
- HashiCorp Vault _Key-Value_ Store (KV)
- HashiCorp Vault SSH Secrets Engine
- Microsoft Azure _Key Management System_ (KMS)
- Thycotic DevOps Secrets Vault
- Thycotic Secret Server
- GitHub app token lookup


These external secret values are fetched before running a playbook that needs them.

**Additional resources**

For more information about specifying secret management system credentials in the user interface, see [Managing user credentials](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/index#controller-credentials) .


## 13.1. Configuring and linking secret lookups




When pulling a secret from a third-party system, you are linking credential fields to external systems. To link a credential field to a value stored in an external system, select the external credential corresponding to that system and provide `metadata` to look up the required value. The metadata input fields are part of the external credential type definition of the source credential.

Automation controller provides a credential plugin interface for developers, integrators, system administrators, and power-users with the ability to add new external credential types to extend it to support other secret management systems.

Use the following procedure to use automation controller to configure and use each of the supported third-party secret management systems.

**Procedure**

1. Create an external credential for authenticating with the secret management system. At minimum, give a name for the external credential and select one of the following for the **Credential type** field:


-  [AWS Secrets Manager Lookup](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/assembly-controller-secret-management#ref-aws-secrets-manager-lookup)
-  [Centrify Vault Credential Provider Lookup](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/assembly-controller-secret-management#ref-centrify-vault-lookup)
-  [CyberArk Central Credential Provider (CCP) Lookup](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/assembly-controller-secret-management#ref-cyberark-ccp-lookup)
-  [CyberArk Conjur Secrets Manager Lookup](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/assembly-controller-secret-management#ref-cyberark-conjur-lookup)
-  [HashiCorp Vault Secret Lookup](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/assembly-controller-secret-management#ref-hashicorp-vault-lookup)
-  [HashiCorp Vault Signed SSH](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/assembly-controller-secret-management#ref-hashicorp-signed-ssh)
-  [Microsoft Azure Key Vault](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/assembly-controller-secret-management#ref-azure-key-vault-lookup)
-  [Thycotic DevOps Secrets Vault](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/assembly-controller-secret-management#ref-thycotic-devops-vault)
-  [Thycotic Secret Server](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/assembly-controller-secret-management#ref-thycotic-secret-server)
-  [Configuring a GitHub App Installation Access Token Lookup](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/assembly-controller-secret-management#controller-github-app-token)

In this example, the _Demo Credential_ is the target credential.



1. For any of the fields that follow the **Type Details** area that you want to link to the external credential, click the key![Link](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Configuring_automation_execution-en-US/images/fc669abfeec02bb8bda89a0de40c0391/leftkey.png)
icon in the input field to link one or more input fields to the external credential along with metadata for locating the secret in the external system.
1. Select the input source to use to retrieve your secret information.
1. Select the credential you want to link to, and clickNext. This takes you to the **Metadata** tab of the input source. This example shows the Metadata prompt for HashiVault Secret Lookup. Metadata is specific to the input source you select.

For more information, see the [Metadata for credential input sources](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#ref-controller-metadata-credential-input) table.


1. ClickTestto verify connection to the secret management system. If the lookup is unsuccessful, an error message displays:
1. ClickOK. You return to the **Details** screen of your target credential.
1. Repeat these steps, starting with Step 3 to complete the remaining input fields for the target credential. By linking the information in this manner, automation controller retrieves sensitive information, such as username, password, keys, certificates, and tokens from the third-party management systems and populates the remaining fields of the target credential form with that data.
1. If necessary, supply any information manually for those fields that do not use linking as a way of retrieving sensitive information. For more information about each of the fields, see the appropriate [Credential types](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#ref-controller-credential-types) .
1. ClickSave.


**Additional resources**

For more information, see the development documents for [Credential plugins](https://github.com/ansible/awx/blob/devel/docs/credentials/credential_plugins.md) .


### 13.1.1. Metadata for credential input sources




The information required for the **Metadata** tab of the input source.

**AWS Secrets Manager Lookup**

| Metadata | Description |
| --- | --- |
| AWS Secrets Manager Region (required) | The region where the secrets manager is located. |
| AWS Secret Name (required) | Specify the AWS secret name that was generated by the AWS access key. |


**Centrify Vault Credential Provider Lookup**

| Metadata | Description |
| --- | --- |
| Account name (required) | Name of the system account or domain associated with Centrify Vault. |
| System Name | Specify the name used by the Centrify portal. |


**CyberArk Central Credential Provider Lookup**

| Metadata | Description |
| --- | --- |
| Object Query (Required) | Lookup query for the object. |
| Object Query Format | Select `Exact` for a specific secret name, or `Regexp` for a secret that has a dynamically generated name. |
| Object Property | Specifies the name of the property to return. For example, `UserName` or `Address` other than the default of `Content` . |
| Reason | If required for the object’s policy, supply a reason for checking out the secret, as CyberArk logs those. |


**CyberArk Conjur Secrets Lookup**

| Metadata | Description |
| --- | --- |
| Secret Identifier | The identifier for the secret. |
| Secret Version | Specify a version of the secret, if necessary, otherwise, leave it empty to use the latest version. |


**HashiVault Secret Lookup**

| Metadata | Description |
| --- | --- |
| Name of Secret Backend | Specify the name of the KV backend to use. Leave it blank to use the first path segment of the **Path to Secret** field instead. |
| Path to Secret (required) | Specify the path to where the secret information is stored; for example, `/path/username` . |
| Key Name (required) | Specify the name of the key to look up the secret information. |
| Secret Version (V2 Only) | Specify a version if necessary, otherwise, leave it empty to use the latest version. |


**HashiCorp Signed SSH**

| Metadata | Description |
| --- | --- |
| Unsigned Public Key (required) | Specify the public key of the certificate you want to have signed. It needs to be present in the authorized keys file of the target hosts. |
| Path to Secret (required) | Specify the path to where the secret information is stored; for example, `/path/username` . |
| Role Name (required) | A role is a collection of SSH settings and parameters that are stored in Hashi vault. Typically, you can specify some with different privileges or timeouts, for example. So you could have a role that is permitted to get a certificate signed for root, and other less privileged ones, for example. |
| Valid Principals | Specify a user (or users) other than the default, that you are requesting vault to authorize the cert for the stored key. Hashi vault has a default user for whom it signs, for example, ec2-user. |


**Microsoft Azure KMS**

| Metadata | Description |
| --- | --- |
| Secret Name (required) | The name of the secret as it is referenced in Microsoft Azure’s Key vault app. |
| Secret Version | Specify a version of the secret, if necessary, otherwise, leave it empty to use the latest version. |


**Thycotic DevOps Secrets Vault**

| Metadata | Description |
| --- | --- |
| Secret Path (required) | Specify the path to where the secret information is stored, for example, /path/username. |


**Thycotic Secret Server**

| Metadata | Description |
| --- | --- |
| Secret ID (required) | The identifier for the secret. |
| Secret Field | Specify the field to be used from the secret. |


### 13.1.2. AWS Secrets Manager lookup




This plugin enables Amazon Web Services to be used as a credential input source to pull secrets from the Amazon Web Services Secrets Manager. The AWS Secrets Manager provides similar service to Microsoft Azure Key Vault, and the AWS collection provides a lookup plugin for it.

When AWS Secrets Manager lookup is selected for **Credential type** , give the following metadata to configure your lookup:

-  **AWS Access Key** (required): give the access key used for communicating with AWS key management system
-  **AWS Secret Key** (required): give the secret as obtained by the AWS IAM console


### 13.1.3. Centrify Vault Credential Provider Lookup




You need the Centrify Vault web service running to store secrets for this integration to work. When you select **Centrify Vault Credential Provider Lookup** for **Credential Type** , give the following metadata to configure your lookup:

-  **Centrify Tenant URL** (required): give the URL used for communicating with Centrify’s secret management system
-  **Centrify API User** (required): give the username
-  **Centrify API Password** (required): give the password
-  **OAuth2 Application ID** : specify the identifier given associated with the OAuth2 client
-  **OAuth2 Scope** : specify the scope of the OAuth2 client


### 13.1.4. CyberArk Central Credential Provider (CCP) Lookup




The CyberArk Central Credential Provider web service must be running to store secrets for this integration to work. When you select **CyberArk Central Credential Provider Lookup** for **Credential Type** , give the following metadata to configure your lookup:

-  **CyberArk CCP URL** (required): give the URL used for communicating with CyberArk CCP’s secret management system. It must include the URL scheme such as http or https.
- Optional: **Web Service ID** : specify the identifier for the web service. Leaving this blank defaults to AIMWebService.
-  **Application ID** (required): specify the identifier given by CyberArk CCP services.
-  **Client Key** : paste the client key if provided by CyberArk.
-  **Client Certificate** : include the `    BEGIN CERTIFICATE` and `    END CERTIFICATE` lines when pasting the certificate, if provided by CyberArk.
-  **Verify SSL Certificates** : this option is only available when the URL uses HTTPS. Check this option to verify that the server’s SSL/TLS certificate is valid and trusted. For environments that use internal or private CA’s, leave this option unchecked to disable verification.


### 13.1.5. CyberArk Conjur Secrets Manager Lookup




With a Conjur Cloud tenant available to target, configure the CyberArk Conjur Secrets Lookup external management system credential plugin.

When you select **CyberArk Conjur Secrets Manager Lookup** for **Credential Type** , give the following metadata to configure your lookup:

-  **Conjur URL** (required): provide the URL used for communicating with CyberArk Conjur’s secret management system. This must include the URL scheme, such as http or https.
-  **API Key** (required): provide the key given by your Conjur admin
-  **Account** (required): the organization’s account name
-  **Username** (required): the specific authenticated user for this service
-  **Public Key Certificate** : include the `    BEGIN CERTIFICATE` and `    END CERTIFICATE` lines when pasting the public key, if provided by CyberArk


### 13.1.6. HashiCorp Vault Secret Lookup




When you select **HashiCorp Vault Secret Lookup** for **Credential Type** , give the following metadata to configure your lookup:

-  **Server URL** (required): give the URL used for communicating with HashiCorp Vault’s secret management system.
-  **Token** : specify the access token used to authenticate HashiCorp’s server.
-  **CA Certificate** : specify the CA certificate used to verify HashiCorp’s server.
-  **AppRole role_id** : specify the ID if using AppRole for authentication.
-  **AppRole secret_id** : specify the corresponding secret ID for AppRole authentication.
-  **Client Certificate** : specify a PEM-encoded client certificate when using the TLS authentication method, including any required intermediate certificates expected by Hashicorp Vault.
-  **Client Certificate Key** : specify a PEM-encoded certificate private key when using the TLS authentication method.
-  **TLS Authentication Role** : specify the role or certificate name in Hashicorp Vault that corresponds to your client certificate when using the TLS authentication method. If it is not provided, Hashicorp Vault attempts to match the certificate automatically.
-  **Namespace name** : specify the Namespace name (Hashicorp Vault enterprise only).
-  **Kubernetes role** : specify the role name when using Kubernetes authentication.
-  **Username** : enter the username of the user to be used to authenticate this service.
-  **Password** : enter the password associated with the user to be used to authenticate this service.
-  **Path to Auth** : specify a path if other than the default path of `    /approle` .
-  **API Version** (required): select v1 for static lookups and v2 for versioned lookups.


LDAP authentication requires LDAP to be configured in HashiCorp’s Vault UI and a policy added to the user. Cubbyhole is the name of the default secret mount. If you have proper permissions, you can create other mounts and write key values to those.

To test the lookup, create another credential that uses Hashicorp Vault lookup.

**Additional resources**

For more detail about the LDAP authentication method and its fields, see the [Vault documentation for LDAP auth method](https://developer.hashicorp.com/vault/docs/auth/ldap) .


For more information about AppRole authentication method and its fields, see the [Vault documentation for AppRole auth method](https://developer.hashicorp.com/vault/docs/auth/approle) .

For more information about the userpass authentication method and its fields, see the [Vault documentation for userpass auth method](https://developer.hashicorp.com/vault/docs/auth/userpass) .

For more information about the Kubernetes auth method and its fields, see the [Vault documentation for Kubernetes auth method](https://developer.hashicorp.com/vault/docs/auth/kubernetes) .

For more information about the TLS certificate auth method and its fields, see the [Vault documentation for TLS certificates auth method](https://developer.hashicorp.com/vault/docs/auth/cert) .

### 13.1.7. HashiCorp Vault Signed SSH




When you select **HashiCorp Vault Signed SSH** for **Credential Type** , give the following metadata to configure your lookup:

-  **Server URL** (required): give the URL used for communicating with HashiCorp Signed SSH’s secret management system.
-  **Token** : specify the access token used to authenticate HashiCorp’s server.
-  **CA Certificate** : specify the CA certificate used to verify HashiCorp’s server.
-  **AppRole role_id** : specify the ID for AppRole authentication.
-  **AppRole secret_id** : specify the corresponding secret ID for AppRole authentication.
-  **Client Certificate** : specify a PEM-encoded client certificate when using the TLS authentication method, including any required intermediate certificates expected by Hashicorp Vault.
-  **Client Certificate Key** : specify a PEM-encoded certificate private key when using the TLS authentication method.
-  **TLS Authentication Role** : specify the role or certificate name in Hashicorp Vault that corresponds to your client certificate when using the TLS authentication method. If it is not provided, Hashicorp Vault attempts to match the certificate automatically.
-  **Namespace name** : specify the Namespace name (Hashicorp Vault enterprise only).
-  **Kubernetes role** : specify the role name when using Kubernetes authentication.
-  **Username** : enter the username of the user to be used to authenticate this service.
-  **Password** : enter the password associated with the user to be used to authenticate this service.
-  **Path to Auth** : specify a path if other than the default path of `    /approle` .


**Additional resources**

For more information about AppRole authentication method and its fields, see the [Vault documentation for AppRole Auth Method](https://developer.hashicorp.com/vault/docs/auth/approle) .


For more information about the Kubernetes authentication method and its fields, see the [Vault documentation for Kubernetes auth method](https://developer.hashicorp.com/vault/docs/auth/kubernetes) .

For more information about the TLS certificate auth method and its fields, see the [Vault documentation for TLS certificates auth method](https://developer.hashicorp.com/vault/docs/auth/cert) .

### 13.1.8. Microsoft Azure Key Vault




When you select **Microsoft Azure Key Vault** for **Credential Type** , give the following metadata to configure your lookup:

-  **Vault URL (DNS Name)** (required): give the URL used for communicating with Microsoft Azure’s key management system
-  **Client ID** (required): give the identifier as obtained by Microsoft Entra ID
-  **Client Secret** (required): give the secret as obtained by Microsoft Entra ID
-  **Tenant ID** (required): give the unique identifier that is associated with an Microsoft Entra ID instance within an Azure subscription
-  **Cloud Environment** : select the applicable cloud environment to apply


### 13.1.9. Thycotic DevOps Secrets Vault




When you select **Thycotic DevOps Secrets Vault** for **Credential Type** , give the following metadata to configure your lookup:

-  **Tenant** (required): give the URL used for communicating with Thycotic’s secret management system
-  **Top-level Domain (TLD)** : give the top-level domain designation, for example .com, .edu, or .org, associated with the secret vault you want to integrate
-  **Client ID** (required): give the identifier as obtained by the Thycotic secret management system
-  **Client Secret** (required): give the secret as obtained by the Thycotic secret management system


### 13.1.10. Thycotic Secret Server




When you select **Thycotic Secrets Server** for **Credential Type** , give the following metadata to configure your lookup:

-  **Secret Server URL** (required): give the URL used for communicating with the Thycotic Secrets Server management system
-  **Username** (required): specify the authenticated user for this service
-  **Domain** : give the (application) user domain
-  **Password** (required): give the password associated with the user


### 13.1.11. Configuring a `GitHub App Installation Access Token Lookup`




With this plugin you can use a private GitHub App RSA key as a credential input source to pull access tokens from GitHub App installations. Platform gateway uses existing GitHub authorization from organizations' GitHub repositories.

For more information, see [Generating an installation access token for a GitHub App](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-an-installation-access-token-for-a-github-app) .

**Procedure**

1. Create a lookup credential that stores your secrets. For more information, see [Creating new credentials](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#controller-create-credential) .
1. Select **GitHub App Installation Access Token Lookup** for **Credential type** , and enter the following attributes to properly configure your lookup:


-  **GitHub App ID** : Enter the App ID provided by your instance of GitHub, this is what is used to authenticate.
-  **GitHub App Installation ID** : Enter the ID of the application into your target organization where the access token is scoped. You must set it up to have access to your target repository.
-  **RSA Private Key** : Enter the generated private key that your GitHub instance generated. You can get it from the GitHub App maintainer within GitHub. For more information, see [Managing private keys for GitHub Apps](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/managing-private-keys-for-github-apps) .

1. ClickCreate credentialto confirm and save the credential.

The following is an example of a configured **GitHub App Installation Access Token Lookup** credential:

![GitHub App token lookup credential](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Configuring_automation_execution-en-US/images/ab0be251243460b4189776c30368a26b/credentials-create-github-app-lookup-credential.png)



1. Create a target credential that searches for the lookup credential. To use your lookup in a private repository, select **Source Control** as your **Credential type** . Enter the following attributes to properly configure your target credential:


-  **Username** : Enter the username `        x-access-token` .
-  **Password** : Click the![Link](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Configuring_automation_execution-en-US/images/fc669abfeec02bb8bda89a0de40c0391/leftkey.png)
icon for managing external credentials in the input field. You are prompted to set the input source to use to retrieve your secret information. This is the lookup credential that you have already created.

![Target credential secret info](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Configuring_automation_execution-en-US/images/6f3b5c1fce63a618c14103d1c232e301/credentials-github-app-target-secret-info.png)




1. Enter an optional description for the metadata requested and clickFinish.
1. ClickCreate credentialto confirm and save the credential.
1. Verify both your lookup credential and your target credential are now available on the **Credentials** list view. To use the target credential in a project, create a project and enter the following information:


-  **Name** : Enter the name for your project.
-  **Organization** : Select the name of the organization from the drop-down menu..
-  **Execution environment** : Optionally select an execution environment, if applicable.
-  **Source control type** : If you are syncing with a private repository, select **Git** for your source control.

The **Type Details** view opens for additional input. Enter the following information:


-  **Source control URL** : Enter the URL of the private repository you want to access. The other related fields pertaining to **branch/tag/commit** and **refspec** are not relevant for use with a lookup credential.
-  **Source control credential** : Select the target credential that you have already created.

The following is an example of a configured target credential in a project:

![GitHub App project](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Configuring_automation_execution-en-US/images/2b1bcf72d853fdeaeca592936a1db02f/project-create-git-github-app.png)




1. ClickCreate projectand the project sync automatically starts. The project **Details** tab displays the progress of the job:

![Project sync GitHub App](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Configuring_automation_execution-en-US/images/42f81b0433c68c09e1cb8baeec9d555c/project-sync-github-app.png)





**Troubleshooting**

If your project sync fails, you might have to manually re-enter `<a class="link" href="https://api.github.com">https://api.github.com</a>` in the **GitHub API endpoint URL** field from Step 2 and re-run your project sync.


# Chapter 14. Secret handling and connection security




Automation controller handles secrets and connections securely.

## 14.1. Secret handling




Automation controller manages three sets of secrets:

- User passwords for local automation controller users.
- Secrets for automation controller operational use, such as database password or message bus password.
- Secrets for automation use, such as SSH keys, cloud credentials, or external password vault credentials.


Note
You must have 'local' user access for the following users:

- postgres
- awx
- redis
- receptor
- nginx




### 14.1.1. User passwords for local users




Automation controller hashes local automation controller user passwords with the PBKDF2 algorithm using a SHA256 hash. Users who authenticate by external account mechanisms, such as LDAP, SAML, and OAuth, do not have any password or secret stored.

### 14.1.2. Secret handling for operational use




The operational secrets found in automation controller are as follows:

-  `    /etc/tower/SECRET_KEY` : A secret key used for encrypting automation secrets in the database. If the `    SECRET_KEY` changes or is unknown, you cannot access encrypted fields in the database.
-  `    /etc/tower/tower.{cert,key}` : An SSL certificate and key for the automation controller web service. A self-signed certificate or key is installed by default; you can provide a locally appropriate certificate and key.
- A database password in `    /etc/tower/conf.d/postgres.py` and a message bus password in `    /etc/tower/conf.d/channels.py` .


These secrets are stored unencrypted on the automation controller server, because they are all needed to be read by the automation controller service at startup in an automated fashion. All secrets are protected by UNIX permissions, and restricted to root and the automation controller awx service user.

If you need to hide these secrets, the files that these secrets are read from are interpreted by Python. You can adjust these files to retrieve these secrets by some other mechanism anytime a service restarts. This is a customer provided modification that might need to be reapplied after every upgrade. Red Hat Support and Red Hat Consulting have examples of such modifications.

Note
If the secrets system is down, automation controller cannot get the information and can fail in a way that is recoverable once the service is restored. Using some redundancy on that system is highly recommended.



If you believe the `SECRET_KEY` that automation controller generated for you has been compromised and needs to be regenerated, you can run a tool from the installer that behaves much like the automation controller backup and restore tool.

Important
Ensure that you backup your automation controller database before you generate a new secret key.



To generate a new secret key:

1. Follow the procedure described in the [Backing up and Restoring](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#controller-backup-and-restore) section.
1. Use the inventory from your install (the same inventory with which you run backups and restores), and run the following command:


```
setup.sh -k.
```




A backup copy of the previous key is saved in `/etc/tower/` .

### 14.1.3. Secret handling for automation use




Automation controller stores a variety of secrets in the database that are either used for automation or are a result of automation.

These secrets include the following:

- All secret fields of all credential types, including passwords, secret keys, authentication tokens, and secret cloud credentials.
- Secret tokens and passwords for external services defined automation controller settings.
- "password" type survey field entries.


To encrypt secret fields, automation controller uses AES in CBC mode with a 256-bit key for encryption, PKCS7 padding, and HMAC using SHA256 for authentication.

The encryption or decryption process derives the AES-256 bit encryption key from the `SECRET_KEY` , the field name of the model field and the database assigned auto-incremented record ID. Therefore, if any attribute used in the key generation process changes, the automation controller fails to correctly decrypt the secret.

Automation controller is designed so that:

- The `    SECRET_KEY` is never readable in playbooks that automation controller launches.
- These secrets are never readable by automation controller users.
- No secret field values are ever made available by the automation controller REST API.


If a secret value is used in a playbook, it is recommended that you use `no_log` on the task so that it is not accidentally logged.

## 14.2. Connection security




Automation controller allows for connections to internal services, external access, and managed nodes.

Note
You must have 'local' user access for the following users:

- postgres
- awx
- redis
- receptor
- nginx




### 14.2.1. Internal services




Automation controller connects to the following services as part of internal operation:

### 14.2.2. External access




Automation controller is accessed via standard HTTP/HTTPS on standard ports, provided by Nginx. A self-signed certificate or key is installed by default; you can provide a locally appropriate certificate and key. SSL/TLS algorithm support is configured in the `/etc/nginx/nginx.conf` configuration file. An "intermediate" profile is used by default, that you can configure. You must reapply changes after each update.

### 14.2.3. Managed nodes




Automation controller connects to managed machines and services as part of automation. All connections to managed machines are done by standard secure mechanisms, such as SSH, WinRM, or SSL/TLS. Each of these inherits configuration from the system configuration for the feature in question, such as the system OpenSSL configuration.

# Chapter 15. Security best practices




You can deploy automation controller to automate typical environments securely. However, managing certain operating system environments, automation, and automation platforms, can require additional best practices to ensure security.

To secure Red Hat Enterprise Linux start with the following release-appropriate security guide:

- For Red Hat Enterprise Linux 8, see [Security hardening](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/security_hardening/index) .
- For Red Hat Enterprise Linux 9, see [Security hardening](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening) .


## 15.1. Understand the architecture of Ansible Automation Platform and automation controller




Ansible Automation Platform and automation controller comprise a general-purpose, declarative automation platform. That means that when an Ansible Playbook is launched (by automation controller, or directly on the command line), the playbook, inventory, and credentials provided to Ansible are considered to be the source of truth. If you want policies around external verification of specific playbook content, job definition, or inventory contents, you must complete these processes before the automation is launched, either by the automation controller web UI, or the automation controller API.

The use of source control, branching, and mandatory code review is best practice for Ansible automation. There are tools that can help create process flow around using source control in this manner.

At a higher level, tools exist that enable creation of approvals and policy-based actions around arbitrary workflows, including automation. These tools can then use Ansible through the automation controller’s API to perform automation.

You must use a secure default administrator password at the time of automation controller installation. For more information, see [Change the automation controller Administrator Password](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#ref-controller-change-admin-password) .

Automation controller exposes services on certain well-known ports, such as port 80 for HTTP traffic and port 443 for HTTPS traffic. Do not expose automation controller on the open internet, which reduces the threat surface of your installation.

### 15.1.1. Granting access




Granting access to certain parts of the system exposes security risks. Apply the following practices to help secure access:

-  [Minimize administrative accounts](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#controller-minimize-administrative-accounts)
-  [Minimize local system access](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#controller-minimize-system-access)
-  [Remove access to credentials from users](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#controller-remove-access-credentials)
-  [Enforce separation of duties](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#controller-enforce-separation-duties)


### 15.1.2. Minimize administrative accounts




Minimizing the access to system administrative accounts is crucial for maintaining a secure system. A system administrator or root user can access, edit, and disrupt any system application. Limit the number of people or accounts with root access, where possible. Do not give out _sudo_ to _root_ or _awx_ (the automation controller user) to untrusted users. Note that when restricting administrative access through mechanisms like _sudo_ , restricting to a certain set of commands can still give a wide range of access. Any command that enables execution of a shell or arbitrary shell commands, or any command that can change files on the system, is equal to full root access.

With automation controller, any automation controller "system administrator" or "superuser" account can edit, change, and update an inventory or automation definition in automation controller. Restrict this to the minimum set of users possible for low-level automation controller configuration and disaster recovery only.

### 15.1.3. Minimize local system access




When you use automation controller with best practices, it does not require local user access except for administrative purposes. Non-administrator users do not have access to the automation controller system.

### 15.1.4. Remove user access to credentials




If an automation controller credential is only stored in the controller, you can further secure it. You can configure services such as OpenSSH to only permit credentials on connections from specific addresses. Credentials used by automation can be different from credentials used by system administrators for disaster-recovery or other ad hoc management, allowing for easier auditing.

### 15.1.5. Enforce separation of duties




Different pieces of automation might require access to a system at different levels. For example, you can have low-level system automation that applies patches and performs security baseline checking, while a higher-level piece of automation deploys applications. By using different keys or credentials for each piece of automation, the effect of any one key vulnerability is minimized, while also enabling baseline auditing.

## 15.2. Available resources




Several resources exist in automation controller and elsewhere to ensure a secure platform. Consider using the following functionalities:

-  [Existing security functionality](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#controller-existing-security)
-  [External account stores](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#controller-external-account-stores)
-  [Django password policies](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#controller-django-password-policies)


### 15.2.1. Existing security functionality




Do not disable SELinux or automation controller’s existing multi-tenant containment. Use automation controller’s role-based access control (RBAC) to delegate the minimum level of privileges required to run automation. Use teams in automation controller to assign permissions to groups of users rather than to users individually.

**Additional resources**

For more information, see [Role-Based Access Controls](https://docs.ansible.com/automation-controller/4.4/html/userguide/security.html#rbac-ug) in _Using automation execution_ .


### 15.2.2. External account stores




Maintaining a full set of users in automation controller can be a time-consuming task in a large organization. Automation controller supports connecting to external account sources by LDAP, SAML 2.0, and certain OAuth providers. Using this eliminates a source of error when working with permissions.

### 15.2.3. Django password policies




Automation controller administrators can use Django to set password policies at creation time through `AUTH_PASSWORD_VALIDATORS` to validate automation controller user passwords. In the `custom.py` file located at `/etc/tower/conf.d` of your automation controller instance, add the following code block example:

```
AUTH_PASSWORD_VALIDATORS = [
{
'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
},
{
'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
'OPTIONS': {
'min_length': 9,
}
},
{
'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
},
{
'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
},
]
```

**Additional resources**

- For more information, see [Password validation](https://docs.djangoproject.com/en/3.2/topics/auth/passwords/#module-django.contrib.auth.password_validation) in Django in addition to the preceding example.
- Ensure that you restart your automation controller instance for the change to take effect. For more information, see [Start, stop, and restart automation controller](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#controller-start-stop-controller) .


# Chapter 16. The _awx-manage_ Utility




Use the `awx-manage` utility to access detailed internal information of automation controller. Commands for `awx-manage` must run as the `awx` user only.

## 16.1. Inventory Import




`awx-manage` is a mechanism by which an automation controller administrator can import inventory directly into automation controller.

To use `awx-manage` properly, you must first create an inventory in automation controller to use as the destination for the import.

For help with `awx-manage` , run the following command:

```
awx-manage inventory_import [--help]
```

The `inventory_import` command synchronizes an automation controller inventory object with a text-based inventory file, dynamic inventory script, or a directory of one or more, as supported by core Ansible.

When running this command, specify either an `--inventory-id` or `--inventory-name` , and the path to the Ansible inventory source ( `--source` ).

```
awx-manage inventory_import --source=/ansible/inventory/ --inventory-id=1
```

By default, inventory data already stored in automation controller blends with data from the external source.

To use only the external data, specify `--overwrite` .

To specify that any existing hosts get variable data exclusively from the `--source` , specify `--overwrite_vars` .

The default behavior adds any new variables from the external source, overwriting keys that already exist, but preserving any variables that were not sourced from the external data source.

```
awx-manage inventory_import --source=/ansible/inventory/ --inventory-id=1 --overwrite
```

Note
Edits and additions to Inventory host variables persist beyond an inventory synchronization as long as `--overwrite_vars` is not set.



## 16.2. Cleanup of old data




`awx-manage` has a variety of commands used to clean old data from automation controller. Automation controller administrators can use the automation controller **Management Jobs** interface for access or use the command line.

```
awx-manage cleanup_jobs [--help]
```

This permanently deletes the job details and job output for jobs older than a specified number of days.

```
awx-manage cleanup_activitystream [--help]
```

This permanently deletes any [Activity stream] data older than a specific number of days.

## 16.3. Cluster management




For more information about the `awx-manage provision_instance` and `awx-manage deprovision_instance` commands, see [Clustering](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#controller-clustering) .

Note
Do not run other `awx-manage` commands unless instructed by Ansible Support.



## 16.4. Analytics gathering




Use this command to gather analytics on-demand outside of the predefined window (the default is 4 hours):

`$ awx-manage gather_analytics --ship`

For customers with disconnected environments who want to collect usage information about unique hosts automated across a time period, use this command:

`awx-manage host_metric --since YYYY-MM-DD --json`

The `--since` parameter is optional.

The `--json` flag specifies the output format and is optional.

# Chapter 17. Backup and restore




You can backup and restore your system using the Ansible Automation Platform setup playbook.

For more information, see the [Backup and restore clustered environments](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/index#controller-backup-restore-clustered-environments) section.

Note
When backing up Ansible Automation Platform, use the installation program that matches your currently installed version of Ansible Automation Platform.

When restoring Ansible Automation Platform, use the latest installation program available at the time of the restore. For example, if you are restoring a backup taken from version `2.5-1` , use the latest `2.5-x` installation program available at the time of the restore.

Backup and restore functionality only works with the PostgreSQL versions supported by your current Ansible Automation Platform version. For more information, see [System requirements](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/planning_your_installation/platform-system-requirements) in _Planning your installation_ .



The Ansible Automation Platform setup playbook is invoked as `setup.sh` from the path where you unpacked the platform installer tarball. It uses the same inventory file used by the install playbook. The setup script takes the following arguments for backing up and restoring:

-  `    -b` : Perform a database backup rather than an installation.
-  `    -r` : Perform a database restore rather than an installation.


As the root user, call `setup.sh` with the appropriate parameters and the Ansible Automation Platform backup or restored as configured:

```
root@localhost:~# ./setup.sh -b
root@localhost:~# ./setup.sh -r
```

Backup files are created on the same path that `setup.sh` script exists. You can change it by specifying the following `EXTRA_VARS` :

```
root@localhost:~# ./setup.sh -e 'backup_dest=/path/to/backup_dir/' -b
```

A default restore path is used unless you provide `EXTRA_VARS` with a non-default path, as shown in the following example:

```
root@localhost:~# ./setup.sh -e 'restore_backup_file=/path/to/nondefault/backup.tar.gz' -r
```

Optionally, you can override the inventory file used by passing it as an argument to the setup script:

```
setup.sh -i &lt;inventory file&gt;
```

## 17.1. Backup and restore playbooks




In addition to the `install.yml` file included with your `setup.sh` setup playbook, there are also `backup.yml` and `restore.yml` files.

These playbooks serve to backup and restore.

- The overall backup, backs up:


- The database
- The `        SECRET_KEY` file

- The per-system backups include:


- Custom configuration files
- Manual projects

- The restore backup restores the backed up files and data to a freshly installed and working second instance of automation controller.


When restoring your system, the installer checks to see that the backup file exists before beginning the restoration. If the backup file is not available, your restoration fails.

Note
Make sure that your automation controller hosts are properly set up with SSH keys, user or pass variables in the hosts file, and that the user has `sudo` access.



## 17.2. Backup and restoration considerations




Consider the following points when you backup and restore your system:

## 17.3. Backup and restore clustered environments




The procedure for backup and restore for a clustered environment is similar to a single install, except for some of the following considerations:

Note
For more information on installing clustered environments, see the [Install and configure](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#controller-cluster-install) section.



- If restoring to a new cluster, ensure that the old cluster is shut down before proceeding because they can conflict with each other when accessing the database.
- Per-node backups are only restored to nodes bearing the same hostname as the backup.
- When restoring to an existing cluster, the restore contains the following:


- A dump of the PostgreSQL database
- UI artifacts, included in the database dump
- An automation controller configuration (retrieved from `        /etc/tower` )
- An automation controller secret key
- Manual projects



### 17.3.1. Restore to a different cluster




When restoring a backup to a separate instance or cluster, manual projects and custom settings under `/etc/tower` are retained. Job output and job events are stored in the database, and therefore, not affected.

The restore process does not alter instance groups present before the restore. It does not introduce any new instance groups either. Restored automation controller resources that were associated to instance groups likely need to be reassigned to instance groups present on the new automation controller cluster.

# Chapter 18. Usability Analytics and Data Collection




Usability data collection is included with automation controller to collect data to better understand how automation controller users interact with it.

Only users installing a trial of or a fresh installation of are opted-in for this data collection.

Automation controller collects user data automatically to help improve the product.

For information on setting up Automation Analytics, see [Configuring Automation Analytics](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#proc-controller-configure-analytics) .

## 18.1. Automation Analytics




When you imported your license for the first time, you were automatically opted in for the collection of data that powers Automation Analytics, a cloud service that is part of the Ansible Automation Platform subscription.

Important
For opt-in of Automation Analytics to have any effect, your instance of automation controller must be running on Red Hat Enterprise Linux.



As with Red Hat Insights, Automation Analytics is built to collect the minimum amount of data needed. No credential secrets, personal data, automation variables, or task output is gathered.

When you imported your license for the first time, you were automatically opted in to Automation Analytics. To configure or disable this feature, see [Configuring Automation Analytics](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#proc-controller-configure-analytics) .

By default, the data is collected every four hours. When you enable this feature, data is collected up to a month in arrears (or until the previous collection). You can turn off this data collection at any time in the **Miscellaneous System settings** of the System configuration window.

This setting can also be enabled through the API by specifying `INSIGHTS_TRACKING_STATE = true` in either of these endpoints:

-  `    api/v2/settings/all`
-  `    api/v2/settings/system`


The Automation Analytics generated from this data collection can be found on the [Red Hat Cloud Services](https://cloud.redhat.com) portal.

**Clusters** data is the default view. This graph represents the number of job runs across all automation controller clusters over a period of time. The previous example shows a span of a week in a stacked bar-style chart that is organized by the number of jobs that ran successfully (in green) and jobs that failed (in red).

Alternatively, you can select a single cluster to view its job status information.

![Job run status](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Configuring_automation_execution-en-US/images/8367194553220359712bc53b67ce39c1/aa-job-run-status-over-time-period.png)


This multi-line chart represents the number of job runs for a single automation controller cluster for a specified period of time. The preceding example shows a span of a week, organized by the number of successfully running jobs (in green) and jobs that failed (in red). You can specify the number of successful and failed job runs for a selected cluster over a span of one week, two weeks, and monthly increments.

On the clouds navigation panel, selectOrganization Statisticsto view information for the following:

-  [Use by organization](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#ref-controller-use-by-organization)
-  [Job runs by organization](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#ref-controller-jobs-run-by-organization)
-  [Organization status](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#ref-controller-organization-status)


Note
The organization statistics page will be deprecated in a future release.



### 18.1.1. Use by organization




The following chart represents the number of tasks run inside all jobs by a particular organization.

![Tasks by organization](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Configuring_automation_execution-en-US/images/4902044c1f01b3ba37373b2aa9c73ad2/aa-usage-by-org-tasks.png)


### 18.1.2. Job runs by organization




This chart represents automation controller use across all automation controller clusters by organization, calculated by the number of jobs run by that organization.

![Jobs by organization](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Configuring_automation_execution-en-US/images/68892f94eecc849a4a290d596046d0ce/aa-usage-by-org.png)


### 18.1.3. Organization status




This bar chart represents automation controller use by organization and date, which is calculated by the number of jobs run by that organization on a particular date.

Alternatively, you can specify to show the number of job runs per organization in one week, two weeks, and monthly increments.

![Organization status](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Configuring_automation_execution-en-US/images/0f8ed00783958a1c019d012596cdfd01/aa-usage-by-org-by-date.png)


## 18.2. Details of data collection




Automation Analytics collects the following classes of data from automation controller:

- Basic configuration, such as which features are enabled, and what operating system is being used
- Topology and status of the automation controller environment and hosts, including capacity and health
- Counts of automation resources:


- organizations, teams, and users
- inventories and hosts
- credentials (indexed by type)
- projects (indexed by type)
- templates
- schedules
- active sessions
- running and pending jobs

- Job execution details (start time, finish time, launch type, and success)
- Automation task details (success, host id, playbook/role, task name, and module used)


You can use `awx-manage gather_analytics` (without `--ship` ) to inspect the data that automation controller sends, so that you can satisfy your data collection concerns. This creates a tarball that contains the analytics data that is sent to Red Hat.

This file contains a number of JSON and CSV files. Each file contains a different set of analytics data.

-  [manifest.json](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#ref-controller-manifest-json)
-  [config.json](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#ref-controller-config-json)
-  [instance_info.json](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#ref-controller-instance-info-json)
-  [counts.json](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#ref-controller-counts-json)
-  [org_counts.json](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#ref-controller-org-counts-json)
-  [cred_type_counts.json](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#ref-controller-cred-type-counts-json)
-  [inventory_counts.json](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#ref-controller-inventory-counts-json)
-  [projects_by_scm_type.json](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#ref-controller-projects-scm-type-json)
-  [query_info.json](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#ref-controller-query-info-json)
-  [job_counts.json](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#ref-controller-job-counts-json)
-  [job_instance_counts.json](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#ref-controller-job-instance-counts-json)
-  [unified_job_template_table.csv](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#ref-controller-unified-job-template-table-csv)
-  [unified_jobs_table.csv](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#ref-controller-unified-jobs-table-csv)
-  [workflow_job_template_node_table.csv](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#ref-controller-workflow-job-template-node-table-csv)
-  [workflow_job_node_table.csv](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#ref-controller-workflow-job-node-table-csv)
-  [events_table.csv](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#ref-controller-events-table-csv)


### 18.2.1. manifest.json




`manifest.json` is the manifest of the analytics data. It describes each file included in the collection, and what version of the schema for that file is included.

The following is an example `manifest.json` file:

```
"config.json": "1.1",
"counts.json": "1.0",
"cred_type_counts.json": "1.0",
"events_table.csv": "1.1",
"instance_info.json": "1.0",
"inventory_counts.json": "1.2",
"job_counts.json": "1.0",
"job_instance_counts.json": "1.0",
"org_counts.json": "1.0",
"projects_by_scm_type.json": "1.0",
"query_info.json": "1.0",
"unified_job_template_table.csv": "1.0",
"unified_jobs_table.csv": "1.0",
"workflow_job_node_table.csv": "1.0",
"workflow_job_template_node_table.csv": "1.0"
}
```

### 18.2.2. config.json




The config.json file contains a subset of the configuration endpoint `/api/v2/config` from the cluster. An example config.json is:

```
{
"ansible_version": "2.9.1",
"authentication_backends": [
"social_core.backends.azuread.AzureADOAuth2",
"django.contrib.auth.backends.ModelBackend"
],
"external_logger_enabled": true,
"external_logger_type": "splunk",
"free_instances": 1234,
"install_uuid": "d3d497f7-9d07-43ab-b8de-9d5cc9752b7c",
"instance_uuid": "bed08c6b-19cc-4a49-bc9e-82c33936e91b",
"license_expiry": 34937373,
"license_type": "enterprise",
"logging_aggregators": [
"awx",
"activity_stream",
"job_events",
"system_tracking"
],
"pendo_tracking": "detailed",
"platform": {
"dist": [
"redhat",
"7.4",
"Maipo"
],
"release": "3.10.0-693.el7.x86_64",
"system": "Linux",
"type": "traditional"
},
"total_licensed_instances": 2500,
"controller_url_base": "https://ansible.rhdemo.io",
"controller_version": "3.6.3"
}
```

Which includes the following fields:

-  **ansible_version** : The system Ansible version on the host
-  **authentication_backends** : The user authentication backends that are available. For more information, see [Configuring an authentication type](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication/index#gw-config-authentication-type) .
-  **external_logger_enabled** : Whether external logging is enabled
-  **external_logger_type** : What logging backend is in use if enabled. For more information, see [Logging and aggregation](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#assembly-controller-logging-aggregation) .
-  **logging_aggregators** : What logging categories are sent to external logging. For more information, see [Logging and aggregation](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#assembly-controller-logging-aggregation) .
-  **free_instances** : How many hosts are available in the license. A value of zero means the cluster is fully consuming its license.
-  **install_uuid** : A UUID for the installation (identical for all cluster nodes)
-  **instance_uuid** : A UUID for the instance (different for each cluster node)
-  **license_expiry** : Time to expiry of the license, in seconds
-  **license_type** : The type of the license (should be 'enterprise' for most cases)
-  **pendo_tracking** : State of `    usability_data_collection`
-  **platform** : The operating system the cluster is running on
-  **total_licensed_instances** : The total number of hosts in the license
-  **controller_url_base** : The base URL for the cluster used by clients (shown in Automation Analytics)
-  **controller_version** : Version of the software on the cluster


### 18.2.3. instance_info.json




The `instance_info.json` file contains detailed information on the instances that make up the cluster, organized by instance UUID.

The following is an example `instance_info.json` file:

```
{
"bed08c6b-19cc-4a49-bc9e-82c33936e91b": {
"capacity": 57,
"cpu": 2,
"enabled": true,
"last_isolated_check": "2019-08-15T14:48:58.553005+00:00",
"managed_by_policy": true,
"memory": 8201400320,
"uuid": "bed08c6b-19cc-4a49-bc9e-82c33936e91b",
"version": "3.6.3"
}
"c0a2a215-0e33-419a-92f5-e3a0f59bfaee": {
"capacity": 57,
"cpu": 2,
"enabled": true,
"last_isolated_check": "2019-08-15T14:48:58.553005+00:00",
"managed_by_policy": true,
"memory": 8201400320,
"uuid": "c0a2a215-0e33-419a-92f5-e3a0f59bfaee",
"version": "3.6.3"
}
}
```

Which includes the following fields:

-  **capacity** : The capacity of the instance for executing tasks.
-  **cpu** : Processor cores for the instance
-  **memory** : Memory for the instance
-  **enabled** : Whether the instance is enabled and accepting tasks
-  **managed_by_policy** : Whether the instance’s membership in instance groups is managed by policy, or manually managed
-  **version** : Version of the software on the instance


### 18.2.4. counts.json




The `counts.json` file contains the total number of objects for each relevant category in a cluster.

The following is an example `counts.json` file:

```
{
"active_anonymous_sessions": 1,
"active_host_count": 682,
"active_sessions": 2,
"active_user_sessions": 1,
"credential": 38,
"custom_inventory_script": 2,
"custom_virtualenvs": 4,
"host": 697,
"inventories": {
"normal": 20,
"smart": 1
},
"inventory": 21,
"job_template": 78,
"notification_template": 5,
"organization": 10,
"pending_jobs": 0,
"project": 20,
"running_jobs": 0,
"schedule": 16,
"team": 5,
"unified_job": 7073,
"user": 28,
"workflow_job_template": 15
}
```

Each entry in this file is for the corresponding API objects in `/api/v2` , with the exception of the active session counts.

### 18.2.5. org_counts.json




The `org_counts.json` file contains information on each organization in the cluster, and the number of users and teams associated with that organization.

The following is an example `org_counts.json` file:

```
{
"1": {
"name": "Operations",
"teams": 5,
"users": 17
},
"2": {
"name": "Development",
"teams": 27,
"users": 154
},
"3": {
"name": "Networking",
"teams": 3,
"users": 28
}
}
```

### 18.2.6. cred_type_counts.json




The `cred_type_counts.json` file contains information on the different credential types in the cluster, and how many credentials exist for each type.

The following is an example `cred_type_counts.json` file:

```
{
"1": {
"credential_count": 15,
"managed_by_controller": true,
"name": "Machine"
},
"2": {
"credential_count": 2,
"managed_by_controller": true,
"name": "Source Control"
},
"3": {
"credential_count": 3,
"managed_by_controller": true,
"name": "Vault"
},
"4": {
"credential_count": 0,
"managed_by_controller": true,
"name": "Network"
},
"5": {
"credential_count": 6,
"managed_by_controller": true,
"name": "Amazon Web Services"
},
"6": {
"credential_count": 0,
"managed_by_controller": true,
"name": "OpenStack"
},
```

### 18.2.7. inventory_counts.json




The `inventory_counts.json` file contains information on the different inventories in the cluster.

The following is an example `inventory_counts.json` file:

```
{
"1": {
"hosts": 211,
"kind": "",
"name": "AWS Inventory",
"source_list": [
{
"name": "AWS",
"num_hosts": 211,
"source": "ec2"
}
],
"sources": 1
},
"2": {
"hosts": 15,
"kind": "",
"name": "Manual inventory",
"source_list": [],
"sources": 0
},
"3": {
"hosts": 25,
"kind": "",
"name": "SCM inventory - test repo",
"source_list": [
{
"name": "Git source",
"num_hosts": 25,
"source": "scm"
}
],
"sources": 1
}
"4": {
"num_hosts": 5,
"kind": "smart",
"name": "Filtered AWS inventory",
"source_list": [],
"sources": 0
}
}
```

### 18.2.8. projects_by_scm_type.json




The `projects_by_scm_type.json` file provides a breakdown of all projects in the cluster, by source control type.

The following is an example `projects_by_scm_type.json` file:

```
{
"git": 27,
"hg": 0,
"insights": 1,
"manual": 0,
"svn": 0
}
```

### 18.2.9. query_info.json




The `query_info.json` file provides details on when and how the data collection happened.

The following is an example `query_info.json` file:

```
{
"collection_type": "manual",
"current_time": "2019-11-22 20:10:27.751267+00:00",
"last_run": "2019-11-22 20:03:40.361225+00:00"
}
```

`collection_type` is one of `manual` or `automatic` .

### 18.2.10. job_counts.json




The `job_counts.json` file provides details on the job history of the cluster, describing both how jobs were launched, and what their finishing status is.

The following is an example `job_counts.json` file:

```
"launch_type": {
"dependency": 3628,
"manual": 799,
"relaunch": 6,
"scheduled": 1286,
"scm": 6,
"workflow": 1348
},
"status": {
"canceled": 7,
"failed": 108,
"successful": 6958
},
"total_jobs": 7073
}
```

### 18.2.11. job_instance_counts.json




The `job_instance_counts.json` file provides the same detail as `job_counts.json` , broken down by instance.

The following is an example `job_instance_counts.json` file:

```
{
"localhost": {
"launch_type": {
"dependency": 3628,
"manual": 770,
"relaunch": 3,
"scheduled": 1009,
"scm": 6,
"workflow": 1336
},
"status": {
"canceled": 2,
"failed": 60,
"successful": 6690
}
}
}
```

Note that instances in this file are by hostname, not by UUID as they are in `instance_info` .

### 18.2.12. unified_job_template_table.csv




The `unified_job_template_table.csv` file provides information on job templates in the system. Each line contains the following fields for the job template:

-  **id** : Job template id.
-  **name** : Job template name.
-  **polymorphic_ctype_id** : The id of the type of template it is.
-  **model** : The name of the `    polymorphic_ctype_id` for the template. Examples include `    project` , `    systemjobtemplate` , `    jobtemplate` , `    inventorysource` , and `    workflowjobtemplate` .
-  **created** : When the template was created.
-  **modified** : When the template was last updated.
-  **created_by_id** : The `    userid` that created the template. Blank if done by the system.
-  **modified_by_id** : The `    userid` that last modified the template. Blank if done by the system.
-  **current_job_id** : Currently executing job id for the template, if any.
-  **last_job_id** : Last execution of the job.
-  **last_job_run** : Time of last execution of the job.
-  **last_job_failed** : Whether the `    last_job_id` failed.
-  **status** : Status of `    last_job_id` .
-  **next_job_run** : Next scheduled execution of the template, if any.
-  **next_schedule_id** : Schedule id for `    next_job_run` , if any.


### 18.2.13. unified_jobs_table.csv




The `unified_jobs_table.csv` file provides information on jobs run by the system.

Each line contains the following fields for a job:

-  **id** : Job id.
-  **name** : Job name (from the template).
-  **polymorphic_ctype_id** : The id of the type of job it is.
-  **model** : The name of the `    polymorphic_ctype_id` for the job. Examples include `    job` and `    workflow` .
-  **organization_id** : The organization ID for the job.
-  **organization_name** : Name for the `    organization_id` .
-  **created** : When the job record was created.
-  **started** : When the job started executing.
-  **finished** : When the job finished.
-  **elapsed** : Elapsed time for the job in seconds.
-  **unified_job_template_id** : The template for this job.
-  **launch_type** : One of `    manual` , `    scheduled` , `    relaunched` , `    scm` , `    workflow` , or `    dependency` .
-  **schedule_id** : The id of the schedule that launched the job, if any,
-  **instance_group_id** : The instance group that executed the job.
-  **execution_node** : The node that executed the job (hostname, not UUID).
-  **controller_node** : The automation controller node for the job, if run as an isolated job, or in a container group.
-  **cancel_flag** : Whether the job was canceled.
-  **status** : Status of the job.
-  **failed** : Whether the job failed.
-  **job_explanation** : Any additional detail for jobs that failed to execute properly.
-  **forks** : Number of forks executed for this job.


### 18.2.14. workflow_job_template_node_table.csv




The `workflow_job_template_node_table.csv` file provides information on the nodes defined in workflow job templates on the system.

Each line contains the following fields for a worfklow job template node:

-  **id** : Node id.
-  **created** : When the node was created.
-  **modified** : When the node was last updated.
-  **unified_job_template_id** : The id of the job template, project, inventory, or other parent resource for this node.
-  **workflow_job_template_id** : The workflow job template that contains this node.
-  **inventory_id** : The inventory used by this node.
-  **success_nodes** : Nodes that are triggered after this node succeeds.
-  **failure_nodes** : Nodes that are triggered after this node fails.
-  **always_nodes** : Nodes that always are triggered after this node finishes.
-  **all_parents_must_converge** : Whether this node requires all its parent conditions satisfied to start.


### 18.2.15. workflow_job_node_table.csv




The `workflow_job_node_table.csv` provides information on the jobs that have been executed as part of a workflow on the system.

Each line contains the following fields for a job run as part of a workflow:

-  **id** : Node id.
-  **created** : When the node was created.
-  **modified** : When the node was last updated.
-  **job_id** : The job id for the job run for this node.
-  **unified_job_template_id** : The id of the job template, project, inventory, or other parent resource for this node.
-  **workflow_job_template_id** : The workflow job template that contains this node.
-  **inventory_id** : The inventory used by this node.
-  **success_nodes** : Nodes that are triggered after this node succeeds.
-  **failure_nodes** : Nodes that are triggered after this node fails.
-  **always_nodes** : Nodes that always are triggered after this node finishes.
-  **do_not_run** : Nodes that were not run in the workflow due to their start conditions not being triggered.
-  **all_parents_must_converge** : Whether this node requires all its parent conditions satisfied to start.


### 18.2.16. events_table.csv




The `events_table.csv` file provides information on all job events from all job runs in the system.

Each line contains the following fields for a job event:

-  **id** : Event id.
-  **uuid** : Event UUID.
-  **created** : When the event was created.
-  **parent_uuid** : The parent UUID for this event, if any.
-  **event** : The Ansible event type.
-  **task_action** : The module associated with this event, if any (such as `    command` or `    yum` ).
-  **failed** : Whether the event returned `    failed` .
-  **changed** : Whether the event returned `    changed` .
-  **playbook** : Playbook associated with the event.
-  **play** : Play name from playbook.
-  **task** : Task name from playbook.
-  **role** : Role name from playbook.
-  **job_id** : Id of the job this event is from.
-  **host_id** : Id of the host this event is associated with, if any.
-  **host_name** : Name of the host this event is associated with, if any.
-  **start** : Start time of the task.
-  **end** : End time of the task.
-  **duration** : Duration of the task.
-  **warnings** : Any warnings from the task or module.
-  **deprecations** : Any deprecation warnings from the task or module.


## 18.3. Analytics Reports




Reports for data collected are available through [console.redhat.com](https://console.redhat.com) .

Other Automation Analytics data currently available and accessible through the platform UI include the following:

**Automation Calculator** is a view-only version of the Automation Calculator utility that shows a report that represents (possible) savings to the subscriber.

![Automation calculator](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Configuring_automation_execution-en-US/images/a9e131d25102206620d772aa00937d5e/aa-automation-calculator.png)


**Host Metrics** is an analytics report collected for host data such as, when they were first automated, when they were most recently automated, how many times they were automated, and how many times each host has been deleted.

**Subscription Usage** reports the historical usage of your subscription. Subscription capacity and licenses consumed per month are displayed, with the ability to filter by the last year, two years, or three years.

# Chapter 19. Troubleshooting automation controller




Useful troubleshooting information for automation controller.

## 19.1. Unable to login to automation controller through HTTP




Access to automation controller is intentionally restricted through a secure protocol (HTTPS). In cases where your configuration is set up to run an automation controller node behind a load balancer or proxy as "HTTP only", and you only want to access it without SSL (for troubleshooting, for example), you must add the following settings in the `custom.py` file located at `/etc/tower/conf.d` of your automation controller instance:

```
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
```

If you change these settings to `false` it enables automation controller to manage cookies and login sessions when using the HTTP protocol. You must do this on every node of a cluster installation.

To apply the changes, run:

```
automation-controller-service restart
```

## 19.2. Unable to run a job




If you are unable to run a job from a playbook, review the playbook YAML file. When importing a playbook, either manually or by a source control mechanism, keep in mind that the host definition is controlled by automation controller and should be set to `hosts:all` .

## 19.3. Playbooks do not show up in the Job Template list




If your playbooks are not showing up in the **Job Template** list, check the following:

- Ensure that the playbook is valid YML and can be parsed by Ansible.
- Ensure that the permissions and ownership of the project path ( `    /var/lib/awx/projects` ) is set up so that the "awx" system user can view the files. Run the following command to change the ownership:


```
chown awx -R /var/lib/awx/projects/
```

## 19.4. Playbook stays in pending




If you are attempting to run a playbook job and it stays in the `Pending` state indefinitely, try the following actions:

- Ensure that all supervisor services are running through `    supervisorctl status` .
- Ensure that the `    /var/ partition` has more than 1 GB of space available. Jobs do not complete with insufficient space on the `    /var/` partition.
- Run `    automation-controller-service restart` on the automation controller server.


If you continue to have issues, run `sosreport` as root on the automation controller server, then file a [support request](http://support.ansible.com/) with the result.

## 19.5. Reusing an external database causes installations to fail




Instances have been reported where reusing the external database during subsequent installation of nodes causes installation failures.

**Example**

You perform a clustered installation. Then, you need to do this again and perform a second clustered installation reusing the same external database, only this subsequent installation failed.


When setting up an external database that has been used in a prior installation, you must manually clear the database used for the clustered node before any additional installations can succeed.

## 19.6. Viewing private EC2 VPC instances in the automation controller inventory




By default, automation controller only shows instances in a VPC that have an Elastic IP (EIP) associated with them.

**Procedure**

1. From the navigation panel, selectAutomation Execution→Infrastructure→Inventories.
1. Select the inventory that has the **Source** set to **Amazon EC2** , and click the **Source** tab. In the **Source Variables** field, enter:


```
vpc_destination_variable: private_ip_address
```


1. ClickSaveand trigger an update of the group.


Once this is done you can see your VPC instances.

Note
Automation controller must be running inside the VPC with access to those instances if you want to configure them.



# Chapter 20. Automation controller tips and tricks




-  [Use the automation controller CLI Tool](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#ref-controller-use-CLI-tool)
-  [Change the automation controller Admin Password](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#ref-controller-change-admin-password)
-  [Create an automation controller Admin from the commandline](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#ref-controller-create-controller-admin)
-  [Set up a jump host to use with automation controller](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#ref-controller-set-up-jump-host)
-  [View Ansible outputs for JSON commands when using automation controller](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#ref-controller-view-ansible-outputs)
-  [Locate and configure the Ansible configuration file](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#ref-controller-locate-ansible-config-file)
-  [View a listing of all ansible_ variables](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#ref-controller-list-ansible-variables)
-  [The ALLOW_JINJA_IN_EXTRA_VARS variable](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#ref-controller-allow-jinja-in-extra-vars)
-  [Configure the controllerhost hostname for notifications](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#ref-controller-configure-host-name-notifications)
-  [Launch Jobs with curl](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#ref-controller-launch-jobs-with-curl)
-  [Filter instances returned by the dynamic inventory sources in automation controller](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#ref-controller-filter-instances)
-  [Use an unreleased module from Ansible source with automation controller](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#ref-controller-use-an-unreleased-module)
-  [Connect to Windows with winrm](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#ref-controller-connect-with-winrm)
-  [Import existing inventory files and host/group vars into automation controller](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#ref-controller-import-inventory-files)


## 20.1. The automation controller CLI Tool




Automation controller has a full-featured command line interface.

For more information on configuration and use, see the [AWX Command Line Interface](https://docs.ansible.com/automation-controller/latest/html/controllercli/usage.html) and the [AWX manage utility](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#assembly-controller-awx-manage-utility) section.

## 20.2. Change the automation controller Administrator Password




During the installation process, you are prompted to enter an administrator password that is used for the `admin` superuser or system administrator created by automation controller. If you log in to the instance by using SSH, it tells you the default administrator password in the prompt.

If you need to change this password at any point, run the following command as root on the automation controller server:

```
awx-manage changepassword admin
```

Next, enter a new password. After that, the password you have entered works as the administrator password in the web UI.

To set policies at creation time for password validation using Django, see [Django password policies](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/configuring_automation_execution/index#controller-django-password-policies) .

## 20.3. Create an automation controller Administrator from the command line




Occasionally you might find it helpful to create a system administrator (superuser) account from the command line.

To create a superuser, run the following command as root on the automation controller server and enter the administrator information as prompted:

```
awx-manage createsuperuser
```

## 20.4. Configuring automation controller to use jump hosts connecting to managed nodes




Credentials supplied by automation controller do not flow to the jump host through ProxyCommand. They are only used for the end-node when the tunneled connection is set up.


<span id="configure_a_fixed_userkeyfile_in_your_ssh_configuration_file"></span>
#### Configure a fixed user/keyfile in your SSH configuration file


You can configure a fixed user/keyfile in your SSH configuration file in the ProxyCommand definition that sets up the connection through the jump host.

**Prerequisites**

- Check whether all jump hosts are reachable from any node that establishes an SSH connection to the managed nodes, such as a Hybrid Controller or an Execution Node.


**Procedure**

1. Create an SSH configuration file `    /var/lib/awx .ssh/config` on each node with the following details


```
Host jumphost.example.com
Hostname jumphost.example.com
User &lt;jumphostuser&gt;
Port &lt;jumphostport&gt;
IdentityFile ~.ssh/id_rsa
StrictHostKeyChecking no
ProxyCommand ssh -W %h:%p jumphost.example.com
```

- The code specifies the configuration required to connect to the jump host 'jumphost.example.com'
- Automation controller establishes an SSH connection from each node to the managed nodes.
- Example values `    jumphost.example.com` , `    jumphostuser` , `    jumphostport` and `    ~/.ssh/id_rsa` must be changed according to your environment
- Add a Host matching block to the already created SSH configuration file `    /var/lib/awx/.ssh/config`` on the node, for example:


```
Host 192.0.*       ...
```


- The `    Host 192.0.*` line indicates that all hosts in that subnet use the settings defined in that block. Specifically all hosts in that subnet are accessed using the `    ProxyCommand` setting and connect through `    jumphost.example.com`
- If `    Host *` is used to indicate that all hosts connect through the specified proxy, ensure that `    jumphost.example.com` is excluded from that matching, for example:


```
Host * !jumphost.example.com        ...
```





<span id="using_the_red_hat_ansible_automation_platform_ui"></span>
##### Using the Red Hat Ansible Automation Platform UI


**Procedure**

1. On the navigation panel, selectSettings→Automation Execution→Job
1. ClickEditand add `    /var/lib/awx .ssh:/home/runner/.ssh:0` to the **Paths to expose isolated jobs** field.
1. ClickSaveto save your changes.



<span id="configuring_jump_hosts_using_ansible_inventory_variables"></span>
#### Configuring jump hosts using Ansible Inventory variables


You can also add a jump host to your automation controller instance through Inventory variables.

These variables can be set at either the inventory, group, or host level. Use this method if you want to control the use of jump hosts inside automation controller using the inventory.

- Navigate to your inventory and in the `    variables` field of whichever level you choose, add the following variables:


```
ansible_user: &lt;user_name&gt;
ansible_connection: ssh
ansible_ssh_common_args: '-o ProxyCommand="ssh -W %h:%p -q &lt;user_name&gt;@&lt;jump_server_name&gt;"'
```

## 20.5. View Ansible outputs for JSON commands when using automation controller




When working with automation controller, you can use the API to obtain the Ansible outputs for commands in JSON format.

To view the Ansible outputs, browse to https://<controller server name>/api/v2/jobs/<job_id>/job_events/

## 20.6. Locate and configure the Ansible configuration file




While Ansible does not require a configuration file, OS packages often include a default one in `/etc/ansible/ansible.cfg` for possible customization.

To use a custom `ansible.cfg` file, place it at the root of your project. Automation controller runs `ansible-playbook` from the root of the project directory, where it finds the custom `ansible.cfg` file.

Note
An `ansible.cfg` file anywhere else in the project is ignored.



To learn which values you can use in this file, see [Generating a sample ansible.cfg file](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#generating-a-sample-ansible-cfg-file) in the Ansible documentation.

Using the defaults are acceptable for starting out, but you can configure the default module path or connection type here, as well as other things.

Automation controller overrides some `ansible.cfg` options. For example, automation controller stores the SSH ControlMaster sockets, the SSH agent socket, and any other per-job run items in a per-job temporary directory that is passed to the container used for job execution.

## 20.7. View a listing of all ansible_ variables




By default, Ansible gathers "facts" about the machines under its management, accessible in Playbooks and in templates.

To view all facts available about a machine, run the `setup` module as an _ad hoc_ action:

```
ansible -m setup hostname
```

This prints out a dictionary of all facts available for that particular host. For more information, see [information-discovered-from-systems-facts](https://docs.ansible.com/ansible/latest/reference_appendices/special_variables.html#facts) in the Ansible documentation.

## 20.8. The ALLOW_JINJA_IN_EXTRA_VARS variable




Setting `ALLOW_JINJA_IN_EXTRA_VARS = template` only works for saved job template extra variables.

Prompted variables and survey variables are excluded from the 'template'.

This parameter has three values:

-  `    Only On Template Definitions` to allow usage of Jinja saved directly on a job template definition (the default).
-  `    Never` to disable all Jinja usage (recommended).
-  `    Always` to always allow Jinja (strongly discouraged, but an option for prior compatibility).


This parameter is configurable in the **Jobs Settings** page of the automation controller UI.

## 20.9. Configuring the `controllerhost` hostname for notifications




From the **System settings** page, you can replace `https://controller.example.com` in the **Base URL of the Service** field with your preferred hostname to change the notification hostname.

Refreshing your automation controller license also changes the notification hostname. New installations of automation controller need not set the hostname for notifications.

## 20.10. Launching Jobs with curl




Launching jobs with the automation controller API is simple.

The following are some easy to follow examples using the `curl` tool.

Assuming that your Job Template ID is '1', your controller IP is 192.168.42.100, and that `admin` and `awxsecret` are valid login credentials, you can create a new job this way:

```
curl -f -k -H 'Content-Type: application/json' -XPOST \
--user admin:awxsecret \
https://192.168.42.100/api/v2/job_templates/1/launch/
```

This returns a JSON object that you can parse and use to extract the 'id' field, which is the ID of the newly created job. You can also pass extra variables to the Job Template call, as in the following example:

```
curl -f -k -H 'Content-Type: application/json' -XPOST \
-d '{"extra_vars": "{\"foo\": \"bar\"}"}' \
--user admin:awxsecret https://192.168.42.100/api/v2/job_templates/1/launch/
```

Note
The `extra_vars` parameter must be a string which contains JSON, not just a JSON dictionary. Use caution when escaping the quotes, etc.



## 20.11. Filtering instances returned by the dynamic inventory sources in the controller




By default, the dynamic inventory sources in automation controller (such as AWS and Google) return all instances available to the cloud credentials being used. They are automatically joined into groups based on various attributes. For example, AWS instances are grouped by region, by tag name, value, and security groups. To target specific instances in your environment, write your playbooks so that they target the generated group names.

For example:

```
---
- hosts: tag_Name_webserver
tasks:
...
```

You can also use the `Limit` field in the Job Template settings to limit a playbook run to a certain group, groups, hosts, or a combination of them. The syntax is the same as the `--limit parameter` on the ansible-playbook command line.

You can also create your own groups by copying the auto-generated groups into your custom groups. Make sure that the `Overwrite` option is disabled on your dynamic inventory source, otherwise subsequent synchronization operations delete and replace your custom groups.

## 20.12. Use an unreleased module from Ansible source with automation controller




If there is a feature that is available in the latest Ansible core branch that you want to use with your automation controller system, making use of it in automation controller is simple.

First, determine which is the updated module you want to use from the available Ansible Core Modules or Ansible Extra Modules GitHub repositories.

Next, create a new directory, at the same directory level of your Ansible source playbooks, named `/library` .

When this is created, copy the module you want to use and drop it into the `/library` directory. It is consumed first by your system modules and can be removed once you have updated the stable version with your normal package manager.

## 20.13. Use callback plugins with automation controller




Ansible has a flexible method of handling actions during playbook runs, called callback plugins. You can use these plugins with automation controller to do things such as notify services upon playbook runs or failures, or send emails after every playbook run.

For official documentation on the callback plugin architecture, see [Developing plugins](http://docs.ansible.com/developing_plugins.html#callbacks) .

Note
Automation controller does not support the `stdout` callback plugin because Ansible only permits one, and it is already being used for streaming event data.



You might also want to review some example plugins, which should be modified for site-specific purposes, such as those available at: [https://github.com/ansible/ansible/tree/devel/lib/ansible/plugins/callback](https://github.com/ansible/ansible/tree/devel/lib/ansible/plugins/callback)

To use these plugins, put the callback plugin `.py` file into a directory called `/callback_plugins` alongside your playbook in your automation controller Project. Then, specify their paths (one path per line) in the **Ansible Callback Plugins** field of the Job settings:

![Ansible Callback plugins](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Configuring_automation_execution-en-US/images/3866c8302282943e8b9d8bd74541d098/configure-controller-jobs-callback.png)


Note
To have most callbacks shipped with Ansible applied globally, you must add them to the `callback_whitelist` section of your `ansible.cfg` .

If you have custom callbacks, see [Enabling callback plugins](https://docs.ansible.com/ansible/latest/plugins/callback.html#enabling-callback-plugins) .



## 20.14. Connect to Windows with winrm




By default, automation controller attempts to `ssh` to hosts.

You must add the `winrm` connection information to the group variables to which the Windows hosts belong.

To get started, edit the Windows group in which the hosts reside and place the variables in the source or edit screen for the group.

To add `winrm` connection info:

- Edit the properties for the selected group by clicking on the Edit![Edit](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Configuring_automation_execution-en-US/images/e5cb7f9b0cfe60ab5ba421bd17ecbb6a/leftpencil.png)
icon of the group name that contains the Windows servers. In the "variables" section, add your connection information as follows: `    ansible_connection: winrm`


When complete, save your edits. If Ansible was previously attempting an SSH connection and failed, you should re-run the job template.

## 20.15. Import existing inventory files and host/group vars into automation controller




To import an existing static inventory and the accompanying host and group variables into automation controller, your inventory must be in a structure similar to the following:

```
inventory/
|-- group_vars
|   `-- mygroup
|-- host_vars
|   `-- myhost
`-- hosts
```

To import these hosts and vars, run the `awx-manage` command:

```
awx-manage inventory_import --source=inventory/ \
--inventory-name="My Controller Inventory"
```

If you only have a single flat file of inventory, a file called ansible-hosts, for example, import it as follows:

```
awx-manage inventory_import --source=./ansible-hosts \
--inventory-name="My Controller Inventory"
```

In case of conflicts or to overwrite an inventory named "My Controller Inventory", run:

```
awx-manage inventory_import --source=inventory/ \
--inventory-name="My Controller Inventory" \
--overwrite --overwrite-vars
```

If you receive an error, such as:

```
ValueError: need more than 1 value to unpack
```

Create a directory to hold the hosts file, as well as the group_vars:

```
mkdir -p inventory-directory/group_vars
```

Then, for each of the groups that have :vars listed, create a file called `inventory-directory/group_vars/&lt;groupname&gt;` and format the variables in YAML format.

The importer then handles the conversion correctly.


<span id="idm140603452571680"></span>
# Legal Notice

Copyright© 2025 Red Hat, Inc.
The text of and illustrations in this document are licensed by Red Hat under a Creative Commons Attribution–Share Alike 3.0 Unported license ("CC-BY-SA"). An explanation of CC-BY-SA is available at [http://creativecommons.org/licenses/by-sa/3.0/](http://creativecommons.org/licenses/by-sa/3.0/) . In accordance with CC-BY-SA, if you distribute this document or an adaptation of it, you must provide the URL for the original version.
Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.
Red Hat, Red Hat Enterprise Linux, the Shadowman logo, the Red Hat logo, JBoss, OpenShift, Fedora, the Infinity logo, and RHCE are trademarks of Red Hat, Inc., registered in the United States and other countries.
Linux® is the registered trademark of Linus Torvalds in the United States and other countries.
Java® is a registered trademark of Oracle and/or its affiliates.
XFS® is a trademark of Silicon Graphics International Corp. or its subsidiaries in the United States and/or other countries.
MySQL® is a registered trademark of MySQL AB in the United States, the European Union and other countries.
Node.js® is an official trademark of Joyent. Red Hat is not formally related to or endorsed by the official Joyent Node.js open source or commercial project.
TheOpenStack® Word Mark and OpenStack logo are either registered trademarks/service marks or trademarks/service marks of the OpenStack Foundation, in the United States and other countries and are used with the OpenStack Foundation's permission. We are not affiliated with, endorsed or sponsored by the OpenStack Foundation, or the OpenStack community.
All other trademarks are the property of their respective owners.





