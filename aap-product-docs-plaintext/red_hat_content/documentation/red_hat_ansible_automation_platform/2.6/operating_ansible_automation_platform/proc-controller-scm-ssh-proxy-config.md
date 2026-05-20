# 3. Configuring Ansible Automation Platform to use egress proxy
## 3.3. Automation controller settings
### 3.3.1. Configuring SCM project sync using SSH to work with a proxy in automation controller

The following procedure for RPM-based Ansible Automation Platform describes how to use automation controller Project Sync by using the SSH protocol to work with a proxy server.

**Procedure**

1. Perform the following steps on the automation controller nodes. If ansible-builder has not been installed yet, install it first.

# subscription-manager repos --enable ansible-automation-platform-2.6-for-rhel-8-x86_64-rpms
# dnf install ansible-builder

2. Build a custom execution environment.


1. First, create a work directory:

# su - awx
$ mkdir -p builder/newee
$ cd builder/newee

3. Create an `execution-environment.yml` file with the following content:

version: 1

build_arg_defaults:
EE_BASE_IMAGE: 'registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8:latest'

additional_build_steps:
prepend:
- RUN microdnf install -y nc

4. Log in to registry.redhat.io.

$ podman login registry.redhat.io

5. Run ansible-builder to start the building process.

$ cd /var/lib/awx/builder/newee/
$ ansible-builder build -t my-env -v 3

6. Add the custom execution environment you created.

7. On the navigation panel, select Automation Execution → Infrastructure → Execution Environments.

8. Click Create execution environment.

9. In the **Image** field add `localhost/my-env:latest`.

10. Click Create execution environment.

11. Re-run the Ansible Automation Platform installation program with the following steps to replace the execution environment from the default to the customized environment which will be used as a Project syncs.


Note
Backup Ansible Automation Platform before running the installation program.

# ./setup.sh -b

12. Create an `automationcontroller` file under the `group_vars` directory in the same location as the `setup.sh` file. The file contents are as follows:

control_plane_execution_environment: localhost/my-env

13. Run `setup.sh`

# ./setup.sh

14. Create `ssh_config` under the directory. For example:

Host github.com
Hostname ssh.github.com
ProxyCommand nc --proxy-type http --proxy proxy.example.com:port %h %p
User git

15. Add the `ssh_config` file’s directory path in PATH to expose the isolated jobs so that the container execution environment can read `ssh_config` file.

16. In the navigation panel, select Settings → Automation Execution → Job.

17. Click Edit.

18. If the `ssh_config` file has been created as `/var/lib/awx/.ssh/ssh_config`, add this to **Paths to expose to isolated jobs**


Note
Ensure `ssh_config` is owned by the AWX user. (`#chown awx:awx /var/lib/awx/.ssh/ssh_config`)

[
"/var/lib/awx/.ssh:/etc/ssh:O"
]

**Additional resources**

- [Build an execution environment](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_automation_execution/assembly-controller-execution-environments#ref-controller-build-exec-envs)

