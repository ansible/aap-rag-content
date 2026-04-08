# 6. Disconnected installation
## 6.2. Synchronizing RPM repositories using reposync




To perform a reposync you need a Red Hat Enterprise Linux host that has access to the internet. After the repositories are synced, you can move the repositories to the disconnected network hosted from a web server.

When downloading RPM, ensure you use the applicable distro.

**Procedure**

1. Attach the BaseOS and AppStream required repositories:


```
# subscription-manager repos \        --enable rhel-9-for-x86_64-baseos-rpms \        --enable rhel-9-for-x86_64-appstream-rpms
```


1. Perform the reposync:


```
# dnf install yum-utils    # reposync -m --download-metadata --gpgcheck \        -p /path/to/download
```


1. Use reposync with `        --download-metadata` and without `        --newest-only` . See [RHEL 8](//https://access.redhat.com/solutions/5186621) Reposync.


- If you are not using `            --newest-only,` the repos downloaded may take an extended amount of time to sync due to the large number of GB.
- If you are using `            --newest-only,` the repos downloaded may take an extended amount of time to sync due to the large number of GB.

After the reposync is completed, your repositories are ready to use with a web server.


1. Move the repositories to your disconnected network.


