# 10. Patch releases
## 10.7. Ansible Automation Platform patch release March 12, 2025
### 10.7.5. Bug fixes




With this update, the following CVEs have been addressed:

[CVE-2025-26791](https://access.redhat.com/security/cve/cve-2025-26791)  `automation-gateway` : Mutation XSS in `DOMPurify` due to improper template literal handling.(AAP-40402)

#### 10.7.5.1. Ansible Automation Platform




- Fixed an issue in the user collection module where running with `    state: present` would cause a stack trace.(AAP-40887)
- Fixed an issue that caused updates to SAML authenticators to ignore an updated public certificate provided via UI or API and then fail with the message **The certificate and private key do not match** .(AAP-40767)
- Fixed an issue with the `    ServiceAuthToken` destroy method to allow HTTP delete via `    ServiceAuth` to work properly.(AAP-37630)


#### 10.7.5.2. Platform gateway




- Fixed an issue that would prevent some types of resources from getting synced if there was a naming conflict.(AAP-41241)
- Fixed an issue where the login failed for users who were members of a team or organization that had a naming conflict.(AAP-41240)
- Fixed an issue where there would be **401 unauthorized** errors thrown at random in the platform gateway UI.(AAP-41165)
- Fixed an issue where services could not request `    cloud.redhat.com` settings from the platform gateway using `    ServiceTokenAuth` .(AAP-39649)


#### 10.7.5.3. Automation controller




- Fixed an issue where upgrading was preventing automation controller administrator password to be set for the platform gateway administrator account.(AAP-40839)
- Fixed an issue where the indirect host counting name recorded the hostname, instead of from the query result.(AAP-41033)
- Fixed an issue where the `    OpaClient` was not initializing properly after timeouts and retries.(AAP-40997)
- Fixed an issue where automation controller was missing the service account credentials for analytics.(AAP-40769)
- Fixed an issue where the ability to enable feature flags via the corresponding setting of the same name was not possible.(AAP-39783)
- Fixed an issue where the DAB feature flags endpoints were not registered in the automation controller API.(AAP-39778)
- Fixed an issue where the API was missing a helper method for fetching the service account token from `    sso.redhat.com` .(AAP-39637)


#### 10.7.5.4. Container-based Ansible Automation Platform




- Fixed an issue where the containerized installer was not creating receptor mesh connections between all automation controller nodes.(AAP-41102)
- Fixed an issue where a default installation of the containerized Ansible Automation Platform was unable to use container groups.(AAP-40431)
- Fixed an issue where errors would be hidden during Event-Driven Ansible status validation.(AAP-40021)
- Fixed an issue where the `    polkit` RPM package was not installed, therefore, not enabling user lingering.(AAP-39860)


#### 10.7.5.5. Event-Driven Ansible




- Fixed an issue where the `    EDA_ACTIVATION_DB_HOST` environment variable in the `    eda-initial-data` container was missing.(AAP-41270)
- Fixed an issue with the behavior of the `    ansible-rulebook` and Event-Driven Ansible controller to help when an activation that was started correctly was considered unresponsive and was scheduled for a restart.(AAP-41070)
- Fixed an issue where editing and copying of rulebook activations in the API were not allowed.(AAP-40254)
- Fixed an issue where the activation was incorrectly restarted with the error message **Missing container for running activation** .(AAP-39545)
- Fixed an issue where the Event-Driven Ansible server did not support `    PG Notify` using certificates.(AAP-39294)
- Fixed an issue where the user was not required to give a unique user defined name when copying a credential.(AAP-39079)
- Fixed an issue where the image URL in the collection `    decision_environment` testing was not OCI compliant.(AAP-39064)
- Fixed an issue where when creating a new team with the same name should have propagated `    IntegrityError` .(AAP-38941)
- Fixed an issue where decision environment URLs were not validated against OCI specification to ensure successful authentication to the container registry when pulling the image.(AAP-38822)
- Fixed an issue where the **Activation** module did not support the `    copy` operation from other activations.(AAP-37306)


#### 10.7.5.6. Receptor




- Fixed an issue where automation mesh receptor was creating too many `    inotify` processes, and where the user would encounter a **too many open files** error.(AAP-22605)


#### 10.7.5.7. RPM-based Ansible Automation Platform




- Fixed an issue where the activation instance logs were missing in RPM deployments.(AAP-40886)
- Fixed an issue where the managed CA would not correctly assign eligible groups during discovery, during installation, and backup and restore.(AAP-40277)
- Fixed an issue where during an installation or upgrade, SELinux relabeling was not occurring even if new `    fcontext` rules were added.(AAP-40489)
- Fixed an issue where the credentials for execution environments and decision environments hosted in automation hub were incorrectly configured.(AAP-40419)
- Fixed an issue where projects failed to sync due to incorrectly configured credentials for Ansible Automation Platform collections hosted in automation hub.(AAP-40418)


