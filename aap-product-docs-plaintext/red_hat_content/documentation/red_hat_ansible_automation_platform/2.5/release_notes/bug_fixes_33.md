# 10. Patch releases
## 10.9. Ansible Automation Platform patch release April 9, 2025
### 10.9.3. Bug fixes




With this update, the following CVEs have been addressed:

-  [CVE-2025-2877](https://access.redhat.com/security/cve/CVE-2025-2877)  `    ansible-rulebook` : exposure of inventory passwords in plain text when starting a rulebook activation with verbosity set to debug in Event-Driven Ansible.(AAP-42817)


#### 10.9.3.1. Ansible Automation Platform




- Fixed an issue where job workflow templates failed with limits.(AAP-33726)
- Fixed an issue where there was non-viable information disclosure for pen testing.(AAP-39977)


#### 10.9.3.2. Ansible Automation Platform Operator




- Fixed an issue on the OpenShift Container Platform Route TLS termination that was always configured with the edge value.(AAP-42051)


#### 10.9.3.3. Container based Ansible Automation Platform




- Fixed an issue where the restore to a new node would fail. Implemented validation and cleanup for service nodes on a restore to a new cluster.(AAP-42781)
- Fixed an issue where podman logs did not show any log messages if the user was not part of the local **administrator** or `    systemd-journal` group.(AAP-42755)
- Fixed an issue where the containerized installer was unable to apply extra settings for automation controller, Event-Driven Ansible, platform gateway, and automation hub.(AAP-40798)
- Fixed an issue where a remote user was not part of the `    systemd-journal` group and could not access container logs.(AAP-42755)


#### 10.9.3.4. Automation execution environments




- Fixed an issue where there was a Python 3.11 incompatibility by updating `    pykerberos` to 1.2.4 in `    ee-minimal` and `    ee-supported` container images.(AAP-42428)


#### 10.9.3.5. Event-Driven Ansible




- Fixed an issue where activations attached with some event streams could not be created in deployments configured with **Postgresql** with **mTLS** .(AAP-42268)


#### 10.9.3.6. RPM-based Ansible Automation Platform




- Fixed an issue where the token refresh prevented Event-Driven Ansible worker nodes from re-authenticating tokens.(AAP-42981)
- Fixed an issue where the bundle installer failed to update automation controller and `    aap-metrics-utility` in the same run.(AAP-42632)
- Fixed an issue where platform UI was not loading when the platform gateway was on a **FIPS** enabled Red Hat Enterprise Linux 9.(AAP-39146)


