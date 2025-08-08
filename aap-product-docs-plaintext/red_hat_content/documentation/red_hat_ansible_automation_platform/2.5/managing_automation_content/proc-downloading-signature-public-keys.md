# 1. Red Hat Certified, validated, and Ansible Galaxy content in automation hub
## 1.3. Collections and content signing in private automation hub
### 1.3.3. Downloading signature public keys




After you sign and approve collections, download the signature public keys from the Ansible Automation Platform UI. You must download the public key before you add it to the local system keyring.

**Procedure**

1. Log in to Ansible Automation Platform.
1. From the navigation panel, selectAutomation Content→Signature Keys. The Signature Keys dashboard displays a list of multiple keys: collections and container images.


- To verify collections, download the key prefixed with `        collections-` .
- To verify container images, download the key prefixed with `        container-` .

1. Choose one of the following methods to download your public key:


- Click theDownload Keyicon to download the public key.
- Click theCopy to clipboardnext to the public key you want to copy.



**Verification**

Use the public key that you copied to verify the content collection that you are installing.


