# 10. Patch releases
## 10.17. Ansible Automation Platform patch release October 28, 2024
### 10.17.1. Enhancements




#### 10.17.1.1. Ansible Automation Platform




- With this update, upgrades from Ansible Automation Platform 2.4 to 2.5 are supported for RPM and Operator-based deployments. For more information on how to upgrade, see [RPM upgrade and migration](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_upgrade_and_migration) . (ANSTRAT-809)


- Upgrades from 2.4 Containerized Ansible Automation Platform Tech Preview to 2.5 Containerized Ansible Automation Platform are unsupported.
- Upgrades for Event-Driven Ansible are unsupported from Ansible Automation Platform 2.4 to Ansible Automation Platform 2.5.



#### 10.17.1.2. Ansible Automation Platform Operator




- An informative redirect page is now shown when you go to the automation hub URL root. (AAP-30915)


#### 10.17.1.3. Container-based Ansible Automation Platform




- The TLS Certificate Authority private key can now use a passphrase. (AAP-33594)
- Automation hub is populated with container images (decision and execution environments) and Ansible collections. (AAP-33759)
- The automation controller, Event-Driven Ansible, and automation hub legacy UIs now display a redirect page to the Platform UI rather than a blank page. (AAP-33794)


#### 10.17.1.4. RPM-based Ansible Automation Platform




- Added platform Redis to RPM-based Ansible Automation Platform. This allows a 6 node cluster for a Redis high availability (HA) deployment. Removed the variable `    aap_caching_mtls` and replaced it with `    redis_disable_tls` and `    redis_disable_mtls` which are boolean flags that disable Redis server TLS and Redis client certificate authentication. (AAP-33773)
- An informative redirect page is now shown when going to automation controller, Event-Driven Ansible, or automation hub URL. (AAP-33827)


