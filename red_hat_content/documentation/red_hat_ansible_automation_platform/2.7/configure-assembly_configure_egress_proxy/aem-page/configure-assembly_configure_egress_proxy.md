+++
title = "Configure proxy servers for egress traffic - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/configure-assembly_configure_egress_proxy"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/configure-configure_a_proxy_to_communicate_with_external_systems/", "Configure a proxy to communicate with external systems"]]
category = "Configure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/configure-assembly_configure_egress_proxy/aem-page/configure-assembly_configure_egress_proxy.html"
last_crumb = "Configure proxy servers for egress traffic"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure proxy servers for egress traffic"
oversized = "false"
page_slug = "configure-assembly_configure_egress_proxy"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/configure-assembly_configure_egress_proxy"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/configure-assembly_configure_egress_proxy/toc/toc.json"
type = "aem-page"
+++

# Configure proxy servers for egress traffic

You can deploy Ansible Automation Platform so that egress from the platform for various purposes functions properly through proxy servers.

Egress proxy allows clients to make indirect (through a proxy server) requests to network services.

The client first connects to the proxy server and requests some resource, for example, email, located on another server. The proxy server then connects to the specified server and retrieves the resource from it.

## Overview

The egress proxy should be configured on the system and component level of Ansible Automation Platform, for all the RPM and containerized installation methods. For containerized installers, the system proxy configuration for Podman on the nodes solves most of the problems with access through the proxy. For RPM installation, both system and component configurations are needed.

## Proxy backends

For HTTP and HTTPS proxies you can use a squid server. Squid is a forward proxy for the Web supporting HTTP, HTTPS, and FTP, reducing bandwidth and improving response times by caching and reusing frequently-requested web pages. It is licensed under the GNU GPL.

Forward proxies are systems that intercept network traffic going to another network (typically the internet) and send it on the behalf of the internal systems. The squid proxy enables all required communication to pass through it.

Make sure all the required Ansible Automation Platform control plane ports are opened on the squid proxy backend. Ansible Automation Platform-specific ports:

```
acl Safe_ports port 81
acl Safe_ports port 82
acl Safe_ports port 389
acl Safe_ports port 444
acl Safe_ports port 445
acl SSL_ports port 22
```
The following ports are for containerized installations:

```
acl SSL_ports port 444
acl SSL_ports port 445
acl SSL_ports port 8443
acl SSL_ports port 8444
acl SSL_ports port 8445
acl SSL_ports port 8446
acl SSL_ports port 44321
acl SSL_ports port 44322

http_access deny !Safe_ports
http_access deny CONNECT !SSL_ports
```

## Configure the system-level outbound proxy

An outbound proxy (egress proxy) is a server that acts as an intermediary for requests from clients seeking resources from other servers on the internet. It is used to regulate and secure client traffic, and to provide caching services to improve performance.

The outbound proxy is configured on the system level for all the nodes in the control plane.

You must set the following environment variables:

```
http_proxy=“http://external-proxy_0:3128”
https_proxy=“http://external-proxy_0:3128”
no_proxy=“localhost,127.0.0.0/8,10.0.0.0/8”
```
You can also add those variables to the '/etc/environment' file to make them permanent.

The installation program ensures that all external communication during the installation goes through the proxy. For containerized installation, those variables ensure that Podman uses the egress proxy.

## Configure component-level proxy settings

After using the RPM installation program, you must configure automation controller to use egress proxy.

### About this task

Note:

This is not required for containerized installers because Podman uses system configured proxy and redirects all the container traffic to the proxy.

For automation controller, set the `AWX_TASK_ENV` variable in `/api/v2/settings/`. To do this through the UI use the following procedure:

### Procedure

1.  From the navigation panel, select Settings> (and then)Automation Execution> (and then)Job.
2.  Click Edit.
3.  Add the variables to the **Extra Environment Variables** field
      and set:

```
"AWX_TASK_ENV": {
"http_proxy": "http://external-proxy_0:3128",
"https_proxy": "http://external-proxy_0:3128",
"no_proxy": "localhost,127.0.0.0/8"
                }
```

## Configure project syncing using SSH to work with a proxy server

The following procedure for RPM-based Ansible Automation Platform describes how to use automation controller Project Sync by using the SSH protocol to work with a proxy server.

### Procedure

1.  Perform the following steps on the automation controller nodes. If ansible-builder has not been installed yet, install it first.

