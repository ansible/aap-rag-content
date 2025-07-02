# 5. Jobs in automation controller
## 5.3. Playbook run jobs
### 5.3.3. Playbook access and information sharing




Automation controller’s use of automation execution environments and Linux containers prevents playbooks from reading files outside of their project directory.

By default, the only data exposed to the ansible-playbook process inside the container is the current project being used.

You can customize this in the Job Settings and expose additional directories from the host into the container.

