# 9. Patch releases
## 9.9. Ansible Automation Platform patch release October 28, 2025
### 9.9.2. Ansible Automation Platform

#### 9.9.2.1. Features

- Added a step in the subscription wizard that allows the user to configure automation analytics.(AAP-55094)
- Added two new toggle options on the subscription wizard to allow for fetching subscriptions using basic authentication.(AAP-47865)

#### 9.9.2.2. Bug Fixes

- Fixed an issue where the `ansible-builder` and `ansible-navigator` did not use execution environment images from ansible-automation-platform-26 namespace by default.(AAP-54934)
- Fixed an issue where the settings did not display **Red Hat** consistently in the API and UI.(AAP-54276)
- Fixed an issue where the decision environment dropdown was broken. Replaced the dropdown type for decision environments in the rulebook activation form so that when there are no decision environments available, the dropdown displays No results found instead of an empty dropdown.(AAP-53844)
- Fixed an issue where creating resources with `cookie/xcrf` token failed. Aligned dependency versions between Konflux build and component repository.(AAP-53561)
- Fixed an issue where the component label for the Platform Auditor role did not display all components.(AAP-53551)
- Fixed an issue where empty strings were displayed in the extra variables field on the **Jobs > Details** page.(AAP-49448)
- Fixed an issue where the **Load More** in authentication mapping role dropdown did not work.(AAP-54049) HubName
- Fixed an issue where the user was unable to create Event-Driven Ansible or automation hub roles when creating a custom role and selecting the **Automation Decisions** project or credential types because the UI displayed only the automation controller permissions.(AAP-54756) ControllerName
- Fixed an issue where the PatternFly 6 Upgrade broke the Ansible Automation Platform topology layout and fullscreen mode.(AAP-51106)
- Fixed an issue where some fields were missing `autocomplete = new-password` setting.(AAP-55783)
- Fixed an issue where the user was unable to select the default execution environment in the automation settings page.(AAP-39321)
- Fixed an issue where the LDAP Group Type parameters failed to save user preferences when the language was initially set to `es_ES`, resulting in a wrong version displayed on the user interface due to an uninitialized translation object.(AAP-56356)
- Fixed an issue that prevented SAML and AzureAD authentication when local user accounts share the same email address.(AAP-56518)

#### 9.9.2.3. Deprecated

- Subscription credentials can no longer be viewed/edited from the system settings page.(AAP-55014)