```
# subscription-manager repos --enable ansible-automation-platform-2.6-for-rhel-8-x86_64-rpms
# dnf install ansible-builder
```

2.  Build a custom execution environment.   1.  First, create a work directory:
  

```
# su - awx
$ mkdir -p builder/newee
$ cd builder/newee
```

3.  Create an `execution-environment.yml` file with the following content:
  

```
version: 1

    build_arg_defaults:
  EE_BASE_IMAGE: 'registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8:latest'

    additional_build_steps:
  prepend:
    - RUN microdnf install -y nc
```

4.  Log in to registry.redhat.io.

```
$ podman login registry.redhat.io
```

5.  Run ansible-builder to start the building process.

```
$ cd /var/lib/awx/builder/newee/
$ ansible-builder build -t my-env -v 3
```

6.  Add the custom execution environment you created.
7.  On the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Execution Environments.
8.  Click Create execution environment.
9.  In the **Image** field add `localhost/my-env:latest`.
10.  Click Create execution environment.
11.  Re-run the Ansible Automation Platform installation program with the following steps to replace the execution environment from the default to the customized environment which will be used as a Project syncs. Note:
      Backup Ansible Automation Platform before running the installation program.

```
# ./setup.sh -b
```

12.  Create an `automationcontroller` file under the `group_vars` directory in the same location as the `setup.sh` file. The file contents are as follows:
  

```
control_plane_execution_environment: localhost/my-env
```

13.  Run `setup.sh`
  

```
# ./setup.sh
```

14.  Create `ssh_config` under the directory. For example:
  

```
Host github.com
Hostname ssh.github.com
ProxyCommand nc --proxy-type http --proxy proxy.example.com:port %h %p
User git
```

15.  Add the `ssh_config` file’s directory path in PATH to expose the isolated jobs so that the container execution environment can read `ssh_config` file.
16.  In the navigation panel, select Settings> (and then)Automation Execution> (and then)Job.
17.  Click Edit.
18.  If the `ssh_config` file has been created as `/var/lib/awx/.ssh/ssh_config`, add this to **Paths to expose to isolated jobs**
  
  Note:
      Ensure `ssh_config` is owned by the AWX user. (`#chown awx:awx /var/lib/awx/.ssh/ssh_config`)

```
[
"/var/lib/awx/.ssh:/etc/ssh:O"
]
```

## Enable a configurable proxy environment for AWS inventory synchronization

To enable a configurable proxy environment for AWS inventory synchronization, you can manually edit the override configuration file or set the configuration in the platform UI:

### About this task

1. Manually edit `/usr/lib/systemd/system/receptor.service.d/override.conf` and add the following `http_proxy` environment variables there:

```
http_proxy:<value>
https_proxy:<value>
proxy_username:<value>
Proxy_password:<value>
```
    Or

2. To do this through the UI use the following procedure:

### Procedure

1.  From the navigation panel, select Settings> (and then)Automation Execution> (and then)Job.
2.  Click Edit.
3.  Add the variables to the **Extra Environment Variables** field
      For example:

```
"AWX_TASK_ENV": {
        "no_proxy": "localhost,127.0.0.0/8,10.0.0.0/8",
        "http_proxy": "http://proxy_host:3128/",
        "https_proxy": "http://proxy_host:3128/"
                },
```

## Configure proxy settings for private automation hub

Allow your private automation hub to sync Ansible Galaxy content with proxy settings.

### Before you begin

- You have a `requirements.yml` file that identifies those collections to synchronize from Ansible Galaxy as in the following example:     **Requirements.yml example**

```
collections:
  # Install a collection from Ansible Galaxy.
  - name: community.aws
    version: 5.2.0
    source: https://galaxy.ansible.com
```

### About this task

You can edit the **community** remote repository to synchronize chosen collections from Ansible Galaxy to your private automation hub. By default, your private automation hub community repository directs to `galaxy.ansible.com/api/`.

### Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select Automation Content> (and then)Remotes.
3.  In the **Details** tab in the **Community** remote, click Edit remote.
4.  In the **YAML requirements** field, paste the contents of your `requirements.yml` file.
5.  Click Save remote.

### Results

You can now synchronize collections identified in your `requirements.yml` file from Ansible Galaxy to your private automation hub.

### What to do next

See [Synchronizing content collections](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_create_synclist "You can sync certified and validated collections in Ansible automation hub from console.redhat.com.")for syncing steps.
