# 10. Patch releases
## 10.2. Ansible Automation Platform patch release August 27, 2025
### 10.2.5. Bug fixes




- Fixed an issue in the **PostgreSQL** password encryption when upgrading from PG13 to PG15 on FIPS.(AAP-50443)
- Fixed an issue where requests time out at client or proxy, but work continues long past the timeout.(AAP-50311)
- Fixed an issue to align **NGINX** and web server timeouts to avoid issues where requests time out but work continues on already timed out requests.(AAP-50310)
- Fixed an issue to align **envoy** , **NGINX** , web server, and `    jwt` token timeouts to avoid issues where requests time out but work continues or tokens expire before they are used.(AAP-50309)
- Fixed an issue to align web server timeouts to avoid issues where requests time out at client or proxy, but work continues long past the timeout.(AAP-50308)
- Fixed backup and restores for deployments with external databases and refactored the tasks for managed database restores to be a separate code path.(AAP-50299)
- Fixed an issue where the platform gateway operator `    client_request_timeout` was not the same as `    haproxy` timeout in OpenShift Container Platform.(AAP-51749)


