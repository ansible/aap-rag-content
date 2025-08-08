# 10. Patch releases
## 10.15. Ansible Automation Platform patch release December 18, 2024
### 10.15.2. Bug fixes




#### 10.15.2.1. General




- Fixed an issue where `    django-ansible-base` fallback cache kept creating a **tmp** file even if the **LOCATION** was set to another path.(AAP-36869)
- Fixed an issue where the OIDC authenticator was not allowed to use the JSON key to extract user groups, or for a user to be modified via the new `    GROUPS_CLAIM` configuration setting.(AAP-36716)


With this update, the following CVEs have been addressed:

-  [CVE-2024-11079](https://access.redhat.com/security/cve/cve-2024-11079)  `    ansible-core` : Unsafe Tagging Bypass via `    hostvars` Object in Ansible-Core.(AAP-35563)
-  [CVE-2024-53908](https://access.redhat.com/security/cve/cve-2024-53908)  `    ansible-lightspeed-container` : Potential SQL injection in `    HasKey(lhs, rhs)` on Oracle.(AAP-36767)
-  [CVE-2024-53907](https://access.redhat.com/security/cve/cve-2024-53907)  `    ansible-lightspeed-container` : Potential denial-of-service in `    django.utils.html.strip_tags()` .(AAP-36755)
-  [CVE-2024-11483](https://access.redhat.com/security/cve/cve-2024-11483) which allowed users to escape the scope of their personal access **OAuth2** tokens, from read-scoped to read-write-scoped, in the gateway.(AAP-36261)


#### 10.15.2.2. Red Hat Ansible Automation Platform




- Fixed an issue where when role user assignments were queried in the platform UI, the query is successful about 75% of the time.(AAP-36872)
- Fixed an issue where the user was unable to filter job templates by **label** in Ansible Automation Platform 2.5.(AAP-36540)
- Fixed an issue where it was not possible to open a job template after removing the user that created the template.(AAP-35820)
- Fixed an issue where the inventory source update failed, and did not allow selection of the inventory file.(AAP-35246)
- Fixed an issue where the **Login Redirect Override** setting was missing and not functioning as expected in Ansible Automation Platform 2.5.(AAP-33295)
- Fixed an issue where users were able to select a credential that required a password when defining a schedule.(AAP-32821)
- Fixed an issue where the job output did not show unless you switched tabs. This also fixed other display issues.(AAP-31125)
- Fixed an issue where adding a new Automation Decision role to a team did not work from theAccess Management→Teamsnavigation path.(AAP-31873)
- Fixed an issue where migration was missing from Ansible Automation Platform.(AAP-37015)
- Fixed an issue where the gateway **OAuth** token was not encrypted at rest.(AAP-36715)
- Fixed an issue where the API forces the user to save a service with an API port even if one does not exist.(AAP-36714)
- Fixed an issue where the Gateway did not properly interpret SAML attributes for mappings.(AAP-36713)
- Fixed an issue where non-self-signed **certificate+key** pairs were allowed to be used in SAML authenticator configurations.(AAP-36707)
- Fixed an issue where the login page was not redirecting to `    /api/gateway/v1` if a user was already logged in.(AAP-36638)


#### 10.15.2.3. Ansible automation hub




- When configuring an **Ansible Remote** to sync collections from other servers, a requirements file is only required for syncs from Galaxy, and optional otherwise. Without a requirements file, all collections are synced.(AAP-31238)


##### 10.15.2.3.1. Container-based Ansible Automation Platform




- Fixed an issue that allowed automation controller nodes to override the `    receptor_peers` variable. (AAP-37085)
- Fixed an issue where the containerized installer ignored `    receptor_type` for automation controller hosts and always installed them as hybrid.(AAP-37012)
- Fixed an issue where Podman was not present in the task container, and the cleanup image task failed.(AAP-37011)
- Fixed an issue where only one automation controller node was configured with Execution/Hop node peers rather than all automation controller nodes.(AAP-36851)
- Fixed an issue where the automation controller services lost connection to the database, where the containers are stopped and the `    systemd` unit does not try to restart.(AAP-36850)
- Fixed an issue where receptor_type and `    receptor_protocol` variables validation checks were skipped during the preflight role execution.(AAP-36857)


#### 10.15.2.4. Event-Driven Ansible




- Fixed an issue where the url field of the event stream was not updated if `    EDA_EVENT_STREAM_BASE_URL` setting changed. (AAP-33819)
- Fixed an issue where Event-Driven Ansible and automation controller fields were pre-populated with gateway credentials when `    secret: true` is set on custom credentials.(AAP-33188)
- Fixed an issue where the bulk removal of selected role permissions disappeared when more than 4 permissions were selected.(AAP-28030)
- Fixed an issue where **Enabled options** had its own scrollbar on the **Rulebook Activation Details** page.(AAP-31130)
- Fixed an issue where the status of an activation was occasionally inconsistent with the status of the latest instance after a restart.(AAP-29755)
- Fixed an issue where importing a project from a non-existing branch resulted in the completed state instead of a Failed status.(AAP-29144)
- Fixed an issue with respect to the custom credential types where if the user clicked **The generate extra vars** before the `    fields: key` in the input configuration it would create an empty line that is uneditable.(AAP-28084)
- Fixed an issue where the project sync would not fail on an empty or unstructured git repository.(AAP-35777)
- Fixed an issue where rulebook validation import/sync fails when a rulebook has a duplicated rule name.(AAP-35164)
- Fixed an issue where the Event Driven Ansible API allowed a credential’s type to be changed.(AAP-34968)
- Fixed an issue where a previously failed project could be accidentally changed to **completed** after a resync.(AAP-34744)
- Fixed an issue where no message was recorded when a project did not contain any rulebooks.(AAP-34555)
- Fixed an issue where the name for credentials in the rulebook activation form field was not updated.(AAP-34123)
- Updated the message for the rulebook activation/event streams for better clarity.(AAP-33485)
- Fixed an issue where the source plugin was not able to use the `    env vars` to establish a successful connection to the remote source.(AAP-35597)
- Fixed an issue in the collection where the activation module failed with a misleading error message if the rulebook, project, decision environment, or organization, could not be found.(AAP-35360)
- Fixed an issue where the validation a host specified as part of a container registry credential did not conform to container registry standards. The specified host was previously able to use a non-syntactically valid host (name or net address) and optional port value `    (&lt;valid-host&gt;[:&lt;port&gt;])` . The validation is now applied when creating a credential as well as when modifying an existing credential regardless of fields being modified.(AAP-34969)
- Fixed an issue whereby multiple Red Hat Ansible Automation Platform credentials were being attached to activations.(AAP-34025)
- Fixed an issue where there was an erroneous dependency on the existence of an organization named **Default** .(AAP-33551)
- Fixed an issue where occasionally an activation is reported as running, before it is ready to receive events.(AAP-31225)
- Fixed an issue where the user could not edit auto-generated **injector vars** while creating Event-Driven Ansible custom credentials.(AAP-29752)
- Fixed an issue where in some cases the `    file_watch` source plugin in an Event-Driven Ansible collection raised the **QueueFull** exception.(AAP-29139)
- Fixed an issue where the Event-Driven Ansible database increased in size continuously, even if the database was unused. Addend the purge_record script to clean up outdated database records.(AAP-30684)


