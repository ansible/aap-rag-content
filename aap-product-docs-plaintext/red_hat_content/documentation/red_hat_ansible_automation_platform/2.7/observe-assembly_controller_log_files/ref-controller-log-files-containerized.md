# Access log information
## Access automation controller logs for containerized Ansible Automation Platform

Logs for containerized Ansible Automation Platform are not saved to specific files. The application logs are sent to the container `stdout` and handled by Podman with `journald`.

The three containers associated with automation controller are:

-  `automation-controller-rsyslog`
-  `automation-controller-task`
-  `automation-controller-web`


For more information about the purpose of each of these containers and how to inspect the logs, see [Diagnosing the problem](/documentation/en-us/red_hat_ansible_automation_platform/2.7/troubleshoot-assembly_appendix_troubleshoot_containerized_aap#diagnosing-the-problem "For general container-based troubleshooting, you can inspect the container logs for any running service to help troubleshoot underlying issues.") in *Containerized installation*.

