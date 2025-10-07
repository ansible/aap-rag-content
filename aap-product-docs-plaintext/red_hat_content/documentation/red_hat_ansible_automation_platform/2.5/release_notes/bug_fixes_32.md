# 10. Patch releases
## 10.8. Ansible Automation Platform patch release May 7, 2025
### 10.8.5. Bug fixes




With this update, the following CVEs have been addressed:

[CVE-2025-26699](https://access.redhat.com/security/cve/cve-2025-26699)  `automation-controller` : Potential denial-of-service vulnerability in `django.utils.text.wrap()` .(AAP-41139)

#### 10.8.5.1. Ansible Automation Platform




- Fixed an issue where In AAP 2.5, the user needed to press Ctrl+Enter to start a new line.(AAP-43499)
- Fixed an issue where the change anchor tag on API html view violated semantic rules. (AAP-43802)
- LDAP Authenticator field `    USER_SEARCH` field now properly supports LDAP Unions. Previously you could only define one search term in the field like:


```
[
"ou=users,dc=example,dc=com",
"SCOPE_SUBTREE",
"uid=%(user)s"
]

[
"ou=users,dc=example,dc=com",
"SCOPE_SUBTREE",
"uid=%(user)s"
],
[
"ou=users,dc=example,dc=com",
"SCOPE_SUBTREE",
"uid=%(user)s"
]
]
```

-  `    USER_DN_TEMPLATE` will still take precedence over the `    USER_SEARCH` field. If non-unique users are found when performing multiple searches, those users will be unable to login to Ansible Automation Platform.(AAP-42883)
- Fixed an issue where there was a file not found error with Dynaconf.(AP-43144)
- Fixed an issue where dynaconf mishandled the openapi schema.(AAP-43143)
- Fixed an issue when editing an authenticator with a large number of Organization/Team mappings in platform-gateway would affect the loading time of the web page, potentially making the page unresponsive.(AAP-40963)
- Fixed an issue where unreachable hosts were not being filtered out of CCSP reports usage.(AAP-38735)
- Fixed an issue where the `    X-DAB-JW-TOKEN` header message would flood logs.(AAP-38169)
- Fixed an issue where after upgrading to Ansible Automation Platform 2.5 managed on Azure, the ability to see job output while the job was running was lost. (AAP-43894)
- Fixed an issue where customers were not allowed to view output details for filtered job outputs.(AAP-38925)
- Fixed an issue where unreachable hosts from CCSP usage reports were not excluded.(AAP-38735)
- Fixed an issue where indirect hosts were being counted in the first tab as quantity.(AAP-44676)
- Fixed an issue where the platform-gateway could not be installed with a different name for the admin user.(AAP-44180)
- Fixed an issue where an Ansible Automation Platform UI session was being logged out even if the user is actively working.(AAP-43622)
- Fixed an issue where exceptions handled on SSO login were not allowing for error messages to be properly captured.(AAP-43369)
- Fixed an issue where the job output was slow and making it hard to read due to missing parts of the output.(AAP-41434)
- Fixed an issue where the user was unable to edit an existing rulebook activation.(AAP-37299)


#### 10.8.5.2. Ansible Automation Platform Operator




- Fixed an issue where the pod affinity/anti-affinity was not configurable for the aap-gateway-operator to allow for pod placement on unique nodes.(AAP-42983)
- Fixed an issue where Red Hat Ansible Lightspeed was incorrectly passing DAB settings.(AAP-43542)
- Fixed an issue where the Lightspeed Operator WCA configuration was not optional.(AAP-42370)
- Fixed an issue where `    status.conditions` validation would not allow auto-reporting errors on CR statuses.(AAP-44081)
- Fixed an issue where the Ansible Automation Platform gateway had the incorrect Lightspeed deployment name.(AAP-43837)
- Fixed an issue where Lightspeed devel CRD was incompatible with 2.5 CRD.(AAP-43657)
- Fixed an issue where `    status.conditions` validation was not allowing auto-reporting errors on the CR statuses.(AAP-44083)
- If the user is migrating between OpenShift Container Platform Operator on AAP 2.5 fails because of a postgres permission issue. The automation controller operator now grants permission to the automation controller user to avoid permissions errors when migrating the data.(AAP-44846)
- Fixed an issue where there was an Intermittent **502 Bad Gateway** error on Ansible Automation Platform 2.5 operator deployment.(AAP-44176)


#### 10.8.5.3. Automation controller




- Fixed usage of Django password validator `    UserAttributeSimilarityValidator` .(AAP-43046)
- Fixed an issue where there was no lookup credential without user Inputs, and where the credential defaults were not passing between awx-plugins and AWX.(AAP-38589)
- Fixed an issue where there was an incorrect deprecation warning for `    awx.awx.schedule_rrule` .(AAP-43474)
- Fixed an issue where facts were unintentionally deleted when an inventory is modified during a job execution.(AAP-39365)


#### 10.8.5.4. Container based Ansible Automation Platform




- Fixed an issue where the paths to expose isolated jobs' settings did not work.(AAP-37599)


The ansible.gateway_configuration collection was replaced by ansible.platform.(AAP-44230)

- Fixed an issue where the automation hub would fail to upload collections due to a missing worker temporary directory.(AAP-44166)


#### 10.8.5.5. Event-Driven Ansible




- Fixed an issue where the log messages were not using the correct log level.(AAP-43607)
- Fixed an issue where the **ansible-rulebook** logs were not logged into the activation-worker log.(AAP-43549)
- Fixed an issue where the container was not always deleted correctly, or it missed the last output entries in VM based installations.(AAP-42935)
- Fixed an issue where Event-Driven Ansible logging did not allow searching.(AAP-43338)
- Fixed an issue where the rulebook activations and event streams would not remain due to a cascading delete after the user who created them was deleted.(AAP-41769)
- Fixed an issue where the decision environment was not using the image to authenticate and pull successfully when using an image registry with a custom port.(AAP-41281)
- Fixed an issue where timestamps were not formatted to the local timezone of the user.(AAP-38396)
- Fixed an issue where the activation failed with the message **It will attempt to restart (1/5) in 60 seconds according to the restart policy always** , but it does not restart.(AAP-43969)
- Fixed an issue where a race condition would occur while cleaning up activation in OpenShift Container Platform, causing unexpected behavior.(AAP-44108)
- Fixed an issue where the Event-Driven Ansible logs showed no information about an internal server error.(AAP-42271)
- Fixed an issue where there was a duplicate error message in the CLI.(AAP-41745)
- Fixed an issue where Envoy was stripping the `    Authorization` header from client requests.(AAP-44700)
- Fixed an issue where Event-Driven Ansible had not selected a standard component for settings mechanism.(AAP-41684)
- Fixed an issue where documentation was missing for Event-Driven Ansible source plugins.(AAP-8630)
- Fixed an issue where there was a memory leak in Event-Driven Ansible using the **ansible-rulebook**  `    sqs` plugin.(AAP-42623)
- Fixed an issue where rulebook activations were not editable or copyable either through the UI or API.(AAP-37294)
- Fixed an issue where the rule engine used in **ansible-rulebook** was keeping events that do not match in memory for the `    default_events_ttl` of two hours causing a memory leak.(AAP-44899)
- Fixed an issue where there was a memory leak in Event-Driven Ansible using **ansible-rulebook**  `    sqs` plugin.(AAP-44899)
- Fixed an issue where the rulebook activation module in the Event-Driven Ansible collection lacked support for restarting the activation.(AAP-42542)
- Fixed an issue where AAP aliases were unable to be used to specify Event-Driven Ansible collection variables.(AAP-42280)


#### 10.8.5.6. Red Hat Ansible Lightspeed Operator




- Fixed an issue where the `    auth_config_secret_name` configuration in Lightspeed Operator was not optional in the automation controller.(AAP-44203)


#### 10.8.5.7. Receptor




- Fixed an issue where the kube API would lock up on every call by moving `    kubeAPIWapperInstance` inside each `    kubeUnit` and removing `    kubeAPIWapperlocks` .(AAP-43111)


#### 10.8.5.8. RPM-based Ansible Automation Platform




- Fixed an issue where platform gateway services were not aligned after restore with the target environment.


- Fixed an issue where old instance nodes were still registered in automation controller post restore.
- Fixed an issue where **nginx** would attempt to reload before the configuration was finalized.(AAP-44231)



