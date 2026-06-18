# Troubleshoot your containerized deployment

Use this information to troubleshoot your containerized Ansible Automation Platform installation.

## Gather logs from your containerized deployment

Use the `sos` utility to collect configuration and diagnostic data for Red Hat Technical Support. An `sos` report is the standard starting point for troubleshooting.

### About this task

You can collect an `sos` report for each host in your containerized Ansible Automation Platform deployment by running the `log_gathering` playbook with the appropriate parameters.

### Procedure

1.  Go to the Ansible Automation Platform installation directory.
2.  Run the `log_gathering` playbook. This playbook connects to each host in the inventory file, installs the `sos` tool, and generates the `sos` report.

```
$ ansible-playbook -i <path_to_inventory_file> ansible.containerized_installer.log_gathering
```

3.  To collect container-level logs, run the `sos` report directly on each host with the `aap_containerized` plugin enabled:


```
$ sudo sos report -e aap_containerized -k aap_containerized.username=*<username>*
```
where *<username>* is the service account or user running the containerized installation.

4.  Optional: To define additional parameters, specify them with the `-e` option. For example:


```
$ ansible-playbook -i <path_to_inventory_file> ansible.containerized_installer.log_gathering -e 'target_sos_directory=<path_to_files>' -e 'case_number=0000000' -e 'clean=true' -e 'upload=true' -s
```
1.  You can use the `-s` option to step through each task in the playbook and confirm its execution. This is optional but can be helpful for debugging.
2.  The following is a list of the parameters you can use with the `log_gathering` playbook:
*Table 1. Parameter reference*

| Parameter name              | Description                                                              | Default                                     |
| --------------------------- | ------------------------------------------------------------------------ | ------------------------------------------- |
| <br> `target_sos_directory` | <br>Used to change the default location for the `sos` report files.      | <br>`/tmp` directory of the current server. |
| <br> `case_number`          | <br>Specifies the support case number if relevant to the log gathering.  |                                             |
| <br> `clean`                | <br>Obfuscates sensitive data that might be present on the `sos` report. | <br> `false`                                |
| <br> `upload`               | <br>Automatically uploads the `sos` report data to Red Hat.              | <br> `false`                                |

5.  Gather the `sos` report files described in the playbook output and share them with the support engineer or directly upload the `sos` report to Red Hat using the `upload=true` additional parameter.

## Diagnose the problem

For general container-based troubleshooting, you can inspect the container logs for any running service to help troubleshoot underlying issues.

**Identifying the running containers**

To get a list of the running container names run the following command:

```
$ podman ps --all --format "{{.Names}}"
```

*Table 2. Container details*

