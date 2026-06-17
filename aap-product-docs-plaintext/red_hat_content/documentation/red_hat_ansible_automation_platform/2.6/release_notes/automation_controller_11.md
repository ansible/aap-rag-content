# 9. Patch releases
## 9.7. Ansible Automation Platform patch release November 19, 2025
### 9.7.4. Automation controller

#### 9.7.4.1. Features

- Receptor collection version updated to 2.0.6, which is compatible with ansible-core 2.19.(AAP-42617)

#### 9.7.4.2. Bug Fixes

- Fixed an issue where the migrating team mappers which did not include a users field is now supported.(AAP-56395)
- Fixed the following migration error for the migration `0200_template_name_constraint.py` when there was a job template or project with duplicate name in the same organization.(AAP-56222)

**Error Message**

django.db.utils.ProgrammingError: column main_unifiedjobtemplate.org_unique does not exist

- Fixed an issue where some edge cases caused JSON to fail to parse a line from the worker stream with the error: **Expecting value: line 1 column 1 (char 0) Line with invalid JSON data: b**. Updated the pinned version for `receptorctl` in automation controller to address this issue. This effects Tower 4.7.(AAP-58412)
- Fixed an issue where some edge cases caused JSON to fail to parse a line from the worker stream with the error: **Expecting value: line 1 column 1 (char 0) Line with invalid JSON data: b**. Updated the pinned version for `receptorctl` in automation controller to address this issue. This effects Tower 4.6.(AAP-58415)
- Fixed an issue where there was not a meaningful error message whenever the streaming of logs was aborted. Update `ansble-runner` to 2.4.2 to address this issue.(AAP-58390)
- Fixes an issue where jobs failed on `fapolicyd` enabled systems where python3.9 was not installed by default. Updates `automation-controller-fapolicyd` from python3.9 to python3.11 to address this issue.(AAP-55790)

