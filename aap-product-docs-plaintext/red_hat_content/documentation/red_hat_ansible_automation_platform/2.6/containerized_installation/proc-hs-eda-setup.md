# 11. Horizontal scaling in Red Hat Ansible Automation Platform
## 11.1. Horizontal scaling in Event-Driven Ansible controller
### 11.1.2. Setting up horizontal scaling for Event-Driven Ansible controller




To scale up (add more nodes) or scale down (remove nodes), you must update the content of the inventory file to add or remove nodes and rerun the installation program.

**Procedure**

1. Update the inventory to add two more worker nodes:


```
[automationeda]        3.88.116.111 routable_hostname=automationeda-api.example.com eda_type=api        3.88.116.112 routable_hostname=automationeda-api.example.com eda_type=worker        # two more worker nodes    3.88.116.113 routable_hostname=automationeda-api.example.com eda_type=worker        3.88.116.114 routable_hostname=automationeda-api.example.com eda_type=worker
```


1. Re-run the installer.


# Appendix A. Troubleshooting containerized Ansible Automation Platform




Use this information to troubleshoot your containerized Ansible Automation Platform installation.

## A.1. Gathering Ansible Automation Platform logs




With the `sos` utility, you can collect configuration, diagnostic, and troubleshooting data, and give those files to Red Hat Technical Support. An `sos` report is a common starting point for Red Hat technical support engineers when performing analysis of a service request for Ansible Automation Platform.

You can collect an `sos` report for each host in your containerized Ansible Automation Platform deployment by running the `log_gathering` playbook with the appropriate parameters.

**Procedure**

1. Go to the Ansible Automation Platform installation directory.
1. Run the `    log_gathering` playbook. This playbook connects to each host in the inventory file, installs the `    sos` tool, and generates the `    sos` report.


```
$ ansible-playbook -i &lt;path_to_inventory_file&gt; ansible.containerized_installer.log_gathering
```


1. Optional: To define additional parameters, specify them with the `    -e` option. For example:


```
$ ansible-playbook -i &lt;path_to_inventory_file&gt; ansible.containerized_installer.log_gathering -e 'target_sos_directory=&lt;path_to_files&gt;' -e 'case_number=0000000' -e 'clean=true' -e 'upload=true' -s
```


1. You can use the `        -s` option to step through each task in the playbook and confirm its execution. This is optional but can be helpful for debugging.
1. The following is a list of the parameters you can use with the `        log_gathering` playbook:


<span id="idm140279429129632"></span>
**Table A.1. Parameter reference**

| Parameter name | Description | Default |
| --- | --- | --- |
|  `target_sos_directory` | Used to change the default location for the `sos` report files. |  `/tmp` directory of the current server. |
|  `case_number` | Specifies the support case number if relevant to the log gathering. |  |
|  `clean` | Obfuscates sensitive data that might be present on the `sos` report. |  `false` |
|  `upload` | Automatically uploads the `sos` report data to Red Hat. |  `false` |






1. Gather the `    sos` report files described in the playbook output and share them with the support engineer or directly upload the `    sos` report to Red Hat using the `    upload=true` additional parameter.


**Additional resources**