| Component group           | Container name                                   | Purpose                                                                                                                                                                  |
| ------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <br>Automation controller | <br> `automation-controller-rsyslog`             | <br>Handles centralized logging for automation controller.                                                                                                               |
| <br>Automation controller | <br> `automation-controller-task`                | <br>Manages and runs tasks related to automation controller, such as running playbooks and interacting with inventories.                                                 |
| <br>Automation controller | <br> `automation-controller-web`                 | <br>A web server that provides a REST API for automation controller. This is accessed and routed through platform gateway for user interaction.                          |
| <br>Event-Driven Ansible  | <br> `automation-eda-api`                        | <br>Exposes the API for Event-Driven Ansible, allowing external systems to trigger and manage event-driven automations.                                                  |
| <br>Event-Driven Ansible  | <br> `automation-eda-daphne`                     | <br>A web server for Event-Driven Ansible, handling WebSocket connections and serving static files.                                                                      |
| <br>Event-Driven Ansible  | <br> `automation-eda-web`                        | <br>A web server that provides a REST API for Event-Driven Ansible. This is accessed and routed through platform gateway for user interaction.                           |
| <br>Event-Driven Ansible  | <br> `automation-eda-worker-<number>`            | <br>These containers run the automation rules and playbooks based on incoming events.                                                                                    |
| <br>Event-Driven Ansible  | <br> `automation-eda-activation-worker-<number>` | <br>These containers manage the activation of automation rules, ensuring they run when specific conditions are met.                                                      |
| <br>Event-Driven Ansible  | <br> `automation-eda-scheduler`                  | <br>Responsible for scheduling and managing recurring tasks and rule activations.                                                                                        |
| <br>Platform gateway      | <br> `automation-gateway-proxy`                  | <br>Acts as a reverse proxy, routing incoming requests to the appropriate Ansible Automation Platform services.                                                          |
| <br>Platform gateway      | <br> `automation-gateway`                        | <br>Responsible for authentication, authorization, and overall request handling for the platform, all of which is exposed through a REST API and served by a web server. |
| <br>Automation hub        | <br> `automation-hub-api`                        | <br>Provides the API for automation hub, enabling interaction with collection content, user management, and other automation hub functionality.                          |
| <br>Automation hub        | <br> `automation-hub-content`                    | <br>Manages and serves Ansible Content Collections, roles, and modules stored in automation hub.                                                                         |
| <br>Automation hub        | <br> `automation-hub-web`                        | <br>A web server that provides a REST API for automation hub. This is accessed and routed through platform gateway for user interaction.                                 |
| <br>Automation hub        | <br> `automation-hub-worker-<number>`            | <br>These containers handle background tasks for automation hub, such as content synchronization, indexing, and validation.                                              |
| <br>Performance Co-Pilot  | <br> `pcp`                                       | <br>If Performance Co-Pilot Monitoring is enabled, this container is used for system performance monitoring and data collection.                                         |
| <br>PostgreSQL            | <br> `postgresql`                                | <br>Hosts the PostgreSQL database for Ansible Automation Platform.                                                                                                       |
| <br>Receptor              | <br> `receptor`                                  | <br>Facilitates secure and reliable communication within Ansible Automation Platform.                                                                                    |
| <br>Redis                 | <br> `redis-<suffix>`                            | <br>Responsible for caching, real-time analytics and fast data retrieval.                                                                                                |


**Inspecting the logs**

Containerized Ansible Automation Platform uses `journald` for Podman logging. To inspect any running container logs, run the `journalctl` command:

```
$ journalctl CONTAINER_NAME=<container_name>
```
Example command with output:

```
$ journalctl CONTAINER_NAME=automation-gateway-proxy

Oct 08 01:40:12 aap.example.org automation-gateway-proxy[1919]: [2024-10-08 00:40:12.885][2][info][upstream] [external/envoy/source/common/upstream/cds_ap>
Oct 08 01:40:12 aap.example.org automation-gateway-proxy[1919]: [2024-10-08 00:40:12.885][2][info][upstream] [external/envoy/source/common/upstream/cds_ap>
Oct 08 01:40:19 aap.example.org automation-gateway-proxy[1919]: [2024-10-08T00:40:16.753Z] "GET /up HTTP/1.1" 200 - 0 1138 10 0 "192.0.2.1" "python->
```
To view the logs of a running container in real-time, run the `podman logs -f` command:

```
$ podman logs -f <container_name>
```
**Controlling container operations**

You can control operations for a container by running the `systemctl` command:

```
$ systemctl --user status <container_name>
```
Example command with output:

