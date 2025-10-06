# 10. Patch releases
## 10.20. Ansible Automation Platform patch release November 18, 2024
### 10.20.2. Bug fixes




#### 10.20.2.1. General




With this update, the following CVEs have been addressed:

[CVE-2024-9902](https://access.redhat.com/security/cve/cve-2024-9902) ansible-core: Ansible-core user may read/write unauthorized content.

[CVE-2024-8775](https://access.redhat.com/security/cve/cve-2024-8775) ansible-core: Exposure of sensitive information in Ansible vault files due to improper logging.

#### 10.20.2.2. Ansible Automation Platform




- Fixed an issue where the user was unable to filter out hosts on inventory groups where it returned a **Failed to load** options on Ansible Automation Platform UI.(AAP-34752)


#### 10.20.2.3. Execution Environment




- Update **pywinrm** to 0.4.3 in **ee-minimal** and **ee-supported** container images to fix Python 3.11 compatibility.(AAP-34077)


#### 10.20.2.4. Ansible Automation Platform Operator




- Fixed a syntax error when `    bundle_cacert_secret` was defined due to incorrect indentation.(AAP-35358)
- Fixed an issue where the default operator catalog for Ansible Automation Platform aligned to cluster-scoped versus namespace-scoped.(AAP-35313)
- Added the ability to set tolerations and `    node_selector` for the Redis **statefulset** and the gateway deployment.(AAP-33192)
- Ensure the platform URL status is set when **Ingress** is used to resolve an issue with Microsoft Azure on Cloud managed deployments. This is due to the Ansible Automation Platform operator failing to finish because it is looking for OpenShift Container Platform routes that are not available on Azure Kubernetes Service.(AAP-34036)
- Fixed an issue where the Ansible Automation Platform Operator description did not render code block correctly.(AAP-34589)
- It is necessary to specify the `    CONTROLLER_SSO_URL` and `    AUTOMATION_HUB_SSO_URL` settings in Gateway to fix the OIDC auth redirect flow.(AAP-34080)
- It is necessary to set the `    SERVICE_BACKED_SSO_AUTH_CODE_REDIRECT_URL` setting to fix the OIDC auth redirect flow.(AAP-34079)


#### 10.20.2.5. Container-based Ansible Automation Platform




- Fixed an issue when the port value was not defined in the `    gateway_main_url` variable, the containerized installer failed with incorrect execution environment image reference error.(AAP-34716)
- Fixed an issue where the containerized installer used port number when specifying the `    image_url` for a decision environment. The user should not add a port to image URLs when using the default value.(AAP-34070)


#### 10.20.2.6. RPM-based Ansible Automation Platform




- Fixed an issue where not setting up the **gpg** agent socket properly when multiple hub nodes are configured resulted in not creating a **gpg** socket file in `    /var/run/pulp` .(AAP-34067)


#### 10.20.2.7. Ansible development tools




- Fixed an issue where missing data files were not included in the molecule RPM package.(AAP-35758)


