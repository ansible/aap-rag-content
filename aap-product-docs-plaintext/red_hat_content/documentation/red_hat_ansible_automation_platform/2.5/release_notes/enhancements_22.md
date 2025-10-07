# 10. Patch releases
## 10.8. Ansible Automation Platform patch release May 7, 2025
### 10.8.4. Enhancements




#### 10.8.4.1. Ansible Automation Platform




- Updated platform gateway to adopt selected standard component for settings mechanism.(AAP-34939)
- Refactored the `    authenticate()` method inside the `    AuthenticatorPlugin` class in `    legacy_password.py` and `    legacy_sso.py` to their common parent `    LegacyMixin` . Added comments to classes and their methods for code clarity.(AAP-44460)


#### 10.8.4.2. Ansible Automation Platform Operator




- Fixed an issue where the Lightspeed Operator would not use the `    ANSIBLE_AI_MODEL_MESH_CONFIG` .(AAP-41335)
- Extended CCSP and renewal guidance reports to include inventory scope and node/host details.(AAP-38802)


#### 10.8.4.3. Automation controller




- Updated the pinned version of `    receptorctl` in automation controller to 1.5.5.(AAP-44823)
- Updated the pinned version for `    ansible-runner` in automation controller.(AAP-43357)


#### 10.8.4.4. Container-based Ansible Automation Platform




- Added new variable `    use_archive_compression` with default `    value: true` . Added new variable component `    Name_use_archive_compression` for each component with the default `    value: true` .(AAP-41242)


#### 10.8.4.5. Event-Driven Ansible




- Event-Driven Ansible collection standardization enhancements.(AAP-41402)
- Relevant settings and versions are emitted in logs when the ansible-rulebook starts in worker mode.(AAP-40781)
- Added log entries with settings and version at startup.(AAP-40781)
- Enhanced the Ansible Automation Platform injectors for `    eda-server` to include common platform variables as `    extra_vars` or environment variables if they are specified.(AAP-43029)
- Event-Driven Ansible decision environment validation errors now display under the decision environment text box in the decision environment UI page.(AAP-42147)
- Added a automation controller URL check for the CLI.(AAP-41575)
- If a source plugin terminates you are now able to see the stack trace with the source file name, the function name, and line number.(AAP-41774)


#### 10.8.4.6. RPM-based Ansible Automation Platform




- Added compression for archive and database artifacts used in backup/restore


- Updated database filename used for automation controller `        pg_dump` from tower to automation controller while maintaining backward compatibility for backups using `        tower.db` filename.(AAP-42055)



