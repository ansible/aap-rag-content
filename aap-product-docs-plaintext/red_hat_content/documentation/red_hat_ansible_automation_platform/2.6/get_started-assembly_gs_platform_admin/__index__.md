# Get started as a platform administrator

As a platform administrator, Ansible Automation Platform helps you enable your users and teams to develop and run automation.

Learn the basic steps to get set up as an administrator for Ansible Automation Platform, including configuring and maintaining the platform for users.

To get started as an administrator, learn to:

- Log in for the first time.
- Configure authentication.
- Manage user access with role-based access control.

## Log in for the first time

Log in to the Ansible Automation Platform as an administrator and enter your subscription information. You can then create user profiles and assign roles.

### Procedure

1.  With the login information provided after your installation completed, open a web browser and log in to Red Hat Ansible Automation Platform by navigating to the server URL at: `https://<AAP_SERVER_NAME>/`
2.  Use the credentials specified during the installation process to login:

- The default username is **admin**.
- The password for **admin** is the value specified during installation.

### What to do next

After your first login, you must add your subscription information to begin using the platform.

## Add your subscription

To add your subscription information, you can either upload your subscription manifest, or use your service account credentials to find the subscription associated with your account.

### Before you begin

To add your subscription by uploading a subscription manifest, you must first:

- Obtain your manifest file. See [Obtaining a manifest file](/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_aap_manifest_files#assembly-aap-obtain-manifest-files "You can obtain a subscription manifest in the Subscription Allocations section of Red Hat Subscription Management.") for more information.


To add your subscription using your service account credentials, you must first:

- Have [created a service account](https://docs.redhat.com/en/documentation/red_hat_hybrid_cloud_console/1-latest/html/creating_and_managing_service_accounts/proc-ciam-svc-acct-overview-creating-service-acct#proc-ciam-svc-acct-create-creating-service-acct) and saved the client ID and client secret.
- Add your service account to the Subscription viewer user group to give it the ability to see your subscriptions. See the "Updates to subscription management" section in the Knowledgebase article [Configure Ansible Automation Platform to authenticate through service account credentials](https://access.redhat.com/articles/7112649) for instructions on how to do so.

### Procedure

1.  To add your subscription by uploading a subscription manifest:
1.  Drag the file to the field beneath **Red Hat subscription manifest** or browse for the file on your local machine.
2.  To add your subscription with your service account credentials:
1.  Click the **Service Account** tab.
2.  Enter the **client ID** you received when you created your service account in the field labeled Client ID.
3.  Enter the **client secret** you received when you created your service account in the field labeled Client secret. Your subscription appears in the **Subscription** list.

3.  Select your subscription and click Next.   1.  Check the box indicating that you agree to the **End User License Agreement**.
2.  Review your information and click Finish.

If you enter your client ID and client secret but cannot locate your subscription, you might not have the correct permissions set on your service account. For more information and troubleshooting guidance for service accounts, see [Configure Ansible Automation Platform to authenticate through service account credentials](https://access.redhat.com/articles/7112649).

## Configure authentication

After your first login as an administrator, begin configuring authentication for your users. Depending on your organization’s needs and resources, you can either:

- Set up authentication by creating users, teams, and organizations, and then assigning them roles that govern access.
- Use an external source such as GitHub to configure authentication for your system.


The following sections serve as an introduction to authentication in Ansible Automation Platform.

## Manage user access with role-based access control

Role-based access control (RBAC) restricts user access based on the user’s role within the organization they are assigned to in Ansible Automation Platform. The roles in RBAC refer to the levels of access that users have to Ansible Automation Platform components and resources.

Use RBAC to control what users can do with the components of Ansible Automation Platform at a broad or granular level. You can choose whether the user is a system administrator or normal user, and align roles and access permissions with their positions within the organization.

You can define roles with multiple permissions that can then be assigned to resources, teams, and users. The permissions that make up a role govern what the assigned role allows. Permissions are allocated with only the access needed for a user to perform the tasks appropriate for their role.

The following procedures show how to get started with RBAC by creating a team, and a user to assign to the team.

Important:

When managing users, teams, and organizations, use the Unified UI or the platform gateway API to ensure real-time synchronization across all platform components, including Event-Driven Ansible controller. If you use the legacy automation controller API, changes can take up to 15 minutes to propagate to Event-Driven Ansible controller, which can result in authentication errors for new users or teams.

## Create an organization

Ansible Automation Platform automatically creates a default organization. If you have a self-support level license, you have only the default organization available and cannot delete it.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Organizations.
2.  Click Create organization.
3.  Enter the **Name** and give a **Description** for your organization. Note:
If automation controller is enabled on the platform, continue with Step 4. Otherwise, proceed to Step 6.

4.  Select the name of the **Execution environment** or search for one that members of this organization can use to run automation.
5.  Enter the name of the **Instance Groups** on which to run this organization.
6.  Optional: Enter the **Galaxy credentials** or search from a list of existing ones.
7.  Select the **Max hosts** for this organization. The default is 0. When this value is 0, it signifies no limit. If you try to add a host to an organization that has reached or exceeded its cap on hosts, an error message displays:


```
You have already reached the maximum number of 1 hosts allowed for your organization. Contact your System Administrator for assistance.
```

8.  Click Next.
9.  If you selected more than 1 instance group, you can manage the order by dragging and dropping the instance group up or down in the list and clicking Confirm. Note:
The execution precedence is determined by the order in which the instance groups are listed.

10.  Click Next and verify the organization settings.
11.  Click Finish.

## Create a team

Manage teams by creating them, assigning an organization, and adding [users](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_controller_teams#proc-gw-team-add-user "To assign a user to a team, the user must already have been created. For more information, see Creating a user. Assigning a user to a team adds them as a member only. Use the Roles tab to assign a role that gives users on the team resource access.") or [administrators](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_controller_teams#proc-gw-add-admin-team "Assign existing users as administrators to a team so they can manage its membership and settings. This allows designated administrators to create new users and grant permissions within the team."). Team members automatically inherit all assigned roles and permissions. Users must exist in the system before they can be added to a team.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Teams.
2.  Click Create team.
3.  Enter a **Name** and optionally give a **Description** for the team.
4.  Select an **Organization** to be associated with this team. Note:
Each team can only be assigned to one organization.

5.  Click Create team. The **Details** page opens, where you can review and edit your team information and access.

## Create a user

You can create three types of users in Ansible Automation Platform:

### About this task

Normal user
Normal users have read and write access limited to the resources (such as inventory, projects, and job templates) for which that user has been granted the appropriate roles and privileges. Normal users are the default type of user when no other **User type** is specified.

Ansible Automation Platform Administrator
An administrator (also known as a Superuser) has full system administration privileges, with full read and write privileges over the entire installation. An administrator is typically responsible for managing all aspects of and delegating responsibilities for day-to-day work to various users.

Ansible Automation Platform Auditor
Auditors have read-only capability for all objects within the environment.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Users.
2.  Click Create user.
3.  Enter the details about your new user in the fields on the **Create user** page. Fields marked with an asterisk (*) are required.
4.  Normal users are the default when no **User type** is specified. To define a user as an administrator or auditor, select a **User type** from the drop-down menu. Note:
If you are modifying your own password, log out and log back in for the change to take effect.

5.  Select the **Organization** to be assigned for this user. For information about creating a new organization, see [Creating an organization](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-proc_controller_create_organization#proc-controller-create-organization "Ansible Automation Platform automatically creates a default organization. If you have a self-support level license, you have only the default organization available and cannot delete it.").
6.  Click Create user. When the user is successfully created, the **User** details screen opens. From here, you can review and change the user’s teams, roles, tokens and other membership details.

Note:
If the user is not newly-created, the details screen displays the user’s last login activity.

### What to do next

If you log in as yourself, and view the details of your user profile, you can manage tokens from your user profile by selecting the **Tokens** tab. For more information, see [Adding a token](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-proc_controller_create_application#proc-controller-apps-create-tokens "You can view a list of users that have tokens to access an application by selecting the Tokens tab in the OAuth Applications details page.").
