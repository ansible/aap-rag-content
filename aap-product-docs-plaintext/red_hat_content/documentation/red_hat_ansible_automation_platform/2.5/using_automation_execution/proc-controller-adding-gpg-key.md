# 12. Project Signing and Verification
## 12.3. Adding a GPG key to automation controller




To use the GPG key for content signing and validation in automation controller, add it by running the following command in the CLI:

```
$ gpg --list-keys
$ gpg --export --armour &lt;key fingerprint&gt; &gt; my_public_key.asc
```

1. From the navigation panel, selectAutomation Execution→Infrastructure→Credentials.
1. ClickCreate credential.
1. Give a meaningful name for the new credential, for example, "Infrastructure team public GPG key".
1. In the **Credential type** field, select **GPG Public Key** .
1. Click **Browse** to locate and select the public key file, for example, `    my_public_key.asc` .
1. ClickCreate credential.

You can select this credential in `    projects &lt;ug_projects_add&gt;` , and content verification automatically takes place on future project synchronizations.




Note
Use the project cache SCM timeout to control how often you want automation controller to re-validate the signed content. When a project is configured to update on launch (of any job template configured to use that project), you can enable the cache timeout setting, which sets it to update after `N` seconds have passed since the last update. If validation is running too often, you can slow down how often project updates occur by specifying the time in the **Cache Timeout** field of the **Options Details** view of the project.

![Project Cache Timeout option](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_automation_execution-en-US/images/27be51ae415c06538624e8f308ddd487/project-update-launch-cache-timeout.png)




