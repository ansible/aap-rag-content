# 10. Patch releases
## 10.4. Ansible Automation Platform patch release June 9, 2025
### 10.4.2. Ansible Automation Platform




#### 10.4.2.1. Features




- Adds `    ansible_base.lib.utils.address.classify_address` providing common recognition and parsing of machine addressing hostname, IPv4 and IPv6 with and without an appended `    :&lt;port&gt;` .(AAP-45910)


#### 10.4.2.2. Enhancements




- LDAP filter validation improved such that all filters that meet LDAP standards including and/or should be properly validated.(AAP-46249)
- Completely updated interface for managing authentication methods and mappings.(AAP-45750)
- Default validity period for **Oauth** tokens reduced from 1000 years to 1 year. Existing tokens will NOT be updated. If you wish to reduce the validity period of existing tokens, please remove and re-issue them. The default validity period for **Oauth** tokens can be modified via the django setting `    ACCESS_TOKEN_EXPIRE_SECONDS in OAUTH2_PROVIDER` .(AAP-46187)


#### 10.4.2.3. Bug fixes




- Fixed an issue where there was a degraded logging performance notice removed on the job output page. Polling fallback functionality still exists.(AAP-46120)
- Fixed an issue where the gateway proxy was not properly ejecting nodes failing health checks.(AAP-43931)
- Fixed an issue where installations with Red Hat Ansible Lightspeed enabled were not handled properly during upgrade.(AAP-46154)


