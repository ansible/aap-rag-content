# 6. Red Hat Ansible Automation Platform credential
## 6.1. Replacing controller tokens in Red Hat Ansible Automation Platform 2.6
### 6.1.2. Deleting controller tokens




Before configuring the new Red Hat Ansible Automation Platform credentials, delete all existing controller tokens, which are now deprecated and will conflict with the new Red Hat Ansible Automation Platform credentials.

**Prerequisites**

- You have deleted all rulebook activations that use controller tokens.


**Procedure**

1. Log in to the Ansible Automation Platform Dashboard.
1. From the top navigation panel, select your profile.
1. Click **User details** .
1. Select the **Tokens** tab.
1. Delete all of your previous controller tokens.


**Next steps**

After deleting the controller tokens and rulebook activations, proceed with [Setting up a Red Hat Ansible Automation Platform credential](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_automation_decisions/eda-set-up-rhaap-credential-type#eda-set-up-rhaap-credential) .


