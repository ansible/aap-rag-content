# Integrate with Red Hat Lightspeed (formerly Insights)
## Create Red Hat Lightspeed credentials

To create a Red Hat Lightspeed credential, use the following procedure.

### Before you begin

- To use token-based authentication, you must [create a Red Hat service account](https://docs.redhat.com/en/documentation/red_hat_hybrid_cloud_console/1-latest/html/creating_and_managing_service_accounts/proc-ciam-svc-acct-overview-creating-service-acct#proc-ciam-svc-acct-create-creating-service-acct) to generate a **Client ID** and **Client secret**.
- Assign this service account to the appropriate **User Access** group with necessary permissions.


To enable integration between Ansible Automation Platform and Red Hat Lightspeed, assign the service account the following permissions:

- **inventory:hosts:read** (included in the Inventory Hosts viewer role)
- **patch:read** (included in the Patch viewer role)
- **remediations:remediation:read** and **playbook-dispatcher:run:read** (included in the Remediations user role)


You might consider associating your service account with an existing user access group that already has the required permissions, or creating a new user access group.

Note:

In adherence to security guidelines, service accounts are not automatically included in the default access group. To grant access, you must manually add them to the appropriate user access groups.

If you are not an organization administrator, you can create a service account and then ask your administrator to add your account to the appropriate user access groups.

After you have created a service account and assigned it the appropriate permissions, you can create a new credential for use with Red Hat Lightspeed.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Credentials.
2.  Click Create credential.
3.  Enter the appropriate details in the following fields:

- **Name**: Enter the name of the credential.
- Optional: **Description**: Enter a description for the credential.
- Optional: **Organization**: Enter the name of the organization with which the credential is associated, or click the search ![Search](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/search.png) icon and select it from the **Select organization** window.
- **Credential type**: Enter **Red Hat Lightspeed** or select it from the list.  Note:
Use the **Username** and **Password** fields for Basic authentication. You can leave these blank if using **Client ID** and **Client secret**.

- **Client ID**: Enter the client ID you received when you created your service account.
- **Client secret**: Enter the client secret you received when you created your service account.

4.  Click Create credential. You can now use this credential in an [Source an inventory from Red Hat Lightspeed](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_add_source#proc-controller-inv-source-rhlightspeed "You can create an inventory source that uses Red Hat Lightspeed as the source of hosts.") and [Red Hat Lightspeed project](/documentation/en-us/red_hat_ansible_automation_platform/2.7/integrate-assembly_ug_controller_setting_up_insights#controller-create-insights-project "Create an automation controller project linked to Red Hat Lightspeed and retrieve remediation playbooks. This streamlines your efforts to address vulnerabilities and keep system configurations.").

- If you receive a project sync failure, see the steps in [Remediating a Red Hat Lightspeed inventory](/documentation/en-us/red_hat_ansible_automation_platform/2.7/integrate-assembly_ug_controller_setting_up_insights#controller-remediate-insights-inventory "Remediation of a Red Hat Lightspeed inventory enables automation controller to run Red Hat Lightspeed playbooks with a single click.") and check your analytics logs.


Important:

You must recreate existing credentials and reassociate them with existing projects and inventory sources to support token-based authentication.

