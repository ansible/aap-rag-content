# 10. Patch releases
## 10.3. Ansible Automation Platform patch release July 30, 2025
### 10.3.3. Ansible Automation Platform




#### 10.3.3.1. Features




-  `    PosixUIDGroupType` can be selected for LDAP Group Type.(AAP-49347)


#### 10.3.3.2. Enhancements




- Optimized the handling of web socket messages from the Workflow Visualizer.(AAP-46800)


#### 10.3.3.3. Bug fixes




- Fixed the fields `    content_type` for role user assignments to indicate that null values are valid responses from the API.(AAP-49494)
- Fixed the fields `    team_ansible_id` for role team assignments to indicate that null values can be POSTed to the API.(AAP-49812)
- Fixed an issue where `    auto-complete` was not disabled on all forms for sensitive information such as usernames, passwords, secret keys, etc.(AAP-49079)
- Fixed an issue related to workflow job template limits overriding workflow job template node limits upon save.(AAP-48946)
- Fixed the **Min** and **Max** Limit values displayed on the **Edit Survey** form.(AAP-39933)
- Fixed an issue where the case insensitivity for authentication map user attribute names and values and for group names was not available. Feature flag `    FEATURE_CASE_INSENSITIVE_AUTH_MAPS` must be set to true to enable case insensitive comparisons.(AAP-49327)
- Fixed an issue that adds an OIDC Callback URL field that, after creation of authenticator, displays the URL to use in setting up the IdP. The URL field is displayed on the creation page and this field is to be left blank.(AAP-49874)


