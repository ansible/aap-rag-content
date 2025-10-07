# 8. Fixed issues
## 8.1. Ansible Automation Platform




Note
Ansible Automation Platform 2.6 also includes the fixes from the latest 2.5 patch release. For more information see [Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/release_notes/patch_releases#aap-25-20250923) patch release September 23, 2025.



Ansible Automation Platform

- The `    SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL` configuration parameter now functions as expected, allowing social auth logins to set the platform gateway username to the user’s email when enabled.(AAP-49736)


RPM-based Ansible Automation Platform

- Fixed an issue where installer managed CA certificates were discovered but not used by the installer.(AAP-53335)



<span id="idm139941017998560"></span>
