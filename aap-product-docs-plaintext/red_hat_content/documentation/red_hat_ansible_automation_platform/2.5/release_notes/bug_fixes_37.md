# 10. Patch releases
## 10.13. Ansible Automation Platform patch release February 25, 2025
### 10.13.2. Bug fixes




#### 10.13.2.1. Ansible Automation Platform




- Fixed an issue where the subscription entitlement expiration notification was visible, even when the subscription was active.(AAP-39982)
- Fixed an issue where upon UI reload/refresh, logs of a running job before the refresh would not appear until new logs were generated from the playbook.(AAP-38924)
- Fixed an issue when the customer was unable to scale down replicas to put Ansible Automation Platform into idle mode.(AAP-39492)
- After launching the **Workflow Job Template** , the launched job for a job template node in the workflow should contain the `    job_tags` and `    skip_tags` that were specified in the **launch prompt** step.(AAP-40395)
- Fixed an issue where the user was not able to create a members role in Ansible Automation Platform 2.5.(AAP-37626)
- Fixed an issue where a custom image showed Base64 encoded data.(AAP-26984)
- Fixed an issue where a custom logo showed Base64 encoded data.(AAP-26909)
- Fixed an issue that restricted users from executing jobs for which they had the correct permissions.(AAP-40398)
- Fixed an issue where the workflow job template node extra vars were not saved.(AAP-40396)
- Fixed an issue where the Creating and using execution environments guide had the incorrect ansible-core version.(AAP-40390)
- Fixed an issue where you were not able to create a members role in Ansible Automation Platform 2.5.(AAP-40698)
- Fixed an issue where the initial login to any of the services from platform gateway could result in the user being given access to the wrong account.(AAP-40617)
- Fixed an issue where the service owned resources were not kept in sync with the platform gateway allowing for duplicate name values on user login.(AAP-40616)
- Fixed an issue where users, organizations, and teams, became permanently out of sync if any user, organization, or team, was deleted from the platform gateway.(AAP-40615)
- Fixed an issue where automation hub would fail to run the sync task if any users were deleted from the system.(AAP-40613)


#### 10.13.2.2. Platform gateway




- Fixed an issue where ping and status checks with resolvable, but nonresponding, URLs could cause all platform gateway `    uwsgi` workers to hang until all were exhausted. The new settings are `    PING_PAGE_CHECK_TIMEOUT` and `    PING_PAGE_CHECK_IGNORE_CERT` .(AAP-39907)


#### 10.13.2.3. Event-Driven Ansible




- Fixed an issue where credentials could be copied in AAP but could not be copied in Event-Driven Ansible.(AAP-35875)


#### 10.13.2.4. Known Issues




- In the platform gateway, the tooltip for **Projects → Create Project - Project Base Path** is undefined.(AAP-27631)
- Deploying the platform gateway on FIPS enabled RHEL 9 is currently not supported.(AAP-39146)


