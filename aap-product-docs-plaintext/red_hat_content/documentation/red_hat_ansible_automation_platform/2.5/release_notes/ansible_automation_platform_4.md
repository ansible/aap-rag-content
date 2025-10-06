# 10. Patch releases
## 10.2. Ansible Automation Platform patch release August 27, 2025
### 10.2.3. Ansible Automation Platform




#### 10.2.3.1. Features




- Added a new field on **Azure AD** authenticator called `    Field to use as username` which allows you to use an arbitrary field from the assertion as the username in Ansible Automation Platform.(AAP-49481)


#### 10.2.3.2. Enhancements




- Enhanced Support for Streaming Chat Responses in Ansible Automation Platform. New settings added:


-  `        stream_idle_timeout` : Controls timeout for idle streaming connections.
-  `        max_stream_duration` : Sets maximum duration for streaming connections.
(AAP-51756)

- Allow for HTTP headers to be passed through **envoy** when https is offloaded by another device in front of **envoy** . This introduces two new settings:


-  `        SECURE_PROXY_SSL_HEADER` indicating which headers should be allowed through. The defaults are `        HTTP_X_FORWARDED_PROTO` , `        https` .
-  `        XDS_XFF_NUM_TRUSTED_HOPS` which says how many entries in the headers should be trusted. The default is 0 if there is only one device in front of **envoy** . Set to 1 if there are more, or increase as needed. These settings can only be changed in the `        /etc/ansible-automation-platform/gateway/settings.py` file.
(AAP-51347)



#### 10.2.3.3. Bug fixes




- Fixed an issue where the **OpenAPI** spec did not reflect all query parameters available.(AAP-49824)
- Fixed an issue where the `    LOGIN_REDIRECT_OVERRIDE` was not being respected.(AAP-49726)
- Fixed an issue where the breadcrumb in a launch template sent users to the wrong URL.(AAP-44194)
- Fixed an issue where legacy users were not properly migrated to platform gateway in some scenarios that were previously leaving the users in a partly migrated state.(AAP-43251)
- Fixed an issue where the LDAP filter splitter/validator did not handle some valid filters.(AAP-51591)
- Fixed an issue that removes the `    required` label from the organization field for galaxy credentials in automation controller credential create and edit forms.(AAP-51587)
- Fixed an issue where subscription entitlement window displayed again after Ansible Automation Platform had been entitled when running in a load-balanced environment with multiple controller web pods.(AAP-43883)
- Fixed an issue that did not allow all users to see the notifiers tab.(AAP-41342)
- Fixed an issue where there was no limit field on the job details page.(AAP-36118)


