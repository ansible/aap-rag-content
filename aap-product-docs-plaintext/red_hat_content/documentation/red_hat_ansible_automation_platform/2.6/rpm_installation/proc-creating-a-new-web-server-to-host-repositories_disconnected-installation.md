# 5. Disconnected installation
## 5.3. Creating a new web server to host repositories




Create and configure a dedicated web server to host repositories for a disconnected environment. This procedure ensures local access to synchronized RPM packages and enables you to streamline content installation and updates on isolated systems.

**Procedure**

1. Install prerequisites:


```
$ sudo dnf install httpd
```


1. Configure httpd to serve the repo directory:


```
/etc/httpd/conf.d/repository.conf        DocumentRoot '/path/to/repos'        &lt;LocationMatch "^/+$"&gt;        Options -Indexes        ErrorDocument 403 /.noindex.html    &lt;/LocationMatch&gt;        &lt;Directory '/path/to/repos'&gt;        Options All Indexes FollowSymLinks        AllowOverride None        Require all granted    &lt;/Directory&gt;
```


1. Ensure that the directory is readable by an apache user:


```
$ sudo chown -R apache /path/to/repos
```


1. Configure SELinux:


```
$ sudo semanage fcontext -a -t httpd_sys_content_t "/path/to/repos(/.*)?"    $ sudo restorecon -ir /path/to/repos
```


1. Enable httpd:


```
$ sudo systemctl enable --now httpd.service
```


1. Open firewall:


```
$ sudo firewall-cmd --zone=public --add-service=http –add-service=https --permanent    $ sudo firewall-cmd --reload
```


1. On automation services, add a repo file at _/etc/yum.repos.d/local.repo_ , and add the optional repos if needed:


```
[Local-BaseOS]    name=Local BaseOS    baseurl=http://&lt;webserver_fqdn&gt;/rhel-8-for-x86_64-baseos-rpms    enabled=1    gpgcheck=1    gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release        [Local-AppStream]    name=Local AppStream    baseurl=http://&lt;webserver_fqdn&gt;/rhel-8-for-x86_64-appstream-rpms    enabled=1    gpgcheck=1    gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release
```