```
$ systemctl --user status automation-gateway-proxy
● automation-gateway-proxy.service - Podman automation-gateway-proxy.service
Loaded: loaded (/home/user/.config/systemd/user/automation-gateway-proxy.service; enabled; preset: disabled)
Active: active (running) since Mon 2024-10-07 12:39:23 BST; 23h ago
Docs: man:podman-generate-systemd(1)
Process: 780 ExecStart=/usr/bin/podman start automation-gateway-proxy (code=exited, status=0/SUCCESS)
Main PID: 1919 (conmon)
Tasks: 1 (limit: 48430)
Memory: 852.0K
CPU: 2.996s
CGroup: /user.slice/user-1000.slice/user@1000.service/app.slice/automation-gateway-proxy.service
└─1919 /usr/bin/conmon --api-version 1 -c 2dc3c7b2cecd73010bad1e0aaa806015065f92556ed3591c9d2084d7ee209c7a -u 2dc3c7b2cecd73010bad1e0aaa80>
Oct 08 11:44:10 aap.example.org automation-gateway-proxy[1919]: [2024-10-08T10:44:02.926Z] "GET /api/galaxy/_ui/v1/settings/ HTTP/1.1" 200 - 0 654 58 47 ">
Oct 08 11:44:10 aap.example.org automation-gateway-proxy[1919]: [2024-10-08T10:44:03.387Z] "GET /api/controller/v2/config/ HTTP/1.1" 200 - 0 4018 58 44 "1>
Oct 08 11:44:10 aap.example.org automation-gateway-proxy[1919]: [2024-10-08T10:44:03.370Z] "GET /api/galaxy/v3/plugin/ansible/search/collection-versions/?>
Oct 08 11:44:10 aap.example.org automation-gateway-proxy[1919]: [2024-10-08T10:44:03.405Z] "GET /api/controller/v2/organizations/?role_level=notification_>
Oct 08 11:44:10 aap.example.org automation-gateway-proxy[1919]: [2024-10-08T10:44:04.366Z] "GET /api/galaxy/_ui/v1/me/ HTTP/1.1" 200 - 0 1368 79 40 "192.1>
Oct 08 11:44:10 aap.example.org automation-gateway-proxy[1919]: [2024-10-08T10:44:04.360Z] "GET /api/controller/v2/workflow_approvals/?page_size=200&statu>
Oct 08 11:44:10 aap.example.org automation-gateway-proxy[1919]: [2024-10-08T10:44:04.379Z] "GET /api/controller/v2/job_templates/7/ HTTP/1.1" 200 - 0 1356>
Oct 08 11:44:10 aap.example.org automation-gateway-proxy[1919]: [2024-10-08T10:44:04.378Z] "GET /api/galaxy/_ui/v1/feature-flags/ HTTP/1.1" 200 - 0 207 81>
Oct 08 11:44:13 aap.example.org automation-gateway-proxy[1919]: [2024-10-08 10:44:13.856][2][info][upstream] [external/envoy/source/common/upstream/cds_ap>
Oct 08 11:44:13 aap.example.org automation-gateway-proxy[1919]: [2024-10-08 10:44:13.856][2][info][upstream] [external/envoy/source/common/upstream/cds_ap
```
**Getting container information about the execution plane**

To get container information about automation controller, Event-Driven Ansible, and `execution_nodes` nodes, prefix any Podman commands with either:

```
CONTAINER_HOST=unix://run/user/<user_id>/podman/podman.sock
```
or

```
CONTAINERS_STORAGE_CONF=<user_home_directory>/aap/containers/storage.conf
```
Example with output:

```
$ CONTAINER_HOST=unix://run/user/1000/podman/podman.sock podman images

REPOSITORY                                                            TAG         IMAGE ID      CREATED     SIZE
registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8  latest      59d1bc680a7c  6 days ago  2.24 GB
registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8    latest      a64b9fc48094  6 days ago  338 MB
```

## Troubleshoot your containerized installation

Use this information to troubleshoot your containerized installation of Ansible Automation Platform.

**The installation takes a long time, or has errors, what should I check?**

1. Ensure your system meets the minimum requirements as outlined in [System requirements](/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-ref_cont_aap_system_requirements "Use this information when planning your installation of containerized Ansible Automation Platform."). Factors such as improper storage choices and high latency when distributing across many hosts will all have an impact on installation time.
2. Review the installation log file which is located by default at `./aap_install.log`. You can change the log file location within the `ansible.cfg` file in the installation directory.
3. Enable task profiling callbacks on an ad hoc basis to give an overview of where the installation program spends the most time. To do this, use the local `ansible.cfg` file. Add a callback line under the `[defaults]` section, for example:

