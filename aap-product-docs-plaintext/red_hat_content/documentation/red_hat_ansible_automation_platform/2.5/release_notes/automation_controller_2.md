# 10. Patch releases
## 10.2. Ansible Automation Platform patch release August 27, 2025
### 10.2.6. Automation controller




#### 10.2.6.1. Bug Fixes




- Fixed regression in `    ansible.controller` collection where the argument `    controller_oauthtoken` was wrongfully removed.


- Fixed newly added `        aap_token` to function the same as `        controller_oauthtoken` .
- Fixed the `        ansible.controller.controller_api` lookup plugin.
(AAP-51289)

- Fixed an issue where the Ansible Galaxy credentials could not be created and edited without specifying an organization.(AAP-51614)
- Fixed an issue where the subscription is attached before subscription credentials have been set, returned a **400 Bad Request** .(AAP-50322)