-  [What is an sos report and how to create one in Red Hat Enterprise Linux?](https://access.redhat.com/solutions/3592)


## A.2. Diagnosing the problem




For general container-based troubleshooting, you can inspect the container logs for any running service to help troubleshoot underlying issues.

**Identifying the running containers**

To get a list of the running container names run the following command:

```
$ podman ps --all --format "{{.Names}}"
```


<span id="idm140279428766544"></span>
**Table A.2. Container details**

| Component group | Container name | Purpose |
| --- | --- | --- |
| Automation controller |  `automation-controller-rsyslog` | Handles centralized logging for automation controller. |
| Automation controller |  `automation-controller-task` | Manages and runs tasks related to automation controller, such as running playbooks and interacting with inventories. |
| Automation controller |  `automation-controller-web` | A web server that provides a REST API for automation controller. This is accessed and routed through platform gateway for user interaction. |
| Event-Driven Ansible |  `automation-eda-api` | Exposes the API for Event-Driven Ansible, allowing external systems to trigger and manage event-driven automations. |
| Event-Driven Ansible |  `automation-eda-daphne` | A web server for Event-Driven Ansible, handling WebSocket connections and serving static files. |
| Event-Driven Ansible |  `automation-eda-web` | A web server that provides a REST API for Event-Driven Ansible. This is accessed and routed through platform gateway for user interaction. |
| Event-Driven Ansible |  `automation-eda-worker-&lt;number&gt;` | These containers run the automation rules and playbooks based on incoming events. |
| Event-Driven Ansible |  `automation-eda-activation-worker-&lt;number&gt;` | These containers manage the activation of automation rules, ensuring they run when specific conditions are met. |
| Event-Driven Ansible |  `automation-eda-scheduler` | Responsible for scheduling and managing recurring tasks and rule activations. |
| Platform gateway |  `automation-gateway-proxy` | Acts as a reverse proxy, routing incoming requests to the appropriate Ansible Automation Platform services. |
| Platform gateway |  `automation-gateway` | Responsible for authentication, authorization, and overall request handling for the platform, all of which is exposed through a REST API and served by a web server. |
| Automation hub |  `automation-hub-api` | Provides the API for automation hub, enabling interaction with collection content, user management, and other automation hub functionality. |
| Automation hub |  `automation-hub-content` | Manages and serves Ansible Content Collections, roles, and modules stored in automation hub. |
| Automation hub |  `automation-hub-web` | A web server that provides a REST API for automation hub. This is accessed and routed through platform gateway for user interaction. |
| Automation hub |  `automation-hub-worker-&lt;number&gt;` | These containers handle background tasks for automation hub, such as content synchronization, indexing, and validation. |
| Performance Co-Pilot |  `pcp` | If Performance Co-Pilot Monitoring is enabled, this container is used for system performance monitoring and data collection. |
| PostgreSQL |  `postgresql` | Hosts the PostgreSQL database for Ansible Automation Platform. |
| Receptor |  `receptor` | Facilitates secure and reliable communication within Ansible Automation Platform. |
| Redis |  `redis-&lt;suffix&gt;` | Responsible for caching, real-time analytics and fast data retrieval. |




**Inspecting the logs**

Containerized Ansible Automation Platform uses `journald` for Podman logging. To inspect any running container logs, run the `journalctl` command:

```
$ journalctl CONTAINER_NAME=&lt;container_name&gt;
```

Example command with output:

```
$ journalctl CONTAINER_NAME=automation-gateway-proxy

Oct 08 01:40:12 aap.example.org automation-gateway-proxy[1919]: [2024-10-08 00:40:12.885][2][info][upstream] [external/envoy/source/common/upstream/cds_ap&gt;
Oct 08 01:40:12 aap.example.org automation-gateway-proxy[1919]: [2024-10-08 00:40:12.885][2][info][upstream] [external/envoy/source/common/upstream/cds_ap&gt;
Oct 08 01:40:19 aap.example.org automation-gateway-proxy[1919]: [2024-10-08T00:40:16.753Z] "GET /up HTTP/1.1" 200 - 0 1138 10 0 "192.0.2.1" "python-&gt;
```

To view the logs of a running container in real-time, run the `podman logs -f` command:

```
$ podman logs -f &lt;container_name&gt;
```

**Controlling container operations**

You can control operations for a container by running the `systemctl` command:

```
$ systemctl --user status &lt;container_name&gt;
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
└─1919 /usr/bin/conmon --api-version 1 -c 2dc3c7b2cecd73010bad1e0aaa806015065f92556ed3591c9d2084d7ee209c7a -u 2dc3c7b2cecd73010bad1e0aaa80&gt;
Oct 08 11:44:10 aap.example.org automation-gateway-proxy[1919]: [2024-10-08T10:44:02.926Z] "GET /api/galaxy/_ui/v1/settings/ HTTP/1.1" 200 - 0 654 58 47 "&gt;
Oct 08 11:44:10 aap.example.org automation-gateway-proxy[1919]: [2024-10-08T10:44:03.387Z] "GET /api/controller/v2/config/ HTTP/1.1" 200 - 0 4018 58 44 "1&gt;
Oct 08 11:44:10 aap.example.org automation-gateway-proxy[1919]: [2024-10-08T10:44:03.370Z] "GET /api/galaxy/v3/plugin/ansible/search/collection-versions/?&gt;
Oct 08 11:44:10 aap.example.org automation-gateway-proxy[1919]: [2024-10-08T10:44:03.405Z] "GET /api/controller/v2/organizations/?role_level=notification_&gt;
Oct 08 11:44:10 aap.example.org automation-gateway-proxy[1919]: [2024-10-08T10:44:04.366Z] "GET /api/galaxy/_ui/v1/me/ HTTP/1.1" 200 - 0 1368 79 40 "192.1&gt;
Oct 08 11:44:10 aap.example.org automation-gateway-proxy[1919]: [2024-10-08T10:44:04.360Z] "GET /api/controller/v2/workflow_approvals/?page_size=200&amp;statu&gt;
Oct 08 11:44:10 aap.example.org automation-gateway-proxy[1919]: [2024-10-08T10:44:04.379Z] "GET /api/controller/v2/job_templates/7/ HTTP/1.1" 200 - 0 1356&gt;
Oct 08 11:44:10 aap.example.org automation-gateway-proxy[1919]: [2024-10-08T10:44:04.378Z] "GET /api/galaxy/_ui/v1/feature-flags/ HTTP/1.1" 200 - 0 207 81&gt;
Oct 08 11:44:13 aap.example.org automation-gateway-proxy[1919]: [2024-10-08 10:44:13.856][2][info][upstream] [external/envoy/source/common/upstream/cds_ap&gt;
Oct 08 11:44:13 aap.example.org automation-gateway-proxy[1919]: [2024-10-08 10:44:13.856][2][info][upstream] [external/envoy/source/common/upstream/cds_ap
```

**Getting container information about the execution plane**

To get container information about automation controller, Event-Driven Ansible, and `execution_nodes` nodes, prefix any Podman commands with either:

```
CONTAINER_HOST=unix://run/user/&lt;user_id&gt;/podman/podman.sock
```

or

```
CONTAINERS_STORAGE_CONF=&lt;user_home_directory&gt;/aap/containers/storage.conf
```

Example with output:

```
$ CONTAINER_HOST=unix://run/user/1000/podman/podman.sock podman images

REPOSITORY                                                            TAG         IMAGE ID      CREATED     SIZE
registry.redhat.io/ansible-automation-platform-26/ee-supported-rhel9  latest      59d1bc680a7c  6 days ago  2.24 GB
registry.redhat.io/ansible-automation-platform-26/ee-minimal-rhel9    latest      a64b9fc48094  6 days ago  338 MB
```

## A.3. Troubleshooting containerized Ansible Automation Platform installation




Use this information to troubleshoot your containerized installation of Ansible Automation Platform.

**The installation takes a long time, or has errors, what should I check?**

1. Ensure your system meets the minimum requirements as outlined in [System requirements](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/preparing-containerized-installation#system-requirements) . Factors such as improper storage choices and high latency when distributing across many hosts will all have an impact on installation time.
1. Review the installation log file which is located by default at `    ./aap_install.log` . You can change the log file location within the `    ansible.cfg` file in the installation directory.
1. Enable task profiling callbacks on an ad hoc basis to give an overview of where the installation program spends the most time. To do this, use the local `    ansible.cfg` file. Add a callback line under the `    [defaults]` section, for example:


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
fatal: [ec2-13-48-25-168.eu-north-1.compute.amazonaws.com]: FAILED! =&gt; {"changed": false, "msg": "Can't create container receptor", "stderr": "Error: creating container storage: creating an ID-mapped copy of layer \"98955f43cc908bd50ff43585fec2c7dd9445eaf05eecd1e3144f93ffc00ed4ba\": error during chown: storage-chown-by-maps: lchown usr/local/lib/python3.9/site-packages/azure/mgmt/network/v2019_11_01/operations/__pycache__/_available_service_aliases_operations.cpython-39.pyc: no space left on device: exit status 1\n", "stderr_lines": ["Error: creating container storage: creating an ID-mapped copy of layer \"98955f43cc908bd50ff43585fec2c7dd9445eaf05eecd1e3144f93ffc00ed4ba\": error during chown: storage-chown-by-maps: lchown usr/local/lib/python3.9/site-packages/azure/mgmt/network/v2019_11_01/operations/__pycache__/_available_service_aliases_operations.cpython-39.pyc: no space left on device: exit status 1"], "stdout": "", "stdout_lines": []}
```

If you are installing a `/home` filesystem into a default Amazon Web Services marketplace RHEL instance, it might be too small since `/home` is part of the root `/` filesystem. To resolve this issue you must make more space available. For more information about the system requirements, see [System requirements](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/preparing-containerized-installation#system-requirements) .

**"Install container tools" task fails due to unavailable packages**

This error can be seen in the installation process output as the following:

```
TASK [ansible.containerized_installer.common : Install container tools] **********************************************************************************************************
fatal: [192.0.2.1]: FAILED! =&gt; {"changed": false, "failures": ["No package crun available.", "No package podman available.", "No package slirp4netns available.", "No package fuse-overlayfs available."], "msg": "Failed to install some of the specified packages", "rc": 1, "results": []}
fatal: [192.0.2.2]: FAILED! =&gt; {"changed": false, "failures": ["No package crun available.", "No package podman available.", "No package slirp4netns available.", "No package fuse-overlayfs available."], "msg": "Failed to install some of the specified packages", "rc": 1, "results": []}
fatal: [192.0.2.3]: FAILED! =&gt; {"changed": false, "failures": ["No package crun available.", "No package podman available.", "No package slirp4netns available.", "No package fuse-overlayfs available."], "msg": "Failed to install some of the specified packages", "rc": 1, "results": []}
fatal: [192.0.2.4]: FAILED! =&gt; {"changed": false, "failures": ["No package crun available.", "No package podman available.", "No package slirp4netns available.", "No package fuse-overlayfs available."], "msg": "Failed to install some of the specified packages", "rc": 1, "results": []}
fatal: [192.0.2.5]: FAILED! =&gt; {"changed": false, "failures": ["No package crun available.", "No package podman available.", "No package slirp4netns available.", "No package fuse-overlayfs available."], "msg": "Failed to install some of the specified packages", "rc": 1, "results": []}
```

To fix this error, run the following command on the target hosts:

```
sudo subscription-manager register
```

## A.4. Troubleshooting containerized Ansible Automation Platform configuration




Use this information to troubleshoot your containerized Ansible Automation Platform configuration.

**Sometimes the post install for seeding my Ansible Automation Platform content errors out**

This could manifest itself as output similar to this:

```
TASK [infra.controller_configuration.projects : Configure Controller Projects | Wait for finish the projects creation] ***************************************
Friday 29 September 2023  11:02:32 +0100 (0:00:00.443)       0:00:53.521 ******
FAILED - RETRYING: [daap1.lan]: Configure Controller Projects | Wait for finish the projects creation (1 retries left).
failed: [daap1.lan] (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '536962174348.33944', 'results_file': '/home/aap/.ansible_async/536962174348.33944', 'changed': False, '__controller_project_item': {'name': 'AAP Config-As-Code Examples', 'organization': 'Default', 'scm_branch': 'main', 'scm_clean': 'no', 'scm_delete_on_update': 'no', 'scm_type': 'git', 'scm_update_on_launch': 'no', 'scm_url': 'https://github.com/user/repo.git'}, 'ansible_loop_var': '__controller_project_item'}) =&gt; {"__projects_job_async_results_item": {"__controller_project_item": {"name": "AAP Config-As-Code Examples", "organization": "Default", "scm_branch": "main", "scm_clean": "no", "scm_delete_on_update": "no", "scm_type": "git", "scm_update_on_launch": "no", "scm_url": "https://github.com/user/repo.git"}, "ansible_job_id": "536962174348.33944", "ansible_loop_var": "__controller_project_item", "changed": false, "failed": 0, "finished": 0, "results_file": "/home/aap/.ansible_async/536962174348.33944", "started": 1}, "ansible_job_id": "536962174348.33944", "ansible_loop_var": "__projects_job_async_results_item", "attempts": 30, "changed": false, "finished": 0, "results_file": "/home/aap/.ansible_async/536962174348.33944", "started": 1, "stderr": "", "stderr_lines": [], "stdout": "", "stdout_lines": []}
```

The `infra.controller_configuration.dispatch` role uses an asynchronous loop with 30 retries to apply each configuration type, and the default delay between retries is 1 second. If the configuration is large, this might not be enough time to apply everything before the last retry occurs.

Increase the retry delay by setting the `controller_configuration_async_delay` variable to 2 seconds for example. You can set this variable in the `[all:vars]` section of the installation program inventory file.

Re-run the installation program to ensure everything works as expected.

## A.5. Containerized Ansible Automation Platform reference




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

Control plane services run with the standard Podman configuration and can be found in: `~/.local/share/containers/storage` .

Execution plane services (automation controller, Event-Driven Ansible and execution nodes) use a dedicated configuration found in `~/aap/containers/storage.conf` . This separation prevents execution plane containers from affecting the control plane services.

You can view the execution plane configuration with one of the following commands:

```
CONTAINERS_STORAGE_CONF=~/aap/containers/storage.conf podman &lt;subcommand&gt;
```

```
CONTAINER_HOST=unix://run/user/&lt;user uid&gt;/podman/podman.sock podman &lt;subcommand&gt;
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

The container volume storage is under the local user at `$HOME/.local/share/containers/storage/volumes` .

1. To view the details of each volume, run the following command:


```
$ podman volume ls
```


1. Run the following command to display detailed information about a specific volume:


```
$ podman volume inspect &lt;volume_name&gt;
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
89e779b81b83	run-postgresql	postgresql    4c33cc77ef7d	run-redis	redis    3d8a028d892d	/usr/bin/receptor...	receptor    09821701645c	/usr/bin/launch_a...	automation-controller-rsyslog    a2ddb5cac71b	/usr/bin/launch_a...	automation-controller-task    fa0029a3b003	/usr/bin/launch_a...	automation-controller-web    20f192534691	gunicorn --bind 1...	automation-eda-api    f49804c7e6cb	daphne -b 127.0.0...	automation-eda-daphne    d340b9c1cb74	/bin/sh -c nginx ...	automation-eda-web    111f47de5205	aap-eda-manage rq...	automation-eda-worker-1    171fcb1785af	aap-eda-manage rq...	automation-eda-worker-2    049d10555b51	aap-eda-manage rq...	automation-eda-activation-worker-1    7a78a41a8425	aap-eda-manage rq...	automation-eda-activation-worker-2    da9afa8ef5e2	aap-eda-manage sc...	automation-eda-scheduler    8a2958be9baf	gunicorn --name p...	automation-hub-api    0a8b57581749	gunicorn --name p...	automation-hub-content    68005b987498	nginx -g daemon o...	automation-hub-web    cb07af77f89f	pulpcore-worker	automation-hub-worker-1    a3ba05136446	pulpcore-worker	automation-hub-worker-2
```


1. Run the following command:


```
$ podman inspect &lt;container_name&gt; | jq -r .[].Mounts[].Source
```

Example output:


```
/home/aap/.local/share/containers/storage/volumes/receptor_run/_data    /home/aap/.local/share/containers/storage/volumes/redis_run/_data    /home/aap/aap/controller/data/rsyslog    /home/aap/aap/controller/etc/tower.key    /home/aap/aap/controller/etc/conf.d/callback_receiver_workers.py    /home/aap/aap/controller/data/job_execution    /home/aap/aap/controller/nginx/etc/controller.conf    /home/aap/aap/controller/etc/conf.d/subscription_usage_model.py    /home/aap/aap/controller/etc/conf.d/cluster_host_id.py    /home/aap/aap/controller/etc/conf.d/insights.py    /home/aap/aap/controller/rsyslog/run    /home/aap/aap/controller/data/projects    /home/aap/aap/controller/etc/settings.py    /home/aap/aap/receptor/etc/receptor.conf    /home/aap/aap/controller/etc/conf.d/execution_environments.py    /home/aap/aap/tls/extracted    /home/aap/aap/controller/supervisor/run    /home/aap/aap/controller/etc/uwsgi.ini    /home/aap/aap/controller/etc/conf.d/container_groups.py    /home/aap/aap/controller/etc/launch_awx_task.sh    /home/aap/aap/controller/etc/tower.cert
```


1. If the `    jq` RPM is not installed, install it by running the following command:


```
$ sudo dnf -y install jq
```




# Appendix B. Inventory file variables




The following tables contain information about the variables used in Ansible Automation Platform’s installation `inventory` files. The tables include the variables that you can use for RPM-based installation and container-based installation.

## B.1. Ansible variables




The following variables control how Ansible Automation Platform interacts with remote hosts.


<span id="idm140279432947840"></span>
**Table B.1. Ansible variables**

| Variable | Description |
| --- | --- |
|  `ansible_connection` | The connection plugin used for the task on the target host. This can be the name of any Ansible connection plugin.

SSH protocol types are `smart` , `ssh` , or `paramiko` . You can also use `local` to run tasks on the control node itself.

Default = `smart` |
|  `ansible_host` | The IP address or name of the target host to use instead of `inventory_hostname` . |
|  `ansible_password` | The password to authenticate to the host.

Do not store this variable in plain text. Always use a vault. |
|  `ansible_port` | The connection port number.

The default for SSH is `22` . |
|  `ansible_scp_extra_args` | This setting is always appended to the default `scp` command line. |
|  `ansible_sftp_extra_args` | This setting is always appended to the default `sftp` command line. |
|  `ansible_shell_executable` | This sets the shell that the Ansible controller uses on the target machine and overrides the executable in `ansible.cfg` which defaults to `/bin/sh` . |
|  `ansible_shell_type` | The shell type of the target system.

Do not use this setting unless you have set the `ansible_shell_executable` to a non-Bourne (sh) compatible shell. By default commands are formatted using sh-style syntax. Setting this to `csh` or `fish` causes commands executed on target systems to follow the syntax of those shells instead. |
|  `ansible_ssh_common_args` | This setting is always appended to the default command line for `sftp` , `scp` , and `ssh` . Useful to configure a `ProxyCommand` for a certain host or group. |
|  `ansible_ssh_executable` | This setting overrides the default behavior to use the system `ssh` . This can override the `ssh_executable` setting in `ansible.cfg` . |
|  `ansible_ssh_extra_args` | This setting is always appended to the default `ssh` command line. |
|  `ansible_ssh_pipelining` | Determines if SSH `pipelining` is used.

This can override the `pipelining` setting in `ansible.cfg` . If using SSH key-based authentication, the key must be managed by an SSH agent. |
|  `ansible_ssh_private_key_file` | Private key file used by SSH.

Useful if using multiple keys and you do not want to use an SSH agent. |
|  `ansible_user` | The user name to use when connecting to the host.

Do not change this variable unless `/bin/sh` is not installed on the target machine or cannot be run from sudo. |
|  `inventory_hostname` | This variable takes the hostname of the machine from the inventory script or the Ansible configuration file. You cannot set the value of this variable. Because the value is taken from the configuration file, the actual runtime hostname value can vary from what is returned by this variable. |




**Additional resources**

-  [Reviewing your Ansible configuration with automation content navigator](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_content_navigator/assembly-review-config-navigator_installing-devtools)


## B.2. Automation hub variables




Inventory file variables for automation hub.

| RPM variable name | Container variable name | Description | Required or optional | Default |
| --- | --- | --- | --- | --- |
|  `automationhub_admin_password` |  `hub_admin_password` | Automation hub administrator password. Use of special characters for this variable is limited. The password can include any printable ASCII character except `/` , `”` , or `@` . | Required |  |
|  `automationhub_api_token` |  | Set the existing token for the installation program. For example, a regenerated token in the automation hub UI will invalidate an existing token. Use this variable to set that token in the installation program the next time you run the installation program. | Optional |  |
|  `automationhub_auto_sign_collections` |  `hub_collection_auto_sign` | If a collection signing service is enabled, collections are not signed automatically by default. Set this variable to `true` to sign collections by default. | Optional |  `false` |
|  `automationhub_backup_collections` |  | Ansible automation hub provides artifacts in `/var/lib/pulp` . These artifacts are automatically backed up by default. Set this variable to `false` to prevent backup or restore of `/var/lib/pulp` . | Optional |  `true` |
|  `automationhub_client_max_body_size` |  `hub_nginx_client_max_body_size` | Maximum allowed size for data sent to automation hub through NGINX. | Optional |  `20m` |
|  `automationhub_collection_download_count` |  | Denote whether or not the collection download count should be displayed in the UI. | Optional |  `false` |
|  `automationhub_collection_seed_repository` |  | Controls the type of content to upload when `hub_seed_collections` is set to `true` . Valid options include: `certified` , `validated` | Optional | Both certified and validated are enabled by default. |
|  `automationhub_collection_signing_service_key` |  `hub_collection_signing_key` | Path to the collection signing key file. | Required if a collection signing service is enabled. |  |
|  `automationhub_container_repair_media_type` |  | Denote whether or not to run the command `pulpcore-manager container-repair-media-type` . Valid options include: `true` , `false` , `auto` | Optional |  `auto` |
|  `automationhub_container_signing_service_key` |  `hub_container_signing_key` | Path to the container signing key file. | Required if a container signing service is enabled. |  |
|  `automationhub_create_default_collection_signing_service` |  `hub_collection_signing` | Set this variable to `true` to enable a collection signing service. | Optional |  `false` |
|  `automationhub_create_default_container_signing_service` |  `hub_container_signing` | Set this variable to `true` to enable a container signing service. | Optional |  `false` |
|  |  `hub_data_path_exclude` | automation hub backup path to exclude. | Optional |  `[]` |
|  `automationhub_disable_hsts` |  `hub_nginx_disable_hsts` | Controls whether HTTP Strict Transport Security (HSTS) is enabled or disabled for automation hub. Set this variable to `true` to disable HSTS. | Optional |  `false` |
|  `automationhub_disable_https` |  `hub_nginx_disable_https` | Controls whether HTTPS is enabled or disabled for automation hub. Set this variable to `true` to disable HTTPS. | Optional |  `false` |
|  `automationhub_enable_api_access_log` |  | Controls whether logging is enabled or disabled at `/var/log/galaxy_api_access.log` . The file logs all user actions made to the platform, including username and IP address. Set this variable to `true` to enable this logging. | Optional |  `false` |
|  `automationhub_enable_unauthenticated_collection_access` |  | Controls whether read-only access is enabled or disabled for unauthorized users viewing collections or namespaces for automation hub. Set this variable to `true` to enable read-only access. | Optional |  `false` |
|  `automationhub_enable_unauthenticated_collection_download` |  | Controls whether or not unauthorized users can download read-only collections from automation hub. Set this variable to `true` to enable download of read-only collections. | Optional |  `false` |
|  `automationhub_firewalld_zone` |  `hub_firewall_zone` | The firewall zone where automation hub related firewall rules are applied. This controls which networks can access automation hub based on the zone’s trust level. | Optional | RPM = no default set. Container = `public` . |
|  `automationhub_force_change_admin_password` |  | Denote whether or not to require the change of the default administrator password for automation hub during installation. Set to `true` to require the user to change the default administrator password during installation. | Optional |  `false` |
|  `automationhub_importer_settings` |  `hub_galaxy_importer` | Dictionary of settings to pass to the `galaxy-importer.cfg` configuration file. These settings control how the `galaxy-importer` service processes and validates Ansible content. Example values include: `ansible-doc` , `ansible-lint` , and `flake8` . | Optional |  |
|  `automationhub_nginx_tls_files_remote` |  | Denote whether the web certificate sources are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional | The value defined in `automationhub_tls_files_remote` . |
|  `automationhub_pg_cert_auth` |  `hub_pg_cert_auth` | Controls whether client certificate authentication is enabled or disabled on the automation hub PostgreSQL database. Set this variable to `true` to enable client certificate authentication. | Optional |  `false` |
|  `automationhub_pg_database` |  `hub_pg_database` | Name of the PostgreSQL database used by automation hub. | Optional | RPM = `automationhub` . Container = `pulp` |
|  `automationhub_pg_host` |  `hub_pg_host` | Hostname of the PostgreSQL database used by automation hub. | Required | RPM = `127.0.0.1` . Container = no default. |
|  `automationhub_pg_password` |  `hub_pg_password` | Password for the automation hub PostgreSQL database user. Use of special characters for this variable is limited. The `!` , `#` , `0` and `@` characters are supported. Use of other special characters can cause the setup to fail. | Optional |  |
|  `automationhub_pg_port` |  `hub_pg_port` | Port number for the PostgreSQL database used by automation hub. | Optional |  `5432` |
|  `automationhub_pg_sslmode` |  `hub_pg_sslmode` | Controls the SSL/TLS mode to use when automation hub connects to the PostgreSQL database. Valid options include `verify-full` , `verify-ca` , `require` , `prefer` , `allow` , `disable` . | Optional |  `prefer` |
|  `automationhub_pg_username` |  `hub_pg_username` | Username for the automation hub PostgreSQL database user. | Optional | RPM = `automationhub` . Container = `pulp` . |
|  `automationhub_pgclient_sslcert` |  `hub_pg_tls_cert` | Path to the PostgreSQL SSL/TLS certificate file for automation hub. | Required if using client certificate authentication. |  |
|  `automationhub_pgclient_sslkey` |  `hub_pg_tls_key` | Path to the PostgreSQL SSL/TLS key file for automation hub. | Required if using client certificate authentication. |  |
|  `automationhub_pgclient_tls_files_remote` |  | Denote whether the PostgreSQL client certificate sources are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional | The value defined in `automationhub_tls_files_remote` . |
|  `automationhub_require_content_approval` |  | Controls whether content signing is enabled or disabled for automation hub. By default when you upload collections to automation hub, an administrator must approve it before they are made available to users. To disable the content approval flow, set the variable to `false` . | Optional |  `true` |
|  `automationhub_restore_signing_keys` |  | Controls whether or not existing signing keys should be restored from a backup. Set to `false` to disable restoration of existing signing keys. | Optional |  `true` |
|  `automationhub_seed_collections` |  `hub_seed_collections` | Controls whether or not pre-loading of collections is enabled. When you run the bundle installer, validated content is uploaded to the `validated` repository, and certified content is uploaded to the `rh-certified` repository. By default, certified content and validated content are both uploaded. If you do not want to pre-load content, set this variable to `false` . For the RPM-based installer, if you only want one type of content, set this variable to `true` and set the `automationhub_collection_seed_repository` variable to the type of content you want to include. | Optional |  `true` |
|  `automationhub_ssl_cert` |  `hub_tls_cert` | Path to the SSL/TLS certificate file for automation hub. | Optional |  |
|  `automationhub_ssl_key` |  `hub_tls_key` | Path to the SSL/TLS key file for automation hub. | Optional |  |
|  `automationhub_tls_files_remote` |  `hub_tls_remote` | Denote whether the automation hub provided certificate files are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional |  `false` |
|  `automationhub_use_archive_compression` |  `hub_use_archive_compression` | Controls whether archive compression is enabled or disabled for automation hub. You can control this functionality globally by using `use_archive_compression` . | Optional |  `true` |
|  `automationhub_use_db_compression` |  `hub_use_db_compression` | Controls whether database compression is enabled or disabled for automation hub. You can control this functionality globally by using `use_db_compression` . | Optional |  `true` |
|  `automationhub_user_headers` |  `hub_nginx_user_headers` | List of additional NGINX headers to add to automation hub’s NGINX configuration. | Optional |  `[]` |
|  `ee_from_hub_only` |  | Controls whether automation hub is the only registry for execution environment images. If set to `true` , automation hub is the exclusive registry. If set to `false` , images are also pulled directly from Red Hat. | Optional |  `true` when using the bundle installer, otherwise `false` . |
|  `generate_automationhub_token` |  | Controls whether or not a token is generated for automation hub during installation. By default, a token is automatically generated during a fresh installation. If set to `true` , a token is regenerated during installation. | Optional |  `false` |
|  |  `hub_extra_settings` | Defines additional settings for use by automation hub during installation.

For example:

```
hub_extra_settings=[{"setting": "REDIRECT_IS_HTTPS", "value": True}]
``` | Optional |  `[]` |
|  `nginx_hsts_max_age` |  `hub_nginx_hsts_max_age` | Maximum duration (in seconds) that HTTP Strict Transport Security (HSTS) is enforced for automation hub. | Optional |  `63072000` |
|  `pulp_secret` |  `hub_secret_key` | Secret key value used by automation hub to sign and encrypt data. | Optional |  |
|  |  `hub_azure_account_key` | Azure blob storage account key. | Required if using an Azure blob storage backend. |  |
|  |  `hub_azure_account_name` | Account name associated with the Azure blob storage. | Required when using an Azure blob storage backend. |  |
|  |  `hub_azure_container` | Name of the Azure blob storage container. | Optional |  `pulp` |
|  |  `hub_azure_extra_settings` | Defines extra parameters for the Azure blob storage backend. For more information about the list of parameters, see [django-storages documentation - Azure Storage](https://django-storages.readthedocs.io/en/latest/backends/azure.html#settings) . | Optional |  `{}` |
|  |  `hub_collection_signing_pass` | Password for the automation content collection signing service. | Required if the collection signing service is protected by a passphrase. |  |
|  |  `hub_collection_signing_service` | Service for signing collections. | Optional |  `ansible-default` |
|  |  `hub_container_signing_pass` | Password for the automation content container signing service. | Required if the container signing service is protected by a passphrase. |  |
|  |  `hub_container_signing_service` | Service for signing containers. | Optional |  `container-default` |
|  |  `hub_nginx_http_port` | Port number that automation hub listens on for HTTP requests. | Optional |  `8081` |
|  |  `hub_nginx_https_port` | Port number that automation hub listens on for HTTPS requests. | Optional |  `8444` |
|  `nginx_tls_protocols` |  `hub_nginx_https_protocols` | Protocols that automation hub will support when handling HTTPS traffic. | Optional |  `[TLSv1.2, TLSv1.3]` |
|  |  `hub_pg_socket` | UNIX socket used by automation hub to connect to the PostgreSQL database. | Optional |  |
|  |  `hub_s3_access_key` | AWS S3 access key. | Required if using an AWS S3 storage backend. |  |
|  |  `hub_s3_bucket_name` | Name of the AWS S3 storage bucket. | Optional |  `pulp` |
|  |  `hub_s3_extra_settings` | Used to define extra parameters for the AWS S3 storage backend. For more information about the list of parameters, see [django-storages documentation - Amazon S3](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings) . | Optional |  `{}` |
|  |  `hub_s3_secret_key` | AWS S3 secret key. | Required if using an AWS S3 storage backend. |  |
|  |  `hub_shared_data_mount_opts` | Mount options for the Network File System (NFS) share. | Optional |  `rw,sync,hard` |
|  |  `hub_shared_data_path` | Path to the Network File System (NFS) share with read, write, and execute (RWX) access. The value must match the format `host:dir` , for example `nfs-server.example.com:/exports/hub` . | Required if installing more than one instance of automation hub with a `file` storage backend. When installing a single instance of automation hub, it is optional. |  |
|  |  `hub_storage_backend` | Automation hub storage backend type. Possible values include: `azure` , `file` , `s3` . | Optional |  `file` |
|  |  `hub_workers` | Number of automation hub workers. | Optional |  `2` |


## B.3. Automation controller variables




Inventory file variables for automation controller.

| RPM variable name | Container variable name | Description | Required or optional | Default |
| --- | --- | --- | --- | --- |
|  `admin_email` |  `controller_admin_email` | Email address used by Django for the admin user for automation controller. | Optional |  `admin@example.com` |
|  `admin_password` |  `controller_admin_password` | Automation controller administrator password. Use of special characters for this variable is limited. The password can include any printable ASCII character except `/` , `”` , or `@` . | Required |  |
|  `admin_username` |  `controller_admin_user` | Username used to identify and create the administrator user in automation controller. | Optional |  `admin` |
|  `automationcontroller_client_max_body_size` |  `controller_nginx_client_max_body_size` | Maximum allowed size for data sent to automation controller through NGINX. | Optional |  `5m` |
|  `automationcontroller_use_archive_compression` |  `controller_use_archive_compression` | Controls whether archive compression is enabled or disabled for automation controller. You can control this functionality globally by using `use_archive_compression` . | Optional |  `true` |
|  `automationcontroller_use_db_compression` |  `controller_use_db_compression` | Controls whether database compression is enabled or disabled for automation controller. You can control this functionality globally by using `use_db_compression` . | Optional |  `true` |
|  `awx_pg_cert_auth` |  `controller_pg_cert_auth` | Controls whether client certificate authentication is enabled or disabled on the automation controller PostgreSQL database. Set this variable to `true` to enable client certificate authentication. | Optional |  `false` |
|  `controller_firewalld_zone` |  `controller_firewall_zone` | The firewall zone where automation controller related firewall rules are applied. This controls which networks can access automation controller based on the zone’s trust level. | Optional |  `public` |
|  `controller_nginx_tls_files_remote` |  | Denote whether the web certificate sources are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional | The value defined in `controller_tls_files_remote` . |
|  `controller_pgclient_tls_files_remote` |  | Denote whether the PostgreSQL client certificate sources are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional | The value defined in `controller_tls_files_remote` . |
|  `controller_tls_files_remote` |  `controller_tls_remote` | Denote whether the automation controller provided certificate files are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional |  `false` |
|  `nginx_disable_hsts` |  `controller_nginx_disable_hsts` | Controls whether HTTP Strict Transport Security (HSTS) is enabled or disabled for automation controller. Set this variable to `true` to disable HSTS. | Optional |  `false` |
|  `nginx_disable_https` |  `controller_nginx_disable_https` | Controls whether HTTPS is enabled or disabled for automation controller. Set this variable to `true` to disable HTTPS. | Optional |  `false` |
|  `nginx_hsts_max_age` |  `controller_nginx_hsts_max_age` | Maximum duration (in seconds) that HTTP Strict Transport Security (HSTS) is enforced for automation controller. | Optional |  `63072000` |
|  `nginx_http_port` |  `controller_nginx_http_port` | Port number that automation controller listens on for HTTP requests. | Optional | RPM = `80` . Container = `8080` |
|  `nginx_https_port` |  `controller_nginx_https_port` | Port number that automation controller listens on for HTTPS requests. | Optional | RPM = `443` . Container = `8443` |
|  `nginx_tls_protocols` |  `controller_nginx_https_protocols` | Protocols that automation controller supports when handling HTTPS traffic. | Optional |  `[TLSv1.2, TLSv1.3]` |
|  `nginx_user_headers` |  `controller_nginx_user_headers` | List of additional NGINX headers to add to automation controller’s NGINX configuration. | Optional |  `[]` |
|  |  `controller_create_preload_data` | Controls whether or not to create preloaded content during installation. | Optional |  `true` |
|  `node_state` |  | The status of a node or group of nodes. Valid options include `active` , `deprovision` to remove a node from a cluster, or `iso_migrate` to migrate a legacy isolated node to an execution node. | Optional |  `active` |
|  `node_type` | See `receptor_type` for the container equivalent variable. | For the `[automationcontroller]` group the two options are:

-  `    node_type=control` - The node only runs project and inventory updates, but not regular jobs.
-  `    node_type=hybrid` - The node runs everything.


For the `[execution_nodes]` group the two options are:

-  `    node_type=hop` - The node forwards jobs to an execution node.
-  `    node_type=execution` - The node can run jobs. | Optional | For `[automationcontroller]` = `hybrid` , for `[execution_nodes]` = `execution` |
|  `peers` | See `receptor_peers` for the container equivalent variable. | Used to indicate which nodes a specific host or group connects to. Wherever this variable is defined, an outbound connection to the specific host or group is established. This variable can be a comma-separated list of hosts and groups from the inventory. This is resolved into a set of hosts that is used to construct the `receptor.conf` file. | Optional |  |
|  `pg_database` |  `controller_pg_database` | Name of the PostgreSQL database used by automation controller. | Optional |  `awx` |
|  `pg_host` |  `controller_pg_host` | Hostname of the PostgreSQL database used by automation controller. | Required |  |
|  `pg_password` |  `controller_pg_password` | Password for the automation controller PostgreSQL database user. Use of special characters for this variable is limited. The `!` , `#` , `0` and `@` characters are supported. Use of other special characters can cause the setup to fail. | Required if not using client certificate authentication. |  |
|  `pg_port` |  `controller_pg_port` | Port number for the PostgreSQL database used by automation controller. | Optional |  `5432` |
|  `pg_sslmode` |  `controller_pg_sslmode` | Controls the SSL/TLS mode to use when automation controller connects to the PostgreSQL database. Valid options include `verify-full` , `verify-ca` , `require` , `prefer` , `allow` , `disable` . | Optional |  `prefer` |
|  `pg_username` |  `controller_pg_username` | Username for the automation controller PostgreSQL database user. | Optional |  `awx` |
|  `pgclient_sslcert` |  `controller_pg_tls_cert` | Path to the PostgreSQL SSL/TLS certificate file for automation controller. | Required if using client certificate authentication. |  |
|  `pgclient_sslkey` |  `controller_pg_tls_key` | Path to the PostgreSQL SSL/TLS key file for automation controller. | Required if using client certificate authentication. |  |
|  `precreate_partition_hours` |  | Number of hours worth of events table partitions to pre-create before starting a backup to avoid `pg_dump` locks. | Optional | 3 |
|  `uwsgi_listen_queue_size` |  `controller_uwsgi_listen_queue_size` | Number of requests `uwsgi` allows in the queue on automation controller until `uwsgi_processes` can serve them. | Optional |  `2048` |
|  `web_server_ssl_cert` |  `controller_tls_cert` | Path to the SSL/TLS certificate file for automation controller. | Optional |  |
|  `web_server_ssl_key` |  `controller_tls_key` | Path to the SSL/TLS key file for automation controller. | Optional |  |
|  |  `controller_event_workers` | Number of event workers that handle job-related events inside automation controller. | Optional |  `4` |
|  |  `controller_extra_settings` | Defines additional settings for use by automation controller during installation.

For example:

```
controller_extra_settings=[{"setting": "USE_X_FORWARDED_HOST", "value": True}]
``` | Optional |  `[]` |
|  |  `controller_license_file` | Path to the automation controller license file. |  |  |
|  |  `controller_percent_memory_capacity` | Memory allocation for automation controller. | Optional |  `1.0` (allocates 100% of the total system memory to automation controller) |
|  |  `controller_pg_socket` | UNIX socket used by automation controller to connect to the PostgreSQL database. | Optional |  |
|  |  `controller_secret_key` | Secret key value used by automation controller to sign and encrypt data. | Optional |  |


## B.4. Database variables




Inventory file variables for the database used with Ansible Automation Platform.

| RPM variable name | Container variable name | Description | Required or optional | Default |
| --- | --- | --- | --- | --- |
|  `install_pg_port` |  `postgresql_port` | Port number for the PostgreSQL database. | Optional |  `5432` |
|  `postgres_extra_settings` |  `postgresql_extra_settings` | Defines additional settings for use by PostgreSQL.

Example usage for RPM:

```
postgresql_extra_settings={'ssl_ciphers': 'HIGH:!aNULL:!MD5'}
```

Example usage for containerized:

```
postgresql_extra_settings=[{"setting": "ssl_ciphers", "value": "HIGH:!aNULL:!MD5"}]
``` | Optional |  |
|  `postgres_firewalld_zone` |  `postgresql_firewall_zone` | The firewall zone where PostgreSQL related firewall rules are applied. This controls which networks can access PostgreSQL based on the zone’s trust level. | Optional | RPM = no default set. Container = `public` . |
|  `postgres_max_connections` |  `postgresql_max_connections` | Maximum number of concurrent connections to the database if you are using an installer-managed database. For more information see [PostgreSQL database configuration and maintenance for automation controller](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/configuring_automation_execution/assembly-controller-improving-performance#ref-controller-database-settings) . | Optional |  `1024` |
|  `postgres_ssl_cert` |  `postgresql_tls_cert` | Path to the PostgreSQL SSL/TLS certificate file. | Optional |  |
|  `postgres_ssl_key` |  `postgresql_tls_key` | Path to the PostgreSQL SSL/TLS key file. | Optional |  |
|  `postgres_use_ssl` |  `postgresql_disable_tls` | Controls whether SSL/TLS is enabled or disabled for the PostgreSQL database. | Optional |  `false` |
|  |  `postgresql_admin_database` | Database name used for connections to the PostgreSQL database server. | Optional |  `postgres` |
|  |  `postgresql_admin_password` | Password for the PostgreSQL admin user. When used, the installation program creates each component’s database and credentials. | Required if using `postgresql_admin_username` . |  |
|  |  `postgresql_admin_username` | Username for the PostgreSQL admin user. When used, the installation program creates each component’s database and credentials. | Optional |  `postgres` |
|  |  `postgresql_effective_cache_size` | Memory allocation available (in MB) for caching data. | Optional |  |
|  |  `postgresql_keep_databases` | Controls whether or not to keep databases during uninstall. This variable applies to databases managed by the installation program only, and not external (customer-managed) databases. Set to `true` to keep databases during uninstall. | Optional |  `false` |
|  |  `postgresql_log_destination` | Destination for server log output. | Optional |  `/dev/stderr` |
|  |  `postgresql_password_encryption` | The algorithm for encrypting passwords. | Optional |  `scram-sha-256` |
|  |  `postgresql_shared_buffers` | Memory allocation (in MB) for shared memory buffers. | Optional |  |
|  |  `postgresql_tls_remote` | Denote whether the PostgreSQL provided certificate files are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional |  `false` |
|  |  `postgresql_use_archive_compression` | Controls whether archive compression is enabled or disabled for PostgreSQL. You can control this functionality globally by using `use_archive_compression` . | Optional |  `true` |


## B.5. Event-Driven Ansible controller variables




Inventory file variables for Event-Driven Ansible controller.

| RPM variable name | Container variable name | Description | Required or optional | Default |
| --- | --- | --- | --- | --- |
|  `automationedacontroller_activation_workers` |  `eda_activation_workers` | Number of workers used for ansible-rulebook activation pods in Event-Driven Ansible. | Optional | RPM = (# of cores or threads) * 2 + 1. Container = `2` |
|  `automationedacontroller_admin_email` |  `eda_admin_email` | Email address used by Django for the admin user for Event-Driven Ansible. | Optional |  `admin@example.com` |
|  `automationedacontroller_admin_password` |  `eda_admin_password` | Event-Driven Ansible administrator password. Use of special characters for this variable is limited. The password can include any printable ASCII character except `/` , `”` , or `@` . | Required |  |
|  `automationedacontroller_admin_username` |  `eda_admin_user` | Username used to identify and create the administrator user in Event-Driven Ansible. | Optional |  `admin` |
|  `automationedacontroller_backend_gunicorn_workers` |  | Number of workers for handling the API served through Gunicorn on worker nodes. | Optional |  `2` |
|  `automationedacontroller_cache_tls_files_remote` |  | Denote whether the cache cert sources are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional |  `false` |
|  `automationedacontroller_client_regen_cert` |  | Controls whether or not to regenerate Event-Driven Ansible client certificates for the platform cache. Set to `true` to regenerate Event-Driven Ansible client certificates. | Optional |  `false` |
|  `automationedacontroller_default_workers` |  `eda_workers` | Number of workers used in Event-Driven Ansible for application work. | Optional | Number of cores or threads |
|  `automationedacontroller_disable_hsts` |  `eda_nginx_disable_hsts` | Controls whether HTTP Strict Transport Security (HSTS) is enabled or disabled for Event-Driven Ansible. Set this variable to `true` to disable HSTS. | Optional |  `false` |
|  `automationedacontroller_disable_https` |  `eda_nginx_disable_https` | Controls whether HTTPS is enabled or disabled for Event-Driven Ansible. Set this variable to `true` to disable HTTPS. | Optional |  `false` |
|  `automationedacontroller_event_stream_mtls` |  `eda_event_stream_mtls` | Controls whether event stream mutual TLS (mTLS) authentication is enabled or disabled for Event-Driven Ansible. Set this variable to `false` to disable mTLS authentication. | Optional |  `true` |
|  `automationedacontroller_event_stream_mtls_path` |  `eda_event_stream_mtls_prefix_path` | The prefix path for the event stream mTLS URLs. | Optional |  `/mtls/eda-event-streams` |
|  `automationedacontroller_event_stream_path` |  `eda_event_stream_prefix_path` | API prefix path used for Event-Driven Ansible event-stream through platform gateway. | Optional |  `/eda-event-streams` |
|  `automationedacontroller_firewalld_zone` |  `eda_firewall_zone` | The firewall zone where Event-Driven Ansible related firewall rules are applied. This controls which networks can access Event-Driven Ansible based on the zone’s trust level. | Optional | RPM = no default set. Container = `public` . |
|  `automationedacontroller_gunicorn_event_stream_workers` |  | Number of workers for handling event streaming for Event-Driven Ansible. | Optional |  `2` |
|  `automationedacontroller_gunicorn_workers` |  `eda_gunicorn_workers` | Number of workers for handling the API served through Gunicorn. | Optional | (Number of cores or threads) * 2 + 1 |
|  `automationedacontroller_http_port` |  `eda_nginx_http_port` | Port number that Event-Driven Ansible listens on for HTTP requests. | Optional | RPM = `80` . Container = `8082` . |
|  `automationedacontroller_https_port` |  `eda_nginx_https_port` | Port number that Event-Driven Ansible listens on for HTTPS requests. | Optional | RPM = `443` . Container = `8445` . |
|  `automationedacontroller_nginx_tls_files_remote` |  | Denote whether the web cert sources are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional |  `false` |
|  `automationedacontroller_pg_cert_auth` |  `eda_pg_cert_auth` | Controls whether client certificate authentication is enabled or disabled on the Event-Driven Ansible PostgreSQL database. Set this variable to `true` to enable client certificate authentication. | Optional |  `false` |
|  `automationedacontroller_pg_database` |  `eda_pg_database` | Name of the PostgreSQL database used by Event-Driven Ansible. | Optional | RPM = `automationedacontroller` . Container = `eda` . |
|  `automationedacontroller_pg_host` |  `eda_pg_host` | Hostname of the PostgreSQL database used by Event-Driven Ansible. | Required |  |
|  `automationedacontroller_pg_password` |  `eda_pg_password` | Password for the Event-Driven Ansible PostgreSQL database user. Use of special characters for this variable is limited. The `!` , `#` , `0` and `@` characters are supported. Use of other special characters can cause the setup to fail. | Required if not using client certificate authentication. |  |
|  `automationedacontroller_pg_port` |  `eda_pg_port` | Port number for the PostgreSQL database used by Event-Driven Ansible. | Optional |  `5432` |
|  `automationedacontroller_pg_sslmode` |  `eda_pg_sslmode` | Determines the level of encryption and authentication for client server connections. Valid options include `verify-full` , `verify-ca` , `require` , `prefer` , `allow` , `disable` . | Optional |  `prefer` |
|  `automationedacontroller_pg_username` |  `eda_pg_username` | Username for the Event-Driven Ansible PostgreSQL database user. | Optional | RPM = `automationedacontroller` . Container = `eda` . |
|  `automationedacontroller_pgclient_sslcert` |  `eda_pg_tls_cert` | Path to the PostgreSQL SSL/TLS certificate file for Event-Driven Ansible. | Required if using client certificate authentication. |  |
|  `automationedacontroller_pgclient_sslkey` |  `eda_pg_tls_key` | Path to the PostgreSQL SSL/TLS key file for Event-Driven Ansible. | Required if using client certificate authentication. |  |
|  `automationedacontroller_pgclient_tls_files_remote` |  | Denote whether the PostgreSQL client cert sources are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional |  `false` |
|  `automationedacontroller_public_event_stream_url` |  `eda_event_stream_url` | URL for connecting to the event stream. The URL must start with the `http://` or `https://` prefix | Optional |  |
|  `automationedacontroller_redis_host` |  `eda_redis_host` | Hostname of the Redis host used by Event-Driven Ansible. | Optional | First node in the `[automationgateway]` inventory group |
|  `automationedacontroller_redis_password` |  `eda_redis_password` | Password for Event-Driven Ansible Redis. | Optional | Randomly generated string |
|  `automationedacontroller_redis_port` |  `eda_redis_port` | Port number for the Redis host for Event-Driven Ansible. | Optional | RPM = The value defined in platform gateway’s implementation ( `automationgateway_redis_port` ). Container = `6379` |
|  `automationedacontroller_redis_username` |  `eda_redis_username` | Username for Event-Driven Ansible Redis. | Optional |  `eda` |
|  `automationedacontroller_secret_key` |  `eda_secret_key` | Secret key value used by Event-Driven Ansible to sign and encrypt data. | Optional |  |
|  `automationedacontroller_ssl_cert` |  `eda_tls_cert` | Path to the SSL/TLS certificate file for Event-Driven Ansible. | Optional |  |
|  `automationedacontroller_ssl_key` |  `eda_tls_key` | Path to the SSL/TLS key file for Event-Driven Ansible. | Optional |  |
|  `automationedacontroller_tls_files_remote` |  `eda_tls_remote` | Denote whether the Event-Driven Ansible provided certificate files are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional |  `false` |
|  `automationedacontroller_trusted_origins` |  | List of host addresses in the form: `&lt;scheme&gt;//:&lt;address&gt;:&lt;port&gt;` for trusted Cross-Site Request Forgery (CSRF) origins. | Optional |  `[]` |
|  `automationedacontroller_use_archive_compression` |  `eda_use_archive_compression` | Controls whether archive compression is enabled or disabled for Event-Driven Ansible. You can control this functionality globally by using `use_archive_compression` . | Optional |  `true` |
|  `automationedacontroller_use_db_compression` |  `eda_use_db_compression` | Controls whether database compression is enabled or disabled for Event-Driven Ansible. You can control this functionality globally by using `use_db_compression` . | Optional |  `true` |
|  `automationedacontroller_user_headers` |  `eda_nginx_user_headers` | List of additional NGINX headers to add to Event-Driven Ansible’s NGINX configuration. | Optional |  `[]` |
|  `automationedacontroller_websocket_ssl_verify` |  | Controls whether or not to perform SSL verification for the Daphne WebSocket used by Podman to communicate from the pod to the host. Set to `false` to disable SSL verification. | Optional |  `true` |
|  `eda_node_type` |  `eda_type` | Event-Driven Ansible node type. Valid options include `api` , `event-stream` , `hybrid` , `worker` . | Optional |  `hybrid` |
|  |  `eda_debug` | Controls whether debug mode is enabled or disabled for Event-Driven Ansible. Set to `true` to enable debug mode for Event-Driven Ansible. | Optional |  `false` |
|  |  `eda_extra_settings` | Defines additional settings for use by Event-Driven Ansible during installation.

For example:

```
eda_extra_settings=[{"setting": "RULEBOOK_READINESS_TIMEOUT_SECONDS", "value": 120}]
``` | Optional |  `[]` |
|  |  `eda_nginx_client_max_body_size` | Maximum allowed size for data sent to Event-Driven Ansible through NGINX. | Optional |  `1m` |
|  |  `eda_nginx_hsts_max_age` | Maximum duration (in seconds) that HTTP Strict Transport Security (HSTS) is enforced for Event-Driven Ansible. | Optional |  `63072000` |
|  `nginx_tls_protocols` |  `eda_nginx_https_protocols` | Protocols that Event-Driven Ansible supports when handling HTTPS traffic. | Optional |  `[TLSv1.2, TLSv1.3]` |
|  |  `eda_pg_socket` | UNIX socket used by Event-Driven Ansible to connect to the PostgreSQL database. | Optional |  |
|  `redis_disable_tls` |  `eda_redis_disable_tls` | Controls whether TLS is enabled or disabled for Event-Driven Ansible Redis. Set this variable to true to disable TLS. | Optional |  `false` |
|  |  `eda_redis_tls_cert` | Path to the Event-Driven Ansible Redis certificate file. | Optional |  |
|  |  `eda_redis_tls_key` | Path to the Event-Driven Ansible Redis key file. | Optional |  |
|  |  `eda_safe_plugins` | List of plugins that are allowed to run within Event-Driven Ansible.

For more information, see [Adding a safe plugin variable to Event-Driven Ansible controller](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/advanced-configuration-containerized#proc-add-eda-safe-plugin-var) . | Optional |  `[]` |


## B.6. General variables




General inventory file variables for Ansible Automation Platform.

| RPM variable name | Container variable name | Description | Required or optional | Default |
| --- | --- | --- | --- | --- |
|  `aap_ca_cert_file` |  `ca_tls_cert` | Path to the user-provided CA certificate file. When you specify this variable, the installation program automatically generates TLS certificates for each Ansible Automation Platform service signed by this CA. You do not need to define individual service certificate variables (such as `gateway_tls_cert` , `controller_tls_cert` , or `hub_tls_cert` ). For more information, see [Configuring custom TLS certificates](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/advanced-configuration-containerized#using-custom-tls-certificates) . | Optional |  |
|  `aap_ca_cert_files_remote` |  `ca_tls_remote` | Denote whether the CA certificate files are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional |  `false` |
|  `aap_ca_cert_size` |  | Bit size of the internally managed CA certificate private key. | Optional |  `4096` |
|  `aap_ca_key_file` |  `ca_tls_key` | Path to the key file for the CA certificate provided in `aap_ca_cert_file` (RPM) and `ca_tls_cert` (Container). The installation program uses this key to sign the automatically generated TLS certificates for each Ansible Automation Platform service. For more information, see [Using custom TLS certificates](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/advanced-configuration-containerized#using-custom-tls-certificates) . | Optional |  |
|  `aap_ca_passphrase_cipher` |  | Cipher used for signing the internally managed CA certificate private key. | Optional |  `aes256` |
|  `aap_ca_regenerate` |  | Denotes whether or not to regenerate the internally managed CA certificate key pair. | Optional |  `false` |
|  `aap_service_cert_size` |  | Bit size of the component key pair managed by the internal CA. | Optional |  `4096` |
|  `aap_service_regen_cert` |  | Denotes whether or not to regenerate the component key pair managed by the internal CA. | Optional |  `false` |
|  `aap_service_san_records` |  | A list of additional SAN records for signing a service. Assign these to components in the inventory file as host variables rather than group or all variables. All strings must also contain their corresponding SAN option prefix such as `DNS:` or `IP:` . | Optional |  `[]` |
|  `backup_dest` |  | Directory local to `setup.sh` for the final backup file. | Optional | The value defined in `setup_dir` . |
|  `backup_dir` |  `backup_dir` | Directory used to store backup files. | Optional | RPM = `/var/backups/automation-platform/` . Container = `~/backups` |
|  `backup_file_prefix` |  | Prefix used for the file backup name for the final backup file. | Optional |  `automation-platform-backup` |
|  `bundle_install` |  `bundle_install` | Controls whether or not to perform an offline or bundled installation. Set this variable to `true` to enable an offline or bundled installation. | Optional |  `false` if using the setup installation program. `true` if using the setup bundle installation program. |
|  `bundle_install_folder` |  `bundle_dir` | Path to the bundle directory used when performing a bundle install. | Required if `bundle_install=true` | RPM = `/var/lib/ansible-automation-platform-bundle` . Container = `&lt;current_dir&gt;/bundle` . |
|  `custom_ca_cert` |  `custom_ca_cert` | Path to the custom CA certificate file. Use this variable when you have manually provided TLS certificates for Ansible Automation Platform services (such as `gateway_tls_cert` , `controller_tls_cert` , or `hub_tls_cert` ) that are signed by a custom CA.

This variable adds the CA certificate to the environment to ensure proper authentication and trust of the manually provided certificates. This variable is not needed when using `ca_tls_cert` and `ca_tls_key` , which automatically generate TLS certificates. For more information, see [Using custom TLS certificates](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/advanced-configuration-containerized#using-custom-tls-certificates) . | Optional |  |
|  `enable_insights_collection` |  | The default install registers the node to the Red Hat Lightspeed for Red Hat Ansible Automation Platform for the Red Hat Ansible Automation Platform Service if the node is registered with Subscription Manager. Set to `false` to disable this functionality. | Optional |  `true` |
|  `registry_password` |  `registry_password` | Password credential for access to the registry source defined in `registry_url` . For more information, see [Setting registry_username and registry_password](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/preparing-containerized-installation#proc-set-registry-username-password) .

Not required for disconnected (bundled) installations where `bundle_install=true` . | RPM = Required if you need a password to access `registry_url` . Container = Required for online installations if `registry_auth=true` . Not required for disconnected installations. |  |
|  `registry_url` |  `registry_url` | URL of the registry source from which to pull execution environment images. | Optional |  `registry.redhat.io` |
|  `registry_username` |  `registry_username` | Username credential for access to the registry source defined in `registry_url` . For more information, see [Setting registry_username and registry_password](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/preparing-containerized-installation#proc-set-registry-username-password) .

Not required for disconnected (bundled) installations where `bundle_install=true` . | RPM = Required if you need a password to access `registry_url` . Container = Required for online installations if `registry_auth=true` . Not required for disconnected installations. |  |
|  `registry_verify_ssl` |  `registry_tls_verify` | Controls whether SSL/TLS certificate verification is enabled or disabled when making HTTPS requests. | Optional |  `true` |
|  `restore_backup_file` |  | Path to the tar file used for the platform restore. | Optional |  `{{ setup_dir }}/automation-platform-backup-latest.tar.gz` |
|  `restore_file_prefix` |  | Path prefix for the staged restore components. | Optional |  `automation-platform-restore` |
|  `routable_hostname` |  `routable_hostname` | Used if the machine running the installation program can only route to the target host through a specific URL. For example, if you use short names in your inventory, but the node running the installation program can only resolve that host by using a FQDN. If `routable_hostname` is not set, it defaults to `ansible_host` . If you do not set `ansible_host` , `inventory_hostname` is used as a last resort. This variable is used as a host variable for particular hosts and not under the `[all:vars]` section. | Optional |  |
|  `use_archive_compression` |  `use_archive_compression` | Controls at a global level whether the filesystem-related backup files are compressed before being sent to the host to run the backup operation. If set to `true` , a `tar.gz` file is generated on each Ansible Automation Platform host and then gzip compression is used. If set to `false` , a simple tar file is generated.

You can control this functionality at a component level by using the `&lt;component_name&gt;_use_archive_compression` variables. | Optional |  `true` |
|  `use_db_compression` |  `use_db_compression` | Controls at a global level whether the database-related backup files are compressed before being sent to the host to run the backup operation.

You can control this functionality at a component level by using the `&lt;component_name&gt;_use_db_compression` variables. | Optional |  `true` |
|  |  `ca_tls_key_passphrase` | Passphrase used to decrypt the key provided in `ca_tls_key` . | Optional |  |
|  |  `client_request_timeout` | Sets the HTTP timeout for end-user requests. The minimum value is `10` seconds. | Optional |  `30` |
|  |  `container_compress` | Compression software to use for compressing container images. | Optional |  `gzip` |
|  |  `container_keep_images` | Controls whether or not to keep container images when uninstalling Ansible Automation Platform. Set to `true` to keep container images when uninstalling Ansible Automation Platform. | Optional |  `false` |
|  |  `container_pull_images` | Controls whether or not to pull newer container images during installation. Set to `false` to prevent pulling newer container images during installation. | Optional |  `true` |
|  |  `images_tmp_dir` | The directory where the installation program temporarily stores container images during installation. | Optional | The system’s temporary directory. |
|  |  `pcp_firewall_zone` | The firewall zone where Performance Co-Pilot related firewall rules are applied. This controls which networks can access Performance Co-Pilot based on the zone’s trust level. | Optional | public |
|  |  `pcp_use_archive_compression` | Controls whether archive compression is enabled or disabled for Performance Co-Pilot. You can control this functionality globally by using `use_archive_compression` . | Optional |  `true` |
|  |  `registry_auth` | Controls whether to use registry authentication. When set to `true` , `registry_username` and `registry_password` are required. Not applicable for disconnected (bundled) installations. | Optional |  `true` |
|  |  `registry_ns_aap` | Ansible Automation Platform registry namespace. | Optional |  `ansible-automation-platform-26` |
|  |  `registry_ns_rhel` | RHEL registry namespace. | Optional |  `rhel8` |
|  |  `setup_monitoring` | Set to `true` to enable Performance Co-Pilot for system performance monitoring and data collection on Ansible Automation Platform control plane nodes. | Optional |  `false` |


## B.7. Image variables




Inventory file variables for images.

| RPM variable name | Container variable name | Description | Required or optional | Default |
| --- | --- | --- | --- | --- |
|  `extra_images` |  | Additional container images to pull from the configured container registry during deployment. | Optional |  `ansible-builder-rhel8` |
|  |  `controller_image` | Container image for automation controller. | Optional |  `controller-rhel9:latest` |
|  |  `de_extra_images` | Additional decision environment container images to pull from the configured container registry during deployment. | Optional |  `[]` |
|  |  `de_supported_image` | Supported decision environment container image. | Optional |  `de-supported-rhel9:latest` |
|  |  `eda_image` | Backend container image for Event-Driven Ansible. | Optional |  `eda-controller-rhel9:latest` |
|  |  `eda_web_image` | Front-end container image for Event-Driven Ansible. | Optional |  `eda-controller-ui-rhel9:latest` |
|  |  `ee_extra_images` | Additional execution environment container images to pull from the configured container registry during deployment. | Optional |  `[]` |
|  |  `ee_minimal_image` | Minimal execution environment container image. | Optional |  `ee-minimal-rhel9:latest` |
|  |  `ee_supported_image` | Supported execution environment container image. | Optional |  `ee-supported-rhel9:latest` |
|  |  `gateway_image` | Container image for platform gateway. | Optional |  `gateway-rhel9:latest` |
|  |  `gateway_proxy_image` | Container image for platform gateway proxy. | Optional |  `gateway-proxy-rhel9:latest` |
|  |  `hub_image` | Backend container image for automation hub. | Optional |  `hub-rhel9:latest` |
|  |  `hub_web_image` | Front-end container image for automation hub. | Optional |  `hub-web-rhel9:latest` |
|  |  `pcp_image` | Container image for Performance Co-Pilot. | Optional |  `pcp:latest` |
|  |  `postgresql_image` | Container image for PostgreSQL. | Optional |  `postgresql-15:latest` |
|  |  `receptor_image` | Container image for receptor. | Optional |  `receptor-rhel9:latest` |
|  |  `redis_image` | Container image for Redis. | Optional |  `redis-6:latest` |


## B.8. Platform gateway variables




Inventory file variables for platform gateway.

| RPM variable name | Container variable name | Description | Required or optional | Default |
| --- | --- | --- | --- | --- |
|  `automationgateway_admin_email` |  `gateway_admin_email` | Email address used by Django for the admin user for platform gateway. | Optional |  `admin@example.com` |
|  `automationgateway_admin_password` |  `gateway_admin_password` | Platform gateway administrator password. Use of special characters for this variable is limited. The password can include any printable ASCII character except `/` , `”` , or `@` . | Required |  |
|  `automationgateway_admin_username` |  `gateway_admin_user` | Username used to identify and create the administrator user in platform gateway. | Optional |  `admin` |
|  `automationgateway_cache_cert` |  `gateway_redis_tls_cert` | Path to the platform gateway Redis certificate file. | Optional |  |
|  `automationgateway_cache_key` |  `gateway_redis_tls_key` | Path to the platform gateway Redis key file. | Optional |  |
|  `automationgateway_cache_tls_files_remote` |  | Denote whether the cache client certificate files are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional | The value defined in `automationgateway_tls_files_remote` which defaults to `false` . |
|  `automationgateway_client_regen_cert` |  | Controls whether or not to regenerate platform gateway client certificates for the platform cache. Set to `true` to regenerate platform gateway client certificates. | Optional |  `false` |
|  `automationgateway_control_plane_port` |  `gateway_control_plane_port` | Port number for the platform gateway control plane. | Optional |  `50051` |
|  `automationgateway_disable_hsts` |  `gateway_nginx_disable_hsts` | Controls whether HTTP Strict Transport Security (HSTS) is enabled or disabled for platform gateway. Set this variable to `true` to disable HSTS. | Optional |  `false` |
|  `automationgateway_disable_https` |  `gateway_nginx_disable_https` | Controls whether HTTPS is enabled or disabled for platform gateway. Set this variable to `true` to disable HTTPS. | Optional | RPM = The value defined in `disable_https` which defaults to `false` . Container = `false` . |
|  `automationgateway_firewalld_zone` |  `gateway_proxy_firewall_zone` | The firewall zone where platform gateway related firewall rules are applied. This controls which networks can access platform gateway based on the zone’s trust level. | Optional | RPM = no default set. Container = 'public'. |
|  `automationgateway_grpc_auth_service_timeout` |  `gateway_grpc_auth_service_timeout` | Timeout duration (in seconds) for requests made to the gRPC service on platform gateway. | Optional |  `30s` |
|  `automationgateway_grpc_server_max_threads_per_process` |  `gateway_grpc_server_max_threads_per_process` | Maximum number of threads that each gRPC server process can create to handle requests on platform gateway. | Optional |  `10` |
|  `automationgateway_grpc_server_processes` |  `gateway_grpc_server_processes` | Number of processes for handling gRPC requests on platform gateway. | Optional |  `5` |
|  `automationgateway_http_port` |  `gateway_nginx_http_port` | Port number that platform gateway listens on for HTTP requests. | Optional | RPM = `8080` . Container = `8083` . |
|  `automationgateway_https_port` |  `gateway_nginx_https_port` | Port number that platform gateway listens on for HTTPS requests. | Optional | RPM = `8443` . Container = `8446` . |
|  `automationgateway_main_url` |  `gateway_main_url` | URL of the main instance of platform gateway that clients connect to. Use if you are performing a clustered deployment and you need to use the URL of the load balancer instead of the component’s server. The URL must start with `http://` or `https://` prefix. | Optional |  |
|  `automationgateway_nginx_tls_files_remote` |  | Denote whether the web cert sources are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional | The value defined in `automationgateway_tls_files_remote` which defaults to `false` . |
|  `automationgateway_pg_cert_auth` |  `gateway_pg_cert_auth` | Controls whether client certificate authentication is enabled or disabled on the platform gateway PostgreSQL database. Set this variable to `true` to enable client certificate authentication. | Optional |  `false` |
|  `automationgateway_pg_database` |  `gateway_pg_database` | Name of the PostgreSQL database used by platform gateway. | Optional | RPM = `automationgateway` . Container = `gateway` . |
|  `automationgateway_pg_host` |  `gateway_pg_host` | Hostname of the PostgreSQL database used by platform gateway. | Required |  |
|  `automationgateway_pg_password` |  `gateway_pg_password` | Password for the platform gateway PostgreSQL database user. Use of special characters for this variable is limited. The `!` , `#` , `0` and `@` characters are supported. Use of other special characters can cause the setup to fail. | Optional |  |
|  `automationgateway_pg_port` |  `gateway_pg_port` | Port number for the PostgreSQL database used by platform gateway. | Optional |  `5432` |
|  `automationgateway_pg_sslmode` |  `gateway_pg_sslmode` | Controls the SSL mode to use when platform gateway connects to the PostgreSQL database. Valid options include `verify-full` , `verify-ca` , `require` , `prefer` , `allow` , `disable` . | Optional |  `prefer` |
|  `automationgateway_pg_username` |  `gateway_pg_username` | Username for the platform gateway PostgreSQL database user. | Optional | RPM = `automationgateway` . Container = `gateway` |
|  `automationgateway_pgclient_sslcert` |  `gateway_pg_tls_cert` | Path to the PostgreSQL SSL/TLS certificate file for platform gateway. | Required if using client certificate authentication. |  |
|  `automationgateway_pgclient_sslkey` |  `gateway_pg_tls_key` | Path to the PostgreSQL SSL/TLS key file for platform gateway. | Required if using client certificate authentication. |  |
|  `automationgateway_pgclient_tls_files_remote` |  | Denote whether the PostgreSQL client cert sources are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional | The value defined in `automationgateway_tls_files_remote` which defaults to `false` . |
|  `automationgateway_redis_host` |  `gateway_redis_host` | Hostname of the Redis host used by platform gateway. | Optional | First node in the `[automationgateway]` inventory group. |
|  `automationgateway_redis_password` |  `gateway_redis_password` | Password for platform gateway Redis. | Optional | Randomly generated string. |
|  `automationgateway_redis_username` |  `gateway_redis_username` | Username for platform gateway Redis. | Optional |  `gateway` |
|  `automationgateway_secret_key` |  `gateway_secret_key` | Secret key value used by platform gateway to sign and encrypt data. | Optional |  |
|  `automationgateway_ssl_cert` |  `gateway_tls_cert` | Path to the SSL/TLS certificate file for platform gateway. | Optional |  |
|  `automationgateway_ssl_key` |  `gateway_tls_key` | Path to the SSL/TLS key file for platform gateway. | Optional |  |
|  `automationgateway_tls_files_remote` |  `gateway_tls_remote` | Denote whether the platform gateway provided certificate files are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional |  `false` |
|  `automationgateway_uwsgi_processes` |  `gateway_uwsgi_processes` | The number of `uwsgi` processes for the platform gateway container. The value is calculated based on the number of available vCPUs (virtual CPUs). | Optional | The number of vCPUs multiplied by two, plus one. |
|  `automationgateway_use_archive_compression` |  `gateway_use_archive_compression` | Controls whether archive compression is enabled or disabled for platform gateway. You can control this functionality globally by using `use_archive_compression` . | Optional |  `true` |
|  `automationgateway_use_db_compression` |  `gateway_use_db_compression` | Controls whether database compression is enabled or disabled for platform gateway. You can control this functionality globally by using `use_db_compression` . | Optional |  `true` |
|  `automationgateway_user_headers` |  `gateway_nginx_user_headers` | List of additional NGINX headers to add to platform gateway’s NGINX configuration. | Optional |  `[]` |
|  `automationgateway_verify_ssl` |  | Denotes whether or not to verify platform gateway’s web certificates when making calls from platform gateway to itself during installation. Set to `false` to disable web certificate verification. | Optional |  `true` |
|  `automationgatewayproxy_disable_https` |  `envoy_disable_https` | Controls whether or not HTTPS is disabled when accessing the platform UI. Set to `true` to disable HTTPS (HTTP is used instead). | Optional | RPM = The value defined in `disable_https` which defaults to `false` . Container = `false` . |
|  `automationgatewayproxy_http_port` |  `envoy_http_port` | Port number on which the Envoy proxy listens for incoming HTTP connections. | Optional |  `80` |
|  `automationgatewayproxy_https_port` |  `envoy_https_port` | Port number on which the Envoy proxy listens for incoming HTTPS connections. | Optional |  `443` |
|  `nginx_tls_protocols` |  `gateway_nginx_https_protocols` | Protocols that platform gateway will support when handling HTTPS traffic. | Optional |  `[TLSv1.2, TLSv1.3]` |
|  `redis_disable_tls` |  `gateway_redis_disable_tls` | Controls whether TLS is enabled or disabled for platform gateway Redis. Set this variable to `true` to disable TLS. | Optional |  `false` |
|  `redis_port` |  `gateway_redis_port` | Port number for the Redis host for platform gateway. | Optional |  `6379` |
|  |  `gateway_extra_settings` | Defines additional settings for use by platform gateway during installation.

For example:

```
gateway_extra_settings=[{"setting": "OAUTH2_PROVIDER['ACCESS_TOKEN_EXPIRE_SECONDS']", "value": 600}]
``` | Optional |  `[]` |
|  |  `gateway_nginx_client_max_body_size` | Maximum allowed size for data sent to platform gateway through NGINX. | Optional |  `5m` |
|  |  `gateway_nginx_hsts_max_age` | Maximum duration (in seconds) that HTTP Strict Transport Security (HSTS) is enforced for platform gateway. | Optional |  `63072000` |
|  |  `gateway_uwsgi_listen_queue_size` | Number of requests `uwsgi` will allow in the queue on platform gateway until `uwsgi_processes` can serve them. | Optional |  `4096` |


## B.9. Receptor variables




Inventory file variables for Receptor.

| RPM variable name | Container variable name | Description | Required or optional | Default |
| --- | --- | --- | --- | --- |
|  `receptor_datadir` |  | The directory where receptor stores its runtime data and local artifacts. The target directory must be accessible to **awx** users. If the target directory is a temporary file system **tmpfs** , ensure it is remounted correctly after a reboot. Failure to do so results in the receptor no longer having a working directory. | Optional |  `/tmp/receptor` |
|  `receptor_listener_port` |  `receptor_port` | Port number that receptor listens on for incoming connections from other receptor nodes. | Optional |  `27199` |
|  `receptor_listener_protocol` |  `receptor_protocol` | Protocol that receptor will support when handling traffic. | Optional |  `tcp` |
|  `receptor_log_level` |  `receptor_log_level` | Controls the verbosity of logging for receptor. Valid options include: `error` , `warning` , `info` , or `debug` . | Optional |  `info` |
|  `receptor_tls` |  | Controls whether TLS is enabled or disabled for receptor. Set this variable to `false` to disable TLS. | Optional |  `true` |
| See `node_type` for the RPM equivalent variable. |  `receptor_type` | For the `[automationcontroller]` group the two options are:

-  `    receptor_type=control` - The node only runs project and inventory updates, but not regular jobs.
-  `    receptor_type=hybrid` - The node runs everything.


For the `[execution_nodes]` group the two options are:

-  `    receptor_type=hop` - The node forwards jobs to an execution node.
-  `    receptor_type=execution` - The node can run jobs. | Optional | For the `[automationcontroller]` group: `hybrid` . For the `[execution_nodes]` group: `execution` . |
| See `peers` for the RPM equivalent variable |  `receptor_peers` | Used to indicate which nodes a specific host connects to. Wherever this variable is defined, an outbound connection to the specific host is established. The value must be a comma-separated list of hostnames. Do not use inventory group names.

This is resolved into a set of hosts that is used to construct the `receptor.conf` file.

For more information, see [Adding execution nodes](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/advanced-configuration-containerized#adding-execution-nodes) . | Optional |  `[]` |
|  |  `receptor_disable_signing` | Controls whether signing of communications between receptor nodes is enabled or disabled. Set this variable to `true` to disable communication signing. | Optional |  `false` |
|  |  `receptor_disable_tls` | Controls whether TLS is enabled or disabled for receptor. Set this variable to `true` to disable TLS. | Optional |  `false` |
|  |  `receptor_firewall_zone` | The firewall zone where receptor related firewall rules are applied. This controls which networks can access receptor based on the zone’s trust level. | Optional |  `public` |
|  |  `receptor_mintls13` | Controls whether or not receptor only accepts connections that use TLS 1.3 or higher. Set to `true` to only accept connections that use TLS 1.3 or higher. | Optional |  `false` |
|  |  `receptor_signing_private_key` | Path to the private key used by receptor to sign communications with other receptor nodes in the network. | Optional |  |
|  |  `receptor_signing_public_key` | Path to the public key used by receptor to sign communications with other receptor nodes in the network. | Optional |  |
|  |  `receptor_signing_remote` | Denote whether the receptor signing files are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional |  `false` |
|  |  `receptor_tls_cert` | Path to the TLS certificate file for receptor. | Optional |  |
|  |  `receptor_tls_key` | Path to the TLS key file for receptor. | Optional |  |
|  |  `receptor_tls_remote` | Denote whether the receptor provided certificate files are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional |  `false` |
|  |  `receptor_use_archive_compression` | Controls whether archive compression is enabled or disabled for receptor. You can control this functionality globally by using `use_archive_compression` . | Optional |  `true` |


## B.10. Redis variables




Inventory file variables for Redis.

| RPM variable name | Container variable name | Description | Required or optional | Default |
| --- | --- | --- | --- | --- |
|  `redis_cluster_ip` |  `redis_cluster_ip` | The IPv4 address used by the Redis cluster to identify each host in the cluster. When defining hosts in the `[redis]` group, use this variable to identify the IPv4 address if the default is not what you want. Specific to container: Redis clusters cannot use hostnames or IPv6 addresses. | Optional | RPM = Discovered IPv4 address from Ansible facts. If IPv4 address is not available, IPv6 address is used. Container = Discovered IPv4 address from Ansible facts. |
|  `redis_disable_mtls` |  | Controls whether mTLS is enabled or disabled for Redis. Set this variable to `true` to disable mTLS. | Optional |  `false` |
|  `redis_firewalld_zone` |  `redis_firewall_zone` | The firewall zone where Redis related firewall rules are applied. This controls which networks can access Redis based on the zone’s trust level. | Optional | RPM = no default set. Container = `public` . |
|  `redis_hostname` |  | Hostname used by the Redis cluster when identifying and routing the host. By default `routable_hostname` is used. | Optional | The value defined in `routable_hostname` |
|  `redis_mode` |  `redis_mode` | The Redis mode to use for your Ansible Automation Platform installation. Valid options include: `standalone` and `cluster` . For more information about Redis, see [Caching and queueing system](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_installation/ha-redis_planning) in _Planning your installation_ . | Optional |  `cluster` |
|  `redis_server_regen_cert` |  | Denotes whether or not to regenerate the Ansible Automation Platform managed TLS key pair for Redis. | Optional |  `false` |
|  `redis_tls_cert` |  `redis_tls_cert` | Path to the Redis server TLS certificate. | Optional |  |
|  `redis_tls_files_remote` |  `redis_tls_remote` | Denote whether the Redis provided certificate files are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional |  `false` |
|  `redis_tls_key` |  `redis_tls_key` | Path to the Redis server TLS certificate key. | Optional |  |
|  |  `redis_use_archive_compression` | Controls whether archive compression is enabled or disabled for Redis. You can control this functionality globally by using `use_archive_compression` . | Optional |  `true` |


## B.11. Red Hat Ansible Lightspeed variables




Configure Red Hat Ansible Lightspeed by setting inventory file variables during installation. Use this reference to determine which variables to set for your deployment requirements.

### B.11.1. Red Hat Ansible Lightspeed variables




Inventory file variables for Red Hat Ansible Lightspeed.

| RPM variable name | Container variable name | Description | Required or optional | Default |
| --- | --- | --- | --- | --- |
| N/A |  `lightspeed_admin_password` | Red Hat Ansible Lightspeed administrator password. Use of special characters for this variable is limited. The password can include any printable ASCII character except `/` , `"` , or `@` . | Required |  |
| N/A |  `lightspeed_admin_user` | Username used to identify and create the Red Hat Ansible Lightspeed admin user. | Optional |  `admin` |
| N/A |  `lightspeed_chat_rate_throttle` | Chat rate throttle. | Optional |  `10/minute` |
| N/A |  `lightspeed_nginx_client_max_body_size` | Maximum allowed size for data sent to Red Hat Ansible Lightspeed through NGINX. | Optional |  `5m` |
| N/A |  `lightspeed_nginx_disable_hsts` | Controls whether HTTP Strict Transport Security (HSTS) is enabled or disabled for Red Hat Ansible Lightspeed. Set this variable to `true` to disable HSTS. | Optional |  `false` |
| N/A |  `lightspeed_nginx_disable_https` | Controls whether HTTPS is enabled or disabled for Red Hat Ansible Lightspeed. Set this variable to `true` to disable HTTPS. | Optional |  `false` |
| N/A |  `lightspeed_nginx_hsts_max_age` | Maximum duration (in seconds) that HTTP Strict Transport Security (HSTS) is enforced for Red Hat Ansible Lightspeed. | Optional |  `63072000` |
| N/A |  `lightspeed_nginx_http_port` | Port number that Red Hat Ansible Lightspeed listens on for HTTP requests. | Optional |  `8084` |
| N/A |  `lightspeed_nginx_https_port` | Port number that Red Hat Ansible Lightspeed listens on for HTTPS requests. | Optional |  `8447` |
| N/A |  `lightspeed_nginx_https_protocols` | Protocols that Red Hat Ansible Lightspeed will support when handling HTTPS traffic. | Optional |  `[TLSv1.2, TLSv1.3]` |
| N/A |  `lightspeed_nginx_user_headers` | Custom Nginx headers. List of additional NGINX headers to add to Red Hat Ansible Lightspeed’s NGINX configuration. | Optional | [] |
| N/A |  `lightspeed_nginx_read_timeout` | Sets the HTTP timeout for end-user requests. The minimum value is `10` seconds. | Optional |  `3600` |
| N/A |  `lightspeed_pg_cert_auth` | Controls whether client certificate authentication is enabled or disabled on the Red Hat Ansible Lightspeed PostgreSQL database. Set this variable to `true` to enable client certificate authentication. | Optional |  `false` |
| N/A |  `lightspeed_pg_database` | Name of the PostgreSQL database used by Red Hat Ansible Lightspeed. | Optional |  `lightspeed` |
| N/A |  `lightspeed_pg_host` | Hostname of the PostgreSQL database used by Red Hat Ansible Lightspeed. | Required |  |
| N/A |  `lightspeed_pg_password` | Password for the Red Hat Ansible Lightspeed PostgreSQL database user. Use of special characters for this variable is limited. The `!` , `#` , `0` and `@` characters are supported. Use of other special characters can cause the setup to fail. | Optional |  |
| N/A |  `lightspeed_pg_port` | Port number for the PostgreSQL database used by Red Hat Ansible Lightspeed. | Optional |  `5432` |
| N/A |  `lightspeed_pg_sslmode` | Controls the SSL mode to use when platform gateway connects to the PostgreSQL database. Valid options include `verify-full` , `verify-ca` , `require` , `prefer` , `allow` , `disable` . | Optional |  `prefer` |
| N/A |  `lightspeed_pg_tls_cert` | Path to the PostgreSQL SSL/TLS certificate file for Red Hat Ansible Lightspeed. | Optional |  |
| N/A |  `lightspeed_pg_tls_key` | Path to the PostgreSQL SSL/TLS key file for Red Hat Ansible Lightspeed. | Optional |  |
| N/A |  `lightspeed_pg_username` | Username for the Red Hat Ansible Lightspeed PostgreSQL database user. | Optional |  `lightspeed` |
| N/A |  `lightspeed_secret_key` | Secret key value used by Red Hat Ansible Lightspeed to sign and encrypt data. | Optional |  |
| N/A |  `lightspeed_tls_cert` | Path to the SSL/TLS certificate file for Red Hat Ansible Lightspeed. | Optional |  |
| N/A |  `lightspeed_tls_key` | Path to the SSL/TLS key file for Red Hat Ansible Lightspeed. | Optional |  |
| N/A |  `lightspeed_tls_remote` | Denote whether the Red Hat Ansible Lightspeed provided certificate files are local to the installation program ( `false` ) or on the remote component server ( `true` ). | Optional |  `false` |
| N/A |  `lightspeed_use_archive_compression` | Controls whether archive compression is enabled or disabled for Red Hat Ansible Lightspeed. You can control this functionality globally by using `use_archive_compression` . | Optional |  `true` |
| N/A |  `lightspeed_use_db_compression` | Controls whether database compression is enabled or disabled for Red Hat Ansible Lightspeed. You can control this functionality globally by using `use_db_compression` . | Optional |  `false` |


### B.11.2. Ansible Lightspeed coding assistant variables




Inventory file variables for Ansible Lightspeed coding assistant.

| RPM variable name | Container variable name | Description | Required or optional | Default |
| --- | --- | --- | --- | --- |
| N/A |  `lightspeed_wca_model_type` | IBM watsonx Code Assistant model deployment mode, cloud ( `wca` ) or on-premise ( `wca-onprem` ). | Optional |  `wca` |
| N/A |  `lightspeed_wca_model_url` | URL of the IBM watsonx Code Assistant model. For cloud deployment, the URL could be `https://api.dataplatform.test.cloud.ibm.com` . | Optional |  |
| N/A |  `lightspeed_wca_model_api_key` | API key of the IBM watsonx Code Assistant model that was generated during the model installation. | Required |  |
| N/A |  `lightspeed_wca_model_id` | ID of the IBM watsonx Code Assistant model. | Optional |  |
| N/A |  `lightspeed_wca_model_verify_ssl` | Denotes whether or not to verify IBM watsonx Code Assistant’s web certificates when making calls from Red Hat Ansible Lightspeed to itself during installation. Set to `false` to disable web certificate verification. | Optional |  `true` |
| N/A |  `lightspeed_wca_model_enable_anonymization` | Controls whether the anonymization of Personally Identifiable Information (PII) is enabled. PII information includes passwords, IP addresses, email addresses, and other sensitive data.

When PII anonymization is enabled, users' personal information is modified to some generic values to protect their data and reduce the risk of data leaks.

You can turn off the anonymization by specifying the value as `false` if you want to retain all original information as entered by users and improve the quality of the answers.

If you set the value to `false` and the Ansible administrator is using Red Hat Ansible Lightspeed in hybrid mode (where the model is in IBM watsonx Code Assistant in IBM Cloud) then their users' PII is sent to IBM Cloud. | Optional |  `true` |
| N/A |  `lightspeed_wca_model_username` | For on-premise deployment only. The username you use to connect to an IBM Cloud Pak for Data deployment. | Optional |  |
| N/A |  `lightspeed_wca_health_check` | Enables or disables IBM watsonx Code Assistant health check. | Optional |  `true` |
| N/A |  `lightspeed_wca_idp_url` | For cloud deployment only. The IBM watsonx Code Assistant Identity Provider (IdP) URL. | Optional |  |
| N/A |  `lightspeed_wca_idp_login` | For cloud deployment only. The IBM watsonx Code Assistant Identity Provider (IdP) username. | Optional |  |
| N/A |  `lightspeed_wca_idp_password` | For cloud deployment only. The IBM watsonx Code Assistant Identity Provider (IdP) password. | Optional |  |


### B.11.3. Ansible Lightspeed intelligent assistant variables




Inventory file variables for Ansible Lightspeed intelligent assistant.

| RPM variable name | Container variable name | Description | Required or optional | Default |
| --- | --- | --- | --- | --- |
| N/A |  `lightspeed_chatbot_model_url` | The inference API base URL on your LLM setup. For example, `https://your_inference_api/v1` . | Optional |  |
| N/A |  `lightspeed_chatbot_model_verify_ssl` | Controls whether SSL/TLS certificate verification is enabled or disabled when making HTTPS requests. | Optional |  `true` |
| N/A |  `lightspeed_chatbot_default_provider` | The provider type of your LLM setup by using one of the following values:

- Red Hat Enterprise Linux AI: `    rhelai`
- Red Hat OpenShift AI: `    rhoai`
- OpenAI: `    openai`
- Microsoft Azure OpenAI: `    azure` | Optional |  `rhoai` |
| N/A |  `lightspeed_chatbot_model_extra_settings` | Use this parameter to pass a JSON dictionary of extra parameters to pass directly to the model provider, for settings not covered by other standard fields.

If you want to use Microsoft Azure OpenAI as the LLM provider, specify the value as `'{"api_type": ""}'` . | Optional |  `{}` |
| N/A |  `lightspeed_chatbot_chatbot_max_tokens` | Maximum number of tokens to generate a chat response. | Optional |  `4096` |
| N/A |  `lightspeed_chatbot_http_port` | Port number that Ansible Lightspeed intelligent assistant listens on for HTTP requests. | Optional |  `8085` |
| N/A |  `lightspeed_chatbot_model_id` | The ID of the LLM model that is configured on your LLM setup. | Optional |  |
| N/A |  `lightspeed_chatbot_model_api_key` | The API token or the API key of your LLM setup. This token is sent along with the authorization header when an inference API is called. | Optional |  |


### B.11.4. Ansible Lightspeed intelligent assistant integration with MCP server variables




Inventory file variables for Ansible Lightspeed intelligent assistant integration with Model Context Protocol (MCP) server.

| RPM variable name | Container variable name | Description | Required or optional | Default |
| --- | --- | --- | --- | --- |
| N/A |  `lightspeed_mcp_controller_enabled` | Controls whether the Ansible Lightspeed MCP controller is enabled or disabled. | Optional |  `false` |
| N/A |  `lightspeed_mcp_controller_port` | Ansible Lightspeed MCP controller port. | Optional |  `8004` |
| N/A |  `lightspeed_mcp_lightspeed_enabled` | Ansible Lightspeed MCP lightspeed enabled. | Optional |  `false` |
| N/A |  `lightspeed_mcp_lightspeed_port` | Ansible Lightspeed MCP lightspeed port. | Optional |  `8005` |


## B.12. Ansible MCP server variables




The following variables govern the access granted to Ansible MCP server.

| RPM variable name | Container variable name | Description | Required or optional | Default |
| --- | --- | --- | --- | --- |
| N/A |  `mcp_allow_write_operations` | Determines whether the Ansible MCP server allows actions that modify state, such as launching jobs or updating templates through the external AI tool.

By default, the variable’s value is set to `false` , so that the Ansible MCP server enables read-only operations and blocks all write operations. To enable the Ansible MCP server to perform write operations, change the value of the variable to `true` . | Optional |  `false` |
| N/A |  `mcp_ignore_certificate_errors` | Specifies whether to skip validation of SSL/TLS certificates when connecting to an MCP server over a secure transport (HTTPS/WSS).

Set this parameter value to `true` to allow connections to servers with self-signed, expired, or otherwise untrusted certificates, primarily during local development or internal testing. | Optional |  `false` |
| N/A |  `mcp_tls_cert` | Path to the SSL/TLS certificate file for the Ansible MCP server. | Required if using client certificate authentication. |  |
| N/A |  `mcp_tls_key` | Path to the SSL/TLS key file for the Ansible MCP server. | Required if using client certificate authentication. |  |



<span id="idm140279425481152"></span>
# Legal Notice

Copyright© Red Hat.
Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution–Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.
Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.
Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.
Linux® is the registered trademark of Linus Torvalds in the United States and other countries.
XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.
TheOpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.
All other trademarks are the property of their respective owners.





