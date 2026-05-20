# 9. Patch releases
## 9.7. Ansible Automation Platform patch release November 19, 2025
### 9.7.2. Ansible Automation Platform

#### 9.7.2.1. Features

- Allows for Event-Driven Ansible to add CA Certificates in gateway which can then be used by **Envoy** to do certificate based authorization for mTLS `EventStreams`.(AAP-56770)

#### 9.7.2.2. Enhancements

- Red Hat Ansible Lightspeed section has been removed from the left navigation bar.(AAP-53006)

- Added fallback-authenticator feature, which allows users to configure `fallback_authentication` for running custom logic in the event local authentication fails.


- Set all existing local authenticators and those created on initial install to fallback to controller credentials.
- The ability to clear the preset if the user does not want to fallback to controller authorization anymore.(AAP-56919)

- Ansible Lightspeed intelligent assistant has expanded its support for third-party Large Language Model (LLM) providers, and now includes OpenAI and Microsoft Azure. Third-party LLM support is available for both OpenShift Container Platform operator installation and containerized installation.


- For more information, see [Deploying the Ansible Lightspeed intelligent assistant on Red Hat OpenShift Container Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/installing_on_openshift_container_platform/deploying-chatbot-operator) and [Deploying the Ansible Lightspeed intelligent assistant on containerized installation](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/deploying-lightspeed-containerized-install).(ANSTRAT-1673)

#### 9.7.2.3. Bug Fixes

- Fixed a significant performance regression in response time for GET requests to */role_definitions/* and related endpoints.(AAP-56868)
- Fixed an issue where users who existed in Ansible Automation Platform 2.5 with controller legacy authentication, but never logged in were unable to attempt authentication with controller in Ansible Automation Platform 2.6, and were left in an unusable state.(AAP-56388)
- Fixed issue in which superuser status would sync from platform gateway to other components if set to `True`, but not if set to `False`, where administrator privileges were not removed from the other components in all cases.(AAP-56296)
- Fixed an issue where platform auditors were not able to view all platform level settings.(AAP-55608)
- Fixed an issues where the **Team** input field on the authentication mapping form was not hidden when an organization role was selected.(AAP-55602)
- Fixed an issue where the workflow visualizer CSS was displaying the incorrect height.(AAP-55164)
- Fixed an issue using the and condition with multiple attributes. Previously the authentication map would skip the missing attributes, now, the map will be applied only if all attributes are present and the condition(s) are met.(AAP-53612)
- Fixed an issue where the `LOGIN_REDIRECT_OVERRIDE` did not allow for a bypass URL. A login page has been added at */login* to bypass the `LOGIN_REDIRECT_OVERRIDE` setting when it is misconfigured.(AAP-53471)
- Fixed the Subscription Usage chart where it did not always display at full height.(AAP-52218)
- Fixed an issue that was preventing users from viewing complete survey question choices that contained a colon.(AAP-50290)
- Fixed an issue where a warning message was not available when a user tried to restart an activation in the **workers offline** status.(AAP-24009)
- Fixed an issue where filtering platform resources by special characters did not work as expected.(AAP-52360)
- Fixed an issue where, applying a domains filter on the Jobs tab and navigating to the **Projects** section, then selecting a project with multiple templates, caused the system to display only the job template that was filtered by the domain, hiding other templates and showing a misleading message.(AAP-48031)
- Fixed an issue where there was no limit filtering to the jobs page.(AAP-45218)
- Fixed a form validation issue on the **Login redirect override** field in platform gateway settings.(AAP-40517)
- Fixed an execution environment deletion warning.(AAP-55135)

