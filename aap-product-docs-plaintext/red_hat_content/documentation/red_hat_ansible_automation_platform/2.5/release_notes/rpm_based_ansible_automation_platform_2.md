# 10. Patch releases
## 10.2. Ansible Automation Platform patch release August 27, 2025
### 10.2.9. RPM-based Ansible Automation Platform




#### 10.2.9.1. Enhancements




- Added `    postgres_extra_settings` for `    postgresql.conf` customization for managed database installations.(AAP-51462)


#### 10.2.9.2. Bug Fixes




- Fixed an issue where automation controller nodes set to a deprovision state were not removed from the platform gateway registry.(AAP-51461)
- Fixed an issue where the missing RPM dependency for **PostgreSQL** client which resulted in container images missing `    psql` binary.(AAP-50941)
- Fixed an issue where disabling `    https` for platform gateway and/or platform gateway proxy ( **envoy** ) caused installation failures.(AAP-48606)


