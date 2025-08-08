# 3. Installing the Red Hat Edge Manager on Ansible Automation Platform
## 3.1. Installing the Red Hat Edge Manager RPM package




Prepare your Red Hat Enterprise Linux host for the installation of the Red Hat Edge Manager by enabling the necessary repositories, installing the `flightctl-services` package, configuring the baseDomain, and then starting and verifying the running services.

**Prerequisites**

- An active Ansible Automation Platform subscription with a running instance and the necessary API URLs and OAuth credentials.
- A separate machine from Ansible Automation Platform to install the Red Hat Edge Manager on.
- Podman installed for managing containers.
- A Red Hat Enterprise Linux host with:


- Minimal installation
- 4 cores and 16GB RAM (recommended)
- Administrative access (root or sudo-capable user)
- SSH access



**Procedure**

1. SSH into your Red Hat Enterprise Linux host.
1. Authenticate and log in to the Red Hat Container Registry:


```
sudo podman login registry.redhat.io
```


1. Install the necessary repositories and packages:


- Ensure that the Ansible Automation Platform repositories are enabled by running the following example command based on the version of Red Hat Enterprise Linux and architecture of your host:


```
sudo subscription-manager repos --enable ansible-automation-platform-2.5-for-rhel-9-x86_64-rpms
```


- Install the Red Hat Edge Manager service by running:


```
sudo dnf install -y flightctl-services
```



1. Update the installed `    /etc/flightctl/service-config.yaml` to set the `    baseDomain` :


```
sudo vi /etc/flightctl/service-config.yaml
```

Important
Ensure that you set the `    baseDomain` in the service configuration correctly. By default, the installation process attempts to automatically set this value based on the IP address of your Red Hat Enterprise Linux host.

However, if your environment uses a specific domain name to access this host, for example `    rhem-example.com` , it is recommended that you manually update the `    baseDomain` in `    /etc/flightctl/service-config.yaml` to this hostname.

Setting the `    baseDomain` correctly ensures that all generated URLs, certificates, and internal configurations within the Red Hat Edge Manager are accurate for your network setup. This is especially important for integration with Ansible Automation Platform and for ensuring that the UI is accessible through the intended domain name.

You can check the currently configured `    baseDomain` using:


```
grep baseDomain: /etc/flightctl/service-config.yaml
```




1. Enable and start the services:


```
sudo systemctl enable flightctl.target    sudo systemctl start flightctl.target
```


1. Verify that services are running:


```
sudo systemctl list-units flightctl-*.service
```

You should see these 7 services running:


- flightctl-db
- flightctl-kv
- flightctl-api
- flightctl-periodic
- flightctl-worker
- flightctl-ui
- flightctl-cli-artifacts

1. Go to the UI at the `    baseDomain` stored in the service configuration file:


```
grep baseDomain: /etc/flightctl/service-config.yaml
```

Visit the displayed `    baseDomain` in your web browser to access the UI.




**Troubleshooting**

If your services do not run correctly, use the following log command to troubleshoot further and remediate:


```
journalctl -u flightctl-&lt;impacted service&gt; -b --no-pager
```

