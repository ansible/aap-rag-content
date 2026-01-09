# 10. Patch releases
## 10.1. Ansible Automation Platform patch release December 10, 2025
### 10.1.5. Automation controller




#### 10.1.5.1. Features




- Updated the pinned version for receptorctl in controller. This addresses edge cases that could cause JSON to fail to parse a line from the worker stream.(AAP-58415)


Error message

```
Error: Expecting value: line 1 column 1 (char 0) Line with invalid JSON data: b
```

#### 10.1.5.2. Bug Fixes




- Fixed an issue where the system would display reminders on unsupported architectures, causing confusion.(AAP-56221)
- Fixed an issue where jobs failed on `    fapolicyd` enabled systems where Python 3.9 was not installed by default. Updates `    automation-controller-fapolicyd` from Python 3.9 to Python 3.11 to address this issue.(AAP-58479)
- Fixed an issue where there was a Redis broken pipe error in the long-running jobs component: API.(AAP-59727)
- Fixed a GitHub application installation access token lookup where it would not accept Iv2 Client IDs.(AAP-58882)
- Fixed an issue where the project update and project deletions failed with no output.(AAP-58532)


