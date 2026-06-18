+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-con_about_ha_hub"
title = "High availability automation hub - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_platform_install_overview/", "Install RPM-based Ansible Automation Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-con_about_ha_hub/aem-page/install-con_about_ha_hub.html"
last_crumb = "High availability automation hub"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "High availability automation hub"
oversized = "false"
page_slug = "install-con_about_ha_hub"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-con_about_ha_hub"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-con_about_ha_hub/toc/toc.json"
type = "aem-page"
+++

# High availability automation hub

High availability increases reliability and scalability for automation hub by distributing workload across many nodes and eliminating single points of failure.

HA deployments of automation hub have multiple nodes that concurrently run the same service with a load balancer distributing workload (an "active-active" configuration). This configuration eliminates single points of failure to minimize service downtime and enable you to easily add or remove nodes to meet workload demands.

## Enable a high availability (HA) deployment of automation hub on SELinux

Enable a high availability deployment of automation hub on SELinux by mounting `/var/lib/pulp` to an external NFS export. This ensures correct security contexts are applied to mount points.

### Before you begin

- You have already configured a NFS export on your server. Note:
      The NFS share is hosted on an external server and is not a part of high availability automation hub deployment.

### About this task

Note:

You must add the context for `/var/lib/pulp` pulpcore_static and run the Ansible Automation Platform installer before adding the context for `/var/lib/pulp`.

### Procedure

1.  Create a mount point at `/var/lib/pulp`:
  

```
$ mkdir /var/lib/pulp/
```

2.  Open `/etc/fstab` using a text editor, then add the following values:
  

```
srv_rhel8:/data /var/lib/pulp nfs defaults,_netdev,nosharecache,context="system_u:object_r:var_lib_t:s0" 0 0
srv_rhel8:/data/pulpcore_static /var/lib/pulp/pulpcore_static nfs defaults,_netdev,nosharecache,context="system_u:object_r:httpd_sys_content_rw_t:s0" 0 0
```

3.  Run the reload systemd manager configuration command:
  

```
$ systemctl daemon-reload
```

4.  Run the mount command for `/var/lib/pulp`:
  

```
$ mount /var/lib/pulp
```

5.  Create a mount point at `/var/lib/pulp/pulpcore_static`:
  

```
$ mkdir /var/lib/pulp/pulpcore_static
```

6.  Run the mount command:
  

```
$ mount -a
```

7.  With the mount points set up, run the Ansible Automation Platform installer:
  

```
$ setup.sh -- -b --become-user root
```

8.  After the installation is complete, unmount the `/var/lib/pulp/` mount point.

### What to do next

1. [Apply the appropriate SELinux context](/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-con_about_ha_hub#proc-apply-selinux-context "By applying the necessary SELinux context to the Pulp directories you ensure proper file access permissions and security policy compliance. They are essential for enabling the high availability (HA) deployment of automation hub on SELinux.").
2. [Configure the pulpcore.serivce](/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-con_about_ha_hub#proc-configure-pulpcore-service "You can configure the pulp service to ensure that automation hub services start only after the network and the mounting of the remote mount points.").

## Configure pulpcore.service

You can configure the `pulp` service to ensure that automation hub services start only after the network and the mounting of the remote mount points.

### About this task

### Procedure

1.  With the two mount points set up, shut down the Pulp service to configure `pulpcore.service`:
  

```
$ systemctl stop pulpcore.service
```

2.  Edit `pulpcore.service` using `systemctl`:
  

```
$ systemctl edit pulpcore.service
```

3.  Add the following entry to `pulpcore.service` to ensure that automation hub services starts only after starting the network and mounting the remote mount points:
  

```
[Unit]
After=network.target var-lib-pulp.mount
```

4.  Enable `remote-fs.target`:
  

```
$ systemctl enable remote-fs.target
```

5.  Reboot the system:
  

```
$ systemctl reboot
```

A bug in the pulpcore SELinux policies can cause the token authentication public/private keys in `etc/pulp/certs/` to not have the proper SELinux labels, causing the pulp process to fail. When this occurs, run the following command to temporarily attach the proper labels:

```
$ chcon system_u:object_r:pulpcore_etc_t:s0 /etc/pulp/certs/token_{private,public}_key.pem
```
Repeat this command to reattach the proper SELinux labels whenever you relabel your system.

## Apply the SELinux context

By applying the necessary SELinux context to the Pulp directories you ensure proper file access permissions and security policy compliance. They are essential for enabling the high availability (HA) deployment of automation hub on SELinux.

### About this task

### Procedure

1.  Shut down the Pulp service:
  

```
$ systemctl stop pulpcore.service
```

2.  Unmount `/var/lib/pulp/pulpcore_static`:
  

```
$ umount /var/lib/pulp/pulpcore_static
```

3.  Unmount `/var/lib/pulp/`:
  

```
$ umount /var/lib/pulp/
```

4.  Modify the `/etc/fstab` file as follows:
  

```
srv_rhel8:/data /var/lib/pulp nfs defaults,_netdev,nosharecache,context="system_u:object_r:pulpcore_var_lib_t:s0" 0 0
```

5.  Run the mount command:
  

```
$ mount -a
```
