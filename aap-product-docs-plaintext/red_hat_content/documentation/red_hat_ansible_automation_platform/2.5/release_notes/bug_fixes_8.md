# 10. Patch releases
## 10.2. Ansible Automation Platform patch release October 22, 2025
### 10.2.7. Bug fixes




#### 10.2.7.1. Ansible Automation Platform




- Fixed an issue where the UI triggered expensive queries on list endpoints that could be avoided. Query performance is now optimized on the Jobs list page and for loading user administrative data during login.(AAP-54299)
- Fixed an issue where the settings displayed **Red Hat** inconsistently in the API and UI.(AAP-54277)
- Fixed an issue where Ansible Automation Platform 2.5 could not set or create a playbook when using branch override.(AAP-52566)
- Fixed an issue where the platform gateway did not use TLSv1.3 when communicating with other Ansible Automation Platform services.(AAP-49456)
- Fixed an issue where empty strings displayed in the extra variables field on the **Jobs > Details** page.(AAP-49448)
- Fixed an issue where the validation of prompt-on-launch credentials in a workflow job template did not handle updated credentials in the wizard.(AAP-40540)
- Fixed an issue where the error handling in the authenticator form did not match other forms in the platform UI. API errors for specific fields are now correctly mapped to the form fields in the UI.(AAP-22928)
- Fixed an issue where the platform auditors were not able to see automation execution and platform level settings.(AAP-53975)
- Fixed an issue where some fields were missing the `    autocomplete = new-password` setting.(AAP-53934)


#### 10.2.7.2. Ansible Automation Platform Operator




- Fixed an issue where the Red Hat Ansible Lightspeed API failed during Ansible Automation Platform idle.(AAP-54175)
- Fixed an issue that caused a failure to gather the job data from the automation controller API.(AAP-55635)
- Fixed an issue where the user could not set an image without the respective version, causing the installation to enter an error loop.(AAP-55927)
- Fixed an issue where backup and restore of an Ansible Automation Platform instance failed, restoring an upgraded Ansible Automation Platform environment from 2.4.(AAP-55649)


#### 10.2.7.3. Automation controller




- Fixed an issue where the platform auditor did not have access to automation controller settings.(AAP-55607)
- Fixed an issue where the `    system_administrator` role creation race condition, which happened on new Openshift deployments, resulted in the default instance group not being created.(AAP-54964)
- Fixed an issue where Grafana notifications could not have an empty dashboard ID or panel ID.(AAP-54654)
- Fixed an issue where the `    awx.awx.license` appears to succeed when given an invalid `    pool / subscription` .(AAP-54650)
- Fixed an issue where the platform auditor was unable to view the controller settings.(AAP-53345)
- Fixed an issue where there were missing instructions to set an environment variable in the CLI.(AAP-37812)
- Fixed an issue for comments in extra vars sections where they were not persistent. All comments in YAML now persist on create and edit operations for a resource.(AAP-37071)
- Fixed an issue where the controller metrics API was not accessible by the user with platform auditor role.(AAP-36492)
- Fixed an issue where there was a duplicate value for subsystem_metrics_pipe_execute_seconds detected under _api/controller/v2/metrics/_ on Ansible Automation Platform 2.5.(AAP-55621)
- Fixed and issue where the `    ansible.platform` collection did not work with the default Red Hat Ansible Automation Platform credential type.(AAP-55685)
- Fixed an issue where re-running the installer with a modified inventory hostname resulted in a traceback when the metrics were collected.(AAP-55638)


#### 10.2.7.4. Automation hub




- Fixed an issue where _/api/galaxy/_ui/v2/users/3/_ user detail displayed the data incorrectly.(AAP-54261)
- Fixed an issue where an http 500 Error was returned when getting _/api/galaxy/_ui/v2/users/3/_ .(AAP-55957)


#### 10.2.7.5. Container-based Ansible Automation Platform




- Fixed an issue where `    REDHAT_CANDLEPIN_VERIFY` CA permission was not set so that the controller could make requests to **subscription.rhsm.redhat.com** .(AAP-55181)
- Fixed an issue where Ansible would fail to gather the system’s UUID for Linux on Power.(AAP-54540)


#### 10.2.7.6. RPM-based Ansible Automation Platform




- Fixed an issue where setting `    automationgateway_disable_https=false` resulted in install failure.(AAP-55475)
- Fixed an issue where `    RESOURCE_KEY SECRET_KEY` was not updated when restoring from a different environment.(AAP-54944)
- Fixed an issue where Event-Driven Ansible DE credentials failed to populate on initial installation.(AAP-54520)
- Fixed an issue where the automation gateway `    envoy.log` did not receive logs after it was rotated.(AAP-54079)
- Fixed an issue where `    REDHAT_CANDLEPIN_VERIFY` CA permission was not set so that the controller could make requests to **subscription.rhsm.redhat.com** .(AAP-55184)


