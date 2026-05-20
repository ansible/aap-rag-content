# 9. Patch releases
## 9.3. Ansible Automation Platform patch release February 25, 2026
### 9.3.10. Event-Driven Ansible

#### 9.3.10.1. Enhancements

- The content of the `de-minimal` and `de-supported` images of the decision environment changes. There are new names for existing plugins, and the old names are still available albeit deprecated. In most of the cases only a change of the used event source or event filter is needed.(AAP-48005)


- For example:

- name: Production ruleset
sources:
- ansible.eda.pg_listener:
postgres_params:
host: postgresql_hostname
port: postgresql_port
dbname: postgresql_database
channels:
- my_events
- my_alerts
[...]

- The event source name will need to be changed as follows:

- name: Production ruleset
sources:
- eda.builtin.pg_listener:
postgres_params:
host: postgresql_hostname
port: postgresql_port
dbname: postgresql_database
channels:
- my_events
- my_alerts
[...]

#### 9.3.10.2. Bug Fixes

- Fixed an issue where the activation worker failed to reconnect to redis after disconnection.Override RQ’s default heartbeat to call `register_birth`, allowing worker re-registration in case of worker disconnects from Redis, and also eliminating ghost workers. Upgraded rq version to 2.6.1.(AAP-56872)

