# 2. System requirements
## 2.6. PostgreSQL requirements




Red Hat Ansible Automation Platform 2.5 uses PostgreSQL 15 and requires the external (customer supported) databases to have ICU support. PostgreSQL user passwords are hashed with SCRAM-SHA-256 secure hashing algorithm before storing in the database.

To determine if your automation controller instance has access to the database, you can do so with the command, `awx-manage check_db` command.

Note
- Automation controller data is stored in the database. Database storage increases with the number of hosts managed, number of jobs run, number of facts stored in the fact cache, and number of tasks in any individual job. For example, a playbook runs every hour (24 times a day) across 250 hosts, with 20 tasks, stores over 800000 events in the database every week.
- If not enough space is reserved in the database, the old job runs and facts must be cleaned on a regular basis. For more information, see [Management Jobs](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/assembly-controller-management-jobs) in the _Configuring automation execution_ guide.




