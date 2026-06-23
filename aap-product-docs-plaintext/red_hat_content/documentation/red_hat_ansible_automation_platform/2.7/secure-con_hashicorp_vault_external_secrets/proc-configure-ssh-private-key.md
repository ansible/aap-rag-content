# Integrate with HashiCorp to secure sensitive data
## Configure the machine credential’s SSH private key

Link your machine credential's SSH private key to HashiCorp Vault. Retrieving this key from an external secret management system helps ensure that sensitive authentication details are securely injected into your automation workflows.

### Procedure

1.  To configure the **Username**, click the ![Key](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/leftkey.png) icon.
2.  Select the HashiCorp Vault credentials that you created.
3.  Populate the **Path to Secret** and the **Key Name**.
4.  Select the name of the private key as the **Key Name**.
5.  Optionally, click Test. Otherwise, click Finish.
