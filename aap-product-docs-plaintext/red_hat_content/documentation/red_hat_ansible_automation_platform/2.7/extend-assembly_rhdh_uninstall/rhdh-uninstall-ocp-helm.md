# Uninstall the Ansible plug-ins
## Uninstall a Helm chart installation

To uninstall the Ansible plug-ins from a Helm chart installation, remove the plug-in configuration from the Helm chart YAML, remove the `extraContainers` section, and delete the Ansible block from the custom ConfigMap.

### Procedure

1.  In Red Hat Developer Hub, remove any software templates that use the `ansible:content:create` action.
2.  In the OpenShift Developer UI, navigate to **Helm** > **developer-hub** > **Actions** > **Upgrade** > **Yaml view**.
3.  Remove the Ansible plug-ins configuration under the `plugins` section (all `oci://registry.redhat.io/ansible-automation-platform/automation-portal` entries).

Note:
If you used the deprecated HTTP plug-in registry method, remove the `http://plugin-registry:8080/...` entries instead.

4.  Remove the `extraContainers` section.


```
upstream:
backstage:
...
extraContainers:
- command:
- adt
- server
image: >-
registry.redhat.io/ansible-automation-platform-2.7/ansible-dev-tools-rhel9:latest
imagePullPolicy: IfNotPresent
name: ansible-devtools-server
ports:
- containerPort: 8000
```

5.  Click **Upgrade**.
6.  Edit your custom Red Hat Developer Hub config map, for example `app-config-rhdh`.
7.  Remove the `ansible` section.
8.  Restart the Red Hat Developer Hub deployment.
9.  If you used OCI delivery, delete the registry auth secret:


```terminal
$ oc delete secret <deployment-name>-dynamic-plugins-registry-auth
```

10.  If you used the HTTP plug-in registry method, remove the plug-in registry application:


```terminal
$ oc delete all -l app=plugin-registry
```

