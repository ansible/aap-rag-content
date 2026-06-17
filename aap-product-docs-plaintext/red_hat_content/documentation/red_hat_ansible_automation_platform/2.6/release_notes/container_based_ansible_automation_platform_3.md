# 9. Patch releases
## 9.6. Ansible Automation Platform patch release December 10, 2025
### 9.6.7. Container-based Ansible Automation Platform

#### 9.6.7.1. Enhancements

- Configured podman PID limits, `sysctls` for `inotify` and kernel keys, and ulimit `nofile` for user running Ansible Automation Platform service containers based on system resources.(AAP-59438)

#### 9.6.7.2. Bug Fixes

- Fixed an issue where after uninstall/re-install of receptor jobs were unable to start due to stale exited containers with the same name were still present.(AAP-59609)

