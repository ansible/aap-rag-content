# 2. Installing the Ansible plug-ins with a Helm chart on OpenShift Container Platform
## 2.4. Creating a registry for the Ansible plug-ins




Set up a registry in your OpenShift cluster to host the Ansible plug-ins and make them available for installation in Red Hat Developer Hub (RHDH).

**Procedure**

1. Log in to your OpenShift Container Platform instance with credentials to create a new application.
1. Open your Red Hat Developer Hub OpenShift project.


```
$ oc project &lt;YOUR_DEVELOPER_HUB_PROJECT&gt;
```


1. Run the following commands to create a plug-in registry build in the OpenShift cluster.


```
$ oc new-build httpd --name=plugin-registry --binary    $ oc start-build plugin-registry --from-dir=$DYNAMIC_PLUGIN_ROOT_DIR --wait    $ oc new-app --image-stream=plugin-registry
```




**Verification**

To verify that the plugin-registry was deployed successfully, open the **Topology** view in the **Developer** perspective on the Red Hat Developer Hub application in the OpenShift Web console.


1. Click the plug-in registry to view the log.

![Developer perspective](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Installing_Ansible_plug-ins_for_Red_Hat_Developer_Hub-en-US/images/569de994c3fd61a583f4b81b85bf852e/rhdh-plugin-registry.png)


(1) Developer hub instance

(2) Plug-in registry


1. Click the terminal tab and login to the container.
1. In the terminal, run `    ls` to confirm that the `    .tar` files are in the plugin registry.


```
ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz    ansible-plugin-backstage-rhaap-backend-dynamic-x.y.z.tgz    ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz
```

The version numbers and file names can differ.




