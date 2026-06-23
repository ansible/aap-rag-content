# Configure platform gateway route timeouts
## Configure gateway routes using the ansible.platform collection

You can configure platform gateway route timeouts during installation or redeployment to support large file uploads to automation hub.

### Before you begin

- The `ansible.platform` collection is installed.
- You have administrator access to the deployment environment.
- For Red Hat OpenShift Container Platform deployments, you have cluster administrator privileges.

### Procedure

1.  Create or edit your platform gateway deployment playbook.
2.  Add the route timeout configuration for your deployment type.
For OpenShift Container Platform deployments:

```
---
- name: Set hub container registry route timeout
ansible.platform.route:
name: "hub container registry"
request_timeout_seconds: 600
idle_timeout_seconds: 600
```
For containerized deployments:

```
---
- name: Set hub container registry route timeout
ansible.platform.route:
name: "hub container registry"
request_timeout_seconds: 600
idle_timeout_seconds: 600
```

3.  Run the playbook to apply the configuration:


```
$ ansible-playbook -i inventory gateway-deploy.yml
```

### Results

Upload a large container image to automation hub:

```
$ podman push <large-image> <gateway-host>/automation-hub/<repository>/<image>:<tag>
```
Confirm that the upload completes without timeout errors.

