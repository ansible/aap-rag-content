# Configure local authentication

As a platform administrator, you can configure local system authentication. With local authentication, users and their passwords are checked against local system accounts.

## About this task

Note:

A local authenticator is automatically created by the Ansible Automation Platform installation process, and is configured with the specified admin credentials in the inventory file before installation. After successful installation, you can log in to the Ansible Automation Platform using those credentials.

## Procedure

1.  From the navigation panel, select Access Management> (and then)Authentication Methods.
2.  Click Create authentication.
3.  Enter a **Name** for this Local configuration. The configuration name is required, must be unique across all authenticators, and must not be longer than 512 characters.
4.  Select **Local** from the **Authentication type** list.
5.  Optional: Enter any **Additional Authenticator Fields** that this authenticator can take. These fields are not validated and are passed directly back to the authenticator. Note:
Values defined in this field override the dedicated fields provided in the UI. Any values not defined here are not provided to the authenticator.

6.  To automatically create organizations, users, and teams upon successful login, select **Create objects**.
7.  To enable this authentication method upon creation, select **Enabled**.
8.  To remove a user for any groups they were previously added to when they authenticate from this source, select **Remove users**.
9.  Click Next.

## What to do next

To control which users are allowed into the Ansible Automation Platform server, and placed into Ansible Automation Platform organizations or teams based on their attributes (such as username and email address) or to what groups they belong, continue to [Mapping](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_mapping#gw-mapping "To control which users are allowed into the Ansible Automation Platform server, and placed into Ansible Automation Platform organizations or teams based on their attributes (such as username and email address) or what groups they belong to, you can configure authenticator maps.").