```
$ cat ansible.cfg
[defaults]
callbacks_enabled = ansible.posix.profile_tasks
```

**Automation controller returns an error of 413**

This error occurs when `manifest.zip` license files that are larger than the `controller_nginx_client_max_body_size` setting. If this error occurs, update the inventory file to include the following variable:

```
controller_nginx_client_max_body_size=5m
```
The default setting of `5m` should prevent this issue, but you can increase the value as needed.

**When attempting to install containerized Ansible Automation Platform in Amazon Web Services you receive output that there is no space left on device**

```
TASK [ansible.containerized_installer.automationcontroller : Create the receptor container] ***************************************************
fatal: [ec2-13-48-25-168.eu-north-1.compute.amazonaws.com]: FAILED! => {"changed": false, "msg": "Can't create container receptor", "stderr": "Error: creating container storage: creating an ID-mapped copy of layer \"98955f43cc908bd50ff43585fec2c7dd9445eaf05eecd1e3144f93ffc00ed4ba\": error during chown: storage-chown-by-maps: lchown usr/local/lib/python3.9/site-packages/azure/mgmt/network/v2019_11_01/operations/__pycache__/_available_service_aliases_operations.cpython-39.pyc: no space left on device: exit status 1\n", "stderr_lines": ["Error: creating container storage: creating an ID-mapped copy of layer \"98955f43cc908bd50ff43585fec2c7dd9445eaf05eecd1e3144f93ffc00ed4ba\": error during chown: storage-chown-by-maps: lchown usr/local/lib/python3.9/site-packages/azure/mgmt/network/v2019_11_01/operations/__pycache__/_available_service_aliases_operations.cpython-39.pyc: no space left on device: exit status 1"], "stdout": "", "stdout_lines": []}
```
If you are installing a `/home` filesystem into a default Amazon Web Services marketplace RHEL instance, it might be too small since `/home` is part of the root `/` filesystem. To resolve this issue you must make more space available. For more information about the system requirements, see [System requirements](/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-ref_cont_aap_system_requirements "Use this information when planning your installation of containerized Ansible Automation Platform.").

**"Install container tools" task fails due to unavailable packages**

This error can be seen in the installation process output as the following:

```
TASK [ansible.containerized_installer.common : Install container tools] **********************************************************************************************************
fatal: [192.0.2.1]: FAILED! => {"changed": false, "failures": ["No package crun available.", "No package podman available.", "No package slirp4netns available.", "No package fuse-overlayfs available."], "msg": "Failed to install some of the specified packages", "rc": 1, "results": []}
fatal: [192.0.2.2]: FAILED! => {"changed": false, "failures": ["No package crun available.", "No package podman available.", "No package slirp4netns available.", "No package fuse-overlayfs available."], "msg": "Failed to install some of the specified packages", "rc": 1, "results": []}
fatal: [192.0.2.3]: FAILED! => {"changed": false, "failures": ["No package crun available.", "No package podman available.", "No package slirp4netns available.", "No package fuse-overlayfs available."], "msg": "Failed to install some of the specified packages", "rc": 1, "results": []}
fatal: [192.0.2.4]: FAILED! => {"changed": false, "failures": ["No package crun available.", "No package podman available.", "No package slirp4netns available.", "No package fuse-overlayfs available."], "msg": "Failed to install some of the specified packages", "rc": 1, "results": []}
fatal: [192.0.2.5]: FAILED! => {"changed": false, "failures": ["No package crun available.", "No package podman available.", "No package slirp4netns available.", "No package fuse-overlayfs available."], "msg": "Failed to install some of the specified packages", "rc": 1, "results": []}
```
To fix this error, run the following command on the target hosts:

```
sudo subscription-manager register
```

## Troubleshoot your containerized configuration

Use this information to troubleshoot your containerized Ansible Automation Platform configuration.

