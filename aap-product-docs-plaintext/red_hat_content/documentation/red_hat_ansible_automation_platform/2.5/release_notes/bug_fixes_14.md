# 10. Patch releases
## 10.10. Ansible Automation Platform patch release February 13, 2025
### 10.10.3. Bug fixes




#### 10.10.3.1. Migration




- Fixed an issue where after upgrading Ansible Automation Platform from 2.4 to 2.5, many of the surveys that had multiple choice options displayed a blank space in the drop down menu.(AAP-35093)


#### 10.10.3.2. Ansible Automation Platform




- Fixed a bug in the collections token module where it was unable to find an application if multiple organizations had the same application name.(AAP-38625)
- Fixed an issue where upgrading Ansible Automation Platform 2.5 caused an occasional internal server error for all users with Event-Driven Ansible and Automation hub post upgrade.(AAP-39293)
- Fixed an issue where the administrator was not allowed to configure auto migration of legacy authenticators.(AAP-39949)
- Fixed an issue where there were two launch/relaunch icons displayed from the jobs list for failed jobs.(AAP-38483)
- Fixed an issue where the **Schedules Add** wizard returned a `    RequestError`  **Not Found** .(AAP-37909)
- Fixed an issue where the **EC2 Inventory Source** type required credentials, which is not necessary when using IAM instance profiles.(AAP-37346)
- Fixed an issue when attempting to assign the **Automation Decisions - Organization Admin** role to a user in an organization resulted in the error, **Not managed locally, use the resource server instead** . Administrators can now be added by using the **Organization → Administrators** tab.(AAP-37106)
- Fixed an issue where when updating a workflow node, the Job Tags were lost and Skip Tags were not saved.(AAP-35956)
- Fixed an issue where new users who logged in with legacy authentication were not merged when switching to Gateway authentication.(AAP-40120)
- Fixed an issue where the user was unable to link legacy SSO accounts to Gateway.(AAP-40050)
- Fixed an issue where updating Ansible Automation Platform to 2.5 caused an Internal Service Error for all users with Event-Driven Ansible and Automation hub post upgrade. The migration process will now detect and fix users who were created in services via JWT auth and improperly linked to the service instead of the platform gateway.(AAP-39914)


#### 10.10.3.3. Ansible Automation Platform Operator




- Fixed an issue where `    AnsibleWorkflow` custom resources would not parse and utilize `    extra_vars` if specified.(AAP-39005)


#### 10.10.3.4. Automation controller




- Fixed an issue where when an Azure credential was created using `    awxkit` , the creation failed because the parameter `    client_id` was added to the input fields while the API was not expecting it.(AAP-39846)
- Fixed an issue where the job schedules were running at incorrect times when that schedule’s start time fell within a Daylight Saving Time period.(AAP-39826)


#### 10.10.3.5. Automation hub




- Fixed an issue where the use of empty usernames and passwords when creating a remote registry was not allowed.(AAP-26462)


#### 10.10.3.6. Container-based Ansible Automation Platform




- Fixed an issue where the containerized installer had no preflight check for the Postgres version of an external database.(AAP-39727)
- Fixed an issue where the containerized installer could not register other peers in the database.(AAP-39470)
- Fixed an issue where there was a missing installation user UID check.(AAP-39393)
- Fixed an issue where Postgresql connection errors would be hidden during its configuration.(AAP-39389)
- Fixed an issue in the preflight check regression when the TLS private key provided is not an RSA type.(AAP-39816)


#### 10.10.3.7. Event-Driven Ansible




- Fixed an issue where theGenerate extra varsbutton did not handle file/env injected credentials.(AAP-36003)


#### 10.10.3.8. Known Issues




- In the platform gateway, the tooltip for **Projects → Create Project - Project Base Path** is undefined.(AAP-27631)
- Deploying the platform gateway on FIPS enabled RHEL 9 is currently not supported.(AAP-39146)


