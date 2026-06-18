# Apply configuration changes

Apply configuration changes after modifying your Helm chart values or RHEL appliance configuration file for execution environment builder.

## About this task

You can apply changes at any point — you do not need to complete all configuration sections before applying.

## Procedure

1.  Apply the updated configuration.
**OpenShift — CLI:**

```
$ helm upgrade <release_name> <chart_name> -f <values_file> -n <namespace>
```
**OpenShift — web console:**

1. Navigate to **Helm > Installed Helm Charts**.
2. Select your release and click **Upgrade**.
3. Edit the values and click **Upgrade**.
**RHEL appliance:**

```
$ sudo systemctl daemon-reload
$ sudo systemctl stop portal.service
$ sudo podman rm -f portal
$ sudo systemctl start portal.service
```
Note:
The `daemon-reload` and `stop/rm/start` sequence is required when Quadlet drop-in files have been added or changed (for example, after adding EE Builder secrets). If you only changed `app-config.production.yaml` without modifying drop-in files, `sudo systemctl restart portal` is sufficient.

2.  Verify that the service is running.
**OpenShift — CLI:**

```
$ oc rollout status deployment -n <namespace>
$ oc get pods -n <namespace>
```
**OpenShift — web console:**

Navigate to **Workloads > Pods**. Filter by your namespace and verify that all pods show Running status with no restarts.

**RHEL appliance:**

```
$ sudo systemctl status portal
```

## Results

Log in to automation portal and verify the changes you applied:

- If you configured Git provider integration: check that no `No GitHub integration configured for host` errors appear in the logs.
- If you configured content discovery sources: navigate to **Collections** and verify sources are listed.
- If you configured wizard templates: navigate to **Execution Environments > Create** and verify templates appear.
