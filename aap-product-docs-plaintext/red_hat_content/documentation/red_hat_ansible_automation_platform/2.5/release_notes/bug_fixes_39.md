# 10. Patch releases
## 10.9. Ansible Automation Platform patch release May 28, 2025
### 10.9.4. Bug fixes




With this update, the following CVEs have been addressed:

-  [CVE-2025-43859](https://access.redhat.com/security/cve/CVE-2025-43859)  `    ee-supported-container` : h11 accepts some malformed Chunked-Encoding bodies.(AAP-44783)
-  [CVE-2025-43859](https://access.redhat.com/security/cve/CVE-2025-43859)  `    ee-cloud-services-container` : h11 accepts some malformed Chunked-Encoding bodies.(AAP-44781)
-  [CVE-2025-43859](https://access.redhat.com/security/cve/CVE-2025-43859)  `    ansible-lightspeed-container` : h11 accepts some malformed Chunked-Encoding bodies.(AAP-44779)


#### 10.9.4.1. Ansible Automation Platform




- Fixed an issue found in SaaS deployments where the authentication proxy would use old, invalid database connections after an RDS database reboot.(AAP-44178)
- Fixed an issue where administrators were not allowed to configure auto migration of legacy authenticators.(AAP-36841)
- Fixed an issue where the usernames from LDAP were not case-insensitive. LDAP is case-insensitive so logging in as <Bob> and <bob> would result in two different users in platform gateway even though they are the same user in LDAP. With this change, both users will be authenticated as the lowercase username.(AAP-44177)


#### 10.9.4.2. Ansible Automation Platform Operator




- Fixed a broken document link to Ansible Automation Platform Operator installation documents in the OpenShift Container Platform UI.(AAP-45199)
- Fixed an issue where the user was unable configure `    kind: AnsibleInstanceGroup` , and it failed with an error **policy_spec_override is undefined** .(AAP-45351)


#### 10.9.4.3. Red Hat Ansible Lightspeed




- Fixed an issue where it was not possible to disable SSL verification between Model Server and Red Hat Ansible Lightspeed.(AAP-45269)
- Fixed an issue where the provider type and context window size were not configurable in Red Hat Ansible Lightspeed Operator.(AAP-45166)


#### 10.9.4.4. Automation controller




- Fixed an issue where the VMware credential was not applying to the source correctly.(AAP-45169)
- Fixed an issue where the workflow job template did not have job access parity with `    UnifiedJobAccess` .(AAP-45057)
- Fixed an issue where error handling did not allow event processing to continue even if one event contained invalid data that cannot be parsed by `    jq` .(AAP-44876)


#### 10.9.4.5. Platform gateway




- Fixed `    AttributeError` errors around the `    legacy_base` authenticator which were harmless, but were showing in logs leading to customer and engineer confusion.(AAP-40159)
- Fixed an issue where customized proxy authentication on a per service cluster basis was not allowed.(AAP-35601)
- Fixed and issue where there was a server error on migrating an LDAP user in a freshly upgraded 2.4 → 2.5 instance. The fix prevents the 500 error during LDAP user legacy authentication and migration following an upgrade.(AAP-44958)


#### 10.9.4.6. RPM-based Ansible Automation Platform




- Fixed an issue the `    max keyrings sysctl` would produce common failures when running more than 200 containers on a node.(AAP-45260)
- Fixed an issue where automation platform gateway proxy (envoy) ports were not included in the firewall.(AAP-45489)


