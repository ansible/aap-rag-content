# 1. Red Hat Certified, validated, and Ansible Galaxy content in automation hub
## 1.1. Configuring Ansible automation hub remote repositories to synchronize content
### 1.1.2. Creating the offline token in automation hub




In automation hub, you can create an offline token using **Token management** . The offline token is a secret token used to protect your content, so be sure to store it in a secure location.

**Procedure**

1. Navigate to [Ansible Automation Platform on the Red Hat Hybrid Cloud Console](https://console.redhat.com/ansible/automation-hub/token/) .
1. From the navigation panel, selectAutomation Hub→Connect to Hub.
1. Under **Offline token** , clickLoad Token.
1. Click theCopy to clipboardicon to copy the offline token.
1. Paste the token into a file and store in a secure location.


**Additional resources**

Your offline token expires after 30 days of inactivity. For more on obtaining a new offline token, see [Keeping your offline token active](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/managing_automation_content/managing-cert-valid-content#con-offline-token-active_cloud-sync) .


**Next step**

The offline token is now available for configuring automation hub as your default collections server or for uploading collections by using the `ansible-galaxy` command line tool.


