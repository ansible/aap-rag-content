# Upgrade Ansible automation portal
## Download the plug-in TAR files (deprecated)

Download the latest `.tar.gz` plug-in bundle for Ansible automation portal from the Red Hat Customer Portal.

### About this task

Important:

The HTTP plug-in registry method is deprecated and will be removed in a future release of Ansible Automation Platform. Red Hat recommends OCI container delivery. Use this procedure only if you cannot migrate to OCI yet and your deployment uses `pluginMode: tarball`.

### Procedure

1.  Create a directory on your local machine and set an environment variable to represent the directory path:


```
$ mkdir /path/to/<automation-portal-plugins>
$ export DYNAMIC_PLUGIN_ROOT_DIR=/path/to/<automation-portal-plugins>
```

2.  In a browser, open the Red Hat Ansible Automation Platform product software downloads page and select the Product Software tab.
3.  Download the Ansible automation portal setup bundle that matches your target chart version on the lifecycle page or the Product Software tab.
The filename format is `ansible-backstage-rhaap-bundle-<plugin-version>.tar.gz`.

4.  Extract the archive into `$DYNAMIC_PLUGIN_ROOT_DIR`:


```
$ tar --exclude='*code*' -xzf ansible-backstage-rhaap-bundle-<plugin-version>.tar.gz -C $DYNAMIC_PLUGIN_ROOT_DIR
```

### Results

Verify extracted files:

```
$ ls $DYNAMIC_PLUGIN_ROOT_DIR
```
You should see `.tgz` plug-in files and matching `.integrity` files.