**Sometimes the post install for seeding my Ansible Automation Platform content errors out**

This could manifest itself as output similar to this:

```
TASK [infra.controller_configuration.projects : Configure Controller Projects | Wait for finish the projects creation] ***************************************
Friday 29 September 2023  11:02:32 +0100 (0:00:00.443)       0:00:53.521 ******
FAILED - RETRYING: [daap1.lan]: Configure Controller Projects | Wait for finish the projects creation (1 retries left).
failed: [daap1.lan] (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '536962174348.33944', 'results_file': '/home/aap/.ansible_async/536962174348.33944', 'changed': False, '__controller_project_item': {'name': 'AAP Config-As-Code Examples', 'organization': 'Default', 'scm_branch': 'main', 'scm_clean': 'no', 'scm_delete_on_update': 'no', 'scm_type': 'git', 'scm_update_on_launch': 'no', 'scm_url': 'https://github.com/user/repo.git'}, 'ansible_loop_var': '__controller_project_item'}) => {"__projects_job_async_results_item": {"__controller_project_item": {"name": "AAP Config-As-Code Examples", "organization": "Default", "scm_branch": "main", "scm_clean": "no", "scm_delete_on_update": "no", "scm_type": "git", "scm_update_on_launch": "no", "scm_url": "https://github.com/user/repo.git"}, "ansible_job_id": "536962174348.33944", "ansible_loop_var": "__controller_project_item", "changed": false, "failed": 0, "finished": 0, "results_file": "/home/aap/.ansible_async/536962174348.33944", "started": 1}, "ansible_job_id": "536962174348.33944", "ansible_loop_var": "__projects_job_async_results_item", "attempts": 30, "changed": false, "finished": 0, "results_file": "/home/aap/.ansible_async/536962174348.33944", "started": 1, "stderr": "", "stderr_lines": [], "stdout": "", "stdout_lines": []}
```
The `infra.controller_configuration.dispatch` role uses an asynchronous loop with 30 retries to apply each configuration type, and the default delay between retries is 1 second. If the configuration is large, this might not be enough time to apply everything before the last retry occurs.

Increase the retry delay by setting the `controller_configuration_async_delay` variable to 2 seconds for example. You can set this variable in the `[all:vars]` section of the installation program inventory file.

Re-run the installation program to ensure everything works as expected.

## Understand the architecture of your containerized deployment

Use this information to understand the architecture for your containerized Ansible Automation Platform deployment.

**Can you give details of the architecture for the Ansible Automation Platform containerized design?**

We use as much of the underlying Red Hat Enterprise Linux technology as possible. Podman is used for the container runtime and management of services.

Use `podman ps` to list the running containers on the system.

Use `podman images` to display information about locally stored images.

Containerized Ansible Automation Platform runs as rootless containers for enhanced security by default. This means you can install containerized Ansible Automation Platform by using any local unprivileged user account. Privilege escalation is only needed for certain root level tasks, and by default is not needed to use root directly.

The installation program adds the following files to the filesystem where you run the installation program on the underlying Red Hat Enterprise Linux host:

```
$ tree -L 1
.
├── aap_install.log
├── ansible.cfg
├── collections
├── galaxy.yml
├── inventory
├── LICENSE
├── meta
├── playbooks
├── plugins
├── README.md
├── requirements.yml
├── roles
```
The installation root directory includes other containerized services that make use of Podman volumes.

Here are some examples for further reference:

The `containers` directory includes some of the Podman specifics used and installed for the execution plane:

```
containers/
├── podman
├── storage
│   ├── defaultNetworkBackend
│   ├── libpod
│   ├── networks
│   ├── overlay
│   ├── overlay-containers
│   ├── overlay-images
│   ├── overlay-layers
│   ├── storage.lock
│   └── userns.lock
└── storage.conf
```
The `controller` directory has some of the installed configuration and runtime data points:

