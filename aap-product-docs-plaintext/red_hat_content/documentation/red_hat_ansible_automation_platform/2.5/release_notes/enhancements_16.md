# 10. Patch releases
## 10.8. Ansible Automation Platform patch release March 12, 2025
### 10.8.3. Enhancements




#### 10.8.3.1. Event-Driven Ansible




- Event-Driven Ansible activation logging is now provided via the `    journald` driver.(AAP-39745)
- Rulebook activations' log message field is now separated into timestamps and message fields.(AAP-39743)
- Moved `    ansible.eda` collection from de-supported to de-minimal as elements of the collection are required for all Event-Driven Ansible images.(AAP-39749)


#### 10.8.3.2. RPM-based Ansible Automation Platform




- The `    setup.sh` script now has an option to collect `    sosreport` .(AAP-40085)


