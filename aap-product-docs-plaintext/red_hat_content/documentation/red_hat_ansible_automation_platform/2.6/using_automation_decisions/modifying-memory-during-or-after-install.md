# 11. Performance tuning for Event-Driven Ansible controller
## 11.2. Modifying the default memory limit for each rulebook activation




Memory usage is based on the number of events that Event-Driven Ansible controller has to process. By default, each rulebook activation container has a 200 MB memory limit.

For example, with 4 CPU and 16 GB of RAM, one rulebook activation container with an assigned 200 MB memory limit cannot handle more than 150,000 events per minute. If the number of parallel running rulebook activations is higher, then the maximum number of events each rulebook activation can process is reduced.

If there are too many incoming events at a very high rate, the container can run out of memory trying to process the events, which will kill the container, and your rulebook activation will fail with a status code of 137.

To mitigate this status, you can modify the default memory limit for each rulebook activation _during_ or _after_ installation.

**Procedure**

1. Perform the following steps to modify your default memory limit for your rulebook activations _during_ installation:


1. Navigate to the setup inventory file.
1. Add `        automationedacontroller_podman_mem_limit` in the [all:vars] section. For example, `        automationedacontroller_podman_mem_limit='400m'` .
1. Run the setup.

1. Perform the following steps to modify your default memory limit for your rulebook activations _after_ installation:


1. Navigate to the environment file at `        /etc/ansible-automation-platform/eda/settings.yaml` .
1. Modify the default container memory limit. For example, `        PODMAN_MEM_LIMIT = '300m'` .
1. Restart the Event-Driven Ansible controller services using `        automation-eda-controller-service restart` .



