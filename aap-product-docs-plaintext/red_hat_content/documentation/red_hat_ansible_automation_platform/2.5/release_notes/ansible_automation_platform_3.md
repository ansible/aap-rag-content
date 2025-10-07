# 10. Patch releases
## 10.1. Ansible Automation Platform patch release September 23, 2025
### 10.1.3. Ansible Automation Platform




#### 10.1.3.1. Enhancements




-  `    X-Forwarded-For` and `    Real-Ip` headers are now included in the NGINX logs. (AAP-52562)


#### 10.1.3.2. Bug fixes




- Fixed an issue where if the gRPC server could not connect to the database it would return a 403 HTTP status to envoy. This has been changed to return an error message of 503. (AAP-51931)
- Fixed an issue with the help text for the setting `    ALLOW_OAUTH2_FOR_EXTERNAL_USERS` . (AAP-51886)
- Fixed an incorrectly formatted error message in the SAML authenticator when passing invalid security settings. The error will now properly show the invalid fields and will also indicate what valid field values are. (AAP-51705)
- Fixed an issue where authentication mapping for teams did not work if `    join_condition: and` was used with attributes. (AAP-51639)
- Fixed an issue with authenticator maps not properly evaluating the attribute in conditions. (AAP-51638)
- Fixed an issue where platform gateway did not generate the necessary metadata for the UI to render **Settings > Platform Gateway** when the accessing user is an auditor rather than an administrator. (AAP-53279)
- Fixed an issue where multi-select dialogs only showed a subset of users, and users were unable to scroll or advance to the next page. (AAP-52209)
- Fixed an issue where the SAML based authenticators did not collect the group data even if the field had the attribute specified. (AAP-51503)
- The **View Logs** link now matches the automation controller API being used. (AAP-52674)
- PostgreSQL directory creation now works when TLS is disabled. (AAP-52569)
- Fixed a path issue for `    custom_ca_cert` when checking PostgreSQL connection and version during preflight. (AAP-53213)
- Fixed the restore and implemented migration functionality for the automation controller resource secret key value. (AAP-53535)
- Improved platform gateway control plane authorization performance to reduce sporadic request errors. (AAP-53468)
- Disabled IPv6 binding on PostgreSQL and Redis services when IPv6 is disabled on the host. (AAP-53546)


