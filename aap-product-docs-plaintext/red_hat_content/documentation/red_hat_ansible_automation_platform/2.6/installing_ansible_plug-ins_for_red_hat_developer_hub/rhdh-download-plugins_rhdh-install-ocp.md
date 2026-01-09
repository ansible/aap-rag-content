# 2. Installing the Ansible plug-ins with a Helm chart on OpenShift Container Platform
## 2.3. Downloading the Ansible plug-ins files




Download the Ansible plug-ins for Red Hat Developer Hub **Setup Bundle** from the Red Hat Ansible Automation Platform Product Software downloads page.

**Procedure**

1. In a browser, navigate to the [Red Hat Ansible Automation Platform Product Software downloads page](https://access.redhat.com/downloads/content/480/ver=2.6/rhel---9/2.6/x86_64/product-software) and select the **Product Software** tab.
1. Click **Download now** next to **Ansible plug-ins for Red Hat Developer Hub Setup Bundle** to download the latest version of the plug-ins.

The format of the filename is `    ansible-rhdh-plugins-x.y.z.tar.gz` . Substitute the Ansible plug-ins release version, for example `    2.0.0` , for `    x.y.z` .


1. Create a directory on your local machine to store the `    .tar` files.


```
$ mkdir /path/to/&lt;ansible-backstage-plugins-local-dir-changeme&gt;
```


1. Set an environment variable ( `    $DYNAMIC_PLUGIN_ROOT_DIR` ) to represent the directory path.


```
$ export DYNAMIC_PLUGIN_ROOT_DIR=/path/to/&lt;ansible-backstage-plugins-local-dir-changeme&gt;
```


1. Extract the `    ansible-rhdh-plugins-&lt;version-number&gt;.tar.gz` contents to `    $DYNAMIC_PLUGIN_ROOT_DIR` .


```
$ tar --exclude='*code*' -xzf ansible-rhdh-plugins-x.y.z.tar.gz -C $DYNAMIC_PLUGIN_ROOT_DIR
```

Substitute the Ansible plug-ins release version, for example `    2.0.0` , for `    x.y.z` .




**Verification**

Run `ls` to verify that the extracted files are in the `$DYNAMIC_PLUGIN_ROOT_DIR` directory:


```
$ ls $DYNAMIC_PLUGIN_ROOT_DIR
ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz
ansible-plugin-backstage-rhaap-dynamic-x.y.z.tgz.integrity
ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz
ansible-plugin-scaffolder-backend-module-backstage-rhaap-dynamic-x.y.z.tgz.integrity
```

The files with the `.integrity` file type contain the plugin SHA value. The SHA value is used during the plug-in configuration.

