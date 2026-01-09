# 10. Patch releases
## 10.21. Ansible Automation Platform patch release December 3, 2024
### 10.21.1. Enhancements




#### 10.21.1.1. Ansible Automation Platform




- Red Hat Ansible Lightspeed has been updated to 2.5.241127.(AAP-35307)
-  `    redhat.insights` Ansible collection has been updated to 1.3.0.(AAP-35161)
-  `    ansible.eda` collection has been updated to 2.2.0 in execution environment and decision environment images.(AAP-3398)


#### 10.21.1.2. Ansible Automation Platform Operator




- With this update, you can set PostgreSQL SSL/TLS mode to `    verify-full` or `    verify-ca` with the proper `    sslrootcert` configuration in the automation hub Operator.(AAP-35368)


#### 10.21.1.3. Container-based Ansible Automation Platform




- With this update, `    ID` and `    Image` fields from a container image are used instead of `    Digest` and `    ImageDigest` to trigger a container update.(AAP-36575)
- With this update, you can now update the registry URL value in Event-Driven Ansible credentials.(AAP-35085)
- With this update, the `    kernel.keys.maxkeys` and `    kernel.keys.maxbytes` settings are increased on systems with large memory configuration.(AAP-34019)
- Added `    ansible_connection=local` to the `    inventory-growth file` and clarified its usage.(AAP-34016)


#### 10.21.1.4. Documentation updates




- With this update, the Container growth topology and Container enterprise topology have been updated to include s390x (IBM Z) architecture test support.(AAP-35969)


#### 10.21.1.5. RPM-based Ansible Automation Platform




- With this update, you can now update the registry URL value in Event-Driven Ansible credentials.(AAP-35162)


