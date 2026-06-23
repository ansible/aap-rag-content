# Install Ansible plug-ins using an HTTP plug-in registry (deprecated)
## Create a registry for the Ansible plug-ins

Set up a registry in your OpenShift cluster to host the Ansible plug-ins and make them available for installation in Red Hat Developer Hub (RHDH).

### Procedure

1.  Log in to your OpenShift Container Platform instance with credentials to create a new application.
2.  Open your Red Hat Developer Hub OpenShift project.

```
$ oc project <YOUR_DEVELOPER_HUB_PROJECT>
```

3.  Run the following commands to create a plug-in registry build in the OpenShift cluster.

```
$ oc new-build httpd --name=plugin-registry --binary
$ oc start-build plugin-registry --from-dir=$DYNAMIC_PLUGIN_ROOT_DIR --wait
$ oc new-app --image-stream=plugin-registry
```

### Results

To verify that the plugin-registry was deployed successfully, open the **Topology** view in the **Developer** perspective on the Red Hat Developer Hub application in the OpenShift Web console.

1. Click the plug-in registry to view the log.
![Developer perspective](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/rhdh-plugin-registry.png)
(1) Developer hub instance

(2) Plug-in registry

2. Click the terminal tab and login to the container.

3. In the terminal, run `ls` to confirm that the `.tar` files are in the plugin registry.

```
ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz
ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz
```
The version numbers and file names can differ.

