# Ansible Automation Platform patch release December 10, 2025
## Container-based Ansible Automation Platform

Enhancements
- Configured podman PID limits, `sysctls` for `inotify` and kernel keys, and ulimit `nofile` for user running Ansible Automation Platform service containers based on system resources.(AAP-59438)

Bug Fixes
- Fixed an issue where after uninstall/re-install of receptor jobs were unable to start due to stale exited containers with the same name were still present.(AAP-59609)

