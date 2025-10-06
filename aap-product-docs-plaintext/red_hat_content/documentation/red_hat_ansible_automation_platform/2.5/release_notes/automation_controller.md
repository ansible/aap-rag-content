# 10. Patch releases
## 10.1. Ansible Automation Platform patch release September 23, 2025
### 10.1.6. Automation controller




#### 10.1.6.1. Bug Fixes




- Fixed an issue where the galaxy credentials could not be created and edited without the need to specify an organization. (AAP-52197)
- Fixed an issue where the job template creation failed using `    ansible.controller.job_template` when multiple inventories shared the same name across different organizations. (AAP-51311)
- Fixed an issue that did not allow a user to save **Schedule for Workflow** job template when **Limit has Prompt on Launch** was enabled. (AAP-49794)
- The export command now works through the automation controller collection or with `    awxkit` when the correct environment variable is provided. (AAP-49452)
- Fixed an issue where there were double escaped quotes in `    api/v2/jobs/{id}/stdout/?format=txt` . (AAP-49077)
- Fixed an issue where the fact storage was not working when automation controller’s time zone was not UTC. (AAP-45933)
- Fixed a bug where exports did not work on deployments using the platform gateway. The export module in the collection now honors the `    CONTROLLER_OPTIONAL_API_URLPATTERN_PREFIX` environment variable. (AAP-39265)


