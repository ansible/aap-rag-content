# 1. Red Hat Certified, validated, and Ansible Galaxy content in automation hub
## 1.3. Content signing in private automation hub
### 1.3.2. Signing content in private automation hub




After you have configured content signing on your private automation hub, you can manually sign a new collection or replace an existing signature with a new one. When users download a specific collection, this signature indicates that the collection is for them and has not been modified after certification.

You can use content signing on private automation hub in the following scenarios:

- Your system does not have automatic signing configured and you must use a manual signing process to sign collections.
- The current signatures on the automatically configured collections are corrupted and need new signatures.
- You need additional signatures for previously signed content.
- You want to rotate signatures on your collections.


**Procedure**

1. Log in to Ansible Automation Platform.
1. From the navigation panel, selectAutomation Content→Collection Approvals. The Approval dashboard opens and displays a list of collections.
1. Click the thumbs up icon next to the collection you want to approve. On the modal that appears, check the box confirming that you want to approve the collection, and clickApprove and sign collections.


**Verification**

- Navigate toAutomation Content→Collectionsto verify that the collections you signed and approved are displayed.


