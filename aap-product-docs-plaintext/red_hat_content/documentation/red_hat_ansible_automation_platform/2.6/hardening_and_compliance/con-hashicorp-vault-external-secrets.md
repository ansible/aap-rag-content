# 2. Hardening Ansible Automation Platform
## 2.4. Day two operations
### 2.4.3. Using HashiCorp vault for external secrets management




You can integrate HashiCorp Vault with Ansible Automation Platform to manage and retrieve sensitive data.

#### 2.4.3.1. Configuring Ansible Automation Platform to communicate with HashiCorp vault




In an enterprise environment, having externally managed secrets is a convenient way to manage sensitive data across multiple services. One of the most common and recommended authentication methods for the HashiCorp vault is to use AppRoles with policies and login requirements that must be satisfied before a token is issued. To configure Ansible Automation Platform to use secrets stored in HashiCorp vault, set up a new credential with the type of HashiCorp Vault Secret Lookup. For information on how to do this, see [Hashicorp vault secret lookup](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/configuring_automation_execution/assembly-controller-secret-management#ref-hashicorp-vault-lookup) .

Enter relevant information such as an identifiable credential name, organization, and the URL of the vault server, for example, [https://vault.domain.com:8200](https://vault.domain.com:8200) .

Populate the necessary fields with your information such as Token, AppRole role_id, and AppRole secret_id, then select v2 for the API version.

To test the credential to test for functionally and operation, use the following procedure:

**Procedure**

1. Before clicking on **Create Credential** , clickTest.
1. In the pop-up box, enter the **Path to Secret** and the **Key Name** .

Note
The **Path to Secret** will be prefixed by `    kv` if storing a key-value pair, for example, `    kv/key_name` .




1. ClickRun.
1. When the test is successful, clickCreate Credential.
1. When complete, Ansible Automation Platform is properly configured to use HashiCorp Vault as an external secret source.


#### 2.4.3.2. Using HashiCorp Vault credentials within Ansible Automation Platform




To use HashiCorp vault credentials within Ansible Automation Platform, create a new credential with the type **Machine Credential** . Enter relevant information such as an identifiable credential name and an organization.

To configure the use of HashiCorp Vault credentials, use the following procedure:

**Procedure**

1. To configure the **Username** , click the![Key](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Hardening_and_compliance-en-US/images/fc669abfeec02bb8bda89a0de40c0391/leftkey.png)
icon.
1. Select the HashiCorp Vault credentials that were created in step 1.
1. Populate **Path to Secret** and the **Key Name** .
1. Optionally, clickTest. Otherwise, clickFinish.


#### 2.4.3.3. Configuring the machine credential’s SSH private key




Use the following procedure:

**Procedure**

1. To configure the **Username** , click the![Key](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Hardening_and_compliance-en-US/images/fc669abfeec02bb8bda89a0de40c0391/leftkey.png)
icon.
1. Select the HashiCorp Vault credentials that you created.
1. Populate the **Path to Secret** and the **Key Name** .
1. Select the name of the private key as the **Key Name** .
1. Optionally, clickTest. Otherwise, clickFinish.


