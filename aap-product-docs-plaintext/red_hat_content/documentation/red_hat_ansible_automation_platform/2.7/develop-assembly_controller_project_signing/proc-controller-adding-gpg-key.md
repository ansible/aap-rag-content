# Enforce project integrity with signing and verification
## Sign content in automation projects
### Add a GPG key to automation controller

You can add a GPG public key to automation controller and enable content signing and validation for your projects.

#### About this task

To use the GPG key for content signing and validation in automation controller, add it by running the following command in the CLI:

```
$ gpg --list-keys
$ gpg --export --armour <key fingerprint> > my_public_key.asc
```

#### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Credentials.
2.  Click Create credential.
3.  Give a meaningful name for the new credential, for example, "Infrastructure team public GPG key".
4.  In the **Credential type** field, select **GPG Public Key**.
5.  Click **Browse** to locate and select the public key file, for example, `my_public_key.asc`.
6.  Click Create credential. You can select this credential in `projects <ug_projects_add>`, and content verification automatically takes place on future project synchronizations.

Note:
Use the project cache SCM timeout to control how often you want automation controller to re-validate the signed content. When a project is configured to update on launch (of any job template configured to use that project), you can enable the cache timeout setting, which sets it to update after `N` seconds have passed since the last update. If validation is running too often, you can slow down how often project updates occur by specifying the time in the **Cache Timeout** field of the **Options Details** view of the project.

![Project Cache Timeout option](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/project-update-launch-cache-timeout.png)

