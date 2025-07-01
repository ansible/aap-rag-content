# 10. Patch releases
## 10.10. Ansible Automation Platform patch release February 13, 2025
### 10.10.2. Enhancements




#### 10.10.2.1. General




- The `    ansible.controller` collection has been updated to 4.6.8.(AAP-39848)
-  `    ansible.platform` collection has been updated to 2.5.20250213.(AAP-39740)
-  `    ansible.eda` collection has been updated to 2.4.0.(AAP-39577)


#### 10.10.2.2. Ansible Automation Platform




- It is now possible to configure automation hub without Redis PVC.(AAP-39600)


#### 10.10.2.3. Automation controller




- This release sees the addition of `    client_id` and `    client_secret` fields to the Insights credential to support service accounts via console.redhat.com.(AAP-36565)
- You are now able to specify the input for the `    client_id` and `    client_secret` for the insights credential via the `    awx.awx.credential_type` module.(AAP-37441)
- Updated `    awxkit` by adding service account support for Insights credential type, specifically adding the fields `    client_id` and `    client_secret` to `    credential_input_fields` .(AAP-39352)


#### 10.10.2.4. Automation execution environments




- The **file** command has been added to **ee-minimal** and **ee-supported** container images.(AAP-40009)