```
controller/
├── data
│   ├── job_execution
│   ├── projects
│   └── rsyslog
├── etc
│   ├── conf.d
│   ├── launch_awx_task.sh
│   ├── settings.py
│   ├── tower.cert
│   └── tower.key
├── nginx
│   └── etc
├── rsyslog
│   └── run
└── supervisor
└── run
```
The `receptor` directory has the automation mesh configuration:

```
receptor/
├── etc
│   └── receptor.conf
└── run
├── receptor.sock
└── receptor.sock.lock
```
After installation, you will also find other files in the local user’s `/home` directory such as the `.cache` directory:

```
.cache/
├── containers
│   └── short-name-aliases.conf.lock
└── rhsm
└── rhsm.log
```
As services are run using rootless Podman by default, you can use other services such as running `systemd` as non-privileged users. Under `systemd` you can see some of the component service controls available:

The `.config` directory:

```
.config/
├── cni
│   └── net.d
│       └── cni.lock
├── containers
│   ├── auth.json
│   └── containers.conf
└── systemd
└── user
├── automation-controller-rsyslog.service
├── automation-controller-task.service
├── automation-controller-web.service
├── default.target.wants
├── podman.service.d
├── postgresql.service
├── receptor.service
├── redis.service
└── sockets.target.wants
```
This is specific to Podman and conforms to the Open Container Initiative (OCI) specifications. When you run Podman as the root user `/var/lib/containers` is used by default. For standard users the hierarchy under `$HOME/.local` is used.

The `.local` directory:

```
.local/
└── share
└── containers
├── cache
├── podman
└── storage
```
As an example `.local/storage/volumes` contains what the output from `podman volume ls` provides:

```
$ podman volume ls

DRIVER      VOLUME NAME
local       d73d3fe63a957bee04b4853fd38c39bf37c321d14fdab9ee3c9df03645135788
local       postgresql
local       redis_data
local       redis_etc
local       redis_run
```
The execution plane is isolated from the control plane main services to ensure it does not affect the main services.

Control plane services run with the standard Podman configuration and can be found in: `~/.local/share/containers/storage`.

Execution plane services (automation controller, Event-Driven Ansible and execution nodes) use a dedicated configuration found in `~/aap/containers/storage.conf`. This separation prevents execution plane containers from affecting the control plane services.

You can view the execution plane configuration with one of the following commands:

```
CONTAINERS_STORAGE_CONF=~/aap/containers/storage.conf podman <subcommand>
```

```
CONTAINER_HOST=unix://run/user/<user uid>/podman/podman.sock podman <subcommand>
```
**How can I see host resource utilization statistics?**

Run the following command to display host resource utilization statistics:

```
$ podman container stats -a
```
Example output based on a Dell sold and offered containerized Ansible Automation Platform solution (DAAP) install that utilizes ~1.8 GB RAM:

```
ID            NAME                           CPU %       MEM USAGE / LIMIT  MEM %       NET IO      BLOCK IO    PIDS        CPU TIME    AVG CPU %
0d5d8eb93c18  automation-controller-web      0.23%       959.1MB / 3.761GB  25.50%      0B / 0B     0B / 0B     16          20.885142s  1.19%
3429d559836d  automation-controller-rsyslog  0.07%       144.5MB / 3.761GB  3.84%       0B / 0B     0B / 0B     6           4.099565s   0.23%
448d0bae0942  automation-controller-task     1.51%       633.1MB / 3.761GB  16.83%      0B / 0B     0B / 0B     33          34.285272s  1.93%
7f140e65b57e  receptor                       0.01%       5.923MB / 3.761GB  0.16%       0B / 0B     0B / 0B     7           1.010613s   0.06%
c1458367ca9c  redis                          0.48%       10.52MB / 3.761GB  0.28%       0B / 0B     0B / 0B     5           9.074042s   0.47%
ef712cc2dc89  postgresql                     0.09%       21.88MB / 3.761GB  0.58%       0B / 0B     0B / 0B     21          15.571059s  0.80%
```
**How much storage is used and where?**

