# 8. Automation controller logs
## 8.1. Accessing automation controller logs for containerized Ansible Automation Platform




Logs for containerized Ansible Automation Platform are not saved to specific files. The application logs are sent to the container `stdout` and handled by Podman with `journald` .

The three containers associated with automation controller are:

-  `    automation-controller-rsyslog`
-  `    automation-controller-task`
-  `    automation-controller-web`


For more information about the purpose of each of these containers and how to inspect the logs, see [Diagnosing the problem](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/troubleshooting-containerized-ansible-automation-platform#diagnosing-the-problem_troubleshooting-containerized-aap) in _Containerized installation_ .

