# Ansible Automation Platform 2.7 patch release August 24, 2026 (2.7-6)
## Aap Gateway

- Fixed an issue where organization members can now discover and view teams within their organization when assigning permissions. (AAP-84972)
- Fixed an issue where envoy health check intervals and timeouts aligned to prevent timeouts and false node ejection under heavy load. (AAP-85105)
- Fixed an issue where an organization with a large number of role assignments would timeout. (AAP-85660)
- Fixed an issue where updated dependency libraries for jwcrypto to address CVE-2026-39373. (AAP-86141)

