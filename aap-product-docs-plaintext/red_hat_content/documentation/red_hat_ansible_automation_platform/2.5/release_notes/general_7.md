# 10. Patch releases
## 10.8. Ansible Automation Platform patch release March 12, 2025
### 10.8.1. General




- The `    ansible.controller` collection has been updated to 4.6.9.(AAP-41400)
-  `    ansible-lint` has been updated to 25.1.2.(AAP-38116)
- Fixed an issue where the bundle installer/ee-supported did not contain the latest collection versions. The following collections have been updated in the ee-supported and the bundle installer:


- amazon.aws 9.2.0
- ansible.windows 2.7.0
- arista.eos 10.0.1
- cisco.ios 9.1.1
- cisco.iosxr 10.3.0
- cisco.nxos 9.3.0
- cloud.common 4.0.0
- cloud.terraform 3.0.0
- kubernetes.core 5.1.0
- microsoft.ad 1.8.0
- redhat.openshift 4.0.1
- vmware.vmware 1.10.1
- vmware.vmware_rest 4.6.0.(AAP-39960)

- Fixed an issue where `    ansible-rulebook` did not support by default third party python libraries.(AAP-41341)


