# Access Ansible Automation Platform through the CLI
## Fetch the platform gateway web address

A Red Hat OpenShift Container Platform route exposes a service at a host name, so that external clients can reach it by name. When you created the platform gateway instance, a route was created for it. The route inherits the name that you assigned to the platform gateway object in the YAML file.

### About this task

### Procedure

Use the following command to fetch the routes:

```
oc get routes -n <platform_namespace>
```

### Results

You can see in the following example, the `example` platform gateway is running in the `ansible-automation-platform` namespace.

```
$ oc get routes -n ansible-automation-platform

NAME      HOST/PORT                                              PATH   SERVICES          PORT   TERMINATION     WILDCARD
example   example-ansible-automation-platform.apps-crc.testing          example-service   http   edge/Redirect   None
```
The address for the platform gateway instance is `example-ansible-automation-platform.apps-crc.testing`.

