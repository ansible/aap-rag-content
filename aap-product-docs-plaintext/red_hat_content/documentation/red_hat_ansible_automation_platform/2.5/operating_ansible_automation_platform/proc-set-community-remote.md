# 3. Configuring Ansible Automation Platform to use egress proxy
## 3.5. Configuring Proxy settings on automation hub




If your private automation hub is behind a network proxy, you can configure proxy settings on the remote to sync content located outside of your local network.

**Prerequisites**

- You have **Modify Ansible repo content** permissions. For more information on permissions, see [Access management and authentication](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication) .
- You have a `    requirements.yml` file that identifies those collections to synchronize from Ansible Galaxy as in the following example:

**Requirements.yml example**


```
collections:      # Install a collection from Ansible Galaxy.      - name: community.aws        version: 5.2.0        source: https://galaxy.ansible.com
```





**Procedure**

1. Log in to Ansible Automation Platform.
1. From the navigation panel, selectAutomation Content→Remotes.
1. In the **Details** tab in the **Community** remote, clickEdit remote.
1. In the **YAML requirements** field, paste the contents of your `    requirements.yml` file.
1. ClickSave remote.


**Result**

You can now synchronize collections identified in your `requirements.yml` file from Ansible Galaxy to your private automation hub.


**Next steps**

See [Synchronizing Ansible content collections in automation hub](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/managing_automation_content/managing-cert-valid-content#assembly-synclists) for syncing steps.