The container volume storage is under the local user at `$HOME/.local/share/containers/storage/volumes`.

1. To view the details of each volume, run the following command:

```
$ podman volume ls
```

2. Run the following command to display detailed information about a specific volume:

```
$ podman volume inspect <volume_name>
```

For example:

```
$ podman volume inspect postgresql
```
Example output:

```
[
{
"Name": "postgresql",
"Driver": "local",
"Mountpoint": "/home/aap/.local/share/containers/storage/volumes/postgresql/_data",
"CreatedAt": "2024-01-08T23:39:24.983964686Z",
"Labels": {},
"Scope": "local",
"Options": {},
"MountCount": 0,
"NeedsCopyUp": true
}
]
```
Several files created by the installation program are located in `$HOME/aap/` and bind-mounted into various running containers.

1. To view the mounts associated with a container run the following command:

```
$ podman ps --format "{{.ID}}\t{{.Command}}\t{{.Names}}"
```
Example output:

```
89e779b81b83	run-postgresql	postgresql
4c33cc77ef7d	run-redis	redis
3d8a028d892d	/usr/bin/receptor...	receptor
09821701645c	/usr/bin/launch_a...	automation-controller-rsyslog
a2ddb5cac71b	/usr/bin/launch_a...	automation-controller-task
fa0029a3b003	/usr/bin/launch_a...	automation-controller-web
20f192534691	gunicorn --bind 1...	automation-eda-api
f49804c7e6cb	daphne -b 127.0.0...	automation-eda-daphne
d340b9c1cb74	/bin/sh -c nginx ...	automation-eda-web
111f47de5205	aap-eda-manage rq...	automation-eda-worker-1
171fcb1785af	aap-eda-manage rq...	automation-eda-worker-2
049d10555b51	aap-eda-manage rq...	automation-eda-activation-worker-1
7a78a41a8425	aap-eda-manage rq...	automation-eda-activation-worker-2
da9afa8ef5e2	aap-eda-manage sc...	automation-eda-scheduler
8a2958be9baf	gunicorn --name p...	automation-hub-api
0a8b57581749	gunicorn --name p...	automation-hub-content
68005b987498	nginx -g daemon o...	automation-hub-web
cb07af77f89f	pulpcore-worker	automation-hub-worker-1
a3ba05136446	pulpcore-worker	automation-hub-worker-2
```

2. Run the following command:

```
$ podman inspect <container_name> | jq -r .[].Mounts[].Source
```
Example output:

```
/home/aap/.local/share/containers/storage/volumes/receptor_run/_data
/home/aap/.local/share/containers/storage/volumes/redis_run/_data
/home/aap/aap/controller/data/rsyslog
/home/aap/aap/controller/etc/tower.key
/home/aap/aap/controller/etc/conf.d/callback_receiver_workers.py
/home/aap/aap/controller/data/job_execution
/home/aap/aap/controller/nginx/etc/controller.conf
/home/aap/aap/controller/etc/conf.d/subscription_usage_model.py
/home/aap/aap/controller/etc/conf.d/cluster_host_id.py
/home/aap/aap/controller/etc/conf.d/insights.py
/home/aap/aap/controller/rsyslog/run
/home/aap/aap/controller/data/projects
/home/aap/aap/controller/etc/settings.py
/home/aap/aap/receptor/etc/receptor.conf
/home/aap/aap/controller/etc/conf.d/execution_environments.py
/home/aap/aap/tls/extracted
/home/aap/aap/controller/supervisor/run
/home/aap/aap/controller/etc/uwsgi.ini
/home/aap/aap/controller/etc/conf.d/container_groups.py
/home/aap/aap/controller/etc/launch_awx_task.sh
/home/aap/aap/controller/etc/tower.cert
```

3. If the `jq` RPM is not installed, install it by running the following command:

```
$ sudo dnf -y install jq
```
